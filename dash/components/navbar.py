import dash_bootstrap_components as dbc

def getNavbar():
    return dbc.NavbarSimple(
        # children=[
        #     dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        #     dbc.DropdownMenu(
        #         children=[
        #             dbc.DropdownMenuItem("More pages", header=True),
        #             dbc.DropdownMenuItem("Page 2", href="#"),
        #             dbc.DropdownMenuItem("Page 3", href="#"),
        #         ],
        #         nav=True,
        #         in_navbar=True,
        #         label="More",
        #     ),
        # ],
        brand="AI Hackathon",
        brand_href="#",
        color="primary",
        dark=True,
    )