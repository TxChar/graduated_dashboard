import dash_bootstrap_components as dbc
from dash import callback, html, Input, Output, dash_table, dcc

footer_style = {
    "marginTop": "20px",
    "padding": "5px",
    "backgroundColor": "#024070",
    "bottom": "0px",
}


def Footer():
    return html.Div(
        html.Footer(
            dbc.Col(
                [
                    dbc.Col(html.Div("DEVELOPED BY JATURAWICH KHOCHUN")),
                    dbc.Col(html.Div("AIE STUDENT AT PSU")),
                ],
                style={"marginLeft": "1%", "color": "white"},
            ),
            style=footer_style,
        ),
    )
