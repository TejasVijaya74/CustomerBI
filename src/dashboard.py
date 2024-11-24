import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Initialize the Dash app with a modern theme
app = dash.Dash(__name__)

# Custom CSS for better styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Customer BI Dashboard</title>
        {%favicon%}
        {%css%}
        <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100">
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Load and prepare data
data = pd.read_csv('CustomerBI/data/cleaned_customer_churn.csv')
data_encoded = pd.get_dummies(data, columns=['Gender', 'Partner'], drop_first=True)

# Calculate key metrics
total_customers = len(data)
city_counts = data['City'].value_counts()
gender_by_city = data.groupby(['City', 'Gender']).size().unstack(fill_value=0)
partner_counts = data['Partner'].value_counts()

# Create layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("Customer Analytics Dashboard",
                className='text-3xl font-bold text-gray-800 p-4')
    ], className='bg-white shadow-sm'),

    # Main content
    html.Div([
        # Key Metrics Row
        html.Div([
            # Total Customers Card
            html.Div([
                html.Div([
                    html.H3("Total Customers", className='text-lg font-semibold text-gray-600'),
                    html.P(f"{total_customers:,}", className='text-3xl font-bold text-blue-600')
                ], className='bg-white rounded-lg shadow p-6')
            ], className='col-span-1'),

            # Total Cities Card
            html.Div([
                html.Div([
                    html.H3("Total Cities", className='text-lg font-semibold text-gray-600'),
                    html.P(f"{len(city_counts):,}", className='text-3xl font-bold text-green-600')
                ], className='bg-white rounded-lg shadow p-6')
            ], className='col-span-1'),

            # Gender Distribution Card
            html.Div([
                html.Div([
                    html.H3("Gender Distribution", className='text-lg font-semibold text-gray-600'),
                    html.P(f"Male: {(data['Gender'] == 'Male').sum():,}", className='text-3xl font-bold text-purple-600')
                ], className='bg-white rounded-lg shadow p-6')
            ], className='col-span-1'),

            # Partner Status Card
            html.Div([
                html.Div([
                    html.H3("Partner Status", className='text-lg font-semibold text-gray-600'),
                    html.P(f"Partnered: {(data['Partner'] == 'Yes').sum():,}", className='text-3xl font-bold text-orange-600')
                ], className='bg-white rounded-lg shadow p-6')
            ], className='col-span-1'),
        ], className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6'),

        # Charts Row
        html.Div([
            # Customer Distribution by City
            html.Div([
                html.Div([
                    html.H3("Customer Distribution by City", className='text-xl font-semibold mb-4'),
                    dcc.Graph(
                        figure=px.bar(
                            city_counts.reset_index(),
                            x='City',
                            y='count',
                            color_discrete_sequence=['#3B82F6'],
                            labels={'count': 'Number of Customers', 'City': 'City'}
                        ).update_layout(
                            plot_bgcolor='white',
                            paper_bgcolor='white',
                            margin=dict(l=40, r=40, t=40, b=40)
                        )
                    )
                ], className='bg-white rounded-lg shadow p-6')
            ], className='col-span-1'),

            # Gender Distribution by City
            html.Div([
                html.Div([
                    html.H3("Gender Distribution by City", className='text-xl font-semibold mb-4'),
                    dcc.Graph(
                        figure=px.bar(
                            gender_by_city.reset_index(),
                            x='City',
                            y=['Male', 'Female'],
                            barmode='group',
                            color_discrete_sequence=['#8B5CF6', '#EC4899'],
                            labels={'value': 'Number of Customers', 'City': 'City'}
                        ).update_layout(
                            plot_bgcolor='white',
                            paper_bgcolor='white',
                            margin=dict(l=40, r=40, t=40, b=40)
                        )
                    )
                ], className='bg-white rounded-lg shadow p-6')
            ], className='col-span-1'),
        ], className='grid grid-cols-1 lg:grid-cols-2 gap-4'),

        # Partner Status Distribution
        html.Div([
            html.Div([
                html.H3("Partner Status Distribution", className='text-xl font-semibold mb-4'),
                dcc.Graph(
                    figure=px.pie(
                        values=partner_counts.values,
                        names=partner_counts.index,
                        color_discrete_sequence=['#F59E0B', '#10B981']
                    ).update_layout(
                        plot_bgcolor='white',
                        paper_bgcolor='white',
                        margin=dict(l=40, r=40, t=40, b=40)
                    )
                )
            ], className='bg-white rounded-lg shadow p-6')
        ], className='mt-6')
    ], className='container mx-auto p-6')
], className='min-h-screen bg-gray-100')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)