# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

# Load the dataset
df =  pd.read_csv(r'C:\Users\LENOVO\Desktop\wrench\Project Delay Prediction\dataset.csv')

# Simplify RootCause (basic cleaning)
df['RootCause'] = df['RootCause'].fillna('Unknown')
df['RootCause'] = df['RootCause'].str.lower().str.strip()


# Prepare features
features = ['Risk', 'Priority', 'Hours', 'ProjectDiscipline', 
             'Delay', 'RootCause']
X = df[features]
y = df['Overdue']

# Encode categorical features
X_encoded = X.copy()
label_encoders = {}
for col in ['Risk', 'Priority', 'ProjectDiscipline', 'RootCause']:
    le = LabelEncoder()
    X_encoded[col] = le.fit_transform(X[col].str.lower())
    label_encoders[col] = le

# Drop missing y
X_encoded = X_encoded[~y.isna()]
y = y.dropna()

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# 4. Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
print("file model run successfully")
