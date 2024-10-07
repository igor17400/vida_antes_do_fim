from dash import Dash
import dash_bootstrap_components as dbc
from components.layout import create_layout

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Set the app layout
app.layout = create_layout(app)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
