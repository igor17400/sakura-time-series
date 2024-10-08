from dash import Input, Output, dcc, State
import pandas as pd
import plotly.graph_objs as go
from dash import html
import json

# Load the GeoJSON and prefecture data
geojson_path = "../data/japan_prefectures.geojson"
with open(geojson_path, "r") as f:
    japan_geojson = json.load(f)

# Load prefecture data
prefecture_data = pd.DataFrame(
    {
        "id": [feature["id"] for feature in japan_geojson["features"]],
        "name": [
            feature["properties"]["nam"] for feature in japan_geojson["features"]
        ],
        "value": range(len(japan_geojson["features"])),
    }
)


def register_callbacks(app):
    @app.callback(
        Output("modal", "is_open"),
        Output("modal-content", "children"),
        Input("japan-map", "clickData"),
        Input("close-modal", "n_clicks"),
        State("modal", "is_open"),
    )
    def display_prefecture_info(clickData, n_clicks, is_open):
        # If a prefecture is clicked, extract its ID and display the modal
        if clickData:
            prefecture_id = clickData["points"][0]["location"]

            # Get the name of the clicked prefecture
            prefecture_name = prefecture_data[
                prefecture_data["id"] == prefecture_id
            ].iloc[0]["name"]

            # Create content for the modal body
            modal_content = html.Div(
                [
                    html.H4(f"Details for Prefecture: {prefecture_name}"),
                    html.P(f"Prefecture ID: {prefecture_id}"),
                    html.P(
                        "This is where detailed information and analysis will be displayed."
                    ),
                    # Add more details and graphs for the specific prefecture here
                ]
            )

            # Open the modal
            return not is_open, modal_content

        # If the close button is clicked, close the modal
        if n_clicks:
            return not is_open, None

        # If no interaction, keep the modal closed
        return is_open, None
