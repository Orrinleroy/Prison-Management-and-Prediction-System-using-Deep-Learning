import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['prison_database']
prisoners_collection = db['prisoners']

# Streamlit UI
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
    }
    .header {
        color: #ffffff;
        background-color: #1f4e79;
        padding: 20px;
        text-align: center;
        font-size: 36px;
        font-family: Arial, sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #333333;
        padding: 20px;
        font-family: Arial, sans-serif;
        font-size: 18px;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #1f4e79;
        font-size: 18px;
        font-family: Arial, sans-serif;
    }
    .stTextInput>div>div>input {
        color: #000000;
        background-color: #ffffff;
        font-size: 18px;
        font-family: Arial, sans-serif;
    }
    .stText>div {
        color: #000000;
        font-size: 18px;
        font-family: Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to generate background pattern
def generate_background_pattern():
    st.markdown(
        """
        <style>
        body {
            background: repeating-linear-gradient(45deg, #e0e0e0, #e0e0e0 10px, #ffffff 10px, #ffffff 20px);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to generate the background pattern
generate_background_pattern()

# Function to add a prisoner
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

# Function to view all prisoners
def view_prisoners():
    st.subheader('View Prisoners')
    prisoners = prisoners_collection.find()

    prisoners_list = list(prisoners)

    if len(prisoners_list) == 0:
        st.write('No prisoners found.')
    else:
        for prisoner in prisoners_list:
            st.write(f"Name: {prisoner['name']}, Age: {prisoner['age']}, Crime: {prisoner['crime']}, Sentence: {prisoner['sentence']}")
            st.write('---')

# Sidebar menu
menu_options = ['Add Prisoner', 'View Prisoners']
selected_menu = st.sidebar.radio('Menu', menu_options)

# Main content based on selected menu option
if selected_menu == 'Add Prisoner':
    add_prisoner()
elif selected_menu == 'View Prisoners':
    view_prisoners()
