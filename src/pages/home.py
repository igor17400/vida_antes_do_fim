# package imports
import dash
from dash import html, dcc, callback, Input, Output

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
                            "Preserving Indigenous People, Culture and Language Through Technology",
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
            children=[html.H1("Indigenous Populations - Brasil"), html.Div(className="underline")],
        ),
        html.Div(
            className="section-title",
            children=[html.H1("What next?"), html.Div(className="underline")],
        ),
        # Call-to-action buttons
        html.Div(
            [
                html.A(
                    html.Button(
                        "About Indigenous Populations",
                        className="cta-button cta-button-secondary",
                    ),
                    href="/indigenous_populations",
                ),
                html.A(
                    html.Button(
                        "View Research Papers",
                        className="cta-button cta-button-primary",
                    ),
                    href="/research_papers",
                ),
            ],
            className="cta-buttons-container",
        ),
    ],
)
