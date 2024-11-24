import pandas as pd

# Load dataset
data = pd.read_csv('CustomerBI\data\customer_churn.csv')

# Data preprocessing
data.fillna(0, inplace=True)  # Fill missing values

# Save preprocessed data
data.to_csv('CustomerBI\data\cleaned_customer_churn.csv', index=False)
print("Data cleaned and saved to 'CustomerBI\data\cleaned_customer_churn.csv'!")
