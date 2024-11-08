# Usual Dash dependencies
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

# Let us import the app object in case we need to define
# callbacks here
from app import app

navlink_style = {'color': '#000', 'margin-right': '1.5em'}
navlink_style_temp = {'color': '#008000', 'margin-right': '1.5em'}

navbar = dbc.Navbar(
    dbc.Container(
        [
            # Logo on the left
            html.A(
                html.Img(
                    src="/assets/logo.png",  # Path to your logo image
                    height="60px",          # Adjust the height as needed
                ),
                href="/home",
                style={'textDecoration': 'none', 'margin-left': '20px'}
            ),
            # Navigation links on the right
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/home", style=navlink_style_temp),
                    dbc.NavLink("MM", href="/movies/movie_management", style=navlink_style),
                    dbc.NavLink("MM Profile", href="/movies/movie_management_profile?mode=add", style=navlink_style),

                    # Dropdown menu for Customers
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("1.a. Service Request Form", href="/req_form?mode=add", style=navlink_style_temp),
                            dbc.DropdownMenuItem("1.b. Ticket Tracker", href="/ticket-track", style=navlink_style_temp),
                        ],
                        label="For Customers",
                        nav=True,
                        style=navlink_style,
                        toggle_style={'color': 'black', 'border': 'none'}
                    ),

                    # Dropdown menu for Employees
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("2.a. Ticket Management", href="/ticket-management", style=navlink_style_temp),
                            dbc.DropdownMenuItem("2.b. Ticket Profile", href="/ticket-management-profile", style=navlink_style_temp),
                        ],
                        label="For Employees",
                        nav=True,
                        style=navlink_style,
                        toggle_style={'color': 'black', 'border': 'none'}
                    ),
                ],
                className="ms-auto",  # Pushes nav links to the right
                navbar=True  # Ensures proper navbar alignment
            ),
        ],
        fluid=True,  # Makes container fluid to cover full width
    ),
    dark=True,
    color='white',
    style={
        'position': 'sticky',
        'top': '0',
        'z-index': '1000',
        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.2)'  # Adds shadow to navbar
    }
)