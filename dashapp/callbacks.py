from dash.dependencies import Input, Output
from dash import dash_table
import pandas
from api import graduated_api


def register_callbacks(app):
    @app.callback(
        Output("output-table", "children"), [Input("provinces-dropdown", "value")]
    )
    def update_table(selected_province):
        df = (graduated_api()).drop(["pp3year"], axis=1)
        if selected_province:
            df = df[df["schools_province"] == selected_province]
        graduated_df = df.rename(
            columns={
                "level": "ระดับการศึกษา",
                "schools_province": "จังหวัด",
                "totalmale": "จำนวนผู้ชาย",
                "totalfemale": "จำนวนผู้หญิง",
                "totalstd": "จำนวนทั้งหมด",
            }
        )

        return dash_table.DataTable(
            columns=[{"name": col, "id": col} for col in graduated_df.columns],
            data=graduated_df.to_dict("records"),
        )
