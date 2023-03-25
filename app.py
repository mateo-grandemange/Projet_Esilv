import dash
from dash import dcc
from dash import html
from dash import Output, Input
#import time
import datetime
import statistics
from statistics import *


app = dash.Dash(__name__)

def get_data():
    with open('/home/ec2-user/projet/projet.txt', 'r') as file:
        lines = file.readlines()
        #last_line = lines[-1].strip()
        last_line = lines[-1] #On recupère la dernière donnée qu'on a grep
        current_time = datetime.datetime.now().strftime('%Y-%m-%d à %H:%M:%S')
    return {"value": last_line, "time": current_time}

data_points = []

app.layout = html.Div([
    html.H1('Dashboard de Mateo Grandemange IF3', style={'text-align': 'center', 'color': 'darkblue'}),
    html.H2('Valeur de l\'action de Société Générale'),
    html.Div(id='data-update'),
    dcc.Graph(id='data-graph', figure={'data': []}, style={'width': '70%', 'height': '70%', 'margin': 'auto'}),
    dcc.Interval(
        id='interval-component',
        interval=5*60*1000,  # mise à jour toutes les 5 min
        n_intervals=0
    )
], style={'background-color': 'lightblue', 'height': '100vh'})

@app.callback(Output('data-update', 'children'),
              [Input('interval-component', 'n_intervals')])

def update_data(n):
    global data_points
    data = get_data()
    data_points.append(data)
    
    daily_values = [float(point['value']) for point in data_points if point['time'].startswith(datetime.datetime.now().strftime('%Y-%m-%d'))]
    daily_average = round(statistics.mean(daily_values), 2) if daily_values else 0
    daily_max = round(max(daily_values), 2)
    daily_min = round(min(daily_values), 2) 

    if datetime.datetime.now().strftime('%H:%M:%S') >= '20:00:00' and datetime.datetime.now().strftime('%H:%M:%S') <= '23:59:59':
        return html.Div([
            html.Div(f'La valeur actuelle est de {data["value"]} €, le {data["time"]}'),
            html.Div(f'Voici les stats de la journée :\n'),
            html.Div(f'Moyenne: {daily_average} €'),
            html.Div(f'Valeur maximale: {daily_max} €'),
            html.Div(f'Valeur minimale: {daily_min} €')
            ])
    else:
        return html.Div([
            html.Div(f'La valeur actuelle est de {data["value"]} €, le {data["time"]}'),
            html.Div(f'Les stats de la journée ne sont pas encore disponibles, veuillez revenir à partir de 20h\n')
            ])
        
    
@app.callback(Output('data-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])

def update_graph(n):
    global data_points
    x_values = [point['time'] for point in data_points if point['time'].startswith(datetime.datetime.now().strftime('%Y-%m-%d'))
                    and '09:00:00' <= point['time'].split(' ')[-1] <= '17:30:00']
    y_values = [point['value'] for point in data_points if point['time'].startswith(datetime.datetime.now().strftime('%Y-%m-%d'))
                    and '09:00:00' <= point['time'].split(' ')[-1] <= '17:30:00']
    return {
        'data': [{
            'x': x_values,
            'y': y_values,
            'type': 'line'
        }],
        'layout': {
            'title': 'Historique des valeurs de l\'action de Société Générale',
            'xaxis': {'title': 'Date et heure'},
            'yaxis': {'title': 'Valeur de l\'action (€)'}
        }
    }

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8050,debug=True)

