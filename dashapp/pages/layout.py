import dash_bootstrap_components as dbc
from callbacks.api import graduated_api
from components.navbar import Navbar
from components.footer import Footer
from dash import dcc, html

# เตรียมข้อมูล
df = graduated_api()

# สร้าง dropdown options
dropdown_options = [
    {"label": str(schools_province), "value": schools_province}
    for schools_province in df["schools_province"]
]

# กำหนดเลย์เอาท์ของแอป
layout = html.Div(
    children=[
        Navbar(),
        html.Br(),
        dbc.Container(
            [
                html.Hr(),
                dbc.Col([html.H4("ตาราง")]),
                html.Hr(),
                dbc.Container(
                    [
                        dbc.Container(
                            [
                                dcc.Dropdown(
                                    id="provinces-dropdown",
                                    options=dropdown_options,
                                    placeholder="กรุณาเลือกจังหวัด",
                                    multi=True,
                                    style={
                                        "color": "black",
                                    },
                                ),
                            ]
                        ),
                        html.Br(),
                        dbc.Container(
                            [
                                html.Div(id="output-table"),
                            ]
                        ),
                    ],
                    style={"marginTop": 20, "Align": "center"},
                ),
            ],
            style={"backgroundColor": "#161A1D"},
        ),
        Footer(),
    ]
)
