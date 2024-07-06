import dash_bootstrap_components as dbc


def Navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("หน้าหลัก", href="/")),
            dbc.NavItem(dbc.NavLink("ตาราง", href="/layout")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("กรุณาเลือกหน้า", header=True),
                    dbc.DropdownMenuItem("ตาราง", href="/layout"),
                ],
                nav=True,
                in_navbar=True,
                label="อื่น ๆ",
            ),
        ],
        brand="แดชบอร์ด นักเรียนมัธยมศึกษาปีที่6 ที่สำเร็จการศึกษาประจำปี2566",
        brand_href="/",
        color="primary",
        dark=True,
        className="navbar",
    )
