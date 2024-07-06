from callbacks.api import graduated_api, provinces_location
from dash.dependencies import Input, Output
from dash import Input, Output, dash_table, dcc
import plotly


def table_slection(app):
    @app.callback(
        Output("output-table", "children"), [Input("provinces-dropdown", "value")]
    )
    def update_table(selected_province):
        df = (graduated_api()).drop(["pp3year", "level"], axis=1)

        if selected_province:
            df = df[df["schools_province"].isin(selected_province)]

        graduated_df = df.rename(
            columns={
                "level": "ระดับการศึกษา",
                "schools_province": "จังหวัด",
                "totalmale": "จำนวนผู้ชาย",
                "totalfemale": "จำนวนผู้หญิง",
                "totalstd": "จำนวนทั้งหมด",
            }
        )

        graduated_table = dash_table.DataTable(
            columns=[{"name": col, "id": col} for col in graduated_df.columns],
            data=graduated_df.to_dict("records"),
            style_header={
                "color": "black",
                "fontWeight": "bold",
                "backgroundColor": "rgb(200, 200, 200)",
            },
            style_cell={"padding-right": "10px", "fontSize": 18},
            style_data={"color": "black", "backgroundColor": "white"},
            style_table={"borderRadius": "10px", "overflow": "hidden"},
            style_data_conditional=[
                {
                    "if": {"row_index": "odd"},
                    "backgroundColor": "rgb(220, 220, 220)",
                }
            ],
        )
        return graduated_table


def map_selection(app):
    @app.callback(
        Output("output-map", "children"), [Input("provinces-dropdown", "value")]
    )
    def update_map(selected_province):
        # df = (graduated_api()).drop(["pp3year", "level"], axis=1)
        df_merge_locations = provinces_location()
        df_merge_locations = df_merge_locations.rename(
            columns={
                "latitude": "lat",
                "longitude": "lon",
            }
        )
        # fig = px.scatter_mapbox(
        #     df_merge_locations,
        #     lat="lat",
        #     lon="lon",
        #     hover_name="City",
        #     hover_data=["State", "Population"],
        #     color_discrete_sequence=["fuchsia"],
        #     zoom=3,
        #     height=300,
        # )
        # fig.update_layout(mapbox_style="open-street-map")
        # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig = plotly.express.density_mapbox(
            df_merge_locations,
            radius=20,
            # lat=df_merge_locations["lat"],
            # lon=df_merge_locations["lon"],
            z="totalstd",
            zoom=5,
            height=800,
            center=dict(lat=13.736717, lon=100.523186),
            mapbox_style="open-street-map",
            color_continuous_scale="Jet",
            range_color=(0, 20000),
        )
        print(">>>>", df_merge_locations)

        fig.update_layout(paper_bgcolor="#024070", plot_bgcolor="#024070")

        fig = dcc.Graph(figure=fig)
        return fig


def register_callbacks(app):
    table_slection(app)
    map_selection(app)
