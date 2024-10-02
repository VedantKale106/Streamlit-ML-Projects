import streamlit as st
from PIL import Image
import apps.about as about
import apps.gallery as gallery
import apps.contact as contact
import apps.courses as courses

# Function to display the Home page
def home():
    st.title("Welcome to Adarsh Coaching Classes")
    st.image("1.jpg", use_column_width=True)
    st.write("""
        Adarsh Coaching Classes provides quality education for students from 5th to 12th standard.
        We aim to foster a love of learning and help students achieve their academic goals.
    """)
    
    st.header("Why Choose Us?")
    st.write("""
        - Experienced and dedicated faculty
        - Modern teaching methods
        - Personalized attention
        - Excellent track record of results
        - State-of-the-art infrastructure
    """)
    
    st.header("Testimonials")
    
    testimonials = [
        {
            "text": "Adarsh Coaching Classes transformed my learning experience. The teachers are incredibly supportive and knowledgeable. I was able to overcome my weaknesses in mathematics and science, and now I excel in both subjects.",
            "author": "Student A",
            "image": "1.jpg"
        },
        {
            "text": "I achieved top marks thanks to the excellent guidance and teaching at Adarsh Coaching Classes. The personalized attention and modern teaching methods made all the difference in my academic journey.",
            "author": "Student B",
            "image": "2.jpg"
        }
    ]
    
    for testimonial in testimonials:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(testimonial["image"])
        with col2:
            st.write(f"**{testimonial['author']}**")
            st.write(testimonial["text"])

# Main function to control the app flow
def main():
    st.sidebar.title("Navigation")
    
    if st.sidebar.button("Home"):
        st.session_state.page = 'Home'
    if st.sidebar.button("About Us"):
        st.session_state.page = 'About Us'
    if st.sidebar.button("Gallery"):
        st.session_state.page = 'Gallery'
    if st.sidebar.button("Contact Us"):
        st.session_state.page = 'Contact Us'
    if st.sidebar.button("Courses Offered"):
        st.session_state.page = 'Courses Offered'

    # Initialize page state
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'

    # Display the selected page
    if st.session_state.page == 'Home':
        home()
    elif st.session_state.page == 'About Us':
        about.app()
    elif st.session_state.page == 'Gallery':
        gallery.app()
    elif st.session_state.page == 'Contact Us':
        contact.app()
    elif st.session_state.page == 'Courses Offered':
        courses.app()

if __name__ == "__main__":
    main()
