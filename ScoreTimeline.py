# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 08:18:10 2023

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

    st.title('Scores Timeline')
    st.write(
        """
        Select the different filters to show a score timeline visual of the games played. 
        On a laptop device, right-click to save the image.
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
        #df = df[df['Category'].isin(['Attack', 'Shot'])]
        df = df[df['Category'].isin(['Shot'])]
        
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
        
        # Line Break
        st.markdown('')
        
        ### ----- TWO COLUMN FILTER - HOME AWAY TEAMS -----
        
        col1, col2 = st.columns(2, gap="small")
        with col1:
            # Filter for Home Team
            unique_home = sorted(df_select_event.Team.unique())
            selected_home = st.multiselect('**Choose Offaly**', unique_home)
            # Filtering data
            df_select_home = df_select_event[(df_select_event.Team.isin(selected_home))]
        
            ### ----- HOME SCORES DATA -----
            # Keep only Attack scores
            HomeScores = df_select_home[df_select_home['Outcome'].isin(['Point', 'Goal'])]
            
            # Assign Point & Goal values to Outcome column - what if statement
            HomeScores.loc[HomeScores['Outcome'] == 'Point', 'Points'] = 1
            HomeScores.loc[HomeScores['Outcome'] == 'Goal', 'Points'] = 3
                
            # Group Shots data for Home Team
            HomeScores = HomeScores.groupby(['Team', 'Start', 'Date']).agg({'Points':['sum']})
            HomeScores = HomeScores.reset_index()
            HomeScores.columns = ['Home', 'Start', 'Date', 'Points']
            
            # Make a Home cumulative Scores column
            HomeScores['HomeCumulativePoints']= HomeScores['Points'].cumsum(axis = 0)
            
            # Count Home Team scores in game
            homescores = len(HomeScores)
            
            #st.write(HomeScores)
        
        with col2:
            # Filter for Away Team
            unique_away = sorted(df_select_event.Team.unique())
            selected_away = st.multiselect('**Choose Opposition Team**', unique_away)
            # Filtering data
            df_select_away = df_select_event[(df_select_event.Team.isin(selected_away))]
        
        ### ----- AWAY SCORES DATA -----
            # Keep only Scores data
            AwayScores = df_select_away[df_select_away['Outcome'].isin(['Point', 'Goal'])]
            
            # Assign Point & Goal values to Outcome column - what if statement
            AwayScores.loc[AwayScores['Outcome'] == 'Point', 'Points'] = 1
            AwayScores.loc[AwayScores['Outcome'] == 'Goal', 'Points'] = 3
            
            # Group Scores data for Away Team
            AwayScores = AwayScores.groupby(['Team', 'Start', 'Date']).agg({'Points':['sum']})
            AwayScores = AwayScores.reset_index()
            AwayScores.columns = ['Away', 'Start', 'Date', 'Points']
            
            # Make a Away cumulative Scores column
            AwayScores['AwayCumulativePoints']= AwayScores['Points'].cumsum(axis = 0)
            
            # Count Away Team scores in game
            awayscores = len(AwayScores)
            
            #st.write(AwayScores)
    
        
        ### ----- ATTACK VIZ -----
        
        # Set Home Team & Away Team variables
        Home_Team = HomeScores.Home.iloc[0]
        #Home_Attacks = len(HA)
        Away_Team = AwayScores.Away.iloc[0]
        #Away_Goals = len(AG)
        Date = df_select_event.Date.iloc[0]
        Game = df_select_event.Game.iloc[0]
        #Dot = 'o'
        
        # Set variable names
        text_color = 'black'
        background = '#FFFFFF'

        ### Create Figure
        # Plot the figure
        fig = plt.figure(figsize=(15,8), dpi=300)
        ax = plt.subplot()
        #gs = fig.add_gridspec(nrows=1,ncols=2)
        fig.patch.set_facecolor(background)
        fig.tight_layout()

        # Set facecolour
        fig.set_facecolor(background)
        # Setting the background color
        ax.set_facecolor(background)

        # Tidy Axes
        plt.axis('off')
        
        # Line break
        st.write("""
                 """)
        
        ### ----- PLOT LINE CHART OF SCORES ON SAME CHART FOR EACH TEAM -----
        
        # Plot line chart of Scores - both teams
        ax.plot(HomeScores['Start'], HomeScores['HomeCumulativePoints'], c='green',
                        linewidth=5, drawstyle="steps-post")
        ax.plot(AwayScores['Start'], AwayScores['AwayCumulativePoints'], c='black',
                        linewidth=5, drawstyle="steps-post")
        
        ### ----- FIGURE, AXIS, TICKS ETC -----
        
        ### Create the axes - Left
        #ax1 = fig.add_subplot(gs[0,:1])
        
        # Plot title
        ax.text(x=25, y=25, s=f'{Game} - Score Trendline', color=text_color,
                      fontweight='bold', size='20')
        
        # Plot sub-title
        ax.text(x=28, y=24, s='Timeline of scores made by each team', va='center', ha='left',
                 size=15, color=text_color)
        
        # Set the axes labels
        plt.xlabel('\nMinute', color=text_color, fontsize=20)
        plt.ylabel('\nCumulative Scores count\n', color=text_color, fontsize=20)
        
        # Figure Title
        #plt.text(0.005, 10, f'{Game} - Scores Timeline\n', fontweight='bold',
        #         size='35')
        
        # Figure description
        #ax.text(0.005, 1.05, "Every time a line goes, it signals that a score occured during that minute of the game\n",
        #         size='25')

        # Set the x axis with values reflective of minute periods
        plt.xticks([0,10,20,30,40,50,60,70,80], color=text_color, fontsize=15)
        plt.yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22], color=text_color, fontsize=15)

        # Remove the pins on each axis
        #ax.tick_params(axis='both', length=0)
        
        # Remove axis
        plt.axis('on')
        
        #plt.legend()
        
        # Legend
        legend = ax.legend(frameon=True)
        ax.legend([f'{Home_Team}', f'{Away_Team}'], fontsize=15, markerscale=10, 
                  prop = {'size':15}, bbox_to_anchor= (0.16, 0.925));

        # Remove top and right spines
        spines = ['top', 'right']
        for s in spines:
            if s in ['top', 'right']:
                ax.spines[s].set_visible(False)
            else:
                ax.spines[s].set_color(text_color)
                
                
        

        # Plot the figure
        st.pyplot(fig)

    except Exception:
        pass