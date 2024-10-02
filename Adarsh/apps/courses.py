import streamlit as st

def app():
    st.title("Courses Offered")
    st.write("We offer a variety of courses to cater to the needs of students from 5th to 12th standard.")
    
    st.header("5th to 10th Standard")
    st.write("""
        **Subjects Offered:**
        - Mathematics
        - Science
        - English
        - Social Studies

        Our courses are designed to build a strong foundation in these subjects, with a focus on conceptual understanding and practical application.
    """)
    
    st.header("11th and 12th Science")
    st.write("""
        **Subjects Offered:**
        - Physics
        - Chemistry
        - Mathematics
        - Biology
        - Computer Science

        We prepare students for board exams and competitive entrance exams like IIT-JEE, NEET, and others. Our teaching methods include:
        - Regular assessments
        - Interactive sessions
        - Personalized guidance
    """)
    
    st.header("Special Features")
    st.write("""
        - **Doubt Clearing Sessions:** Dedicated time for resolving individual queries.
        - **Mock Tests:** Regular practice tests to evaluate progress and prepare for exams.
        - **Workshops:** Special workshops on exam strategies, time management, and career guidance.
    """)
