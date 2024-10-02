import streamlit as st
from PIL import Image

# Function to set up the sidebar
def sidebar():
    st.sidebar.title("Adarsh Coaching Classes")
    st.sidebar.markdown("Navigate through the sections:")
    pages = ["About Us", "Gallery", "Contact Us", "Courses Offered"]
    page = st.sidebar.radio("Go to", pages)
    return page

# About Us Page
def about_us():
    st.title("About Us")
    st.image("1.jpg", use_column_width=True)
    st.write("""
        Welcome to Adarsh Coaching Classes! We provide quality education for students from 5th to 12th standard.
        Our mission is to foster a love of learning and help students achieve their academic goals.
    """)
    st.write("""
        Our experienced faculty, modern teaching methods, and a nurturing environment make us the perfect choice for your child's education.
    """)

# Gallery Page
def gallery():
    st.title("Gallery")
    st.write("Here are some pictures from our coaching classes.")
    images = ["2.jpg", "3.jpg", "4.jpg"]
    for img in images:
        image = Image.open(img)
        st.image(image, caption=f"Image: {img}", use_column_width=True)

# Contact Us Page
def contact_us():
    st.title("Contact Us")
    st.write("Feel free to reach out to us with any questions or to enroll your child.")
    st.write("""
        **Address:** 1234 Education Lane, Knowledge City, Country
        **Phone:** +123 456 7890
        **Email:** contact@adarshcoaching.com
    """)
    st.write("Alternatively, you can fill out the form below to get in touch with us.")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you! We have received your message.")

# Courses Offered Page
def courses_offered():
    st.title("Courses Offered")
    st.write("We offer a variety of courses to cater to the needs of students from 5th to 12th standard.")
    courses = {
        "5th to 10th Standard": ["Mathematics", "Science", "English", "Social Studies"],
        "11th and 12th Science": ["Physics", "Chemistry", "Mathematics", "Biology"]
    }
    for grade, subjects in courses.items():
        st.write(f"**{grade}:**")
        st.write(", ".join(subjects))

# Main function to control the app flow
def main():
    page = sidebar()
    if page == "About Us":
        about_us()
    elif page == "Gallery":
        gallery()
    elif page == "Contact Us":
        contact_us()
    elif page == "Courses Offered":
        courses_offered()

if __name__ == "__main__":
    main()
