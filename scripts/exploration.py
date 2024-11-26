import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('data/Cleaned_Telco_Churn.csv')

# Print 
print(data.shape)

# Timing the heatmap render:
start_time = time.time()

# Visualize correlations
correlation = data.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Stop time and print
end_time = time.time()
time_taken = end_time - start_time
print("The heatmap took ", time_taken, " seconds to render.")