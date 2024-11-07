import plotly.express as px
import pandas as pd

# Sample data
data = {
    "Region": ["Region A", "Region B", "Region C"],
    "Indigenous Population": [1000, 1500, 500],
    "Info": [
        "Info about Region A",
        "Info about Region B",
        "Info about Region C",
    ],
}

df = pd.DataFrame(data)


def create_map():
    fig = px.scatter_geo(
        df,
        locations="Region",
        size="Indigenous Population",
        hover_name="Region",
        hover_data=["Info"],
        projection="natural earth",
    )
    return fig
