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
                                "เกี่ยวกับผู้จัดทำ",
                                style={"color": "white", "marginLeft": "20px"},
                            )
                        ]
                    ),
                    dbc.Container(
                        [
                            dbc.Container(
                                [html.H1("HELLO WORLD!", style={"color": "white"})]
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#024070", "border-radius": "20px"},
            ),
        ),
    ]
)
