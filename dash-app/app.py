from dash import Dash
from components.layout import create_layout
from components.callbacks import register_callbacks

# Initialize the Dash app
app = Dash(__name__, assets_folder="assets")

# Set the layout for the app
app.layout = create_layout()

# Register callbacks (if any)
register_callbacks(app)

# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
