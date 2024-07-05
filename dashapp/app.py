import dash_bootstrap_components as dbc
from callbacks.callbacks import register_callbacks
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from pages import homepage, layout

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.DARKLY],
)
app.title = "GRADUATED STUDENTS DASH"

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content"),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/layout":
        return layout.layout
    else:
        return homepage.layout


if __name__ == "__main__":
    server = app.server
    register_callbacks(app)
    app.run_server(debug=True)
