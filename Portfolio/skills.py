import streamlit as st
from PIL import Image

def app():
    st.title("Skills")

    skills = [
        {"name": "Python", "logo": "Logos/python.jpeg"},
        {"name": "C", "logo": "Logos/c.jpeg"},
        {"name": "C++", "logo": "Logos/cpp.jpeg"},
        {"name": "Java", "logo": "Logos/java.jpeg"},
        {"name": "SQL", "logo": "Logos/mysql.jpeg"},
        {"name": "GitHub", "logo": "Logos/github.jpeg"},
        {"name": "Jupyter", "logo": "Logos/jupyter.jpeg"},
        {"name": "Android Studio", "logo": "Logos/jupp.jpeg"},
        {"name": "Machine Learning", "logo": "Logos/ml.jpeg"},
        {"name": "Data Science", "logo": "Logos/ds.jpeg"},
        {"name": "Data Structures and Algorithms", "logo": "Logos/dsa.jpeg"},
    ]

    # Display skills in a grid layout
    num_columns = 3
    columns = st.columns(num_columns)
    for i, skill in enumerate(skills):
        with columns[i % num_columns]:
            img = Image.open(skill["logo"]).convert("RGBA")
            img = img.resize((120, 120))  # Ensure consistent size
            st.image(img, width=200)
            st.write(f"**{skill['name']}**")

if __name__ == "__main__":
    app()
