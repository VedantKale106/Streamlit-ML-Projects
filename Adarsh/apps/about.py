import streamlit as st

def app():
    st.title("About Us")
    st.image("1.jpg", use_column_width=True)
    st.write("""
        Welcome to Adarsh Coaching Classes! We provide quality education for students from 5th to 12th standard.
        Our mission is to foster a love of learning and help students achieve their academic goals.
    """)
    
    st.header("Our History")
    st.write("""
        Adarsh Coaching Classes was established in 2000 with a vision to provide exceptional educational services.
        Over the past two decades, we have grown into a reputed institution known for our dedication to student success.
    """)

    st.header("Our Mission")
    st.write("""
        Our mission is to empower students with the knowledge and skills they need to excel academically and in life.
        We believe in holistic development and strive to create an engaging and supportive learning environment.
    """)

    st.header("Meet Our Faculty")
    
    faculty_members = [
        {
            "name": "Mule Sir",
            "description": "Algebra Expert with 15 years of teaching experience.",
            "image": "1.jpg"
        },
        {
            "name": "Malve Sir",
            "description": "Geometry Expert with 15 years of teaching experience.",
            "image": "2.jpg"
        },
        {
            "name": "Manoj Sir",
            "description": "English Literature and Language Educator with a focus on critical thinking and communication skills.",
            "image": "4.jpg"
        }
    ]
    
    for faculty in faculty_members:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(faculty["image"])
        with col2:
            st.write(f"**{faculty['name']}**")
            st.write(faculty["description"])

if __name__ == "__main__":
    app()
