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
submit_button = st.form_submit_button(label='Predict')

if st.form_submit_button:
    # Convert categorical data to numerical
    gender_map = {'Male': 1, 'Female': 0}
    income_map = {
        'No Income': 4,
        'Below Rs.10000': 2,
        '10001 to 25000': 0,
        '25001 to 50000': 1,
        'More than 50000': 3
    }

    features = np.array([[age, gender_map[gender], income_map[monthly_income], family_size]])
    
    # Convert features to a DataFrame with correct column names if needed
    features_df = pd.DataFrame(features, columns=['Age', 'Gender', 'Monthly_Income', 'Family_Size'])
    
    # Predict
    prediction = model.predict(features_df)[0]
    st.write(f'The prediction is: {"Yes" if prediction == 1 else "No"}')
