import streamlit as st
from pymongo import MongoClient
import bcrypt
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['prison_management']
users_collection = db['users']
prisoners_collection = db['prisoners']

# Load the deep learning model
model = load_model('my_model.h5')

# Function to display the logo in the sidebar
def display_logo():
    image = Image.open("Prison Pro Logo.png")  # Replace with your image path
    logo = image.resize((100, 100))  # Resize the image to 100x100 pixels
    st.sidebar.image(logo, use_column_width=False)

# User registration
def register_user():
    st.subheader('Register User')
    with st.form(key='register_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button(label='Register')
        if submit_button:
            if users_collection.find_one({'username': username}):
                st.error('Username already exists!')
            else:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                user_data = {
                    'username': username,
                    'password': hashed_password
                }
                users_collection.insert_one(user_data)
                st.success('User registered successfully!')

# User login
def login_user():
    st.subheader('User Login')
    with st.form(key='login_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button(label='Login')
        if submit_button:
            user = users_collection.find_one({'username': username})
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success('Login successful!')
                st.experimental_rerun()
            else:
                st.error('Invalid username or password')

# Add a prisoner
def add_prisoner():
    st.subheader('Add Prisoner')
    with st.form(key='add_prisoner_form'):
        name = st.text_input('Name')
        age = st.number_input('Age', min_value=0, max_value=150)
        crime = st.text_input('Crime')
        sentence = st.text_input('Sentence')
        submit_button = st.form_submit_button(label='Add Prisoner')
        if submit_button:
            prisoner_data = {
                'name': name,
                'age': age,
                'crime': crime,
                'sentence': sentence
            }
            prisoners_collection.insert_one(prisoner_data)
            st.success('Prisoner added successfully!')

# View all prisoners
def view_prisoners():
    st.subheader('View Prisoners')
    prisoners = prisoners_collection.find()
    prisoners_list = list(prisoners)

    if len(prisoners_list) == 0:
        st.write('No prisoners found.')
    else:
        for prisoner in prisoners_list:
            st.write(f"Name: {prisoner['name']}, Age: {prisoner['age']}, Crime: {prisoner['crime']}, Sentence: {prisoner['sentence']}")
            if st.button(f"Delete {prisoner['name']}", key=prisoner['_id']):
                prisoners_collection.delete_one({'_id': prisoner['_id']})
                st.experimental_rerun()
            st.write('---')

# Predict prison sentence
def predict_sentence():
    st.subheader("Prison Sentence Prediction")
    st.write("Enter the values for crime type, severity, and criminal history:")

    crime_type_options = ["theft", "assault", "robbery"]
    severity_options = ["low", "medium", "high"]
    criminal_history_options = ['none', 'minor', 'repeat']

    crime_type = st.selectbox("Crime Type", options=crime_type_options, index=0)
    severity = st.selectbox("Severity", options=severity_options, index=0)
    criminal_history = st.selectbox("Criminal History", options=criminal_history_options, index=0)

    input_data = np.array([[crime_type_options.index(crime_type), severity_options.index(severity), criminal_history_options.index(criminal_history)]])

    prediction = model.predict(input_data)
    prediction = np.round(prediction)

    st.write(f"Predicted years in prison: {prediction[0][0]}")

# Main function
def main():
    st.sidebar.title('Prison Management System')
    display_logo()

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        st.sidebar.header(f"Welcome, {st.session_state['username']}!")
        menu_options = ['Add Prisoner', 'View Prisoners', 'Predict Sentence', 'Logout']
        selected_menu = st.sidebar.selectbox('Menu', menu_options)

        if selected_menu == 'Add Prisoner':
            add_prisoner()
        elif selected_menu == 'View Prisoners':
            view_prisoners()
        elif selected_menu == 'Predict Sentence':
            predict_sentence()
        elif selected_menu == 'Logout':
            st.session_state['logged_in'] = False
            st.experimental_rerun()
    else:
        auth_options = ['Login', 'Register']
        selected_auth = st.sidebar.selectbox('Authenticate', auth_options)

        if selected_auth == 'Login':
            login_user()
        elif selected_auth == 'Register':
            register_user()

if __name__ == '__main__':
    main()
