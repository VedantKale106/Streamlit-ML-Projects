import streamlit as st
import pandas as pd
import csv

def app():
    st.title("Contact Us")
    st.write("Feel free to reach out to us with any questions or to enroll your child.")
    
    st.header("Our Contact Information")
    st.write("""
        **Address:** 6V5G+CHW, Brahman Budhwar Peth, Junnar, Maharashtra 410502\n
        **Phone:** +123 456 7890\n
        **Email:** contact@adarshcoaching.com
    """)
    
    st.header("Office Hours")
    st.write("""
        - Monday to Friday: 9:00 AM - 6:00 PM
        - Saturday: 10:00 AM - 4:00 PM
        - Sunday: Closed
    """)
    
    st.header("Find Us Here")
    
    # Example location (Bangalore, India)
    location_data = pd.DataFrame({
        'LAT': [19.2084],
        'LON': [73.8764]
    })
    
    st.map(location_data)  # Display map using OpenStreetMap
    
    st.write("Alternatively, you can fill out the form below to get in touch with us.")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            # Save data to CSV file
            with open('contact_data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, email, message])
            
            st.success("Thank you! We have received your message.")

if __name__ == "__main__":
    app()
