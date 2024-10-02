import streamlit as st
import webbrowser
import skills
import projects
import education

# Your details
name = "Vedant Kale"
bio = "🚀 Passionate and innovative, I thrive in Python, Machine Learning, Android Development, C/C++, Java, and Data Structures & Algorithms. Proficient in Jupyter Notebook, Git, and GitHub, I drive impactful tech projects to success🌟. Eager to lead and shape innovation, let's connect and transform the tech landscape!  With a love for reading books, watching Anime, and playing games, I find inspiration and relaxation in these pursuits. 😁 Let's collaborate and push boundaries together, creating remarkable solutions that leave a lasting impact 🤝"
email = "vedant.kale22@pccoepune.org"
phone = "+91-8421204009"
linkedin = "https://www.linkedin.com/in/vedant-kale-a057b2257/"
github = "https://github.com/VedantKale106"
profile_pic = "img.jpg"
whatsapp_link = "https://wa.me/918421204009"  # WhatsApp chat link with your number

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Page navigation
def navigate_to(page):
    st.session_state.page = page

# Configure the page
st.set_page_config(page_title=f"{name} - Portfolio", layout="wide")

# Sidebar with navigation
with st.sidebar:
    st.title("Navigation")
    if st.button("Home"):
        navigate_to('home')
    if st.button("Skills"):
        navigate_to('skills')
    if st.button("Projects"):
        navigate_to('projects')
    if st.button("Education"):
        navigate_to('education')

# Page content based on the current page in session state
if st.session_state.page == 'home':
    st.title(f"Welcome to My Portfolio Website\n")

    # Main content
    col1, col2 = st.columns([4, 7])  # Adjust column width as needed
    with col1:
        st.image(profile_pic, width=300, use_column_width=True, output_format='PNG')
    with col2:
        st.write(f"# {name}")
        st.write(bio)

    # Contact details
    st.subheader("Contact Me")
    st.write(f"📧 [Email](mailto:{email})")
    st.write(f"📞 {phone}")
    st.write(f"🔗 [LinkedIn]({linkedin})")
    st.write(f"💻 [GitHub]({github})")
    if st.button("Contact via WhatsApp", key='whatsapp_home'):
        webbrowser.open(whatsapp_link)
elif st.session_state.page == 'skills':
    skills.app()
elif st.session_state.page == 'projects':
    projects.app()
elif st.session_state.page == 'education':
    education.app()

# Adding a footer in the bottom right corner
st.markdown("""
    <style>
        footer {
            visibility: hidden;
        }
        .footer {
            visibility: visible;
            position: fixed;
            right: 0;
            bottom: 0;
            text-align: right;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        Made by Vedant Kale 🫡
    </div>
""", unsafe_allow_html=True)
