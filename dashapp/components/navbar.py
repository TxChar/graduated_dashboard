import dash_bootstrap_components as dbc
from dash import callback, html, Input, Output, dash_table, dcc


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
                                "เกี่ยวกับ",
                                href="/about",
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
