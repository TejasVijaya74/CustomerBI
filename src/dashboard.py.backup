import dash
from dash import dcc, html
import pandas as pd
import joblib

# Load dataset and model (if needed for prediction)
data = pd.read_csv('CustomerBI/data/cleaned_customer_churn.csv')

# Apply one-hot encoding to categorical columns
data_encoded = pd.get_dummies(data, columns=['Gender', 'Partner'], drop_first=True)

# Feature selection (after encoding, selecting the columns)
X = data_encoded[['Gender_Male', 'Partner_Yes']]  # After encoding column names
y = data['City']  # Target column remains the same

# Prepare data for visualization (e.g., count of customers in each country for the given features)
country_count = data.groupby('City').size().reset_index(name='Count')

# Create a Dash app
app = dash.Dash(__name__)

# Layout for the dashboard
app.layout = html.Div([
    html.H1("AI-Driven Business Intelligence Dashboard"),

    # Bar chart for country distribution based on Gender_Male and Partner_Yes features
    dcc.Graph(
        figure={
            "data": [
                {
                    "x": country_count['City'],  # Countries
                    "y": country_count['Count'],  # Count of customers in each country
                    "type": "bar",
                    "name": "Customer Distribution by City"
                }
            ],
            "layout": {"title": "Customer Distribution by City"}
        }
    ),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
