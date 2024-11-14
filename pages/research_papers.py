# package imports
import dash
from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc
import json
import os

dash.register_page(__name__, path="/research_papers", title="Research Papers")

# Define the path to the JSON file
json_file_path = os.path.join("../data/papers.json")

# Load the JSON data
with open(json_file_path, "r") as file:
    papers = json.load(file)

# Now `papers` contains the list of dictionaries from the JSON file

layout = html.Div(
    [
        html.Div(className="page-top"),
        html.Div(
            className="section-title",
            children=[html.H1("Research Papers"), html.Div(className="underline")],
        ),
        html.Div(
            className="research-papers-container",
            children=[
                html.P(
                    "The papers below each focus on different aspects of Indigenous topics"
                ),
            ],
        ),
        html.Div(
            className="papers-container",
            children=[
                html.Article(
                    className="card box",
                    id={"type": "view-card", "index": i},
                    children=[
                        html.Img(
                            src="./assets/cards/" + paper["image"],
                            className="card__background",
                            alt=f"Background image for {paper['title']}",
                        ),
                        html.Div(
                            className="card__content flow",
                            children=[
                                html.Div(
                                    className="card__content--container flow",
                                    children=[
                                        html.H2(
                                            paper["title"],
                                            className="card__title box__title",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                )
                for i, paper in enumerate(papers)
            ],
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(id="modal-title")),
                dbc.ModalBody(id="modal-content"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-modal", className="ml-auto")
                ),
            ],
            id="paper-modal",
            is_open=False,
            size="lg",
        ),
    ],
)


# Callbacks
@callback(
    Output("paper-modal", "is_open"),
    Output("modal-title", "children"),
    Output("modal-content", "children"),
    Input({"type": "view-card", "index": dash.ALL}, "n_clicks"),
    Input("close-modal", "n_clicks"),
    State({"type": "view-card", "index": dash.ALL}, "id"),
    State("paper-modal", "is_open"),
    prevent_initial_call=True,
)
def display_paper_details(view_clicks, close_click, ids, is_open):
    ctx = dash.callback_context

    if not ctx.triggered:
        return is_open, "", ""

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if "close-modal" in triggered_id:
        return False, "", ""

    if view_clicks:
        index = eval(triggered_id)["index"]
        paper = papers[index]
        content = html.Div(
            [
                html.P(paper["abstract"], style={"font-style": "italic"}),
                html.P(f"Date: {paper['date']}"),
                html.A(
                    "Read Full Paper",
                    href=paper["link"],
                    target="_blank",
                    className="paper-link",
                ),
                html.A(
                    "GitHub Repository" if paper["github"] else "Code not available",
                    href=paper["github"] if paper["github"] else "#",
                    target="_blank" if paper["github"] else "",
                    className="paper-link",
                ),
            ]
        )
        return True, paper["title"], content

    return is_open, "", ""
