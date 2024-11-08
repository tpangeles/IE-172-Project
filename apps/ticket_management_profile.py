import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate

from app import app
from apps.dbconnect import getDataFromDB, modifyDB

def clienttype_loadtype():
    """Fetch ticket statuses dynamically from the database."""
    sql = "SELECT DISTINCT client_type_name FROM client_type"
    col = ["client_type"]
    df = getDataFromDB(sql, [], col)
    return [{'label': status, 'value': status} for status in df['client_type']]
def machinestatus_loadstatus():
    """Fetch ticket statuses dynamically from the database."""
    sql = "SELECT DISTINCT machine_status_name FROM machine_status"
    col = ["machine_status"]
    df = getDataFromDB(sql, [], col)
    return [{'label': status, 'value': status} for status in df['machine_status']]


layout = html.Div(
    [
        html.H2('Ticket Management Profile'), # Page Header
        html.Hr(),
        dbc.Alert(id='request_alert', is_open=False), # For feedback purposes
        
        dbc.Row(
            [
                dbc.Col(
                    html.H3('Job Ticket No. {{request_id}}')
                ),
                
                dbc.Col(
                    html.H3('Current Status: {{Y}}')
                )

            ]

        ),




        dbc.Form(
            [
                dbc.Row(
                    [
                        # For Left Half
                        dbc.Col(
                            [
                                html.H4('Client Details'),
                                dbc.Row(
                                    [
                                        dbc.Label("Client Name", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text', 
                                                id='request_title',
                                                placeholder="Client Name"
                                            ),
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),
                                dbc.Row(
                                    [
                                        dbc.Label("Client Company", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text', 
                                                id='request_company',
                                                placeholder="Client Company"
                                            ),
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),
                                dbc.Row(
                                    [
                                        dbc.Label("Client Type", width=2),
                                        dbc.Col(
                                            html.Div(
                                                dcc.Dropdown(
                                                    id='request_type',
                                                    options=clienttype_loadtype(),
                                                    placeholder='Client Type'
                                                ),
                                                className='dash-bootstrap'
                                            ),
                                            width=7,
                                        ),
                                    ],
                                    className='mb-3'
                                ),
                                dbc.Row(
                                    [
                                        dbc.Label("Client Address", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text', 
                                                id='request_address',
                                                placeholder="Client Address"
                                            ),
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),
                                dbc.Row(
                                    [
                                        dbc.Label("Product Serial No.", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text', 
                                                id='request_prod_serial',
                                                placeholder="Product Serial No."
                                            ),
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),
                                dbc.Row(
                                    [
                                        dbc.Label("Product Name", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text', 
                                                id='request_prod_name',
                                                placeholder="Product Name"
                                            ),
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),
                                dbc.Row(
                                    [
                                        dbc.Label("Warranty", width=2),
                                        dbc.Col(
                                            dbc.RadioItems(
                                                options=[
                                                    {"label": "Yes", "value": 1},
                                                    {"label": "No", "value": 2},
                                                ],
                                                value=1,
                                                id='request_warranty',
                                            ),
                                        ),
                                    ],
                                    className='mb-3'
                                ),
                            ]
                        ),




                        # For Right Half
                        dbc.Col(
                            [

                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Label("Product Issue", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text', 
                                                id='request_prod_issue',
                                                placeholder="Product Issue"
                                            ),
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),

                                dbc.Row(
                                    [
                                        dbc.Label("Issue Details", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text', 
                                                id='request_prod_issue_detailds',
                                                placeholder="Issue Details"
                                            ),
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),
                                dbc.Row(
                                    [
                                        dbc.Label("Machine Status", width=2),
                                        dbc.Col(
                                            html.Div(
                                                dcc.Dropdown(
                                                    id='request_type',
                                                    options=machinestatus_loadstatus(),
                                                    placeholder='Machine Status'
                                                ),
                                                className='dash-bootstrap'
                                            ),
                                            width=7,
                                        ),
                                    ],
                                    className='mb-3'
                                ),
                                

                                dbc.Row(
                                    [
                                        dbc.Label("Next Step", width=2),
                                        dbc.Col(     
                                            [                             
                                                dbc.Button(
                                                    'Approve',
                                                    id='request_approve',
                                                    n_clicks=0, # Initialize number of clicks
                                                    className='me-2'  # Adds margin-end (right) spacing
                                                ),
                                                dbc.Button(
                                                    'Disapprove',
                                                    id='request_disapprove',
                                                    n_clicks=0 # Initialize number of clicks
                                                )
                                            ],
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),

                                dbc.Row(
                                    [
                                        dbc.Label("Remarks", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type='text', 
                                                id='remarks',
                                                placeholder="Remarks"
                                            ),
                                            width=7
                                        )
                                    ],
                                    className='mb-3'
                                ),
                                
                            ]
                        ),
                    ]
                )




            ]
        ),
        dbc.Button(
            'Submit',
            id='request_submit',
            n_clicks=0 # Initialize number of clicks
        ),
        dbc.Modal( # Modal = dialog box; feedback for successful saving.
            [
                dbc.ModalHeader(
                    html.H4('Save Success')
                ),
                dbc.ModalBody(
                    'Message here! Edit me please!'
                ),
                dbc.ModalFooter(
                    dbc.Button(
                        "Proceed",
                        href='/movies/movie_management' # Clicking this would lead to a change of pages
                    )
                )
            ],
            centered=True,
            id='movieprofile_successmodal',
            backdrop='static' # Dialog box does not go away if you click at the background
        )
    ]
)