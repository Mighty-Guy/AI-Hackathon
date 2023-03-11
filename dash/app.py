from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from components.navbar import getNavbar

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options




app.layout = html.Div(children=[
    getNavbar()
])

if __name__ == '__main__':
    app.run_server(debug=True)