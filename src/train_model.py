import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load preprocessed data
data = pd.read_csv('CustomerBI\data\cleaned_customer_churn.csv')

# Feature selection
X = data[['feature1', 'feature2']]  # Replace with actual column names
y = data['churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'CustomerBI\models\churn_model.pkl')
print("Model trained and saved to 'CustomerBI\models\churn_model.pkl'!")
