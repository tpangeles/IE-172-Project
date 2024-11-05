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



layout = html.Div(
    [
        html.H2('Service Request Form'), # Page Header
        html.Hr(),
        dbc.Alert(id='request_alert', is_open=False), # For feedback purposes
        dbc.Form(
            [
                html.H4('Client Details'),
                dbc.Row(
                    [
                        dbc.Label("Client Name", width=1),
                        dbc.Col(
                            dbc.Input(
                                type='text', 
                                id='request_title',
                                placeholder="Client Name"
                            ),
                            width=5
                        )
                    ],
                    className='mb-3'
                ),
                dbc.Row(
                    [
                        dbc.Label("Client Company", width=1),
                        dbc.Col(
                            dbc.Input(
                                type='text', 
                                id='request_company',
                                placeholder="Client Company"
                            ),
                            width=5
                        )
                    ],
                    className='mb-3'
                ),
                dbc.Row(
                    [
                        dbc.Label("Client Type", width=1),
                        dbc.Col(
                            html.Div(
                                dcc.Dropdown(
                                    id='request_type',
                                    options=clienttype_loadtype(),
                                    placeholder='Client Type'
                                ),
                                className='dash-bootstrap'
                            ),
                            width=5,
                        ),
                    ],
                    className='mb-3'
                ),
                dbc.Row(
                    [
                        dbc.Label("Client Address", width=1),
                        dbc.Col(
                            dbc.Input(
                                type='text', 
                                id='request_address',
                                placeholder="Client Address"
                            ),
                            width=5
                        )
                    ],
                    className='mb-3'
                ),
                dbc.Row(
                    [
                        dbc.Label("Product Name", width=1),
                        dbc.Col(
                            dbc.Input(
                                type='text', 
                                id='request_prod_name',
                                placeholder="Product Name"
                            ),
                            width=5
                        )
                    ],
                    className='mb-3'
                ),
                dbc.Row(
                    [
                        dbc.Label("Warranty", width=1),
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
                dbc.Row(
                    [
                        dbc.Label("Product Issue", width=1),
                        dbc.Col(
                            dbc.Input(
                                type='text', 
                                id='request_prod_issue',
                                placeholder="Product Issue"
                            ),
                            width=5
                        )
                    ],
                    className='mb-3'
                ),
                dbc.Row(
                    [
                        dbc.Label("Issue Details", width=1),
                        dbc.Col(
                            dbc.Input(
                                type='text', 
                                id='request_prod_issue_details',
                                placeholder="Issue Details"
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

#@app.callback(
#    [
#        Output('request_genre', 'options')
#    ],
#    [
#        Input('url', 'pathname')
#    ]
#)
#def movieprofile_populategenres(pathname):
#    if pathname == '/movies/movie_management_profile':
#        sql = """
#        SELECT genre_name as label, genre_id as value
#        FROM genres 
#        WHERE genre_delete_ind = False
#        """
#        values = []
#        cols = ['label', 'value']
#
#        df = getDataFromDB(sql, values, cols)
#        # The output must be a dictionary with the following structure
#        # options=[
#        #     {'label': "Factorial", 'value': 1},
#        #     {'label': "Palindrome Checker", 'value': 2},
#        #     {'label': "Greeter", 'value': 3},
#        # ]
#
#        genre_options = df.to_dict('records')
#        return [genre_options]
#    else:
#        raise PreventUpdate
#
#        
#@app.callback(
#    [
#        # dbc.Alert Properties
#        Output('request_alert', 'color'),
#        Output('request_alert', 'children'),
#        Output('request_alert', 'is_open'),
#        # dbc.Modal Properties
#        Output('movieprofile_successmodal', 'is_open')
#    ],
#    [
#        # For buttons, the property n_clicks 
#        Input('request_submit', 'n_clicks')
#    ],
#    [
#        # The values of the fields are States 
#        # They are required in this process but they 
#        # do not trigger this callback
#        State('request_title', 'value'),
#        State('request_genre', 'value'),
#        State('request_releasedate', 'date'),
#    ]
#)
#def movieprofile_saveprofile(submitbtn, title, genre, releasedate):
#    ctx = dash.callback_context
#    # The ctx filter -- ensures that only a change in url will activate this callback
#    if ctx.triggered:
#        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
#        if eventid == 'request_submit' and submitbtn:
#            # the submitbtn condition checks if the callback was indeed activated by a click
#            # and not by having the submit button appear in the layout
#
#            # Set default outputs
#            alert_open = False
#            modal_open = False
#            alert_color = ''
#            alert_text = ''
#
#            # We need to check inputs
#            if not title: # If title is blank, not title = True
#                alert_open = True
#                alert_color = 'danger'
#                alert_text = 'Check your inputs. Please supply the movie title.'
#            elif not genre:
#                alert_open = True
#                alert_color = 'danger'
#                alert_text = 'Check your inputs. Please supply the movie genre.'
#            elif not releasedate:
#                alert_open = True
#                alert_color = 'danger'
#                alert_text = 'Check your inputs. Please supply the movie release date.'
#            else: # all inputs are valid
#                # Add the data into the db
#
#                sql = '''
#                    INSERT INTO movies (movie_name, genre_id,
#                        movie_release_date, movie_delete_ind)
#                    VALUES (%s, %s, %s, %s)
#                '''
#                values = [title, genre, releasedate, False]
#
#                modifyDB(sql, values)
#
#                # If this is successful, we want the successmodal to show
#                modal_open = True
#
#            return [alert_color, alert_text, alert_open, modal_open]
#
#        else: 
#            raise PreventUpdate
#
#    else:
#        raise PreventUpdate
