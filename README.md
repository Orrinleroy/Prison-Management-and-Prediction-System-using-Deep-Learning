# Prison Management System
This project is a web application for managing a prison system, including user registration, login, managing prisoners, and predicting prison sentences using a deep learning model. The application is built using Streamlit for the frontend, MongoDB for the database, and TensorFlow for the deep learning model.

## Features
-> User Registration and Login </br>
-> Add, View, and Delete Prisoners </br>
-> Predict Prison Sentence using a deep learning model </br>

## Installation
### Prerequisites
-> Python 3.6 or higher </br>
-> MongoDB </br>

### Step-by-Step Installation
1. Clone the repository :- </br>
```
  git clone https://github.com/your-username/prison-management-system.git </br>
  cd prison-management-system </br>
```  
2. Craete a Virtual Environment
```
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages
```
  pip install -r requirements.txt
```
4. Ensure MongoDB is running 

   MongoDB should be installed and running on your local machine. The default connection string is `mongodb://localhost:27017/`.
  
5. Ensure you have the deep learning model file (`my_model.h5`) in the project directory.
6. Run the streamlit application
  ```
   streamlit run prison_management.py
  ```
7. Open the application in your browser:

     The application will be available at `http://localhost:8501`.

## Usage
### User Authentication   
**1. Register a new user**:
   + Go to the Register page from the sidebar.
   + Fill in the username and password.
   + Click the Register button.

**2. Login:**
   + Go to the Login page from the sidebar.
   + Fill in the username and password.
   + Click the Login button.

### Managing Prisoners
**1. Add a prisoner**:
   + After logging in, select "Add Prisoner" from the sidebar.
   + Fill in the prisoner's details and click "Add Prisoner".

**2. View and delete prisoners**:
   + Select "View Prisoners" from the sidebar.
   + The list of prisoners will be displayed.
   + To delete a prisoner, click the "Delete" button next to the prisoner’s details.

### Predicting Prison Sentence
**1. Predict Sentence**
   + Select "Predict Sentence" from the sidebar.
   + Select the values for crime type, severity, and criminal history from the dropdowns.
   + The predicted years in prison will be displayed.

## Project Structure
```
prison-management-system/
│
├── prison_management.py    # Main application file
├── requirements.txt        # Python dependencies
├── my_model.h5             # Deep learning model file
└── README.md               # This README file
```

## Dependencies
  + streamlit
  + pymongo
  + bcrypt
  + tensorflow
  + numpy

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
