import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps.dbconnect import getDataFromDB


def ticketstatus_loadstatus():
    """Fetch ticket statuses dynamically from the database."""
    sql = "SELECT DISTINCT ticket_status_name FROM ticket_status"
    col = ["ticket_status_name"]
    df = getDataFromDB(sql, [], col)
    return [{'label': status, 'value': status} for status in df['ticket_status_name']]

def teamname_loadname():
    """Fetch ticket statuses dynamically from the database."""
    sql = "SELECT DISTINCT personnel_team_name FROM personnel_team"
    col = ["personnel_team"]
    df = getDataFromDB(sql, [], col)
    return [{'label': choice, 'value': choice} for choice in df['personnel_team']]

layout = html.Div(
    [
        
        html.H2('Ticket Management'), # Page Header
        html.Hr(),
        dbc.Card( # Card Container
            [
                dbc.CardHeader( # Define Card Header
                    [
                        html.H3('Manage Records')
                    ]
                ),
                dbc.CardBody( # Define Card Contents
                    [
                        html.Div( # Create section to show list of movies
                            [
                                html.H4('Find Movies'),
                                html.Div(
                                    dbc.Form(
                                        dbc.Row(
                                            [
                                                dbc.Label("Filter by Status", width=1),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        id='ticket_filter',
                                                        options=ticketstatus_loadstatus(), 
                                                        placeholder='Select Ticket Status',
                                                        clearable=True
                                                    ),
                                                    width=5
                                                ),
                                                dbc.Label("Filter by Team", width=1),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        id='ticket_filter_team',
                                                        options = teamname_loadname(), 
                                                        placeholder='Select Team',
                                                        clearable=True
                                                    ),
                                                    width = 4
                                                ),
                                                
                                            ],
                                        )
                                    )
                                ),
                                html.Div(
                                    "Table with movies will go here.",
                                    id='ticket_list'
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)


#TICKETS [NEWWWW]
@app.callback(
    [
        Output('ticket_list', 'children'),
    ],
    [
        Input('url', 'pathname'),
        Input('ticket_filter', 'value'),
    ],
)
def updateRecordsTable(pathname, titlefilter):

    if pathname == '/ticket-management':
        pass
    else:
        raise PreventUpdate

    sql = """ SELECT request_id, ticket_status_name
    FROM request r
        INNER JOIN ticket_status t ON r.ticket_status_id = t.ticket_status_id
    """
    val = []

    if titlefilter:
        sql += """ WHERE ticket_status_name ilike %s"""
        val += [f'%{titlefilter}%']
    
    col = ["Request No.", "Status"]

    df = getDataFromDB(sql, val, col)

    df['Action'] = [
        html.Div(
            dbc.Button("Edit", color='warning', size='sm', 
                        href = f"/ticket-management-profile?mode=edit&id={row['Request No.']}"),
            className='text-center'
        ) for idx, row in df.iterrows()
    ]
    
    # we don't want to display the 'id' column -- let's exclude it
    df = df[["Request No.", "Status", 'Action']]

    movie_table = dbc.Table.from_dataframe(df, striped=True, bordered=True,
                                        hover=True, size='sm')
#
    
    return [movie_table]







