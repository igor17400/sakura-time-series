from dash import Dash
import dash_bootstrap_components as dbc
from components.layout import create_layout
from components.callbacks import register_callbacks

# Initialize the Dash app with Bootstrap styles
app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder="assets"
)

# Set up the layout for the app
app.layout = create_layout()

# Register the callbacks for interactivity
register_callbacks(app)

# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
