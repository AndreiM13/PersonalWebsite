from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Andrei Macovei", page_icon=":tada:", layout="wide")


def load_lottiurl(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):

    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("styles/style.css")


# -----LOAD ASSETS----

LOTTIE_URL = "https://lottie.host/827823ff-5ea9-4bc9-9cdd-eb7da9919c3f/g0cyw6CSGC.json"
NLP_IMAGE_PATH = "images/nlp.PNG"
DASH_IMAGE_PATH = "images/dash.PNG"
TWITTER_IMAGE_PATH = "images/Capture.PNG"
GITHUB = "https://th.bing.com/th/id/OIP.8SVgggxQcO5L6Dw_61ac4QHaEK?w=297&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7"
LINKEDIN = "https://th.bing.com/th?q=LinkedIn+Logo+Outline&w=120&h=120&c=1&rs=1&qlt=90&cb=1&dpr=1.3&pid=InlineBlock&mkt=pt-PT&cc=PT&setlang=en&adlt=strict&t=1&mw=247"

# ----HEADER SEACTION-----

with st.container():
    st.subheader("Hi, I'm Andrei! :wave:")
    st.title("I'm a Master's Student in Data Science and Advanced Analytics")
    st.write(
        "I'm passionate about coding, especially in Python. I'm also interested in web development, data analysis, and NLP.")

# ---ABOUT ME ----

with st.container():
    st.write("---")

    left_column, right_column = st.columns(2)

    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """
            My passion for technology began at a young age when I endeavored to understand how computers work. 
            Currently, I'm actively developing my skills in Python, NLP, and data analysis. 
            Additionally, I'm in the process of learning HTML, CSS, and JavaScript.

            """
        )
    with right_column:
        st_lottie(LOTTIE_URL, height=300, key="coding")



# --PROJECTS--

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(NLP_IMAGE_PATH)
    with text_column:
        st.subheader("Predicting Airbnb Unlisting-NLP Project")
        st.write(
            """
            Description:
        This NLP project, undertaken as part of a Text Mining course, involved the development of a predictive pipeline
         using Python and Jupyter Notebook.
        
        Problem Solved:
        The primary objective was to predict unlisted properties within datasets, leveraging NLP techniques to extract valuable insights 
        from textual data.
        
        Tools Utilized:
        Key tools included Python for flexibility, NLP methods for text analysis, and Jupyter Notebook 
        for an efficient and interactive workflow.
        
         

            """
        )
        st.markdown("[Github repository](https://github.com/AndreiM13/Predicting-Airbnb-Unlisting)")


with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(DASH_IMAGE_PATH)
    with text_column:
        st.subheader("Electricity Production By Source -Data Visualization Project")
        st.write(
            """
            Description:
            This project was collaboratively undertaken by four students from NOVA IMS as part of a Data Visualization course. 
            The project's focus was on the creation of an interactive dashboard using Python and Dash.
            
            Problem Solved:
            The aim of the project was to design and implement a dynamic and user-friendly dashboard for effective data visualization and presentation.
            
            Tools Utilized:
            Key tools and technologies employed in this project encompassed Python for scripting, Dash for interactive web applications,
             and CSS/HTML for styling and web design.

            """
        )
        st.markdown("[Github repository](https://github.com/AndreiM13/Electricity-Production-By-Source)")
        st.markdown("[Website]( https://electricity-production.onrender.com)")

with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(TWITTER_IMAGE_PATH)
    with text_column:
        st.subheader("Twitter Homepage Clone -Web Development Project")
        st.write(
            """

            Description:
            This project involved the creation of a clone for Twitter's homepage.
             It was designed as a personal learning endeavor.
            
            Objective:
            The primary objective of this project was to acquire and develop new skills, particularly 
            in the areas of web development, HTML, and CSS.
            
            Tools Utilized:
            Key tools employed in this project encompassed HTML for structuring web content
             and CSS for styling, ultimately enabling the recreation of Twitter's homepage.

            """
        )
        st.markdown("[Github repository](https://github.com/AndreiM13/Twitter-HomePage-Clone)")


#---CONTACT-----


with st.container():

    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
     <form action="https://formsubmit.co/macoveiandrei13@yahoo.fr" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email"  required>
     <textarea name="message" placeholder="Your message here" required> </textarea>
     <button type="submit">Send</button>
        </form>
    """

    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()



#---FOOTER---

GITHUB_URL = "https://github.com/AndreiM13"
LINKEDIN_URL ="https://www.linkedin.com/in/andrei-macovei-bbaa7b1a6"

with st.container():
    # Use HTML and CSS for the footer
    st.markdown(
        f"""
        <style>
        /* Add your custom CSS styles here */
        .footer-content {{
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: rgba(14, 17, 23, 0.5);
            padding: 10px;
            margin-top: 190px;
    
        }}
        .footer-content a {{
            margin: 0 10px;
            text-decoration: none;
            color: black;
        }}
        .footer-content img {{
            width: 60px;  /* Adjust the width of the images as needed */
            height: 30px;
            margin-right: 5px; /* Add some spacing between the image and text */
            border-radius: 20px;
        }}
        </style>
        <div class="footer-content">
            <a href="{GITHUB_URL}" target="_blank"><img src="{GITHUB}" alt="GitHub"></a>
            <a href="{LINKEDIN_URL}" target="_blank"><img src="{LINKEDIN}" alt="LinkedIn"></a>
        </div>
        """,
        unsafe_allow_html=True,
    )











