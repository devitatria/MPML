import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model_knn.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit application
def main():
    st.title('Customer Prediction using KNN Model')

with st.form(key='prediction_form'):
        age = st.number_input('Age', min_value=0)
        gender = st.selectbox('Gender', ['Female', 'Male'])
        monthly_income = st.selectbox('Monthly Income', ['No Income', 'Below Rs.10000', '10001 to 25000', '25001 to 50000', 'More than 50000'])
        family_size = st.number_input('Family Size', min_value=1, max_value=10)
st.button = st.form_submit_button(label='Predict')

        if st.button:
            # Convert inputs into a DataFrame with correct column names
            gender_map = {'Female': 0, 'Male': 1}
            income_map = {
                'No Income': 4,
                'Below Rs.10000': 2,
                '10001 to 25000': 0,
                '25001 to 50000': 1,
                'More than 50000': 3
            }

            data = pd.DataFrame({
                'Age': [age],
                'Gender': [gender_map[gender]],
                'Monthly_Income': [income_map[monthly_income]],
                'Family_Size': [family_size]
            })

            # Predict
            prediction = model.predict(data)[0]
            st.write(f'Prediction: {"Yes" if prediction == 1 else "No"}')

if _name_ == "_main_":
    main()
