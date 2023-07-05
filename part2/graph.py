import pandas as pd
import plotly.express as px
from dash import dcc, callback, Input, Output
from dash.exceptions import PreventUpdate


def build_graph_area():
    return dcc.Graph(id="data-graph")


@callback(Output("data-graph", "figure"), Input("data-store", "data"))
def update_graph(data):
    if data is None:
        raise PreventUpdate
    df = pd.read_json(data)
    fig = px.scatter(df, x="Day", y="Temperature")
    return fig
