import plotly.express as px


def create_indigenous_map(gdf):
    fig = px.choropleth_mapbox(
        gdf,
        geojson=gdf.geometry,
        locations=gdf.index,
        color="etnia_nome",
        mapbox_style="carto-positron",
        center={"lat": -14.2350, "lon": -51.9253},
        zoom=3,
        opacity=0.5,
        labels={"etnia_nome": "Indigenous Community"},
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig
