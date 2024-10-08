from dash import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load the data again
sakura_first_bloom = pd.read_csv("../data/sakura_first_bloom_dates.csv")


# Register the callback function
def register_callbacks(app):
    @app.callback(Output("city-bloom-graph", "figure"), Input("city-dropdown", "value"))
    def update_graph(selected_city):
        # Filter data for the selected city
        years = sakura_first_bloom.columns[3:-2].astype(int)
        bloom_dates = pd.to_datetime(
            sakura_first_bloom.loc[
                sakura_first_bloom["Site Name"] == selected_city, years.astype(str)
            ].iloc[0]
        )

        # Create scatter plot for the selected city
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=years,
                y=bloom_dates,
                mode="markers+lines",
                marker=dict(color="pink"),
                line=dict(dash="dash"),
                name="Bloom Dates",
            )
        )

        # Update figure layout
        fig.update_layout(
            title=f"Sakura Bloom Dates in {selected_city} (1953-2023)",
            xaxis_title="Year",
            yaxis_title="Bloom Date",
            yaxis=dict(tickformat="%b %d"),
            hovermode="closest",
        )
        return fig
