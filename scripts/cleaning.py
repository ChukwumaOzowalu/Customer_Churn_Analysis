import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('data/Telco_Customer_Churn.csv')

# Handle missing data
print(data.isnull().sum())
data.fillna(method='ffill', inplace=True)

# Encode categorical data
data = pd.get_dummies(data, drop_first=True)
print(data.head())

# Scale data
scaler = StandardScaler()
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
print(data.columns)

# Save cleaned data to new file
data.to_csv('data/Cleaned_Telco_Churn.csv', index=False)