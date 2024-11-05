# Usual Dash dependencies
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

# Let us import the app object in case we need to define
# callbacks here
from app import app

navlink_style = {'color': '#fff', 'margin-right': '1.5em'}

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Template", className="ms-2")),
                    ],
                    align="center",
                    className='g-0 me-4'
                ),
                href="/home",
                style={'textDecoration': 'none'}
            ),
            dbc.NavLink("Home", href="/home", style=navlink_style),
            dbc.NavLink("Movies", href="/movies", style=navlink_style),
            dbc.NavLink("Genres", href="/genres", style=navlink_style),
            dbc.NavLink("MM", href="/movies/movie_management", style=navlink_style),
            dbc.NavLink("MM Profile", href="/movies/movie_management_profile?mode=add", style=navlink_style),
            dbc.NavLink("1.a. Service Request Form", href="/req_form", style={'color': '#008000', 'margin-right': '1.5em'}),
            dbc.NavLink("1.b. Ticket Tracker", href="/ticket-track", style={'color': '#008000', 'margin-right': '1.5em'}),


            dbc.NavLink("2.a. Ticket Management", href="/ticket-management", style={'color': '#008000', 'margin-right': '1.5em'}),
            dbc.NavLink("2.b. Ticket Profile", href="/ticket-management-profile", style={'color': '#008000', 'margin-right': '1.5em'}),


        ], className='m-0 justify-content-start'
        
    ),
    dark=True,
    color='dark'
)