import pickle 
import streamlit as st
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### We need some Information to predict the salary""")

    # Add the custom text at the bottom right corner
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            right: 10px;
            bottom: 10px;
            font-size: 12px;
            color: gray;
        }
        </style>
        <div class="footer">
        Made by Vedant Kale
        </div>
        """,
        unsafe_allow_html=True
    )

show_predict_page()

countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

educations = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

country = st.selectbox("Country",countries)
education = st.selectbox("Education Level",educations)

exp = st.slider("Years of Experience", 0, 50, 5)

ok = st.button("Calculate Salary")

if ok:
    X = np.array([[country,education,exp]])
    X[:,0] = le_country.transform(X[:,0])
    X[:,1] = le_education.transform(X[:,1])
    X = X.astype(float)

    salary = regressor.predict(X)
    salary = salary * 82
    st.subheader(f"The Estimated Salary is {salary[0]:.2f}Rs per Annum")
