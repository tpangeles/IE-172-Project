import webbrowser

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from apps import commonmodules as cm
from apps import home

from apps.movies import movie_management
from apps.movies import movie_management_profile

from apps import req_form
from apps import ticket_track
from apps import ticket_management
from apps import ticket_management_profile

# Importing your app variable from app.py so we can use it
from app import app

app.layout = html.Div(
    [
        # Location Variable -- contains details about the url
        dcc.Location(id='url', refresh=True),

        cm.navbar,

        # Page Content -- Div that contains page layout
        html.Div(id='page_content', className='m-2 p-2'),
    ]
)

@app.callback(
    [
        Output('page_content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)
def displaypage (pathname):
    
    # This code block extracts the id of the triggered input
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]   
    else:
        raise PreventUpdate

        
    # This code block executes action based on the value of eventid
    if eventid == 'url':
        if pathname == '/' or pathname == '/home':
            returnlayout = home.layout

        elif pathname == '/movies/movie_management':
            returnlayout = movie_management.layout

        elif pathname == '/movies/movie_management_profile':
            returnlayout = movie_management_profile.layout


        elif pathname == '/req_form':
            returnlayout = req_form.layout
        elif pathname == '/ticket-track':
            returnlayout = ticket_track.layout
        elif pathname == '/ticket-management':
            returnlayout = ticket_management.layout
        elif pathname == '/ticket-management-profile':
            returnlayout = ticket_management_profile.layout


        else:
            returnlayout = 'error404'
    
    else: 
        raise PreventUpdate
    
    return [returnlayout]
    

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)
