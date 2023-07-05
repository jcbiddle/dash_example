import dash_bootstrap_components as dbc
from dash import Dash

from part1.components import build_button_area

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
    return dbc.Container([build_button_area()],
                         fluid=True)


# Set the app layout
app.layout = serve_layout

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
