import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
import altair as alt

# Loading model
with open('medical_model.pkl', 'rb') as file:
    model = pickle.load(file)

data = pd.read_csv('dataset.csv')

# Transforming data
label_encoder = LabelEncoder()
data['prognosis'] = label_encoder.fit_transform(data['prognosis'])

st.title('MediScan 🥼')
st.write("Welcome to MediScan. Please select your symptoms from the list below to get a prediction of the possible disease.")

# Converting case
symptom_map = {symptom: symptom.replace('_', ' ').title() for symptom in data.columns[:-1]}
reverse_symptom_map = {v: k for k, v in symptom_map.items()}

# Using Multiselect
symptoms_display = list(symptom_map.values())
selected_symptoms_display = st.multiselect('Select your symptoms', symptoms_display, help="Select symptoms that you are experiencing.")

selected_symptoms = [reverse_symptom_map[symptom] for symptom in selected_symptoms_display]

# Data Input
input_data = np.zeros(len(symptom_map))
for symptom in selected_symptoms:
    index = list(symptom_map.keys()).index(symptom)
    input_data[index] = 1

input_df = pd.DataFrame([input_data], columns=symptom_map.keys())

# Predicting
if st.button('Predict'):
    if len(selected_symptoms) == 0:
        st.warning('Please select symptoms before predicting.')
    else:
        with st.spinner('Predicting...'):
            prediction = model.predict(input_df)
            disease = label_encoder.inverse_transform(prediction)
            st.success(f'The predicted disease is: {disease[0]}')

st.sidebar.title('About')
st.sidebar.info("""
    This application is a demonstration of a medical recommendation system built using machine learning.
    - **Model**: Random Forest Classifier
    - **Data**: Synthetic dataset with symptoms and corresponding diseases
    - **Author**: Vedant Kale
    - **Version**: 1.0
""")

st.subheader('Data Insights')
st.write("Here are some insights from the dataset used to train the model:")

symptom_counts = data.drop(columns='prognosis').sum().sort_values(ascending=False)
symptom_names = [symptom_map[symptom] for symptom in symptom_counts.index]

df_symptoms = pd.DataFrame({
    'Symptom': symptom_names,
    'Count': symptom_counts.values
})

# Adding Chart
chart = alt.Chart(df_symptoms).mark_bar().encode(
    x='Symptom',
    y='Count',
    tooltip=['Symptom', 'Count']
).interactive()

st.altair_chart(chart, use_container_width=True)

st.write("The bar chart above shows the frequency of each symptom in the dataset. This can help understand which symptoms are most commonly associated with diseases in the training data.")

st.sidebar.title('How to Use')
st.sidebar.info("""
    1. Select symptoms from the list.
    2. Click on the 'Predict' button to see the predicted disease.
    3. Explore data insights and other information provided.
""")

st.sidebar.markdown("""
    <div style="padding: 10px; margin-top: 10px; border-radius: 5px; background-color: #ffe6e6; color: #cc0000;">
    <strong>Disclaimer:</strong> This project is for educational purposes only. It is not intended for medical diagnosis or treatment. The predictions provided are based on a machine learning model trained on synthetic data and should not be used as a substitute for professional medical advice. The author does not take responsibility for any misuse of the information provided.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div style="position: fixed; bottom: 10px; right: 10px; font-size: 12px; color: #777;">Made by Vedant 💖</div>', unsafe_allow_html=True)
