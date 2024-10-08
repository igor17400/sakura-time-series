import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.graph_objs as go
import json

# Load the GeoJSON file for Japanese prefectures
geojson_path = "../data/japan_prefectures.geojson"
with open(geojson_path, "r") as f:
    japan_geojson = json.load(f)

# Create a sample DataFrame to assign a color value to each prefecture
prefecture_data = pd.DataFrame(
    {
        "id": [
            feature["id"] for feature in japan_geojson["features"]
        ],  # Extract IDs from GeoJSON
        "value": range(
            len(japan_geojson["features"])
        ),  # Assign a different value for each prefecture
    }
)

# Create the choropleth map
map_fig = go.Figure(
    go.Choroplethmapbox(
        geojson=japan_geojson,  # Use the GeoJSON data for prefecture boundaries
        locations=prefecture_data[
            "id"
        ],  # Match prefecture IDs to locations in the GeoJSON
        z=prefecture_data["value"],  # The values to use for coloring
        colorscale="PuRd",  # Choose a colorscale
        marker_line_width=0.5,  # Boundary line thickness
        marker_line_color="black",  # Boundary line color
        featureidkey="id",  # Match GeoJSON id field directly
        showscale=False,
    )
)

# Set layout to center the map around Japan
map_fig.update_layout(
    mapbox=dict(
        style="carto-positron",  # Map style
        center={"lat": 38.2048, "lon": 138.2529},  # Center on Japan
        zoom=4.2,  # Adjust zoom level to fit all of Japan
    ),
    margin={"r": 0, "t": 0, "l": 0, "b": 0},  # Remove extra margins
)


# Define the layout using Bootstrap components for a cleaner look
def create_layout():
    return dbc.Container(
        fluid=True,
        children=[
            dbc.Row(
                dbc.Col(
                    html.H1(
                        "Japanese Sakura Blooms Analysis",
                        className="text-center my-4",
                        style={
                            "fontFamily": "Arial, sans-serif",
                            "fontSize": "48px",
                            "color": "white",
                        },
                    ),
                    width=12,
                ),
                justify="center",
            ),
            dbc.Row(
                dbc.Col(
                    html.P(
                        "Click on a prefecture to see more details about the bloom patterns.",
                        className="text-center",
                        style={
                            "fontSize": "20px",
                            "color": "white",
                            "fontStyle": "italic"
                        },
                    ),
                ),
                justify="center",
            ),
            dbc.Row(
                dbc.Col(
                    dcc.Graph(
                        id="japan-map",
                        figure=map_fig,
                        config={"scrollZoom": True},
                        style={
                            "flex-grow": "1",  # Allow the graph to grow and occupy remaining space
                            "width": "100%",  # Set full width
                            "margin": "0",  # Remove any margins
                            "padding": "0",  # Remove any padding
                        },
                    ),
                    width=12,  # Make the map occupy the full width
                    style={
                        "display": "flex",
                        "height": "calc(100vh - 170px)",
                    },  # Adjust height based on header and instructions
                ),
                justify="center",
                style={
                    "height": "100vh",
                    "overflow": "hidden",
                },  # Prevent the page from being scrollable
            ),
            # Modal window definition
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Prefecture Analysis")),
                    dbc.ModalBody(id="modal-content"),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal", className="ml-auto")
                    ),
                ],
                id="modal",
                size="lg",
                is_open=False,  # Modal is closed by default
            ),
        ],
    )
