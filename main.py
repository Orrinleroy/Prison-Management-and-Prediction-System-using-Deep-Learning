from tensorflow.keras.models import load_model
import numpy as np
import streamlit as st

model = load_model('my_model.h5')

# Streamlit UI for user input
st.title("Prison Sentence Prediction")
st.write("Enter the values for crime type, severity, and criminal history:")

crime_type_options = ["theft", "assault", "robbery"]
severity_options = ["low", "medium", "high"]
criminal_history_options = ['none', 'minor', 'repeat']


# Get user input from dropdowns and number input
crime_type = st.selectbox("Crime Type", options=crime_type_options, index=0)
severity = st.selectbox("Severity", options=severity_options, index=0)
criminal_history = st.selectbox("Criminal History", options=criminal_history_options, index=0)

# Prepare the input data
input_data = np.array([[crime_type_options.index(crime_type), severity_options.index(severity), criminal_history_options.index(criminal_history)]])

# Make a prediction
prediction = model.predict(input_data)
prediction = np.round(prediction)

# Display the prediction
st.write(f"Predicted years in prison: {prediction[0][0]}")