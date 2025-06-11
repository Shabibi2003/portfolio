import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
#from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander

#test

# Set page title
st.set_page_config(page_title="Yousuf Shabibi", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Yousuf Shabibi';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("images/utown.JPG")
img_lh = Image.open("images/lh.jpg")
img_ifg = Image.open("images/ifg.jpg")
#Assets for competitions
img_lit = Image.open("images/legalease.jpg")
img_lifehack2 = Image.open("images/lifehack2.jpg")
img_lifehack = Image.open("images/lifehack.jpg")
img_he4d = Image.open("images/he4d.jpg")
img_ecc = Image.open("images/ecc.jpg")
img_shopee = Image.open("images/shopee.png")
img_sbcc = Image.open("images/sbcc.png")
img_runes = Image.open("images/runes.png")
# Assets for education
img_sji = Image.open("images/sji.jpg")
img_tpjc = Image.open("images/tpjc.jpg")
img_nus = Image.open("images/nus.jpeg")
img_poc = Image.open("images/poc.jpg")
img_gmss = Image.open("images/gmss.jpg")
img_sjij = Image.open("images/sjij.jpg")
img_dsa = Image.open("images/dsa.jpg")
# Assets for experiences
img_quest = Image.open("images/EDSlogo.jpg")
img_scor = Image.open("images/scor.jpg")
img_iasg = Image.open("images/iasg.jpg")
img_sshsph = Image.open("images/sshsph.jpg")
img_yll = Image.open("images/yll.jpg")
img_saf = Image.open("images/saf.jpg")
img_bitmetrix = Image.open("images/bitmetrix.jpg")
img_groundup = Image.open("images/groundup.jpg")
img_hedgedrip = Image.open("images/hedgedrip.jpg")
# Assets for projects
image_names_projects = ["ecom", "chatgpt", "videogames", "health", 
                         "biopics", "anime", "word2vec", "cellphone", 
                         "spotify", "map", "gephi", "fob", "get", "ttdb",
                         "blockchain"]
images_projects = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_projects]
# Assets for volunteering
# image_names_vol = ["sdslogo", "sportslogo", "gdsclogo", "csclogo", 
#                          "nussulogo", "sklogo", "simlogo", "tpjclogo", 
#                          "sjilogo", "nuspc", "hcs", "fintech"]
# images_vol = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_vol]
# Assets for blog
img_qb = Image.open("images/qb.jpg")
img_mayans = Image.open("images/mayans.jpg")
img_outlier = Image.open("images/outlier.png")
img_dac = Image.open("images/dac.png")
img_raffles = Image.open("images/raffles.jpg")
img_covid = Image.open("images/covid.jpg")
img_gender = Image.open("images/gender.jpg")
img_hci = Image.open("images/hci.jpg")
img_wordcloud = Image.open("images/wordcloud.jpg")
img_taste = Image.open("images/taste.jpg")
img_measles = Image.open("images/measles.jpeg")
img_bmsaew = Image.open("images/bmsaew.png")
img_dac1 = Image.open("images/dac1.png")
img_dac2 = Image.open("images/dac2.png")
# Assets for gallery
# 2005
# img_2005_1 = Image.open("gallery/2005_1.jpg")
# img_2005_2 = Image.open("gallery/2005_2.jpg")
# # 2006
# img_2006_1 = Image.open("gallery/2006_1.jpg")
# # 2008
# img_2008_1 = Image.open("gallery/2008_1.jpg")
# # 2009
# img_2009_1 = Image.open("gallery/2009_1.jpg")
# # 2011
# image_dict = {}
# num_images = 4
# for i in range(1, num_images + 1):
#     image_key = f"img_2011_{i}"
#     image_path = f"gallery/2011_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2012 
# image_dict = {}
# num_images = 7
# for i in range(1, num_images + 1):
#     image_key = f"img_2012_{i}"
#     image_path = f"gallery/2012_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2013
# image_dict = {}
# num_images = 11
# for i in range(1, num_images + 1):
#     image_key = f"img_2013_{i}"
#     image_path = f"gallery/2013_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2014
# image_dict = {}
# num_images = 13
# for i in range(1, num_images + 1):
#     image_key = f"img_2014_{i}"
#     image_path = f"gallery/2014_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2015
# image_dict = {}
# num_images = 48
# for i in range(1, num_images + 1):
#     image_key = f"img_2015_{i}"
#     image_path = f"gallery/2015_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2016
# image_dict = {}
# num_images = 25
# for i in range(1, num_images + 1):
#     image_key = f"img_2016_{i}"
#     image_path = f"gallery/2016_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2017
# image_dict = {}
# num_images = 4
# for i in range(1, num_images + 1):
#     image_key = f"img_2017_{i}"
#     image_path = f"gallery/2017_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2018
# image_dict = {}
# num_images = 16
# for i in range(1, num_images + 1):
#     image_key = f"img_2018_{i}"
#     image_path = f"gallery/2018_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# # 2019
# image_dict = {}
# num_images = 20
# for i in range(1, num_images + 1):
#     image_key = f"img_2019_{i}"
#     image_path = f"gallery/2019_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #2020
# image_dict = {}
# num_images = 3
# for i in range(1, num_images + 1):
#     image_key = f"img_2020_{i}"
#     image_path = f"gallery/2020_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #2021
# image_dict = {}
# num_images = 14
# for i in range(1, num_images + 1):
#     image_key = f"img_2021_{i}"
#     image_path = f"gallery/2021_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #2022
# image_dict = {}
# num_images = 19
# for i in range(1, num_images + 1):
#     image_key = f"img_2022_{i}"
#     image_path = f"gallery/2022_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #2023
# image_dict = {}
# num_images = 22
# for i in range(1, num_images + 1):
#     image_key = f"img_2023_{i}"
#     image_path = f"gallery/2023_{i}.jpg"
#     image_dict[image_key] = Image.open(image_path)
# #img_lottie_animation = Image.open("images/lottie_animation.gif")
# # Assets for contact
# lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

