import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load dataset
file_path = "data/Telco_Customer_Churn.csv"
df = pd.read_csv(file_path)

# Handle TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df.drop