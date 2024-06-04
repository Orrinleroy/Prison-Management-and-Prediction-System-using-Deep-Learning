import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
data = pd.read_csv('prison_data.csv')

# Encode categorical variables
label_encoder = LabelEncoder()
data['crime_type'] = label_encoder.fit_transform(data['crime_type'])
data['severity'] = label_encoder.fit_transform(data['severity'])
data['criminal_history'] = label_encoder.fit_transform(data['criminal_history'])

# Split the data into features and target
X = data[['crime_type', 'severity', 'criminal_history']]
y = data['years']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
