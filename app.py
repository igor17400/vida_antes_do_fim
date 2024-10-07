import pandas as pd
import json
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# Load population data
pop = pd.read_csv("./data/pop.csv")

# Remove accents and normalize string columns
pop = pop.apply(
    lambda x: (
        x.str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")
        if x.dtype == "object"
        else x
    )
)

# Remove the first row if necessary
pop = pop.iloc[1:]

# Ensure the 'V' column is numeric, forcing errors to NaN
pop["V"] = pd.to_numeric(pop["V"], errors="coerce")

# Pivot table to organize the data
pop = pop.pivot_table(index=["D1C", "D1N"], columns="D3N", values="V").reset_index()
pop.columns.name = None

# Define a mapping for column names
column_mapping = {
    "D1C": "CD_MUN",
    "D1N": "NM_MUN",
    "Populacao residente": "POP_RESIDENTE",
    "Variacao absoluta da populacao residente 2010 compatibilizada": "VAR_ABS",
    "Taxa de crescimento geometrico": "TX_CRESC",
}

# Rename columns
pop = pop.rename(columns=column_mapping)

# Read GeoJSON file for Brazil
with open("./data/brazil_geo_2022.json", "r", encoding="utf-8") as file:
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

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the app layout
app.layout = dbc.Container(
    [
        html.H1("Brazil Population Growth Map"),
        html.P("Visualizing population growth based on the 2022 Census"),
        dcc.Graph(figure=fig),
    ],
    fluid=True,
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
