import pandas as pd

# Load dataset
data = pd.read_csv('data/customer_churn.csv')

# Data preprocessing
data.fillna(0, inplace=True)  # Fill missing values

# Save preprocessed data
data.to_csv('data/cleaned_customer_churn.csv', index=False)
print("Data cleaned and saved to 'data/cleaned_customer_churn.csv'!")
