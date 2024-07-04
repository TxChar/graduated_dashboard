from dash.dependencies import Input, Output
from dash import dash_table
import pandas
from api import graduated_api


def register_callbacks(app):
    @app.callback(Output("output-table", "children"), [Input("year-dropdown", "value")])
    def update_table(selected_year):
        # filtered_df = df[df["Year"] == selected_year]
        filtered_df = graduated_api()

        return dash_table.DataTable(
            columns=[{"name": col, "id": col} for col in filtered_df.columns],
            data=filtered_df.to_dict("records"),
        )
