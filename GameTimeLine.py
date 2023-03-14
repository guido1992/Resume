# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:28:24 2023

@author: Alex
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import patches as mpatches
import matplotlib.patheffects as path_effects
from matplotlib.patches import Arc
from PIL import Image
import io

def app():

    st.title('Attack & Shots - Game Time Line')
    st.write(
        """
        Select the different filters to show a game time line visual of the games 
        and on a laptop, right-click to save the image.
        """)
        
    # Wrap everything into a function to avoid errors while waiting to select a file
    try:
        
        # Read data
        df = pd.read_csv('Test - Data.csv')
        
        ### ----- DATA PREP -----
                
        # Clean up Category column
        df['Category'] = df['Category'].replace({'TA Poss':'Possession',
                                                 'TA Attack':'Attack',
                                                 'TA Shot':'Shot',
                                                 'TA Turnover':'Turnover',
                                                 'TA Kickout':'Kickout',
                                                 'TB Poss':'Possession',
                                                 'TB Attack':'Attack',
                                                 'TB Shot':'Shot',
                                                 'TB Turnover':'Turnover',
                                                 'TB Kickout':'Kickout'})
        
        # Clean up Outcome column
        #df['Situation'] = df['Situation'].replace({'Free 2':'Free',
        #                                         'Sideline 2':'Sideline',
        #                                         'Break2':'Break'})
        
        # Clean up Situation column
        #df['Outcome'] = df['Outcome'].replace({'TA Won':'Offaly won',
        #                                       'TB Won':'Opposition won'})
        
        # Remove row data - not needed
        df = df[~df['Category'].isin(['Score Source'])]
        
        # Keep only Attack & Shot data
        df = df[df['Category'].isin(['Attack', 'Shot'])]
        
        # Only keep the following columns
        df = df[['Date', 'Competition', 'Game', 'Score', 'Team', 'Opposition',
                 'Category', 'Start', 'Situation', 'Outcome', 'Des 3', 'Des 4', 'Des 5']]
        
        # Change Start column to int 
        df = df.astype({'Start':'int'})       
        
        
        ### ----- FILTER SECTION -----
        
        # Filter for Competition
        sorted_unique_comp = sorted(df.Competition.unique())
        selected_comp = st.multiselect('**Choose a Competition**', sorted_unique_comp)
        # Filtering data
        df_select_comp = df[(df.Competition.isin(selected_comp))]
        
        # Filter for Game
        sorted_unique_game = sorted(df_select_comp.Game.unique())
        selected_game = st.multiselect('**Choose a Game**', sorted_unique_game)
        # Filtering data
        df_select_event = df_select_comp[(df_select_comp.Game.isin(selected_game))]
        
        ### ----- TWO COLUMN FILTER - HOME AWAY TEAMS -----
        
        col1, col2 = st.columns(2, gap="small")
        with col1:
            # Filter for Home Team
            unique_home = sorted(df_select_event.Team.unique())
            selected_home = st.multiselect('**Choose Offaly**', unique_home)
            # Filtering data
            df_select_home = df_select_event[(df_select_event.Team.isin(selected_home))]
    
        ### ----- HOME ATTACK DATA -----
            # Keep only Attack data
            HomeAttack = df_select_home[df_select_home['Category'].isin(['Attack'])]
            
            # Group Attack data for Home Team
            HomeAttack = HomeAttack.groupby(['Team', 'Start', 'Date']).agg({'Category':['count']})
            HomeAttack = HomeAttack.reset_index()
            HomeAttack.columns = ['Home', 'Start', 'Date', 'Attacks']
        
            # Make a Home cumulative Attack column
            HomeAttack['HomeCumulativeAttack']= HomeAttack['Attacks'].cumsum(axis = 0)
            
            # Count Home Team attacks in game
            homeattacks = len(HomeAttack)
            
            #st.write(HomeAttack)
        
        with col2:
            # Filter for Away Team
            unique_away = sorted(df_select_event.Team.unique())
            selected_away = st.multiselect('**Choose Opposition Team**', unique_away)
            # Filtering data
            df_select_away = df_select_event[(df_select_event.Team.isin(selected_away))]
        
        ### ----- AWAY ATTACK DATA -----
            # Keep only Attack data
            AwayAttack = df_select_away[df_select_away['Category'].isin(['Attack'])]
            
            # Group Attack data for Away Team
            AwayAttack = AwayAttack.groupby(['Team', 'Start', 'Date']).agg({'Category':['count']})
            AwayAttack = AwayAttack.reset_index()
            AwayAttack.columns = ['Away', 'Start', 'Date', 'Attacks']
            
            # Make a Away cumulative Attack column
            AwayAttack['AwayCumulativeAttack']= AwayAttack['Attacks'].cumsum(axis = 0)
            
            # Count Away Team attacks in game
            awayattacks = len(AwayAttack)
            
            #st.write(AwayAttack)
            
        # Line Break
        st.markdown('')
        
        ### ----- ATTACK VIZ -----
        
        # Set Home Team & Away Team variables
        Home_Team = HomeAttack.Home.iloc[0]
        #Home_Attacks = len(HA)
        Away_Team = AwayAttack.Away.iloc[0]
        #Away_Goals = len(AG)
        Date = df_select_event.Date.iloc[0]
        Game = df_select_event.Game.iloc[0]
        #Dot = 'o'
        
        # Set variable names
        text_color = 'black'
        background = '#FFFFFF'

        ### Create Figure
        # Set up gridspec figure
        fig = plt.figure(figsize=(40,15))
        gs = fig.add_gridspec(nrows=1,ncols=2)
        fig.set_facecolor(background)
        fig.patch.set_facecolor(background)
        fig.tight_layout()

        # Set facecolour
        fig.set_facecolor(background)
        # Setting the background color
        #ax.set_facecolor(background)

        # Tidy Axes
        plt.axis('off')
        
        ### ----- FIGURE, AXIS, TICKS ETC -----
        
        # Figure Title
        plt.text(0.005, 1.08, f'{Game} - Attack and Shot Timeline\n', fontweight='bold',
                 size='35')
        
        # Figure description
        plt.text(0.005, 1.05, "Every time a line goes, it signals that an attack/shot was taken during that minute of the game\n",
                 size='25')
    
        ### Create the axes - Left
        ax1 = fig.add_subplot(gs[0,:1])
        
        # Plot title
        ##ax1.set_title(f'\nOffaly Cumulative Attack & Shot Trend', color=text_color,
        ##              fontweight='bold', size='20')
        
        # Plot sub-title
        ##ax1.text(x=28, y=36.75, s='Timeline of attacks for each team', va='center', ha='left',
        ##         size=15, color=text_color)

        # Set the x axis with values reflective of minute periods
        plt.xticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80], color=text_color,
                   fontsize=15)
        plt.yticks([0,5,10,15,20,25,30,35,40,45], color=text_color, fontsize=15)

        # Remove the pins on each axis
        ##ax1.tick_params(axis='both', length=0)

        # Set the axes labels
        plt.xlabel('\nMinute', color=text_color, fontsize=20)
        plt.ylabel('\nCumulative Attack & Shot count\n', color=text_color, fontsize=20)
        
        # Legend
        ##legend = ax1.legend(frameon=True)
        ##ax1.legend([f'{Home_Team}', f'{Away_Team}'], fontsize=15, markerscale=10,
        ##          prop = {'size':20}, bbox_to_anchor= (0.20, 0.97));

        # Remove top and right spines
        spines = ['top', 'right', 'bottom', 'left']
        for s in spines:
            if s in ['top', 'right']:
                ax1.spines[s].set_visible(False)
            else:
                ax1.spines[s].set_color(text_color)

        ### ----- HOME TEAM ATTACK & SHOT CALC & VISUALISATION -----
        
        # Filtering data for Home Team
        df_select_home1 = df_select_event[(df_select_event.Team.isin(selected_home))]
        
        # Keep only Shot data
        HomeShot = df_select_home1[df_select_home1['Category'].isin(['Shot'])]
            
        # Group Shot data for Home Team      
        HomeShot = HomeShot.groupby(['Team', 'Start', 'Date']).agg({'Category':['count']})
        HomeShot = HomeShot.reset_index()
        HomeShot.columns = ['Home', 'Start', 'Date', 'HomeShots']
    
        # Make a Home cumulative Shot column
        HomeShot['HomeCumulativeShot']= HomeShot['HomeShots'].cumsum(axis = 0)
        
        # Count Home Team shots taken in game
        homeshots = len(HomeShot)
        
        # Display df
        #st.write(HomeShot)
        
        # Add text into visual - sentence explaining viz
        ax1.text(0.01, 30, s=f"Over the course of the game, {Home_Team} had {homeattacks}\n"
                 f'attacks which resulted in {homeshots} shots taken.\n'
                 'How often these events occurred can be seen\n' 
                 'in the chart below', va='center', ha='left', size=15, color=text_color)
        
        ### ----- AWAY SHOT DATA -----
        # Filtering data for Away Team
        df_select_away1 = df_select_event[(df_select_event.Team.isin(selected_away))]
        
        # Keep only Shot data
        AwayShot = df_select_away1[df_select_away1['Category'].isin(['Shot'])]
        
        # Group Shot data for Away Team
        AwayShot = AwayShot.groupby(['Team', 'Start', 'Date']).agg({'Category':['count']})
        AwayShot = AwayShot.reset_index()
        AwayShot.columns = ['Away', 'Start', 'Date', 'AwayShots']
        
        # Make a Away cumulative Shot column
        AwayShot['AwayCumulativeShot']= AwayShot['AwayShots'].cumsum(axis = 0)
        
        # Count Home Team shots taken in game
        awayshots = len(AwayShot)
        
        # Display df
        #st.write(AwayShot)
        
        ### Create the axes - Right
        ax2 = fig.add_subplot(gs[0,1])
        # Plot title
        ##ax2.set_title(f'{Away_Team} - Cumulative Attack & Shot Trend', color=text_color,
        ##              fontweight='bold', size='20')
        
        # Add text into visual - sentence explaining viz
        ax2.text(0.01, 35, s=f"Over the course of the game, {Away_Team} had {awayattacks}\n"
                 f'attacks which resulted in {awayshots} shots taken. \n'
                 'How often these events occurred can be seen\n' 
                 'in the chart below', va='center', ha='left', size=15, color=text_color)
        
        ### ----- PLOT LINE CHART OF BOTH ATTACKS AND SHOTS ON SAME CHART FOR EACH TEAM -----
        
        # Plot line chart of Attacks - both teams
        ax1.plot(HomeAttack["Start"], HomeAttack['HomeCumulativeAttack'], c='green',
                        linewidth=5, alpha=0.7, drawstyle="steps-post")
        ax1.plot(HomeShot['Start'], HomeShot['HomeCumulativeShot'], c='gray', 
                 linewidth=5, alpha=0.7, drawstyle="steps-post")
        
        # Plot line chart of Shots - both teams
        ax2.plot(AwayAttack["Start"], AwayAttack['AwayCumulativeAttack'], c='blue',
                        linewidth=5, alpha=0.7, drawstyle="steps-post")
        
        ax2.plot(AwayShot['Start'], AwayShot['AwayCumulativeShot'], c='gray',
                linewidth=5, alpha=0.7, drawstyle="steps-post")
        
        # Set the x axis with values reflective of minute periods
        ##plt.xticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80], color=text_color,
        ##           fontsize=15)
        ##plt.yticks([0,5,10,15,20,25,30,35,40], color=text_color, fontsize=15)

        # Remove the pins on each axis
        ax2.tick_params(axis='both', length=0)

        # Set the axes labels
        plt.xlabel('\nMinute', color=text_color, fontsize=20)
        plt.ylabel('Cumulative Attack & Shot count\n', color=text_color, fontsize=20)

        # Remove top and right spines
        spines = ['top', 'right', 'bottom', 'left']
        for s in spines:
            if s in ['top', 'right']:
                ax2.spines[s].set_visible(False)
            else:
                ax2.spines[s].set_color(text_color)
        
        # Add text description
        fig.text(
            x=0.125, y= 0.02,
            s=r'$\bfAttacks: %s}$ Possession gained in opponent half or when the team in possession crosses the opposition 45 creating a scoring chance.',
            ha='left',
            va='bottom',
            size=15
        )
        
        fig.text(
            x=0.125, y= 0.00,
            s=r'$\bfShots: %s}$    Any strike that ends with a point, goal, wide, short to keeper, hit the post or is saved.',
            ha='left',
            va='bottom',
            size=15
        )

        # Plot the figure
        st.pyplot(fig)

    except Exception:
        pass