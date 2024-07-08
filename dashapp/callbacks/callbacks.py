from callbacks.api import graduated_api, provinces_location
from dash.dependencies import Input, Output
from dash import Input, Output, dash_table, dcc, html
import dash_bootstrap_components as dbc
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
        df_merge_locations = provinces_location()
        df_merge_locations.columns = df_merge_locations.columns.str.strip()

        if selected_province:
            df_merge_locations = df_merge_locations[
                df_merge_locations["schools_province"].isin(selected_province)
            ]

        df_merge_locations = df_merge_locations.rename(
            columns={
                "latitude": "ละติจูด",
                "longitude": "ลองจิจูด",
                "level": "ระดับการศึกษา",
                "schools_province": "จังหวัด",
                "totalmale": "จำนวนผู้ชาย",
                "totalfemale": "จำนวนผู้หญิง",
                "totalstd": "จำนวนทั้งหมด",
            }
        )

        fig = plotly.express.scatter_mapbox(
            df_merge_locations,
            lat="ละติจูด",
            lon="ลองจิจูด",
            hover_name="จังหวัด",
            hover_data=["จำนวนผู้ชาย", "จำนวนผู้หญิง", "จำนวนทั้งหมด"],
            center=dict(lat=13.736717, lon=100.523186),
            color="จำนวนทั้งหมด",
            size="จำนวนทั้งหมด",
            color_continuous_scale=plotly.express.colors.sequential.Rainbow,
            size_max=30,
            zoom=5,
            height=750,
        )
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.update_layout(paper_bgcolor="#024070", plot_bgcolor="#024070")

        fig = dcc.Graph(figure=fig)
        return fig


def summarization_students(app):
    @app.callback(
        [
            Output("male-card", "children"),
            Output("female-card", "children"),
            Output("summary-card", "children"),
        ],
        [Input("provinces-dropdown", "value")],
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

        male_card = [
            dbc.CardHeader("จำนวนผู้ชาย"),
            dbc.CardBody(
                [
                    html.H5("Card title", className="card-title"),
                    html.P(
                        "This is some card content that we'll reuse",
                        className="card-text",
                    ),
                ]
            ),
        ]

        female_card = [
            dbc.CardHeader("จำนวนผู้หญิง"),
            dbc.CardBody(
                [
                    html.H5("Card title", className="card-title"),
                    html.P(
                        "This is some card content that we'll reuse",
                        className="card-text",
                    ),
                ]
            ),
        ]

        summary_card = [
            dbc.CardHeader("จำนวนทั้งหมด"),
            dbc.CardBody(
                [
                    html.H5("Card title", className="card-title"),
                    html.P(
                        "This is some card content that we'll reuse",
                        className="card-text",
                    ),
                ]
            ),
        ]

        return (male_card, female_card, summary_card)


def register_callbacks(app):
    table_slection(app)
    map_selection(app)
