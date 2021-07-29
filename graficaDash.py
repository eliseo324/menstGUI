from dash.dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


class VentanaGrafica(Dash):
    def __init__(self):
        super(VentanaGrafica, self).__init__()
        df = pd.read_csv('Datos/data.csv')
        self.layout = html.Div(children=[
            html.H1(children='Reporte'),
            html.Div(children='''Reporte temperatura.'''),
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [{'x': df['fecha'], 'y': df['temperatura'], 'type': 'line', 'name': 'Temperatura'}],
                    'layout':
                        go.Layout(title='Reporte de temperatura por dia', barmode='stack')
                })
        ])


if __name__ == '__main__':
    VentanaGrafica().run_server(debug=True)
