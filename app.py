# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:42:18 2022

@author: Alex
"""

# Import dependencies

from pathlib import Path

import streamlit as st
from PIL import Image

# ----- PATH SETTINGS -----

# Point everything to the local directory
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Alex_Rathke_CV.pdf"
MSc_file = current_dir / "assets" / "MSc_Pub.pdf"
profile_pic = current_dir / "assets" / "Alex_Rathke.jpg"


# ----- GENERAL SETTINGS -----
PAGE_TITLE = "Digital CV | Alex Rathke"
PAGE_ICON = ":wave:"
NAME = "Alex Rathke"
DESCRIPTION = """
Data Analyst, Business Intelligence Analyst\n, Data Visualisation
"""
DESCRIPTION1 = """
Assisting businesses by supporting data-driven decision-making.
"""

EMAIL = "rathkealex@gmail.com"
MSc = "https://www.redalyc.org/articulo.oa?id=301052437005"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rathkealex/",
    "GitHub": "https://github.com/guido1992",
    "Tableau": "https://public.tableau.com/app/profile/alex.rathke#!/",
    "Twitter": "https://twitter.com/AnalyticsLaduma",
    }

PROJECTS = {
    " 📁 Tableau Portfolio - My Tableau Public profile": "https://public.tableau.com/app/profile/alex.rathke#!/",
    " 📈 FIFA World Rankings - A python web application built in Streamlit": "https://ladumaanalytics-world-rankings-fifa-rankings-p2vyq8.streamlitapp.com/",
    " 📝 MSc Publication": "https://www.redalyc.org/articulo.oa?id=301052437005",
    }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ----- LOAD CSS, PDF & PROF PIC -----
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ----- HERO SECTION -----
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    
st.download_button(
label=" 📄 Download MSc Publication",
data=PDFbyte,
file_name=MSc_file.name,
mime="appication/octet-stream",
)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(DESCRIPTION1)

    st.write("📧", EMAIL, color='white')

st.download_button(
label=" 📄 Download Resume",
data=PDFbyte,
file_name=resume_file.name,
mime="appication/octet-stream",
)
    
st.write(
    """
    - ✔️ 5+ years experience extracting actionable insights from data
    - ✔️ Strong hands on experience and knowledge across various software tools
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )

st.markdown('')
    
