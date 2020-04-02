# -*- coding: utf-8 -*-
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State

from src.outcome import string_map, predict_input_outcome
from src.time_in_shelter import x_scatter, y_scatter

app = dash.Dash(__name__)
server = app.server

# collect options for dropdowns in outcome prediction
prediction_altered = list(string_map[1].keys())
prediction_sex = list(string_map[2].keys())
prediction_animal_type = list(string_map[4].keys())
prediction_color = list(string_map[5].keys())
prediction_month = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
prediction_breed = list(string_map[7].keys())
prediction_intake_condition = list(string_map[8].keys())

# adoptions by month/year
monthly_adoption_data = pd.read_csv('data/monthly_adoption.csv')
monthly_adoption_data = monthly_adoption_data[monthly_adoption_data['Outcome'] == 'Adoption']
monthly_adoption_data = monthly_adoption_data[monthly_adoption_data['Date'] != '2018-04']
by_date = monthly_adoption_data.groupby('Date')['Outcome'].count()
x_date = by_date.index
y_date = by_date.values

app.title = 'Animal Shelter'

app.layout = html.Div([
    html.H1('Animal Shelter Statistics'),
    html.Div([
        html.H2('Predict Outcome'),
        html.Div([
            html.Div([
                html.Label(
                    [
                        'Spayed/Neutered/Intact *',
                        dcc.Dropdown(
                            id='altered-input',
                            options=[{'label': i, 'value': i} for i in prediction_altered]
                        ),
                    ]
                ),
                html.Label(
                    [
                        'Sex *',
                        dcc.Dropdown(
                            id='sex-input',
                            options=[{'label': i, 'value': i} for i in prediction_sex]
                        ),
                    ]
                ),
                html.Label(
                    [
                        'Age (years) *',
                        dcc.Input(
                            id='age-input',
                            type='number',
                            placeholder='Age in Years',
                            min=0
                        ),
                    ]
                ),
                html.Label(
                    [
                        'Animal *',
                        dcc.Dropdown(
                            id='animal-input',
                            options=[{'label': i, 'value': i} for i in prediction_animal_type]
                        ),
                    ]
                ),
                html.Label(
                    [
                        'Color *',
                        dcc.Dropdown(
                            id='color-input',
                            options=[{'label': i, 'value': i} for i in prediction_color]
                        ),
                    ]
                ),
                html.Label(
                    [
                        'Month of Outcome *',
                        dcc.Dropdown(
                            id='month-input',
                            options=[{'label': i, 'value': i} for i in prediction_month]
                        ),
                    ]
                ),
                html.Label(
                    [
                        'Breed *',
                        dcc.Dropdown(
                            id='breed-input',
                            options=[{'label': i, 'value': i} for i in prediction_breed]
                        ),
                    ]
                ),
                html.Label(
                    [
                        'Intake Condition *',
                        dcc.Dropdown(
                            id='intake-condition-input',
                            options=[{'label': i, 'value': i} for i in prediction_intake_condition]
                        ),
                    ]
                )
            ], className='predict_outcome_input'),
            html.Div([
                html.Div([
                    html.Button(id='submit-params', n_clicks=0, children='Predict'),

                ], className='outcome_button'),
                html.Div(id='outcome-result', className='result_display')
            ], className='predict_outcome_result')
        ], className='predict_outcome')
    ]),
    html.Hr(),
    html.Div([
        dcc.Graph(
            figure={
                'data': [
                    {'x': x_date,
                     'y': y_date,
                     'type': 'line'}
                ],
                'layout': {
                    'title': 'Adoptions by Month',
                    'xaxis': {'title': 'Date'},
                    'yaxis': {'title': 'Adoption Count'}
                }
            }
        )
    ], className='monthly_adoption'),
    html.Hr(),
    html.Div([
        dcc.Graph(
            figure={
                'data': [
                    {'x': x_scatter,
                     'y': y_scatter,
                     'mode': 'markers'}
                ],
                'layout': {
                    'title': 'Time in Shelter by Age',
                    'xaxis': {'title': 'Age (months)'},
                    'yaxis': {'title': 'Time in Shelter (months)'}
                }
            }
        )
    ], className='time_in_shelter')
], className='main')


# submit inputted information to predict outcome of animal
@app.callback(Output('outcome-result', 'children'),
              [Input('submit-params', 'n_clicks')],
              [State('altered-input', 'value'),
               State('sex-input', 'value'),
               State('age-input', 'value'),
               State('animal-input', 'value'),
               State('color-input', 'value'),
               State('month-input', 'value'),
               State('breed-input', 'value'),
               State('intake-condition-input', 'value')])
def return_outcome(n_clicks, input1, input2, input3, input4, input5, input6, input7, input8):
    if n_clicks == 0:
        return ''
    else:
        return predict_input_outcome(input1, input2, input3, input4, input5, input6, input7, input8)


if __name__ == '__main__':
    app.server.run(debug=False)
