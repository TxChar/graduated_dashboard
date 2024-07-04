from dash import html, dcc
import pandas as pd

# เตรียมข้อมูล
df = pd.DataFrame(
    {"Year": [2000, 2001, 2002, 2003, 2004], "Value": [10, 15, 13, 17, 20]}
)

# สร้าง dropdown options
dropdown_options = [{"label": str(year), "value": year} for year in df["Year"]]

# กำหนดเลย์เอาท์ของแอป
layout = html.Div(
    children=[
        html.H1(children="Dash: Dropdown Example"),
        dcc.Dropdown(
            id="year-dropdown", options=dropdown_options, value=2000  # ค่าเริ่มต้น
        ),
        html.Div(id="output-table"),
    ]
)
