import dash_bootstrap_components as dbc
from components.navbar import Navbar
from dash import dcc, html

layout = html.Div(
    children=[
        Navbar(),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns"), width=3),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns"), width=3),
            ]
        ),
    ],
)
