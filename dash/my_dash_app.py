from dash import Dash, html
import dash_bootstrap_components as dbc
from components.navbar import getNavbar
from components.microphone import getMicrophoneComponent, start_recording, stop_recording, update_app
from dash.dependencies import Input, Output

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    getNavbar(),
    html.Div([
        getMicrophoneComponent()
    ]),
    html.Div([
        html.Button("test", id="test"),
        html.Div('', id="test1234")
    ]),


])


app.callback(Output("update-interval", "disabled"), [Input("record-button", "n_clicks")])(start_recording)
app.callback(Output("update-interval-2", "disabled"), [Input("stop-button", "n_clicks")])(stop_recording)
app.callback(Output("output", "children"), [Input("update-interval", "n_intervals")])(update_app)


# @app.callback(Output("test", "figure"), [Input("test", "test")])
# def test(n):
#     print('test 12')


if __name__ == '__main__':
    app.run_server(debug=True)