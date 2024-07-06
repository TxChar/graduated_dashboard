import dash_bootstrap_components as dbc
from dash import callback, html, Input, Output, dash_table, dcc


# def Navbar():
#     return dbc.NavbarSimple(
#         children=[
#             dbc.NavItem(dbc.NavLink("หน้าหลัก", href="/")),
#             dbc.NavItem(dbc.NavLink("ตาราง", href="/layout")),
#             dbc.DropdownMenu(
#                 children=[
#                     dbc.DropdownMenuItem("กรุณาเลือกหน้า", header=True),
#                     dbc.DropdownMenuItem("ตาราง", href="/layout"),
#                 ],
#                 nav=True,
#                 in_navbar=True,
#                 label="อื่น ๆ",
#             ),
#         ],
#         brand="แดชบอร์ด นักเรียนมัธยมศึกษาปีที่6 ที่สำเร็จการศึกษาประจำปี2566",
#         brand_href="/",
#         color="primary",
#         dark=True,
#         className="navbar",
#     )


def Navbar():
    return html.Div(
        [
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(
                        dbc.Button(
                            dbc.NavLink("หน้าหลัก", href="/"),
                            color="primary",
                            className="ms-2",
                            n_clicks=0,
                        )
                    ),
                    dbc.NavItem(
                        dbc.Button(
                            dbc.NavLink(
                                "ตาราง",
                                href="/layout",
                            ),
                            color="primary",
                            className="ms-2",
                            n_clicks=0,
                            id="planet_reports_button",
                        )
                    ),
                ],
                brand="แดชบอร์ด นักเรียนมัธยมศึกษาปีที่6 ที่สำเร็จการศึกษาประจำปี2566",
                brand_style={"fontSize": 20},
                brand_href="/",
                color="#024070",
                dark=True,
            ),
        ]
    )
