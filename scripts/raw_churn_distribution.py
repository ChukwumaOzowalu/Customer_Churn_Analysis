import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data/Telco-Customer-Churn.csv')

# Preview the dataset
print(data.head())
print(data.info())

# Understand the Data
print(data.describe())
print(data.isnull().sum())

# Generate count plot
sns.countplot(x='Churn', data=data)
plt.title('Churn Distribution')
plt.show()