# img_linkedin = Image.open("images/linkedin.png")
# img_github = Image.open("images/github.png")
# img_email = Image.open("images/email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "wordpress": "https://img.icons8.com/ios-filled/100/ff8c00/wordpress--v1.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Yousuf Shabibi", 
                        ["About Me", "Site Overview", "Experience", "Technical Skills", "Education", "Projects", "Blog", "Resume", "Contact"],
                         icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'heart', 'pencil square', 'image', 'paperclip', 'star fill', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )

    linkedin_url = "https://www.linkedin.com/in/yousufshabibi/"
    github_url = "https://github.com/Shabibi2003"
    email_url = "shabibiyousuf@gmail.com"
    
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url,Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Yousuf Shabibi")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Aspiring Data Analyst")
            st.write("👋🏻 I’m Yousuf, an Artificial Intelligence and Data Science undergraduate based in Delhi. I have a strong foundation in AI and Data Science, with specialization in Python, data visualization, and analytics. I possess hands-on experience in machine learning projects and predictive modeling, along with developing web applications using Flask and Streamlit. Currently, I am working as a Data Analyst Intern at EDS Company (Delhi), where I am further enhancing my analytical skills..")
            # st.write("💼 With the COVID-19 pandemic behind us, I believe there is potential for data science to be applied in the retail industry. In response to the increasing demand for data analytics from both online and brick-and-mortar sales, I am thus aiming to enter this industry for my first full-time job.")
            st.write("🏋🏻 In addition, I like to run, write, play video games and... enjoy eating good food in my free time!")
            st.write("👨🏼‍💻 Academic interests: Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing, Deep Learning, Machine Learning")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst, ML Engineer")
            st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/1N6n1v52rHJ5Rk1tJDfwB488UR3afPTi7/view?pli=1)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)
elif choose == "Site Overview":   
    #overview.createPage()
    st.header("Site Overview")
    st.markdown("""
    Initally creating this as a portfolio website in the form of an extended resume, I came to discover the uniqueness of Streamlit as compared to typical front-end frameworks such as Angular and Bootstrap. Even though Streamlit is primarily used as a web application for dashboarding, its extensive features make it more aesthetically appealing to explore with as compared to alternatives such as Plotly and Shiny.
    
    With the convenience of using Python as a beginner-friendly programming language, I have now decided to evolve this personal project into a time capsule - documenting key moments and achievements that I have attained since commencing my formal education at 7 years old.


    """)
    # with st.container():
    #         col1, col2, col3 = st.columns((1,3,1))
    #         with col1:
    #             st.empty()
    #         with col2:
    #             st.video("https://youtu.be/1QlgizeKg44")
    #         with col3:
    #             st.empty()
    # st.markdown("""
    # *For an optimal experience, do browse this site on desktop!*

    # Updated May 1, 2023
    # """)
# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    # with st.container():
    #     image_column, text_column = st.columns((1,5))
    #     with image_column:
    #         st.image(img_hedgedrip)
    #     with text_column:
    #         st.subheader("Product Manager, [HedgeDrip](https://hedgedrip.vercel.app)")
    #         st.write("*September 2023 to Present*")
    #         st.markdown("""
    #         `Figma` `Notion` `Product Management`
    #         """)
    # with st.container():
    #     image_column, text_column = st.columns((1,5))
    #     with image_column:
    #         st.image(img_groundup)
    #     with text_column:
    #         st.subheader("Data Science Intern, [Groundup.ai](https://groundup.ai)")
    #         st.write("*July to December 2023 (Expected)*")
    #         st.markdown("""
    #         - Deployed sound sensors using Raspberry Pi technology to acquire real-time noise data from naval vessels and support comprehensive analysis using spectrograms for anomaly detection
    #         - Utilised Librosa, Matplotlib and Scikit-Learn to detect anomalies for predictive maintenance of machines using spectrograms and principal component analysis (PCA)
    #         - Leveraged AWS CloudFormation and YAML to script automatic configuration of Amazon S3 buckets, leading to significant reduction in manual setup time and minimizing potential for human error
    #         - Collaborated with Product Lead, AI Lead and Software Engineers to improve usability and customization for sound predictive maintenance dashboard
            
    #         `Python` `Raspberry Pi` `Jira` `Confluence` `Amazon S3` `EC2` `Librosa` `Docker` `Git` `Scikit-Learn` `MLFlow` `YAML` `InfluxDB` `ScyllaDB` `PostgreSQL` `Matplotlib` `Plotly` `Minio`
    #         """)
    # with st.container():
    #     image_column, text_column = st.columns((1,5))
    #     with image_column:
    #         st.image(img_bitmetrix)
    #     with text_column:
    #         st.subheader("Data Science Intern, [Bitmetrix](https://bitmetrix.ai)")
    #         st.write("*June to July 2023*")
    #         st.markdown("""
    #         - Built social media scraper using snscrape to scrape Tweets from popular blockchain websites based on rankings from CoinGecko and CoinMarketCap
    #         - Constructed webscraper using Streamlit and BeautifulSoup4 to collate news articles from various sources (e.g https://blockchain.news) into Pandas dataframe for future analysis using natural language processing methods

    #         `Python` `BeautifulSoup4` `snscrape` `Streamlit` `Pandas`
    #         """)
    # with st.container():
    #     image_column, text_column = st.columns((1,5))
    #     with image_column:
    #         st.image(img_scor)
    #     with text_column:
    #         st.subheader("Actuarial Intern, [SCOR](https://scor.com)")
    #         st.write("*May to August 2022* | [*Testimonial*](https://drive.google.com/file/d/1seUP5OcXV5irA1Y1qt0cKnd7uQnLJLzw/view?usp=share_link)")
    #         st.markdown("""
    #         - Performed actuarial analysis of reinsurance treaties in various APAC markets, including entry of client portfolio and loss data into xAct (treaty pricing system)
    #         - Regularly updated and analysed risk profiles and claims databases for insurance markets in Pakistan, Thailand and Vietnam
    #         - Trained machine learning models (logistic regression, random forest) to predict insurance claims, with an average accuracy of 80% for each model

    #         `Excel` `Python` `R` `xAct` `VBA`
    #         """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_quest)
        with text_column:
            st.subheader("Data Analytics Intern, [EDS](https://www.edsglobal.com/)")
            st.write("*Nov 2024 to June 2025*")
            st.markdown("""
            - Developed Data visualization dashboard using Python (Streamlit, Plotly, Matplotlib).
            - Performed Exploratory Data Analysis (EDA) on large datasets to identify trends and outliers.
            - Utilized machine learning algorithms (KNN, Random Forest) to predict outcomes and optimize performance.
            - Created SQL queries to extract relevant information from relational databases for variour projects.


            `Python` `R` `Tableau` `Excel`  `Google Analytics`  `SQL` `ML` `DL`
            """)
    # with st.container():
    #     image_column, text_column = st.columns((1,5))
    #     with image_column:
    #         st.image(img_sshsph)
    #     with text_column:
    #         st.subheader("Public Health Intern, [Saw Swee Hock School of Public Health](https://sph.nus.edu.sg/)")
    #         st.write("*January to May 2021*")
    #         st.markdown("""
    #         - Conducted literature reviews and summarized papers related to public health
    #         - Drafted case study report on British population health system, including impacts from COVID-19
    #         - Collaborated with other students to compare successes and challenges of Britain, Canada and New Zealand’s healthcare systems
    #         """)
    # with st.container():
    #     image_column, text_column = st.columns((1,5))
    #     with image_column:
    #         st.image(img_iasg)
    #     with text_column:
    #         st.subheader("Data Migration Intern, [Immigration@SG LLP](https://iasg.com.sg/)")
    #         st.write("*October 2020 to January 2021* | [*Testimonial*](https://drive.google.com/file/d/11qFI-9TMfjOk1OxuyQ9ho9A7D6KuIsXp/view?usp=sharing)")
    #         st.markdown("""
    #         - Cleaned over 30,000 records using Pandas to facilitate smooth data migration into new CRM system
    #         - Derived customer segmentation models using regression models and market basket analysis (association rule mining) to improve company’s marketing strategies
    #         - Completed time series analysis using past sales data to forecast future monthly revenue

    #         `Excel` `ggplot2` `Python` `pandas` `R`
    #         """)
    # with st.container():
    #     image_column, text_column = st.columns((1,5))
    #     with image_column:
    #         st.image(img_yll)
    #     with text_column:
    #         st.subheader("Temporary Management Support Staff, [Yong Loo Lin School of Medicine](https://medicine.nus.edu.sg/)")
    #         st.write("*February to June 2019*")
    #         st.markdown("""
    #         - Answered up to 100 different queries daily regarding undergraduate admissions
    #         - Managed venue preparations for admissions interviews involving over 1,000 candidates over the span of 2 weeks
    #         - Supported set-up of faculty booth for NUS Open House, with an estimated attendance of 30,000 visitors in one day
    #         """)
    # with st.container():
    #     image_column, text_column = st.columns((1,5))
    #     with image_column:
    #         st.image(img_saf)
    #     with text_column:
    #         st.subheader("Administrative Support Assistant, [Singapore Armed Forces](https://www.mindef.gov.sg/web/portal/mindef/home)")
    #         st.write("*January 2017 to January 2019* | [*Testimonial*](https://drive.google.com/file/d/1O6Yu0P65dU8LCSDuXkf9BvlQJoz_5mRW/view?usp=sharing)")
    #         st.markdown("""
    #         - Assisted in organising division-level In-Camp Trainings, conferences and welfare events
    #         - Handled daily administration of Operations Branch, including indentation of office equipment, budget management and food rations
    #         - Promoted to Corporal First Class (CFC) for outstanding efforts
            
    #         `Excel` `GeBiz` `GIS` `Outlook` `PowerPoint` `Word`
    #         """)
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages","`Python`, `SQL`, `HTML & CSS`, `JS`, `C`")
    txt3("Academic Interests","`Data Visualization`, `Deep Learning`, `Recommendation Systems`, `Natural Language Processing`")
    txt3("Data Visualization", " `matplotlib`, `seaborn`, `Plotly`, `Tableau`, `Power BI`, `Google Data Studio`, `Google Analytics`")
    txt3("Database Systems", "`MySQL`, `PostgreSQL`, `SQLite`, `NoSQL`")
    txt3("Cloud Platforms", "`Google Cloud Platform`, `Amazon Web Services`, `Heroku`, `Streamlit Cloud`, `TiDB Cloud`, `Hugging Face`")
    txt3("Natural Language Processing", "`NLTK`, `Word2Vec`, `TF-IDF`, `TextStat`")
    txt3("Version Control", "`Git`, `Docker`, `MLFlow`")
    txt3("Design and Front-end Development", "`Canva`, `HTML`, `CSS`, `Streamlit`, ")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`, `Text Classification`, `Sentiment Analysis`, `Matrix Factorisation`, `Collaborative Filtering`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`")
    txt3("Data Analysis", "`Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Plotly`, `Scikit-Learn`, `TensorFlow`, `Keras`, `NLTK`, `Word2Vec`, `TF-IDF`, `TextStat`")
# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    selected_options = ["Summary", "Modules"
                        ]
    selected = st.selectbox("Which section would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Summary":
        st.subheader("Summary")
        st.write("*Summary of education from primary school till university*")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_nus)
            with text_column:
                st.subheader("Bachelor of Technology - [Artificial Intelligence and Data Science](https://www.stat.nus.edu.sg/wp-content/uploads/sites/8/2022/12/NUS-CHS-DSA-Print-FA.pdf), [CSMSS Chh. Shahu colluege of Engineering, Aurangabad](https://www.csmssengg.org/) (2021-2024)")
                st.write("Relevant Coursework: Computers System and Architecture, Signal Processing, Data Science in Practice, Data Structures and Algorithms, Data Visualization, Database Technology and Management, Linear Algebra, Multivariable Calculus, Optimization for Large-Scale Data-Driven Inference, Advance Mathamatics, Programming Tools, Regression Analysis, Statistical Learning")
                # st.markdown("""
                # - [NUS Product Club](https://linkedin.com/company/nusproductclub) - Co-founder & President (2023-24)
                # - [NUS Statistics and Data Science Society](https://sites.google.com/view/nussds/home) - President (2022), Marketing Director (2021-22)
                # - [Google Developer Student Clubs NUS](https://dsc.comp.nus.edu.sg/) - Deputy Head of Finance (2021-22)
                # """)
        # with st.container():
        #     image_column, text_column = st.columns((1,2.5))
        #     with image_column:
        #         st.image(img_poc)
        #     with text_column:
        #         st.subheader("Bachelor of Science - Pharmaceutical Science, [National University of Singapore](https://nus.edu.sg) (2019)")
        #         st.write("Coursework: Foundations of Medicinal Chemistry, Pharmaceutical Biochemistry, Statistics for Life Sciences, Human Anatomy and Physiology, Quantitative Reasoning")
        #         st.markdown("""
        #         Withdrew from course in 2020, before performing a clean slate transfer to pursue a Bachelor's Degree in Data Science and Analytics
        #         - [NUS Students' Science Club](https://www.nussciencelife.com/) - Marketing Executive, Welfare Subcommittee
        #         - Pharmaceutical Science (Class of 2023) - Assistant Class Representative
        #         """)
        # with st.container():
        #     image_column, text_column = st.columns((1,2.5))
        #     with image_column:
        #         st.image(img_tpjc)
        #     with text_column:
        #         st.subheader("GCE A Level - [Tampines Junior College](https://www.tmjc.moe.edu.sg/our-heritage/tampines-jc/) (2015 - 2016)")
        #         st.write("Coursework: H2 Chemistry, H2 Economics, H2 Mathematics, H1 Project Work, H1 Chinese, H1 History")
        #         st.markdown(""" 
        #         - Track and Field - 100m (2016 A Division Semi-finalist), 200m, 4x100m
        #         - TPJC Economics and Financial Literacy Fair 2015 - Games Facilitator
        #         """)
        # with st.container():
        #     image_column, text_column = st.columns((1,2.5))
        #     with image_column:
        #         st.image(img_sji)
        #     with text_column:
        #         st.subheader(" - [Saint Joseph's Institution](https://www.sji.edu.sg/) (2012 - 2014)")
        #         st.write("Coursework: English, Mathematics, Additional Mathematics, Physics, Chemistry, History, Geography Elective, Chinese")
        #         st.markdown(""" 
        #         - Track and Field (Long Jump, 100m)
        #         - [Business Design Thinking](https://www.sp.edu.sg/sp/news/sp/Secondary-students-learn-to-innovate)
        #         - Josephian International Experience Programme (Siem Reap, Cambodia)
        #         """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_gmss)
            with text_column:
                st.subheader("Higher Secondary CLASS XII - [Al-Irfan Secondary School](https://www.alirfanschool.com/) (2022 - 2021)")
                st.write("Coursework: English, Mathematics, Physics, Chemistry, Computer Science, Physical Education ")
                st.markdown(""" 
                - Football
                """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_sjij)
            with text_column:
                st.subheader("High School CLASS X - [Al-Irfan Secondary School ](https://www.alirfanschool.com/) (2018 - 2019)")
                st.write("Coursework: English, Mathematics, Science, Chinese, Higher Chinese")
                st.markdown(""" 
                - Football
                """)
    elif selected == "Modules":
        st.subheader("Modules")
        st.write("*List of modules taken at D.BATU University Lonere.*")
        st.write("*To be updated soon*")
   
elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Car Retail Price Prediction")
            # st.write("*Project for US-based stealth startup, Bitmetrix.ai*")
            st.markdown("""
            - Developed a predictive model to estimate car retail price using machine learning algorithms.
            - Utilized data from Kaggle dataset containing information on 1368 cars, including features such as make, model, year, mileage, and fuel type.
            - Implemented linear regression, decision tree regression, random forest regression, and gradient boosting regression models to predict car retail price.
            - Achieved an R-squared score of 0.85 using the gradient boosting regression model.
            """)
            # st.write("[Github Repo](https://github.com/Shabibi2003/house_price_prediction)")
            mention(label="Github Repo", icon="github", url="https://github.com/Shabibi2003/Car-Retail-Price-Prediction-",)
        with image_column:
            st.image(images_projects[14])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Triple Rider and Helmet Detection in real time.")
            st.write("*Self-initiated project*")
            st.markdown("""
            - Developed a Deep Learning system using CNNs to detect trople riders and helmet usage from images and videos, aimed to enhancing road safety
            - Utilized TensorFlow and Keras to build and train the model, achieving an accuracy of 99.1% on the test set
            - Implemented a Streamlit web application to allow users to upload images and videos for real-time detection
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            # mention(label="Streamlit App", icon="streamlit", url="https://huggingface.co/spaces/harrychangjr/tiktok_analytics",)
            mention(label="Github Repo", icon="github", url="https://github.com/Shabibi2003/house_price_prediction",)
        with image_column:
            st.image(images_projects[13])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("EUI Prediction for office typology in Delhi")
            st.write("*Internship Project*")
            st.markdown("""
            - Conducted exploratory data analysis (EDA) to identify relationships between variables using correlation heatmaps and histograms
            - Trained and compared multiple regression, random forest and XGBoost to build optimal model for EUI prediction.
            - Performed randomized search with cross-validation to increase performance of random forest regressor and reduce MSE
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            # mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/sales-prediction",)
        with image_column:
            st.image(images_projects[0])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Creating a Chatbot using LLM of OpenAI")
            st.write("*Self-initiated project *")
            st.markdown("""
            - Developed a chatbot using the OpenAI GPT-3.5 language model
            - Using VectorShift to create an interactive Interface and LLM model.
            - Created a chatbot that can answer questions about the user and provide information on a topic 
            - Implemented a chatbot that can generate responses to user queries using natural language processing techniques
            - Used the OpenAI API to generate responses to user queries
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/sp1541-nlp)")
            mention(label="Chatbot", icon="chatbot", url="https://app.vectorshift.ai/chatbots/deployed/67f55b9957e327dd342faf38",)
            # mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/sp1541-nlp",)
        with image_column:
            st.image(images_projects[1])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Statistical Learning: Analysis on Video Game Sales")
    #         st.write("*Completed project within 48 hours for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
    #         #st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
    #         st.markdown("""
    #         - Utilised multiple regression to investigate impact of publishers on global sales by regression coefficient, including performing one-hot encoding on 'Publisher' categorical variable
    #         - Compared performances of multiple linear regression, random forest and XGBoost to predict global sales using critic scores and user scores from Metacritic
    #         - Trained linear mixed-effects model to investigate impact of publishers, platform and genres in global sales
    #         """)
    #         #st.write("[Github Repo](https://github.com/harrychangjr/st4248-termpaper) | [Term Paper](https://github.com/harrychangjr/st4248-termpaper/blob/main/ST4248%20Term%20Paper%20(A0201825N)%20v5.pdf)")
    #         mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/st4248-termpaper",)
    #     with image_column:
    #         st.image(images_projects[2])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Statistical Learning: Nourish Your Body with Data")
    #         st.write("*Completed group project for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
    #         st.markdown("""
    #         - Adapted [previous project](https://drive.google.com/file/d/10ZOdQ8Q7UnevXxODAQs1YOstNSsiKh7G/view?usp=sharing) from DSA3101: Data Science in Practice, with the usage of statistical learning methods instead
    #         - Performed random forest classification and clustering methods to identify different consumer segments of grocery shoppers in supermarkets
    #         - Built recommendation system using matrix factorisation to recommend healthier food alternatives for grocery shoppers from different backgrounds
    #         """)
    #         #st.write("[Final Report](https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing) | [Pitch Deck](https://www.canva.com/design/DAFeSnJeqgM/uXpz0kw8e7If4T1PG2tpaQ/view?utm_content=DAFeSnJeqgM&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Product Demo](https://www.youtube.com/watch?v=XMlt-kfdC7g)")
    #         mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing",)
    #     with image_column:
    #         st.image(images_projects[3])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Data Science Project on Biopics Dataset from Kaggle")
    #         st.write("*Self-initiated project using various machine learning methods on [biopics dataset](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-biopics-dataset)*")
    #         st.markdown("""
    #         - Ran regression models to predict box office revenue (linear regression, random forest, support vector machines)
    #         - Used k-means clustering with principal components analysis to identify similar types of movies
    #         - Built content-based recommendation system using cosine similarity to recommend similar movies based on input title
    #         """)
    #         #st.write("[Github Repo](https://github.com/harrychangjr/biopics) | [RPubs](https://rpubs.com/harrychangjr/biopics)")
    #         mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/biopics",)
    #     with image_column:
    #         st.image(images_projects[4])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Optimisation for Large-Scale Data-Driven Inference: Anime Recommendation System")
    #         st.write("*Completed assignment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2*")
    #         st.markdown("""
    #         - Built recommendation system using various non-factor models, including content-based collaborative filtering and clustering
    #         - Utilised matrix factorisation (single value decomposition) to optimise performance of recommendation system with lower test MSE
    #         - Provided optional recommendations to further optimise performance e.g scraping additional data, using deep learning methods
    #         """)
    #         #st.write("[Github Repo](https://github.com/harrychangjr/dsa4212) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%202%20Group%2039%20Report.pdf)")
    #         mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/dsa4212",)
    #     with image_column:
    #         st.image(images_projects[5])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Optimisation for Large-Scale Data-Driven Inference: Word Embedding")
    #         st.write("*Completed assigmment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2*")
    #         st.markdown("""
    #         - Trained Word2Vec model on 20 Newsgroups dataset from scikit-learn package in Python, which provides a number of similar words based on input word
    #         - Evaluated usefulness of model by applying model to text classification (46% accuracy) and sentiment analysis (86.4% accuracy)
    #         """)
    #         #st.write("[Github Code](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039%20Report.pdf)")
    #         mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb",)
    #     with image_column:
    #         st.image(images_projects[6])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Data-Driven Marketing: Exploration of cellphone billing and subscriber data")
    #         st.write("*Self-initiated project based on past assignment from module BT4211: Data-Driven Marketing*")
    #         st.markdown("""
    #         - Performed preliminary churn analysis, customer segmentation and descriptive analysis to understand more about dataset
    #         - Trained logit and probit models, as well as providing model estimations for duration models
    #         - Utilised random forest classifier to predict customer churn
    #         """)
    #         #st.write("[Github Repo](https://github.com/harrychangjr/cellphone-billing) | [RPubs](https://rpubs.com/harrychangjr/cellphone)")
    #         mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/cellphone-billing",)
    #     with image_column:
    #         st.image(images_projects[7])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Data Visualization: Analysis on Spotify Dataset from [tidytuesday](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21)")
    #         st.write("*Completed group project for module DSA2101: Essential Data Analytics Tools: Data Visualization in Academic Year 2021/22 Semester 2*")
    #         st.markdown("""
    #         - Investigated variables that differentiates songs of different genres, which could be useful in designing recommendation systems
    #         - Explored how do the four seasons affect number of songs produced in each period
    #         - Visualizations used: ridgeline faceted density plot, boxplot, line chart, faceted donut chart
    #         """)
    #         #st.write("[Github Code](https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd) | [RPubs](https://rpubs.com/harrychangjr/dsa2101-groupb)")
    #         mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd",)
    #     with image_column:
    #         st.image(images_projects[8])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Computers and the Humanities: Chloropleths using Google Sheets and Folium in Python")
    #         st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
    #         st.markdown("""
    #         - Visualized the total number of performances of A Doll's House by country, using a chloropleth from Google Sheets
    #         - Drafted scatterplots and boxplots using seaborn to investigate relationship between number of events per country and number of years these plays have been performed
    #         - Created chloropleth using Folium in Google Colab to compare total performance counts in China, categorised by province
    #         """)
    #         #st.write("[Google Sheets](https://docs.google.com/spreadsheets/d/1NBlGM7Sjcybbpl1Esa55qLRJw-Seti1LhC93EhV_68w/edit?usp=sharing) | [Google Colab](https://colab.research.google.com/drive/1RHqtb5XC7PkJDpNEb-BY3tO-8mI2j32E?usp=sharing)")
    #         mention(label="Google Drive", icon="🗂️", url="https://drive.google.com/drive/folders/1Iva0oLZim6zJlAndoSzR63pUq4NCznim?usp=share_link",)
    #     with image_column:
    #         st.image(images_projects[9])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Computers and the Humanities: Network Analysis on Harry Potter Film Database")
    #         st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
    #         st.markdown("""
    #         - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
    #         - Drafted visualizations using matplotlib and seaborn to compare densities and weighted degree values of nodes from generated networks
    #         - Customised network visualization using Gephi to investigate relationship between various Harry Potter film directors
    #         """)
    #         #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb)")
    #         mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb",)
    #     with image_column:
    #         st.image(images_projects[10])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Computers and the Humanities: Text Processing and Analysis on Song Lyrics")
    #         st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
    #         st.markdown("""
    #         - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
    #         - Drafted visualizations using matplotlib and seaborn to compare proportions of nouns and verbs between different songs
    #         - Analysed type/token ratios of songs from both albums to evaluate which album produced better quality songs based on words used
    #         """)
    #         #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
    #         mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb",)
    #     with image_column:
    #         st.image(images_projects[11])
    # with st.container():
    #     text_column, image_column = st.columns((3,1))
    #     with text_column:
    #         st.subheader("Computers and the Humanities: Spotify in the Covid-19 Era")
    #         st.write("*Completed group project for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
    #         st.markdown("""
    #         - Compiled and scraped Spotify data from [Spotify](https://www.spotifycharts.com), [Kaggle](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks), and [OWID](https://ourworldindata.org/coronavirus/country/singapore) to analyse top songs played in Singapore during Covid-19
    #         - Drafted Tableau dashboard to showcase correlation between various features of top songs, including tempo, acousticness and popularity
    #         - Embedded 30-second snippet of featured song on dashboard for increased interactiveness
    #         """)
    #         #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
    #         mention(label="Final Report", icon="📄", url="https://github.com/harrychangjr/get1030/blob/main/GET1030%20Final%20Project.pdf",)
    #     with image_column:
    #         st.image(images_projects[12])
    
# elif choose == "Competitions":
#     # Create section for Competitions
#     #st.write("---")
#     st.header("Competitions")
#     with st.container():
#         image_column, text_column = st.columns((1,3))
#         with image_column:
#             st.image(img_lit)
#             #st.empty()
#         with text_column:
#             st.subheader("[SMU-LIT Hackathon 2023](https://www.smulit.org/hackathon-2023/) - Hosted by [SMU Legal-in-Tech Club](https://smulit.org)")
#             st.write("Built LegalEase with OpenAI - a Streamlit-based web application empowering lawyers in hybrid working environments with optimal task scheduling.")
#             #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/legalease",)
#     with st.container():
#         image_column, text_column = st.columns((1,3))
#         with image_column:
#             st.image(img_lifehack2)
#             #st.empty()
#         with text_column:
#             st.subheader("[NUS LifeHack 2023](https://lifehack-website.web.app//) - Hosted by [NUS Students' Computing Club](https://nuscomputing.com/)")
#             st.write("Awarded Top 15 Finalist out of 141 team submissions")
#             st.write("Built and integrated PassionPassport with ChatGPT - a Streamlit-based web application that recommends travel locations based on one’s hobbies.")
#             #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
#             mention(label="Github Repo", icon="github", url="https://github.com/BrendanCheong/lifehack-2023",)
#     with st.container():
#         image_column, text_column = st.columns((1,3))
#         with image_column:
#             st.image(img_lifehack)
#         with text_column:
#             st.subheader("[NUS LifeHack 2022](https://lifehack-2022.vercel.app/) - Hosted by [NUS Students' Computing Club](https://nuscomputing.com/)")
#             st.write("Awarded Theme Best - Safety and Overall 2nd Place out of 117 team submissions")
#             st.write("Ideated and developed Drive Woke! - a Flutter-based mobile application that aims to keep drivers awake by simulating conversations")
#             #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
#             mention(label="Github Repo", icon="github", url="https://github.com/yuechen2001/LifeHack2022",)
#     with st.container():
#         image_column, text_column = st.columns((1,3))
#         with image_column:
#             st.image(img_he4d)
#         with text_column:
#             st.subheader("NUS Fintech Month Hackathon 2021 - Hosted by [NUS Fintech Society](https://fintechsociety.comp.nus.edu.sg/)")
#             st.write("Awarded Overall 2nd Place")
#             st.write("Ideated a multi-pronged approach using blockchain and machine learning methods to improve fraud detection amongst complex entities in a digital or hybrid (digital and manual) operating environment")
#             #st.write("[Pitch Deck](https://www.linkedin.com/feed/update/urn:li:ugcPost:6761489595420037120/)")
#             mention(label="Pitch Deck", icon="🪧", url="https://www.linkedin.com/feed/update/urn:li:ugcPost:6761489595420037120/)",)
#     with st.container():
#         image_column, text_column = st.columns((1,3))
#         with image_column:
#             st.image(img_ecc)
#         with text_column:
#             st.subheader("NUS Economics Case Competition - Hosted by [NUS Economics Society](https://www.nuseconsoc.com/)")
#             st.write("Performed financial modelling and market research to suggest methods for brick-and-mortar retailers to compete against e-commerce stores")
#             #st.write("[Report](https://drive.google.com/drive/u/4/folders/1NfsRr1P3xAkuJq3HEJ9LQU1uCo6TZIFK)")
#             mention(label="Report", icon="📄", url="https://drive.google.com/drive/u/4/folders/1NfsRr1P3xAkuJq3HEJ9LQU1uCo6TZIFK",)
#     with st.container():
#         image_column, text_column = st.columns((1,3))
#         with image_column:
#             st.image(img_shopee)
#         with text_column:
#             st.subheader("[Shopee Product and Design Challenge 2021](https://careers.shopee.sg/event-detail/396)")
#             st.write("Redesigned user interface of Shopee mobile app using Figma to reduce clutter and increase user utilization of in-app rewards")
#             #st.write("[Figma Prototype](https://www.figma.com/proto/3UXT29N1RgVGDUlSBeWcPN/UI-Prototype-1?node-id=18-3&viewport=-675%2C231%2C0.32458001375198364&scaling=scale-down) | [Pitch Deck](https://drive.google.com/file/d/12qnveB-SMjG_gF_gwNj3Nr-JsKeyKd6g/view)")
#             mention(label="Figma", icon="📱", url="https://www.figma.com/proto/3UXT29N1RgVGDUlSBeWcPN/UI-Prototype-1?node-id=18-3&viewport=-675%2C231%2C0.32458001375198364&scaling=scale-down",)
#     with st.container():
#         image_column, text_column = st.columns((1,3))
#         with image_column:
#             st.image(img_sbcc)
#         with text_column:
#             st.subheader("Singapore Business Case Competition 2020 - Hosted by [NTU Business Solutions Club](https://clubs.ntu.edu.sg/businesssolutions/)")
#             st.write("Proposed solutions to help increase competitiveness of BreadTalk after performing market research and analysis on the F&B industry")
#             #st.write("[Pitch Deck](https://drive.google.com/file/d/1kLgbBVuth4KvfhjaK00n30xlr4bmn-iM/view)")
#             mention(label="Pitch Deck", icon="🪧", url="https://drive.google.com/file/d/1kLgbBVuth4KvfhjaK00n30xlr4bmn-iM/view",)
#     with st.container():
#         image_column, text_column = st.columns((1,3))
#         with image_column:
#             st.image(img_runes)
#         with text_column:
#             st.subheader("Contest 2.2 Beautiful Runes - CS1010S Programming Methodology")
#             st.write("Awarded 1st Place for 2D Runes category out of over 600 students enrolled in the module for Academic Year 2020/21 Semester 1")
#             st.write("2D pixel art created using Pillow (PIL) Library in Python")
#             #st.write("[Github Repo](https://github.com/harrychangjr/runes)")
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/runes",)
# elif choose == "Volunteering":
#     st.header("Volunteering")
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("NUS Fintech Society")
#             st.write("*August 2023 to April 2024*")
#             st.markdown("""
#             Design Manager (UI/UX Design Lead)


#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[11])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("NUS Human Capital Society")
#             st.write("*July 2023 to April 2024*")
#             st.markdown("""
#             Research & Strategy Executive

#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[10])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("NUS Product Club")
#             st.write("*April 2023 to April 2024*")
#             st.markdown("""
#             Co-founder & President

#             - Designed recruitment posters, club logo and [information deck](https://bit.ly/nuspc-infodeck) using Canva and Figma to increase brand awareness of new club, increasing social media outreach to over 1,000 followers across LinkedIn, Telegram and Instagram within 2 months since club formation
#             - Onboarded Staff Advisor and Product Managers from various industries to organise club events, including fireside chats and curriculum workshops that would better educate students on product management
#             - Currently designing curriculum for future Product Analytics Workshop, covering essential topics including product metrics, A/B testing, predictive analytics and cohort analysis
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[9])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("NUS Statistics and Data Science Society")
#             st.write("*May 2021 to November 2022*")
#             st.markdown("""
#             - President (2022) - Increased recruitment of student club by 50% while overseeing execution of career-related events and technical workshops organised by 56 members
#             - Marketing Director (2021-22) - Led 10 students to secure over $19,000 worth of sponsorships for 850 participants in annual Data Analytics Competition and increase society's merchandise sales revenue by over 50% compared to previous year
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[0])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("NUS Students' Sports Club")
#             st.write("*February to August 2022*")
#             st.markdown("""
#             Publicity Executive, NUS Inter-Faculty Games

