# predict_page.py

import streamlit as st
import pickle
import pandas as pd

# Load the model and encoders from the pickle file
with open('sleep_trouble_model.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

loaded_model = loaded_data['model']
loaded_encoders = loaded_data['encoders']

# Prediction function
def predict_trouble_sleeping(physical_health, pain, stress, medication):
    input_data = pd.DataFrame({
        'Phyiscal Health': [physical_health],
        'Pain Keeps Patient from Sleeping': [pain],
        'Stress Keeps Patient from Sleeping': [stress],
        'Medication Keeps Patient from Sleeping': [medication]
    })

    # Make a prediction using the loaded model
    prediction = loaded_model.predict(input_data)[0]

    if prediction == 1:
        return "No Trouble Sleeping"
    elif prediction == 2:
        return "Little Trouble Sleeping"
    else:
        return "Yes, Trouble Sleeping"

# Streamlit App
def main():
    st.title("Trouble Sleeping Prediction")

    # Create input fields
    st.write("Please input the following details:")

    physical_health = st.selectbox('Physical Health (1: Excellent, 2: Very Good, 3: Good, 4: Fair, 5: Poor)',
                                   [1, 2, 3, 4, 5], format_func=lambda x: loaded_encoders['Physical Health'][x])

    pain = st.selectbox('Pain Keeps Patient from Sleeping (0: No, 1: Yes)',
                        [0, 1], format_func=lambda x: loaded_encoders['Pain Keeps Patient from Sleeping'][x])

    stress = st.selectbox('Stress Keeps Patient from Sleeping (0: No, 1: Yes)',
                          [0, 1], format_func=lambda x: loaded_encoders['Stress Keeps Patient from Sleeping'][x])

    medication = st.selectbox('Medication Keeps Patient from Sleeping (0: No, 1: Yes)',
                              [0, 1], format_func=lambda x: loaded_encoders['Medication Keeps Patient from Sleeping'][x])

    # Predict button
    if st.button("Predict"):
        result = predict_trouble_sleeping(physical_health, pain, stress, medication)
        st.success(f"Prediction: {result}")

if __name__ == "__main__":
    main()
