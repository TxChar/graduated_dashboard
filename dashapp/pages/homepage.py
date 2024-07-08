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

card_content = [
    dbc.CardHeader("Card header"),
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

# กำหนดเลย์เอาท์ของแอป
layout = html.Div(
    children=[
        Navbar(),
        # Dropdown Provinces
        dbc.Container(
            dbc.Container(
                [
                    html.Hr(),
                    dbc.Col(
                        [
                            html.H4(
                                "จังหวัด",
                                style={"color": "white", "marginLeft": "20px"},
                            )
                        ]
                    ),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    dcc.Dropdown(
                                        id="provinces-dropdown",
                                        options=dropdown_options,
                                        placeholder="ทุกจังหวัด",
                                        multi=True,
                                        style={
                                            "color": "black",
                                        },
                                    ),
                                ]
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#024070", "border-radius": "20px"},
            ),
        ),
        # Display Card
        dbc.Container(
            dbc.Container(
                [
                    html.Hr(),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Card(
                                                    id="male-card",
                                                    color="primary",
                                                    inverse=True,
                                                )
                                            ),
                                            dbc.Col(
                                                dbc.Card(
                                                    id="female-card",
                                                    color="danger",
                                                    inverse=True,
                                                )
                                            ),
                                            dbc.Col(
                                                dbc.Card(
                                                    id="summary-card",
                                                    color="success",
                                                    inverse=True,
                                                )
                                            ),
                                        ],
                                        className="mb-4",
                                    ),
                                ]
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#024070", "border-radius": "20px"},
            ),
        ),
        # MAP
        dbc.Container(
            dbc.Container(
                [
                    html.Hr(),
                    dbc.Col(
                        [
                            html.H4(
                                "แผนที่", style={"color": "white", "marginLeft": "20px"}
                            )
                        ]
                    ),
                    html.Hr(),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    html.Div(id="output-map"),
                                ]
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#024070", "border-radius": "20px"},
            ),
        ),
        # Table
        dbc.Container(
            dbc.Container(
                [
                    html.Hr(),
                    dbc.Col(
                        [
                            html.H4(
                                "ตาราง", style={"color": "white", "marginLeft": "20px"}
                            )
                        ]
                    ),
                    html.Hr(),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    html.Div(id="output-table"),
                                ]
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#024070", "border-radius": "20px"},
            ),
        ),
        Footer(),
    ]
)
