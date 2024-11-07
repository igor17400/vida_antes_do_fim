# package imports
from dash import html
import dash_bootstrap_components as dbc

# Define the footer component
footer = html.Footer(
    dbc.Container(
        [
            html.Hr(),
            dbc.Row(
                [
                    # Left side for texts
                    dbc.Col(
                        html.Div(
                            [
                                html.P(
                                    "Life Before The End.",
                                    className="footer-text",
                                ),
                                html.P(
                                    "Preserving indigenous people, culture and language.",
                                    className="footer-subtext",
                                ),
                                html.P(
                                    [
                                        "Icons by ",
                                        html.A(
                                            "icons8",
                                            href="https://icons8.com/",
                                            target="_blank",
                                        ),
                                        ".",
                                    ],
                                    className="footer-subtext",
                                ),
                            ],
                            className="footer-content",
                        ),
                        width=12,  # Use full width on mobile
                        md=5,  # Half width on medium and larger screens
                    ),
                    # Right side for icons
                    dbc.Col(
                        html.Div(
                            [
                                html.A(
                                    html.Img(
                                        src="https://img.icons8.com/ios-filled/24/FFF5E0/twitter-squared.png",
                                    ),
                                    href="https://twitter.com",
                                    style={"marginRight": "15px"},
                                    target="_blank",
                                    className="icons",
                                ),
                                html.A(
                                    html.Img(
                                        src="https://img.icons8.com/ios-filled/24/FFF5E0/github.png",
                                    ),
                                    href="https://github.com",
                                    target="_blank",
                                    className="icons",
                                ),
                            ],
                            className="footer-social",
                            style={
                                "textAlign": "right",
                                "paddingRight": "15px",
                            },  # Align icons and add padding
                        ),
                        width=12,  # Use full width on mobile
                        md=5,  # Half width on medium and larger screens
                    ),
                ],
                className="justify-content-between",  # Distribute space between columns
                style={"padding": "1rem 0"},  # Padding for the row
            ),
        ],
        fluid=True,
    ),
    className="footer-custom",  # Custom class for footer styling
)
