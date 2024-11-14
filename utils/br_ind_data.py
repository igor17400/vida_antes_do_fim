import pandas as pd
import geopandas as gpd
from shapely import wkt


def load_indigenous_data():
    df = pd.read_csv("./large_files/tis_poligonais.csv")
    df = df.iloc[:25]
    df["geometry"] = df["the_geom"].apply(
        lambda x: wkt.loads(x) if pd.notnull(x) else None
    )
    gdf = gpd.GeoDataFrame(df, geometry="geometry")
    gdf.set_crs(epsg=4326, inplace=True)
    return gdf
