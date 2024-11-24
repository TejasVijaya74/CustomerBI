import dash
from dash import dcc, html
import pandas as pd

# Load dataset for visualization
data = pd.read_csv('data/cleaned_customer_churn.csv')

# Create a Dash app
app = dash.Dash(__name__)

# Layout for the dashboard
app.layout = html.Div([
    html.H1("AI-Driven Business Intelligence Dashboard"),
    dcc.Graph(
        id="churn-bar-chart",
        figure={
            "data": [
                {
                    "x": ["Jan", "Feb", "Mar"],  # Replace with actual time periods
                    "y": [10, 20, 15],  # Replace with calculated churn values
                    "type": "bar",
                    "name": "Churn",
                }
            ],
            "layout": {"title": "Customer Churn Over Time"}
        }
    ),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
