import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate

from app import app
from apps.dbconnect import getDataFromDB, modifyDB

layout = html.Div(
    [
        html.H2('Ticket Tracker'), # Page Header
        html.Hr(),
        dbc.Alert(id='movieprofile_alert', is_open=False), # For feedback purposes
        dbc.Form(
            [
                dbc.Row(
                    [
                        dbc.Label("Ticket Number", width=1),
                        dbc.Col(
                            dbc.Input(
                                type='text', 
                                id='ticket_no',
                                placeholder="Ticket Number"
                            ),
                            width=5
                        )
                    ],
                    className='mb-3'
                ),
            ]
        ),
          dbc.Button(
            'Submit',
            id='movieprofile_submit',
            n_clicks=0 # Initialize number of clicks
        ),
    ]
)