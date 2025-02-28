import streamlit as st
st.set_page_config(page_title="Roushan Kumar, Data Scientist", page_icon=":robot:",layout="wide")
from PIL import Image
from my_utils.media_cart import render_media_card, centered_display,render_skill_card
from descriptions import *

st.markdown('''<style>body{
            .st-emotion-cache-u9848z {
                width: 1370.4px;
                position: relative;
                display: flex
            ;
                flex: 1 1 0%;
                flex-direction: column;
                gap: 0.5rem;
            }
            }</style>''',
            unsafe_allow_html=True
            )

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Roushan Kumar, Data Scientist
##### *Portfolio*
''')

col1, col2, col3 = st.columns([0.55, 1, 1],gap="large")
with col2:
  image = Image.open(r'.assets/me2.png')
  st.image(image, width=150)

col1, col2, col3 = st.columns([1, 2.5, 1],gap="large")
with col2:
  centered_display("Summary")
  # st.markdown('## Summary', unsafe_allow_html=True)
  st.info('''
  - Hi there! I’m a Data Scientist with 2 years of experience, passionate about crafting scalable AI solutions. My expertise in **Python** drives my work in **LLMs**, **NLP**, and **ML**, creating impactful real-world systems. 
  - I developed a **91%-accurate BERT-based grievance classification model**, integrated into an AI agent for routing grievances effectively. I’ve also built multilingual AI voice assistants using **Whisper**, **Bhashini**, and **Azure OpenAI** to make technology accessible.
  - My work spans **YOLO-based canal monitoring systems**, deploying AI on **Azure** with **Docker** and **DRF**, and building intuitive interfaces with **Streamlit**. I excel in tools like **PyTorch**, **Langchain**, **Numpy**, **Pandas**, **Huggingface** for end-to-end AI solutions.
  ''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Roushan Kumar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#professional-projects">Professional Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#independent-projects">Independent Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#achievements">Achievements</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

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

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(project_name, project_title, project_desc,skills,github_url = None):
  col1, col2, col3 = st.columns([1,3,2])
  with col1:
    st.markdown(f'###### {project_name}')
  with col2:
    # st.markdown(project_title)
    with st.expander(f"{project_title}"):
      st.write(
              project_desc
          )
  with col3:
    render_skill_card(
        skills=skills,
    )

def achievements(title, desc, link):
  col1, col2,col3 = st.columns([2,4,1])
  with col1:
    st.markdown(title)
  with col2:
    st.markdown(desc)
  with col3:
    st.markdown(link)

#####################
centered_display("Professional Projects")
st.divider()
with st.container():
  # row 1
  col1,col2,col3 = st.columns(3,gap="small")
  with col1:
    render_media_card(
        title="Grievance allocation whatsapp assistant",
        description="",
        video_url="https://youtu.be/",
        skills=['Python', 'AzureOpenAI','NLP','Langchain', 'Azure','Docker', 'Django','BERT','pytorch','Huggingface','Bhashini'],
        # github_url="https://github.com/username/repo", # Optional
    )
    with st.expander("More info"):
      st.write(
              whatsapp_agent
          )

  with col2:
    render_media_card(
        title="Jalvigil",
        description="",
        video_url="https://youtu.be/D1NCk3nZqWg",
        skills=['Python', 'CV','yolov7','GAN','Streamlit','Deep Learning','Analytics'],
        # github_url="https://github.com/username/repo"
        )
    with st.expander("More info"):
      st.write(
              jalvigil_desc
          )
    
  with col3:
    render_media_card(
        title="Auto form filling assistant(POC)",
        description="",
        video_url="https://youtu.be/knANew36qdo",
        skills=['Python', 'NLP','Whisper','Bhashini','AzureOpenAI','Django','Docker','streamlit'],
        # github_url="https://github.com/username/repo"
        )
    with st.expander("More info"):
      st.write(
              autoform_desc
          )
  # row 2
  col1,col2,col3 = st.columns(3,gap="small")
  with col1:
    render_media_card(
        title="GenBI(POC)",
        description="",
        video_url="https://youtu.be/your_video_id",
        skills=['Python', 'NLP','SQL','AzureOpenAI','AI Agents','Streamlit','Chroma vectorstore','RAG','Bhashini'],
        # github_url="https://github.com/username/repo", # Optional
    )
    with st.expander("More info"):
      st.write(
              genbi_description
          )
    
  with col2:
    render_media_card(
        title="ASHA(POC)",
        description="",
        video_url="https://youtu.be/U-gkH3PucOQ",
        skills=['Python','AzureOpenAI','ASR','Whisper','Bhashini','Custom RAG','NLP'],
        # github_url="https://github.com/username/repo"
        )
    with st.expander("More info"):
      st.write(
              asha_desc
          )

st.divider()
#####################
centered_display("Independent Projects")
st.divider()
txt4(project_name='Chakshu', 
     project_title='Intelligent OCR tool', 
     project_desc=chakshu_desc,
     skills=['Python', 'CV','yolo','Tesseract','Deep Learning','LLMs']
     )
st.divider()
#####################
centered_display("Achievements",left=1.4)


st.divider()
achievements(title='Client Extraordinaire (2024-April)',
              desc='Awarded for exceptional and innovative GenAI solutions for clients',
              link='[Certificate](https://drive.google.com/file/d/1jRcmdfn-QXyK2-fUKpsckJA50kUG5iMJ/view?usp=sharing)'
              ) 
achievements(title='Client Extraordinaire (2024-December)',
              desc='Awarded for deploying WhatsApp grievance auto-allocation, JalVigil, and for being a client extraordinaire',
              link='[Certificate](https://drive.google.com/file/d/1NgU1xw17hKG17JPpwl9IKFMiTpO2qRNb/view?usp=sharing)'
              ) 
# txt('Programming', '`Python`, `R`, `Linux`')
# txt2('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
# # txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
# # txt3('Machine Learning', '`scikit-learn`')
# # txt3('Deep Learning', '`TensorFlow`')
# # txt3('Web development', '`Flask`, `HTML`, `CSS`')
# # txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')
# st.divider()

#####################
# centered_display("Certifications",left=1.4)

# st.divider()
# txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
# txt2('Twitter', 'https://twitter.com/thedataprof')
# txt2('GitHub', 'https://github.com/chaninn/')
# txt2('', 'https://github.com/chaninlab/')
# txt2('', 'https://github.com/dataprofessor')
# txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
# txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
# txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
# txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
# txt2('Publons', 'https://publons.com/a/303133/')
# st.divider()