#             - Designed storyboard for publicity videos to hype up school-wide event
#             - Increased publicity of event through extended outreach to over 5,000 students in various Telegram groups
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[1])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("Google Developer Student Clubs NUS")
#             st.write("*September 2021 to April 2022*")
#             st.markdown("""
#             Deputy Head of Finance

#             - Managed budget of student club alongside Core Team to ensure sufficient funds for technical workshops, hackathon and external projects
#             - Liaised with staff advisors and administrative staff to seek funding approvals and process financial claims for other student members
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[2])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("NUS Students' Community Service Club")
#             st.write("*March to July 2021*")
#             st.markdown("""
#             Organising Committee, Project Safe Space

#             - Organised weekly sessions to empower individuals from Anglican Care Centre (Yishun) with important life skills (e.g Zumba, cooking)
#             - Drafted write-ups on psychiatric conditions to raise awareness on debunked mental health myths and promote mental welness
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[3])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("NUS Students' Union")
#             st.write("*January to March 2021*")
#             st.markdown("""
#             Public Relations Executive, Open Day Student Village

#             - Liaised with participating student residences and clubs to increase awareness of event to prospective students
#             - Enforced rules and regulations imposed by school administrative staff to ensure smooth execution of event
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[4])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("Saturday Kids")
#             st.write("*October 2020 to December 2021 - Seasonal*")
#             st.markdown("""
#             Python Instructor, Code in the Community

