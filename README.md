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
  pip install streamlit
  pip install "tensorflow<2.11"
  pip install -U scikit-learn
  pip install pymongo
  pip install bcrypt
  pip install numpy
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
