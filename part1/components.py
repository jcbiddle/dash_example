import dash_bootstrap_components as dbc
from dash import html, callback, Input, Output


def build_button_area():
    """Build the area containing two buttons and a text div"""
    component = dbc.Row([dbc.Col(dbc.Button("Click me!", id="click-btn"), width="auto"),
                         dbc.Col(dbc.Button("Reset counter", id="reset-btn"), width="auto"),
                         dbc.Col(html.Div(id="click-summary-div"))], style={"width": "600px"})
    return component


@callback(Output("click-summary-div", "children"), Input("click-btn", "n_clicks"))
def update_click_summary(n_clicks):
    """Update the text div when the button is pressed"""
    if n_clicks is None:
        return "Not clicked yet"

    return f"You have clicked {n_clicks} times"


@callback(Output("click-btn", "n_clicks"), Input("reset-btn", "n_clicks"))
def update_click_summary(n_clicks):
    """Reset the click counter"""
    return None
