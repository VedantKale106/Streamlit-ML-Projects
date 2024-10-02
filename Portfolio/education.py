import streamlit as st

def app():
    st.title("Education")

    education_details = [
        {
            "name": "Bachelor of Technology in Computer Science (Pursuing)",
            "institution": "Pimpri Chinchwad College of Engineering (PCCOE)",
            "year": "Currently in third year",
            "cgpa": "7.8",
            "image": "Education/pccoe.jpeg",
            "caption": "PCCOE"
        },
        {
            "name": "Higher Secondary School Certificate (HSC), 2022",
            "school": "G.R.P.Sabnis College, Narayangaon",
            "percentage": "79.83% (PCM)",
            "image": "Education/grps.jpeg",
            "caption": "G.R.P.Sabnis College"
        },
        {
            "name": "Secondary School Certificate (SSC), 2020",
            "school": "Shakarrao Butte Patil Vidyalaya, Junnar",
            "percentage": "93.40%",
            "image": "Education/sbp.jpeg",
            "caption": "Shakarrao Butte Patil Vidyalaya"
        }
    ]

    for education in education_details:
        st.markdown(f"## {education['name']}")
        col1, col2 = st.columns([1, 3])  # Adjust the column ratios as needed

        with col1:
            st.image(education["image"], caption=education["caption"], use_column_width=True)

        with col2:
            st.write(f"- **Institution/School:** {education.get('institution', education.get('school'))}")
            st.write(f"- **Year:** {education.get('year', '')}")
            st.write(f"- **CGPA/Percentage:** {education.get('cgpa', education.get('percentage'))}")

# Run the Streamlit app
if __name__ == '__main__':
    app()
