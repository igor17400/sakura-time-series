from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go

# Load data from the CSV file
sakura_first_bloom = pd.read_csv("../data/sakura_first_bloom_dates.csv")

# Select Kyoto data and prepare it for plotting
location = 'Kyoto'
years = sakura_first_bloom.columns[3:-2].astype(int)  # Convert year columns to integers
bloom_dates = pd.to_datetime(sakura_first_bloom.loc[sakura_first_bloom['Site Name'] == location, years.astype(str)].iloc[0])

# Create a scatter plot for the bloom dates
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=years, y=bloom_dates, mode='markers+lines', marker=dict(color='pink'),
    line=dict(dash='dash'), name='Bloom Dates'
))

fig.update_layout(
    title=f'Sakura Bloom Dates in {location} (1953-2023)',
    xaxis_title='Year',
    yaxis_title='Bloom Date',
    yaxis=dict(tickformat='%b %d'),  # Format Y-axis to show month and day
    hovermode='closest'
)


# Define the layout of the app
def create_layout():
    return html.Div(
        className="container",
        children=[
            html.H1("Sakura Time Series Dashboard"),
            html.Div(
                className="graph-title",
                children=[
                    html.H2("First Bloom Dates for Sakura in Kyoto"),
                    dcc.Graph(id="bloom-line-chart", figure=fig),
                ],
            ),
        ],
    )
