# package imports
from dash import html, callback, Output, Input, State
import dash_bootstrap_components as dbc

# local imports
from utils.images import logo_encoded  # Assuming you have a base64 encoded image

# Define the navbar component
navbar = dbc.Navbar(
    dbc.Container(
        [
            # Brand/Logo on the left
            html.A(
                dbc.Row(
                    [
                        # Placeholder for logo, adjust height if necessary
                        dbc.Col(html.Img(src=logo_encoded, height="40px")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                className="logo-link",
                style={"textDecoration": "none"},
            ),
            # Navbar toggler for small screens
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            # Collapsible part of the navbar (for small screens)
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                "About",
                                href="/about",
                                className="nav-link-custom",
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                "Research Papers",
                                href="/research_papers",
                                className="nav-link-custom",
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                "References",
                                href="/references",
                                className="nav-link-custom",
                            )
                        ),
                    ],
                    className="ms-auto",  # Align the navigation links to the right
                    navbar=True,
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    className="navbar-custom",
)


# Callback to toggle the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open"),
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