#             - Conducted weekly lessons for classes of 3-4 secondary school students on Python programming 
#             - Customised curriculum structure to suit the learning needs of students
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[5])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("Singapore Institiute of Management - University of London")
#             st.write("*November 2017*")
#             st.markdown("""
#             Fundraising Volunteer, SIM-UOL Transformers

#             - Collected unwanted items from residents in heartland areas
#             - Successfully raised $8000 from sale of items to refurbish the homes of the less fortunate
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[6])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("Tampines Junior College")
#             st.write("*March 2015 to January 2016 - Seasonal*")
#             st.markdown("""
#             Values in Action (VIA) Projects

#             - Climb for A Cause - Organised and participated in games and activities with members of Singapore Disability Sports Council
#             - Project Ohana - Collaborated with Kwong Wai Shiu Hospital to engage patients in handicraft and games
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[7])
#     with st.container():
#         text_column, mid, image_column = st.columns((3,0.4,1))
#         with text_column:
#             st.subheader("Saint Joseph's Institution")
#             st.write("*June 2012 to June 2013 - Seasonal*")
#             st.markdown("""
#             Values in Action (VIA) Projects

#             - Josephian International Experience Programme - Conducted English lessons at orphanage in Siem Reap, Cambodia
#             - SJIJ Primary 4 Chinese Language Camp - Acted as group facilitator to orientate primary four students in Chinese lessons
#             """)
#         with mid:
#             st.empty()
#         with image_column:
#             st.image(images_vol[8])
elif choose == "Blog":
    st.header("Blog")
    st.write("Coming Soon!")

elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1N6n1v52rHJ5Rk1tJDfwB488UR3afPTi7/view?usp=sharing"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (1 page)**"), unsafe_allow_html=True)
    show_pdf("yousuf_resume.pdf")
    with open("yousuf_resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (1 page)",
            data=file,
            file_name="HarryChang_Resume.pdf",
            mime="application/pdf"
        )
elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,0.5))
        with text_column:
            st.write("Let's connect! You may either reach out to me at shabibiyousuf@gmail.com or use the form below!")
            #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                #st.write('Please help us improve!')
                #Name=st.text_input(label='Your Name',
                                    #max_chars=100, type="default") #Collect user feedback
                #Email=st.text_input(label='Your Email', 
                                    #max_chars=100,type="default") #Collect user feedback
                #Message=st.text_input(label='Your Message',
                                        #max_chars=500, type="default") #Collect user feedback
                #submitted = st.form_submit_button('Submit')
                #if submitted:
                    #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
            def create_database_and_table():
                conn = sqlite3.connect('contact.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (name TEXT, email TEXT, message TEXT)''')
                conn.commit()
                conn.close()
            create_database_and_table()

            st.subheader("Contact Form")
            if "name" not in st.session_state:
                st.session_state["name"] = ""
            if "email" not in st.session_state:
                st.session_state["email"] = ""
            if "message" not in st.session_state:
                st.session_state["message"] = ""
            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


            column1, column2= st.columns([1,5])
            if column1.button("Submit"):
                conn = sqlite3.connect('contact.db')
                c = conn.cursor()
                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                conn.commit()
                conn.close()
                st.success("Your message has been sent!")
                # Clear the input fields
                st.session_state["name"] = ""
                st.session_state["email"] = ""
                st.session_state["message"] = ""
            
            def delete_contact(name):
                conn = sqlite3.connect('contact.db')
                c = conn.cursor()
                c.execute("DELETE FROM contacts WHERE name=?", (name,))
                conn.commit()
                conn.close()
                
            def fetch_all_contacts():
                conn = sqlite3.connect('contact.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts")
                rows = c.fetchall()
                conn.close()
                return rows
            
            
            if "show_contacts" not in st.session_state:
                st.session_state["show_contacts"] = False
            if column2.button("View Submitted Forms"):
                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            if column2.button("Delete All Submitted Forms"):
                st.session_state["show_contacts"] = False
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    for contact in all_contacts:
                        delete_contact(contact[0])
                    st.success("All contacts have been deleted.")
                else:
                    st.warning("No contacts found.")
            if st.session_state["show_contacts"]:
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                    st.markdown(markdown_table)
                else:
                    st.write("No contacts found.")


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/yousufshabibi/"
            github_url = "https://github.com/Shabibi2003"
            email_url = "shabibiyousuf@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()
        # with image_column:
        #     st.image(img_ifg)
# st.markdown("*Copyright © 2023 Yousuf Shabibi*")

