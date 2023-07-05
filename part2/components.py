import base64
import io

import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc, callback, Output, Input
from dash.exceptions import PreventUpdate


def build_data_upload_area():
    component = dbc.Stack(
        [
            html.H3("Upload file"),
            dcc.Upload(
                id="upload-data",
                children=html.Div(
                    ["Drag and drop or ", html.A(html.B("Select data file"))]
                ),
                style={
                    "width": "100%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                },
            ),
        ]
    )

    return component


@callback(
    Output("data-store", "data"),
    Input("upload-data", "contents"),
    prevent_initial_call=True,
)
def parse_upload(contents):
    if contents is None:
        raise PreventUpdate
    df = parse_csv(contents)
    df = df.rename(columns={"Maximum temperature (Degree C)": "Temperature"})
    data = df[["Year", "Month", "Day", "Temperature"]]
    return data.to_json()


def parse_csv(contents) -> pd.DataFrame:
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.BytesIO(decoded))
    return df
