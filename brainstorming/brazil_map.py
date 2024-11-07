import pandas as pd
import geopandas as gpd
from shapely import wkt
import plotly.express as px

df = pd.read_csv("../large_files/tis_poligonais.csv")
# Convert the 'the_geom' column from WKT to a geometry object
df['geometry'] = df['the_geom'].apply(lambda x: wkt.loads(x) if pd.notnull(x) else None)

print(df.shape)
print(df.columns)
print(df.head())

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# Ensure the GeoDataFrame is in the correct coordinate reference system
gdf.set_crs(epsg=4326, inplace=True)

# Plot using Plotly
fig = px.choropleth_mapbox(
    gdf,
    geojson=gdf.geometry,
    locations=gdf.index,
    color='etnia_nome',  # Color by indigenous community
    mapbox_style="carto-positron",
    center={"lat": -14.2350, "lon": -51.9253},  # Center of Brazil
    zoom=3,
    opacity=0.5,
    labels={'etnia_nome': 'Indigenous Community'}
)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()