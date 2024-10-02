import streamlit as st
from PIL import Image

def app():
    st.title("Gallery")
    st.write("Here are some pictures from our coaching classes.")
    
    images = ["1.jpg", "1.jpg", "1.jpg"]
    captions = ["Annual Science Exhibition", "Classroom Session", "Sports Day Celebration"]
    
    for img, caption in zip(images, captions):
        image = Image.open(img)
        st.image(image, caption=caption, use_column_width=True)
    
    st.write("""
        Our gallery showcases the vibrant and dynamic environment at Adarsh Coaching Classes.
        From academic excellence to extracurricular achievements, we celebrate the holistic development of our students.
    """)
