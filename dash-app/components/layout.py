from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go

# Load the Sakura bloom data
sakura_first_bloom = pd.read_csv("../data/sakura_first_bloom_dates.csv")

# Extract the list of unique cities
cities = sakura_first_bloom["Site Name"].unique()


# Define the layout for the Dash app
def create_layout():
    return html.Div(
        className="container",
        children=[
            html.H1("Sakura Time Series Dashboard"),
            html.Div(
                [
                    html.Label("Select a City:", style={"fontWeight": "bold"}),
                    dcc.Dropdown(
                        id="city-dropdown",
                        options=[{"label": city, "value": city} for city in cities],
                        value="Kyoto",  # Default value
                    ),
                ],
                style={"width": "50%", "margin": "auto"},
            ),
            dcc.Graph(id="city-bloom-graph"),  # Placeholder for the dynamic graph
            html.P(
                "Select a city from the dropdown to see its first bloom dates over time.",
                style={"fontStyle": "italic", "textAlign": "center"},
            ),
        ],
    )
