import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

button_style = {'color': '#fff', 'margin-right': '1.5em'}


# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    dbc.Row(
        [
            # 2/3 Section
            dbc.Col(
                html.Div(
                    [
                        html.H2('Welcome to the After-Sales Service Portal'),
                        html.Br(),
                        html.P(
                            "Our platform is designed to streamline the after-sales service process for both customers and employees. "
                            "Whether you're submitting a service request or checking on the status of your existing requests, "
                            "our system makes the process quick and easy."
                        ),
                        html.Br(),
                        html.P(
                            "For Customers: You can submit a service request for any issues you face with our products and track the status "
                            "of your requests in real-time."
                        ),
                        html.Br(),
                        html.P(
                            "For Employees: Our system enables you to manage and update the status of all service requests. You’ll be able to "
                            "see all incoming tickets, prioritize them, and provide timely updates to our customers."
                        ),
                        
                    ]
                ),
                width=8
            ),

            # 1/3 Section
            dbc.Col(
                html.Div(
                    [
                        # For Customers
                        html.Div(
                            [
                                html.H4("For Customers"),
                                html.Div(
                                    [
                                        dcc.Link(
                                            html.Button("Submit a Service Request", id="submit-request-button", className="btn btn-primary", style={'width': '100%', 'margin-bottom': '10px'}),
                                            href="/req_form?mode=add",  # The target URL
                                        ),

                                        dcc.Link(
                                            html.Button("Check Ticket Status", id="check-status-button", className="btn btn-secondary", style={'width': '100%'}),
                                            href="/ticket-track",  # The target URL
                                        ),
                                    ],
                                    style={'text-align': 'center', 'display': 'flex', 'flex-direction': 'column'}
                                ),
                            ],
                            style={'border': '1px solid #dee2e6', 'padding': '15px', 'border-radius': '8px', 'margin-bottom': '20px'}
                        ),

                        # For Employees
                        html.Div(
                            [
                                html.H4("For Employees"),
                                dcc.Input(placeholder='Enter your employee ID', type='text', className="form-control mb-2"),
                                dcc.Input(placeholder='Enter your password', type='password', className="form-control mb-2"),
                                html.Div(
                                    [
                                        html.Button("Login", id="login-button", className="btn btn-success", style={'width': '100%'}),
                                    ]

                                )
                            ],
                            style={'border': '1px solid #dee2e6', 'padding': '15px', 'border-radius': '8px'},
                        ),
                    ]
                ),
                width=4
            )
        ]
    )
)
