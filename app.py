import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model_knn.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('KNN Model Deployment')

# Input fields for user data
with st.form(key='prediction_form'):
    age = st.number_input('Age', min_value=0)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    monthly_income = st.selectbox('Monthly Income', ['No Income', 'Below Rs.10000', '10001 to 25000', '25001 to 50000', 'More than 50000'])
    family_size = st.number_input('Family Size', min_value=1, max_value=10)

# Predict button
if submitted:
    features = np.array([[age, gender, monthly_income, family_size]])
    prediction = model.predict(features)
    st.write(f'The prediction is: {prediction[0]}')
