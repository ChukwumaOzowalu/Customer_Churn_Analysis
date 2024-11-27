import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Loads dataset
file_path = "data/Raw_Customer_Churn.csv"
df = pd.read_csv(file_path)

# No need to handle missing values after inspecting raw data (no missing values)

# Removes irrelevant columns (customerID)
df.drop(columns=['customerID'], inplace=True)

# Encodes categorical variables
# (1) One-Hot Encoding
df = pd.get_dummies(df, columns=['Contract', 'InternetService', 'PaymentMethod', 'MultipleLines', 'gender', "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod"], drop_first=True)
# (2) Label Encoding
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
df['Partner'] = df['Partner'].map({'Yes': 1, 'No': 0})
df['Dependents'] = df['Dependents'].map({'Yes': 1, 'No': 0})
df['PhoneService'] = df['PhoneService'].map({'Yes': 1, 'No': 0})

# Scales numerical features
numerical_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
print("Scaled Data Example: ")
print(df[numerical_columns].head())

