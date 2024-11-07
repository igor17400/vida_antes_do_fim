# notes
"""
This file is for housing the main dash application.
This is where we define the various css items to fetch as well as the layout of our application.
"""

# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc
from flask import Flask
import os

# local imports
from utils.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK
from components import navbar, footer

server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    use_pages=True,  # turn on Dash pages
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
    ],  # fetch the proper css items we want
    meta_tags=[
        {  # check if device is a mobile device. This is a must if you do any mobile styling
            "name": "viewport",
            "content": "width=device-width, initial-scale=1",
        }
    ],
    suppress_callback_exceptions=True,
    title="Dash app structure",
)

server.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))


def serve_layout():
    """Define the layout of the application"""

    return dbc.Container(
        children=[navbar, dash.page_container, footer], fluid=True, class_name="p-0 m-0"
    )


app.layout = serve_layout  # set the layout to the serve_layout function
server = app.server  # the server is needed to deploy the application

if __name__ == "__main__":
    app.run_server(
        host=APP_HOST,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK,
    )
