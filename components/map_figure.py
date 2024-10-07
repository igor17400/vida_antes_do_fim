import json
import pandas as pd
import plotly.express as px

# Function to build the map figure
def create_map_figure(pop_data_path, geojson_path):
    # Load population data
    pop = pd.read_csv(pop_data_path)

    # Read GeoJSON file for Brazil
    with open(geojson_path, "r", encoding="utf-8") as file:
        geo_json = json.load(file)

    # Create the choropleth map using Plotly Express
    fig = px.choropleth_mapbox(
        data_frame=pop,
        geojson=geo_json,
        locations="CD_MUN",
        featureidkey="properties.codarea",
        color="TX_CRESC",
        color_continuous_scale="thermal",
        range_color=(pop["TX_CRESC"].min(), pop["TX_CRESC"].max()),
        mapbox_style="open-street-map",
        zoom=3.5,
        center={"lat": -15.81, "lon": -47.93},
        opacity=1,
        labels={"TX_CRESC": "Tx Cresc Geométrico (%)", "CD_MUN": "Código do município"},
        width=1200,
        height=800,
        title="Variação Pop Censo 2022",
        hover_name="NM_MUN",
    )

    # Customize layout
    fig.update_layout(
        margin={"r": 0, "t": 1, "l": 0, "b": 1},
        coloraxis_colorbar={"title": {"text": "Taxa de Crescimento (%)", "side": "right"}},
    )

    # Customize the individual polygons
    fig.update_geos(showcoastlines=False, visible=False)

    # Update marker settings
    fig.update_traces(marker_line_width=0.05, selector=dict(type="choroplethmapbox"))

    return fig
