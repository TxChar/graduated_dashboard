from dash import html, dcc
import dash_bootstrap_components as dbc
from api import graduated_api
import pandas as pd

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
        html.Br(),
        html.H3(
            children="จำนวนนักเรียนมัธยมศึกษาปีที่ 6 ที่สำเร็จการศึกษาประจำปี 2566",
            style={"textAlign": "center"},
        ),
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
    ]
)
