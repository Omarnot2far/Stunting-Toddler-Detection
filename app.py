import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('nutrition_model.joblib')

st.title('Child Nutrition Status Prediction')

age = st.number_input('Age (months)', min_value=0, max_value=240, value=12)
gender = st.selectbox('Gender', ['male', 'female'])
height = st.number_input('Height (cm)', min_value=0.0, max_value=200.0, value=50.0)

if st.button('Predict'):
    input_data = pd.DataFrame([[age, gender, height]],
                              columns=['Age(months)', 'Gender', 'Height(cm)'])
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Nutrition Status: {prediction}')
