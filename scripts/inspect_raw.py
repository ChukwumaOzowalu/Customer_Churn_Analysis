import pandas as pd
import numpy as np

# Load dataset
file_path = "data/Raw_Customer_Churn.csv"
df = pd.read_csv(file_path)

# Inspect the data
print("\n", "Dataset Shape: ", df.shape, "\n")
print("\n", "Column information: ", df.info(), "\n")
print("\n", "Missing Values: ", df.isnull().sum(), "\n")
print("\n", "First Few Rows: ", df.head(5), "\n")

# Highlight key variable
print(df['Churn'].value_counts())