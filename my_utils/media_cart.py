import streamlit as st
from PIL import Image

def get_youtube_id(url):
    """Extract YouTube video ID from URL"""
    if 'youtu.be' in url:
        return url.split('/')[-1]
    elif 'youtube.com' in url:
        if 'v=' in url:
            return url.split('v=')[1].split('&')[0]
    return url  

def render_media_card(
    title,
    description,
    video_url,
    skills=[],
    github_url=None,
):
    card_style = """
        <style>
        .media-card {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 16px;
            margin-bottom: 16px;
            height: 375px; /* Fixed height */
            overflow: hidden; /* Ensures content doesn't overflow */
        }
        .media-card h5 {
            margin-top: 0;
            text-align: center;
        }
        .media-card a {
            color: #007BFF;
            text-decoration: none;
        }
        .media-card a:hover {
            text-decoration: underline;
        }
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 16px;
        }
        .skill-tag {
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
            color: #fff;
            background-color: #6c757d;
        }
        .skill-tag.python { background-color: #ffcc00; color: #000; }
        .skill-tag.langchain { background-color: #28a745; }
        .skill-tag.pandas { background-color: #17a2b8; }
        .skill-tag.numpy { background-color: #ffc107; color: #000; }
        .skill-tag.django { background-color: #6610f2; }
        .skill-tag.streamlit { background-color: #fd7e14; }
        .skill-tag.pytorch { background-color: #d9534f; }
        .skill-tag.cv { background-color: #5bc0de; }
        .skill-tag.huggingface { background-color: #6f42c1; }
        .skill-tag.azure { background-color: #0078d7; }
        .skill-tag.docker { background-color: #0dcaf0; }
        .skill-tag.git { background-color: #f1502f; }
        .skill-tag.linux { background-color: #4caf50; }
        .skill-tag.llms { background-color: #8e44ad; color: #fff; }
        .skill-tag.nlp { background-color: #3498db; color: #fff; }
        .skill-tag.bhashini { background-color: #ff5722; color: #fff; }
        .skill-tag.azureopenai { background-color: #1e90ff; color: #fff; }

        </style>    
    """
    st.markdown(card_style, unsafe_allow_html=True)

    # Create HTML for skills
    skills_html = ""
    for skill in skills:
        skill_class = skill.lower().replace(" ", "-")  # Generate class names
        skills_html += f'<span class="skill-tag {skill_class}">{skill}</span>'

    skills_container = f"""
        <div class="skills-container">
            {skills_html}
        </div>
    """ if skills else ""

    video_id = get_youtube_id(video_url)

    if github_url:
        card_content = f"""
        <div class="media-card">
            <h5>{title}</h5>
            <p style="text-align: center;">{description}</p>
            <div class="video-container">
                <iframe 
                    width="100%" 
                    height="200"
                    src="https://www.youtube.com/embed/{video_id}"
                    title="{title}"
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>
            {skills_container}
            <p><a href="{github_url}" target="_blank">View on GitHub</a></p>
        </div>
        """
    else:
        card_content = f"""
        <div class="media-card">
            <h5>{title}</h5>
            <p style="text-align: center;">{description}</p>
            <div class="video-container">
                <iframe 
                    width="100%" 
                    height="200"
                    src="https://www.youtube.com/embed/{video_id}"
                    title="{title}"
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>
            {skills_container}
        </div>
        """
    st.markdown(card_content, unsafe_allow_html=True)



# def centered_display(content):
#     _, col2, _ = st.columns([1.15, 1, 1])
#     with col2:
#         st.markdown(f"## {content}")

def centered_display(content,left=1.15,center=1,right=1):
    _, col2, _ = st.columns([left, center, right])
    with col2:
        st.markdown(f"## {content}")


