from dash import dcc, html
import dash_bootstrap_components as dbc
from components.map_figure import create_map_figure

# Create the layout
def create_layout(app):
    # Path to your data files
    pop_data_path = "./data/pop_parsed.csv"
    geojson_path = "./data/brazil_geo_2022.json"

    # Generate the map figure
    fig = create_map_figure(pop_data_path, geojson_path)

    # Define and return the app layout
    return dbc.Container(
        [
            html.H1("Brazil Population Growth Map"),
            html.P("Visualizing population growth based on the 2022 Census"),
            dcc.Graph(figure=fig),
        ],
        fluid=True,
    )
