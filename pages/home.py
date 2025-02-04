# package imports
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from components.indigenous_map import create_indigenous_map
from utils.br_ind_data import load_indigenous_data
import plotly.graph_objs as go

dash.register_page(
    __name__, path="/", redirect_from=["/home"], title="Life Before The End"
)

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src="/assets/coca.png",
                            className="hero-image",
                        ),
                    ],
                    className="hero-image-container",
                ),
                html.Div(
                    [
                        html.H1(
                            "Life Before The End",
                            className="hero-title",
                        ),
                        html.P(
                            "How can we preserve Indigenous People, Culture and Language Through Technology?",
                            className="hero-subtitle",
                        ),
                    ],
                    className="hero-content",
                ),
            ],
            className="hero-container",
        ),
        html.Div(
            className="text-container",
            children=[
                html.Div(
                    children=[
                        html.H1("Life Before the End"),
                    ],
                    className="title-container",
                ),
                html.Div(
                    children=[
                        html.P(
                            'The title is inspired by a Brazilian podcast that explores the extermination of an Indigenous group referred to in Portuguese as the "Índio do Buraco" (Man of the Hole).'
                        ),
                        html.P(
                            'The podcast is titled "Life Before the End," emphasizing the importance of taking action to protect a group of people before they disappear, rather than responding only after they have ceased to exist.'
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.P(
                            "This project compiles various scientific works, primarily those that use artificial intelligence and machine learning to support Indigenous communities."
                        ),
                        html.P(
                            "The ultimate goal is to serve as an open-source tool for sharing knowledge about Indigenous peoples worldwide, providing references and resources for those interested in learning more about them. At the same time, we aim to be a resource for scientists actively working towards the progress of Indigenous communities."
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="section-title",
            children=[html.H1("The Man of the Hole"), html.Div(className="underline")],
        ),
        html.Div(
            className="man-hole-container",
            children=[
                html.Img(
                    src="/assets/man_of_the_hole.jpg",  # Ensure the path is correct
                    className="man-hole-image",
                ),
                html.Blockquote(
                    "It is not known what language the Man of the Hole spoke, what his people called themselves, or what his name was. He was the last surviving member of his people following their genocide by Brazilian settlers in the 1970s–1990s and chose to remain isolated until his death in 2022. Living primarily by hunting and gathering and moving frequently, he left behind a deep hole of unknown purpose in each of his former homes, giving rise to his nickname. After surviving a further attack by armed ranchers in 2009, he was found dead in his home in August 2022."
                ),
            ],
        ),
        html.Div(
            className="section-title",
            children=[
                html.H1("Indigenous Populations - Brasil"),
                html.Div(className="underline"),
            ],
        ),
        html.Div(
            children=[
                html.P(
                    "One of the ways we can learn about Indigenous communities is by learning about their culture specially with a knowledge from where they live.",
                ),
                html.P(
                    "Click on any region to learn more about the indigenous community from that place.",
                ),
            ],
        ),
        # Add the map here with loading spinner
        html.Div(
            className="indigenous-map",
            children=[
                html.Div(
                    id="loading-message",
                    className="loading-message",
                    children="Loading data...",
                ),
                dcc.Loading(
                    id="loading-data",
                    type="circle",
                    children=[
                        dcc.Graph(
                            id="indigenous-map-graph",
                            figure=go.Figure(),  # Initialize with an empty figure
                        )
                    ],
                ),
                dcc.Interval(
                    id="interval-component",
                    interval=1 * 1000,
                    n_intervals=0,
                    max_intervals=1,
                ),  # Triggers once
            ],
        ),
        # Modal for displaying region information without a close button
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Region Information")),
                dbc.ModalBody(id="modal-body"),
            ],
            id="region-modal",
            is_open=False,
        ),
        html.Div(
            className="section-title",
            children=[html.H1("About The Project"), html.Div(className="underline")],
        ),
        # Call-to-action buttons
        html.Div(
            [
                html.A(
                    html.Button(
                        "Indigenous Communities",
                        className="cta-button cta-button-secondary",
                    ),
                    href="/indigenous_populations",
                ),
                html.A(
                    html.Button(
                        "Research Papers",
                        className="cta-button cta-button-primary",
                    ),
                    href="/research_papers",
                ),
            ],
            className="cta-buttons-container",
        ),
        html.Div(
            className="about-container",
            children=[
                html.Img(
                    src="/assets/cards/ind1.jpg",  # Ensure the path is correct
                    className="indigenous-man",
                ),
                html.P(
                    "This project aims to compile and summarize the numerous works and contributions dedicated to the preservation and support of Indigenous communities. By gathering these resources in one place, we hope to make it easier for people to explore the ways in which science, technology, and various initiatives have worked towards uplifting Indigenous groups.",
                ),
                html.P(
                    "Additionally, our goal is to increase awareness and understanding of Indigenous cultures by providing a platform that highlights the rich history, traditions, and ongoing struggles of these communities. Promoting a deeper connection to their cultural significance and the challenges they face.",
                ),
            ],
        ),
    ],
)


# Callback to load the map and update the loading message
@callback(
    Output("indigenous-map-graph", "figure"),
    Output("loading-message", "children"),
    Input("interval-component", "n_intervals"),
    prevent_initial_call=True,
)
def load_map(n_intervals):
    # Update loading message
    loading_message = "The dataset is being loaded..."

    # Load data
    gdf = load_indigenous_data()

    # Update loading message
    loading_message = "The visualization graph is being loaded..."

    # Create map
    fig = create_indigenous_map(gdf)

    # Return the map and final message
    return fig, "Map loaded successfully!"


# Callback to update the modal content and open it based on map click
@callback(
    [Output("modal-body", "children"), Output("region-modal", "is_open")],
    [Input("indigenous-map-graph", "clickData")],
    [dash.dependencies.State("region-modal", "is_open")],
)
def display_region_info(clickData, is_open):
    if clickData:
        # Extract the index of the clicked region
        point_index = clickData["points"][0]["pointIndex"]

        # Retrieve information about the clicked region
        region_info = {
            0: "Information about region 0",
            1: "Information about region 1",
            # Add more entries as needed
        }

        info = region_info.get(point_index, "No information available for this region.")
        return info, True

    return dash.no_update, is_open