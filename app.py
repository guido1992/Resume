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
#MSc_file = current_dir / "assets" / "MSc_Pub.pdf"
profile_pic = current_dir / "assets" / "Alex_Rathke.jpg"
brazil = current_dir / "assets" / "British_Grand_Prix.png"
monza = current_dir / "assets" / "Italian_Grand_Prix.png"
spa = current_dir / "assets" / "Belgium_Grand_Prix.png"

# ----- GENERAL SETTINGS -----
PAGE_TITLE = "Digital CV | Alex Rathke"
PAGE_ICON = ":wave:"
NAME = "Alex Rathke"
DESCRIPTION = """
Data Analyst, Business Intelligence Analyst, \nData Visualisation
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
    " 📁 Tableau Portfolio 1 - My Tableau Public profile": "https://public.tableau.com/app/profile/alex.rathke#!/",
    " 📁 Tableau Portfolio 2 - My Tableau Public profile": "https://public.tableau.com/app/profile/alexander.rathke",
    " 📈 Sample Formula 1 Grand Prix Race Track - Tableau Visualisations": "https://github.com/guido1992/Resume",
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
    st.image(profile_pic, width=250)
    
#st.download_button(
#label=" 📄 Download MSc Publication",
#data=PDFbyte,
#file_name=MSc_file.name,
#mime="appication/octet-stream",
#)
    
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

# ----- JOB -----
st.write("🧑‍💻", "**Visualisation & Reporting Specialist | Clear Strategy**")
st.write("November 2022 - present | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Provided and engaged within the creation process of robust and agile reporting solutions using Power BI and Microsoft Excel to enhance clients’ data utilisation capabilities and provide actionable insights.
    - ➡️ Built and presented Proof of Concepts (POCs), showcasing technical capabilities, and facilitating successful business pitches.
    - ➡️ Contributed to internal and external growth strategies, identifying areas for company expansion, and implementing initiatives to foster both internal efficiency and external business development.
    """)

st.write("#")

# ----- JOB -----
st.write("🧑‍💻", "**Performance Data & Visualisation Analyst | Offaly GAA**") 
st.write("November 2022 – July 2023 | 🌍", "**Offaly, Ireland**")
st.write(
    """
    - ➡️ Conducted comprehensive team and opposition analysis for the Senior Men’s team - providing insights to the coaching staff.
    - ➡️ Generated insightful Tableau-built reports on team and opposition analysis by leveraging in-house collected data.
    - ➡️ Developed and maintained a Python application enhancing the accessibility and interpretability of self-collected data.
    - ➡️ Presented findings in a clear and concise manner, facilitating informed decision-making for coaching and technical staff.
    - ➡️ Assisted in translating complex data insights into actional strategies, contributing to the team’s overall performance improvement. 
    """)

st.write("#")

# ----- JOB -----
st.write("🧑‍💻", "**People Data Analyst | Intercom**")
st.write("September 2021 - September 2022 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Directed the implementation of a comprehensive Diversity, Ethnicity & Inclusion (DEI) data collection strategy.
    - ➡️ Developed & managed DEI quarterly and annual reports tailored for Executives and Leaders which provided actionable insights to support strategic decision-making.
    - ➡️ Played a key role in cross-functional collaboration by contributing to monthly reports on critical HR metrics.
    - ➡️ Took the initiative to build an internal Tableau People Data database, creating dynamic visualisations aimed at enhancing the understanding of HR metrics across the business.
    """)

st.write("#")
    
# ----- JOB -----
st.write("🧑‍💻", "**Data Analyst | Aon ACIA**")
st.write("June 2018 - August 2021 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Successfully re-engineered data manipulation processes, transitioning from Microsoft SQL Server to Alteryx and Trifacta, resulting in enhanced efficiency and streamlined workflows.
    - ➡️ Accomplished the integration of five separate data sources into a cohesive Tableau dashboard, providing a unified and comprehensive view of the business for executives and leaders.
    - ➡️ Leveraged Tableau skills to develop impactful dashboards for colleagues across different departments, facilitating data-driven decision-making.
    - ➡️ Played a pivotal role in providing Tableau training sessions for internal colleagues, contributing to the organisation’s data literacy, and fostering self-sufficiency in data visualisation and analysis.
    """)

st.write("#")
    
# ----- JOB -----
st.write("🧑‍💻", "**Data Analyst | Dundalk FC**")
st.write("June 2019 - October 2019 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Conducted in-depth analysis of opposition team data trends within Dundalk’s qualification pathway to the European Champions League & Europa League.
    - ➡️ Delivered valuable insights to technical staff – highlighting potential playing strategies based on comprehensive data examinations.
    - ➡️ Collaborated closely with the Technical Director to support player scouting efforts and implemented a streamlined data flow process using Alteryx & Python, enhancing the efficiency and accuracy of player assessment and recruitment processes.
    """)
    
st.write("#")
    
# ----- JOB -----
st.write("🧑‍💻", "**Data Analyst | Brand Athlete Agency**")
st.write("January 2019 - August 2019 | 🌍", "**London, UK**")
st.write(
    """
    - ➡️ Developed and built data flow process to ingest third party data.
    - ➡️ Used to analyse and store player data for a recruitment system.
    - ➡️ Compiled & wrote player analysis & recruitment reports to identify players.
    - ➡️ Software tools used: Alteryx, Python & Tableau.
    """)
    
st.write("#")
    
# ----- JOB -----
st.write("🧑‍💻", "**Performance & Data Analyst | Tipperary GAA**")
st.write("September 2017 - June 2019 & January 2022 - May 2022 | 🌍", "**Dublin, Ireland**")
st.write(
    """
    - ➡️ Part-time evening & weekend work with Tipperary Senior Footballers.
    - ➡️ Assisted match-day analysis of data collection & led data flow visualisation process.
    - ➡️ Developed Tableau dashboards to assist and visualise performance metrics.
    - ➡️ Helped to educate management staff on data insights.
    - ➡️ Software tools used: Microsoft Excel, Python & Tableau.
    """)

st.write(""
        )
       
# ----- JOB -----
st.write("🧑‍💻", "**Performance Analyst | Remote**")
st.write("September 2017 - May 2018")

# ----- JOB -----
st.write("👨‍🏫", "**TV Analyst | StarTimes**")
st.write("March 2016 - June 2017 | 🌍", "**Dublin, Ireland**")

# ----- JOB -----
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
st.write("Click on the links below to visit the project")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    
# Line break
st.write("""
         """)

### Sample Data Visualisations
st.subheader("Sample Tableau Data Visualisations")

brazil = Image.open(brazil)
monza = Image.open(monza)
spa = Image.open(spa)

# ----- HERO SECTION -----
col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.image(brazil, width=220)
with col2:
    st.image(monza, width=220)
with col3:
    st.image(spa, width=220)
    
