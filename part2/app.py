import dash_bootstrap_components as dbc
from dash import Dash, html, dcc

from part2.components import build_data_upload_area
from part2.graph import build_graph_area

# Create the app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

# Set the title
app.title = "Example app"


# Define the initial layout
def serve_layout():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            build_data_upload_area(),
                            style={
                                "height": "100%",
                                "padding": "10px",
                                "overflow": "hidden scroll",
                            },
                        ),
                        style={"height": "100%"},
                    ),
                    dbc.Col(
                        [html.Div(children=build_graph_area(), id="graph-area")],
                        width=9,
                    ),
                ],
                style={"height": "100%"},
            ),
            dcc.Store(id="data-store", storage_type="session"),
        ],
        style={"height": "100vh"},
        fluid=True,
    )


# Set the app layout
app.layout = serve_layout

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
