from dash import html, dcc
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
        html.H1(children="จำนวนนักเรียนที่สำเร็จการศึกษาประจำปี 2566"),
        dcc.Dropdown(id="provinces-dropdown", options=dropdown_options),  # ค่าเริ่มต้น
        html.Div(id="output-table"),
    ]
)
