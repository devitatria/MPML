import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model_knn.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('KNN Model Deployment')

# Input fields for user data
st.write('Enter the input features:')
feature1 = st.number_input('Feature 1')
feature2 = st.number_input('Feature 2')
feature3 = st.number_input('Feature 3')
feature4 = st.number_input('Feature 4')

# Predict button
if st.button('Predict'):
    features = np.array([[feature1, feature2, feature3, feature4]])
    prediction = model.predict(features)
    st.write(f'The prediction is: {prediction[0]}')
