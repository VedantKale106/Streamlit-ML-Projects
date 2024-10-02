import streamlit as st

def app():
    st.title("Projects")

    projects = [
        {
            "name": "SalaryScope",
            "description": "A comprehensive machine learning project designed to predict the salary of software engineers based on various parameters such as experience, education level, and location. Leveraging advanced data analysis techniques and machine learning algorithms including regression and ensemble methods, SalaryScope provides accurate salary estimations, aiding both job seekers and employers in making informed decisions.",
            "link": "https://github.com/VedantKale106/SalaryScope",
            "image": "Screenshots/SalaryScope.png"
        },
        {
            "name": "RentWizard",
            "description": "RentWizard is an intelligent rental price prediction tool tailored for real estate markets. By analyzing factors such as property size, number of rooms, amenities, and market trends, RentWizard forecasts rental prices with high precision. Utilizing regression techniques, it offers valuable insights to landlords, tenants, and property investors, facilitating optimal rental pricing strategies and negotiations.",
            "link": "https://github.com/VedantKale106/RentWizard",
            "image": "Screenshots/RentWizard.png"
        },
        {
            "name": "MovieMatch",
            "description": "MovieMatch is a movie recommendation and search system that helps users discover new movies based on their preferences. Utilizing collaborative filtering and content-based algorithms, MovieMatch provides personalized movie suggestions and allows users to search for movies by genre, actor, director, and more. This project enhances the movie-watching experience by making it easier for users to find movies they will enjoy.",
            "link": "https://github.com/VedantKale106/MovieMatch",
            "image": "Screenshots/MovieMatch.png"
        }
    ]

    for project in projects:
        st.subheader(project["name"])
        col1, col2 = st.columns([1.5, 2.5])  # Adjusted column widths
        with col1:
            st.image(project["image"], caption=project["name"], use_column_width=True)  # Use Streamlit's image function
        with col2:
            st.write(project["description"])
            st.markdown(f"[GitHub Repository]({project['link']})")

if __name__ == "__main__":
    app()