# ----- SOCIAL LINKS -----
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate (SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# Line break
st.write("---")

# ----- QUALIFICATIONS ----- 
#st.write("#")
st.subheader("Qualifications")

# MSc degree
st.write("🎓", "**MSc Sports Performance | 🌍 University of Limerick | August 2016**")

# BSc degree
st.write("🎓", "**BSc Sports & Exercise Management | 🌍 University of College Dublin | August 2014**")

# Line Break
st.markdown('')

# Line Break
#st.write("---")

# ----- WORK HISTORY -----
#st.write("#")
st.subheader("Work History")

# ----- JOB 1 -----
st.write("🧑‍💻", "**People Data Analyst | Intercom**")
st.write("September 2021 - September 2022 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Ensured Diversity Ethnicity & Inclusion (DEI) data collection strategies
    - ➡️ Developed & managed DEI quarterly + annual reports for Executives & Leaders
    - ➡️ Collaborated on monthly reports - Headcount, Attrition, Starts, Terms
    - ➡️ Handled data requests from managers and colleagues
    - ➡️ Building of internal Tableau Online People Data database & visualisation dashboards
    """)

st.write("#")
    
# ----- JOB 2 -----
st.write("🧑‍💻", "**Data Analyst | Aon ACIA**")
st.write("June 2018 - August 2021 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Re-developed data manipulation processes from SQL Server to Alteryx & Trifacta
    - ➡️ Build Tableau dashboards for internal colleagues from different departments
    - ➡️ Accomplished with team, combination of 5 data sources into one Tableau dashboard
    - ➡️ Collaborated with colleagues and managers on incoming data requests
    - ➡️ Assisted with Tableau training for internal colleagues
    - ➡️ Co-led an organisation wide Tableau monthly user group
    """)

st.write("#")
    
# ----- JOB 3 -----
st.write("🧑‍💻", "**Data Analyst | Dundalk FC**")
st.write("June 2019 - October 2019 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Part-time work in Dundalk’s qualification pathway to European Club competitions
    - ➡️ Analysed opposition teams using data for trend reporting highlighting styles of play
    - ➡️ Presented work to Technical Director and Technical staff
    - ➡️ Developed Tableau dashboards - assist & educate staff on understanding data
    - ➡️ Aided Technical Director with player scouting & implementation of data flow process
    - ➡️ Software tools used: Alteryx, Python & Tableau
    """)
    
st.write("#")
    
# ----- JOB 4 -----
st.write("🧑‍💻", "**Data Analyst | Brand Athlete Agency**")
st.write("January 2019 - August 2019 | 🌍", "**London, UK**")
st.write(
    """
    - ➡️ Developed and built data flow process to ingest 3rd party data
    - ➡️ Used to analyse and store player data for a recruitment system
    - ➡️ Compiled & wrote player analysis & recruitment reports to identify players
    - ➡️ Software tools used: Alteryx, Python & Tableau
    """)
    
st.write("#")
    
# ----- JOB 5 -----
st.write("🧑‍💻", "**Performance & Data Analyst | Tipperary GAA**")
st.write("September 2017 - June 2019 & January 2022 - May 2022 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Part-time evening & weekend work with Tipperary Senior Footballers
    - ➡️ Assisted match-day analysis of data collection & led data flow visualisation process
    - ➡️ Developed Tableau dashboards to assist and visualise performance metrics 
    - ➡️ Helped to educate management staff on data insights
    - ➡️ Software tools used: Microsoft Excel, Python & Tableau
    """)
    
st.write("#")
    
# ----- JOB 6 -----
st.write("🧑‍💻", "**Performance Analyst | Remote**")
st.write("September 2017 - May 2018")
st.write(
    """
    - ➡️ Part-time evening & weekend work as a remote analyst
    - ➡️ Assisted Head Analyst with match-day analysis of data collection.
    - ➡️ Build a data flow visualisation process using Tableau
    - ➡️ Software tools used: Microsoft Excel & Tableau 
    """)
    
st.write("#")
    
# ----- JOB 7 -----
st.write("👨‍🏫", "**TV Analyst | StarTimes**")
st.write("March 2016 - June 2017 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Football analytics talk show covering highlights of the German Football Bundesliga
    - ➡️ Assisted with script writing to cover content for episodes
    - ➡️ Collaborated on video footage & data sourcing to add insight for stories
    - ➡️ Assisted with post-production editing 
    """)
    
st.write("#")
    
# ----- JOB 7=8 -----
st.write("🧑‍💻", "**Performance Analyst Intern | Houston Dynamo**")
st.write("May 2016 - September 2016 | 🌍", "**Houston, Texas, USA**")
    
# ----- SKILLS -----
# Line break
st.write("---")

st.subheader("Hard Skills")
st.write(
    """
    - 👨‍💻 Programming: Python, Pandas, Matplotlib, R, SQL
    - 📈 Data Visualisation: Tableau, Streamlit, Microsoft Excel, Power BI
    - 🗄️ Databases: SQL, Impala, Snowflake, Mongo DB
    - 🕵️ Data cleaning: Alteryx, Pandas, Tableau Prep, Trifacta
    - 💻 Software dev: HTML, CSS, Javascript
    """
    )
    
# Line break
st.write("---")

st.subheader("Certifications")
st.write(
    """
    - 📜 Introduction to R: Udemy
    - 📜 Hands on Essentials - Data Warehouse: Snowflake
    - 📜 5 day coding challenge: Code Institute
    - 📜 Tableau Desktop: Tableau Software
    - 📜 Alteryx Designer Core: Alteryx
    - 📜 Trifacta - Data Deputy: Alteryx
    - 📜 Trifacta - Data Wranger: Alteryx
    - 📜 Python Programming: Udemy
    - 📜 SQL: W3Schools
    """
    )
    
# Line break
st.write("---")
    
# ----- PROJECTS & ACCOMPLISHMENTS -----
st.subheader("Projects & Accomplishments")
st.write("Hoover over the links below to visit the project")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    
    