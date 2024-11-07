import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Create a simple DataFrame for demo purposes with some regions and coordinates
us_states = pd.DataFrame({
    'state': ['California', 'New York', 'Texas'],
    'info': ['2Pac: A renowned rapper from California', 
             'The Notorious B.I.G.: Iconic rapper from Brooklyn, NY',
             'Beyonce: Singer and artist from Houston, Texas'],
    'latitude': [36.7783, 40.7128, 31.9686],
    'longitude': [-119.4179, -74.0060, -99.9018]
})

# Create a map using Plotly Express
fig = px.scatter_mapbox(
    us_states,
    lat='latitude',
    lon='longitude',
    hover_name='state',
    hover_data={'latitude': False, 'longitude': False},
    size_max=15,
    zoom=3,
    height=500
)

# Update map properties to show markers and center the map
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})

# Set up the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container(
    [
        html.H1("U.S. Rapper Information Map"),
        html.P("Click on a state to view more information about famous artists."),
        dcc.Graph(id="us-map", figure=fig),  # Map with click event
        # Modals for displaying information
        dbc.Modal(
            [
                dbc.ModalHeader(id='modal-header'),
                dbc.ModalBody(id='modal-body'),
                dbc.ModalFooter(dbc.Button("Close", id="close", className="ml-auto")),
            ],
            id="modal",
            centered=True,
            is_open=False
        )
    ],
    fluid=True
)

# Define the callback to update the modal based on clicked region
@app.callback(
    [Output("modal", "is_open"),
     Output("modal-header", "children"),
     Output("modal-body", "children")],
    [Input("us-map", "clickData"),
     Input("close", "n_clicks")],
    prevent_initial_call=True
)
def display_info(clickData, n_clicks):
    # Determine which state was clicked
    ctx = dash.callback_context
    if not ctx.triggered or not clickData:
        return False, "", ""  # If nothing is clicked, don't show the modal

    # If the modal close button is clicked, hide the modal
    if ctx.triggered[0]['prop_id'] == 'close.n_clicks':
        return False, "", ""

    # Extract state information from clickData
    selected_state = clickData['points'][0]['hovertext']

    # Filter the corresponding state information
    state_info = us_states[us_states['state'] == selected_state]['info'].values[0]

    # Create two sample graphs based on the selected state
    graph1 = dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=['Metric 1', 'Metric 2', 'Metric 3'],
                    y=[10, 20, 30],
                    name=f'{selected_state} Bar Graph'
                )
            ],
            layout=go.Layout(title=f"Bar Graph for {selected_state}")
        )
    )

    graph2 = dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=[1, 2, 3, 4],
                    y=[4, 3, 2, 1],
                    mode='lines+markers',
                    name=f'{selected_state} Line Graph'
                )
            ],
            layout=go.Layout(title=f"Line Graph for {selected_state}")
        )
    )

    # Create a carousel component with dummy images (can be replaced with state-specific images)
    carousel = dbc.Carousel(
        items=[
            {"key": "1", "src": "https://via.placeholder.com/600x400?text=Slide+1"},
            {"key": "2", "src": "https://via.placeholder.com/600x400?text=Slide+2"},
            {"key": "3", "src": "https://via.placeholder.com/600x400?text=Slide+3"},
        ],
        controls=True,
        indicators=True,
        interval=2000,
        ride="carousel"
    )

    # Create a tabs component with two tabs for different visualizations
    tabs = dbc.Tabs(
        [
            dbc.Tab(label="Charts", tab_id="tab-1", children=[graph1, graph2]),
            dbc.Tab(label="Carousel", tab_id="tab-2", children=[carousel]),
        ]
    )

    # Create the modal content
    modal_content = html.Div([
        html.P(state_info),  # Display the selected state's info
        html.Hr(),
        tabs  # Include the tabs component
    ])

    # Set modal content and show it
    return True, f"Information about {selected_state}", modal_content

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=5002)
