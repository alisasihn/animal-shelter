# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

from src.outcome import string_map

app = dash.Dash()

prediction_altered = [string_map[1].keys()]
prediction_sex = [string_map[2].keys()]
prediction_animal_type = [string_map[4].keys()]
prediction_color = [string_map[5].keys()]
prediction_breed = [string_map[7].keys()]
prediction_intake_condition = [string_map[8].keys()]

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
    Dash: A web app framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

    html.Div(
        html.Div(
            html.H1(children='Predict Outcome'),
            html.Label(children='Spayed/Neutered/Intact'),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in prediction_altered],
                value=['Intact']
            ),
            html.Label(children='Sex'),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in prediction_sex],
                value=['Male']
            ),
            html.Label(children='Age (years)'),
            dcc.Input(
                type='number',
                placeholder='age in years'
            ),
            html.Label(children="Animal"),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in prediction_animal_type],
                value=['Dog']
            ),
            html.Label(children='Color'),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in prediction_color]
            ),
            html.Label(children='Month'),
            dcc.Dropdown(
                options=[
                    {'label': 1, 'value': 1},
                    {'label': 2, 'value': 2},
                    {'label': 3, 'value': 3},
                    {'label': 4, 'value': 4},
                    {'label': 5, 'value': 5},
                    {'label': 6, 'value': 6},
                    {'label': 7, 'value': 7},
                    {'label': 8, 'value': 8},
                    {'label': 9, 'value': 9},
                    {'label': 10, 'value': 10},
                    {'label': 11, 'value': 11},
                    {'label': 12, 'value': 12},
                ]
            ),
            html.Label(children='Breed'),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in prediction_breed]
            ),
            html.Label(children='Intake Condition'),
            dcc.Dropdown(
                options=[{'label': i, 'value': i} for i in prediction_intake_condition]
            ),
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
