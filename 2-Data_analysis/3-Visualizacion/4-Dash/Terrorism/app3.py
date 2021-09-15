import os
import pathlib
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(__name__)

mapbox_access_token = "pk.eyJ1IjoiZGFvcnRpIiwiYSI6ImNrZnF6M3FlczA3cDEyem16YTNzZmV4M2EifQ.846iF0sMSAXv0kwkwUTYjg"

# Lectura de datos. Importalos desde la ruta donde tengas el CSV
df = pd.read_csv('C:/Users/Daney/Desktop/globalterrorismdb_0718dist.csv', encoding='ISO-8859-1', low_memory=False)

# Limpieza
df.rename(columns={'iyear': 'Year', 'imonth': 'Month', 'iday': 'Day', 'country_txt': 'Country', 'region_txt': 'Region',
                   'attacktype1_txt': 'AttackType', 'target1': 'Target', 'nkill': 'Killed', 'nwound': 'Wounded',
                   'summary': 'Summary', 'gname': 'Group', 'targtype1_txt': 'Target_type',
                   'weaptype1_txt': 'Weapon_type', 'motive': 'Motive'}, inplace=True)

# Filtrado de columnas
list_filtered = ['Year', 'Month', 'Day', 'Country', 'Region', 'city', 'latitude', 'longitude', 'AttackType', 'Killed',
                 'Wounded', 'Target', 'Summary', 'Group', 'Target_type', 'Weapon_type', 'Motive']
df = df[list_filtered]

# TODO Codigo para declarar el figure del mapa (Densitymapbox)


app.layout = html.Div(
    id="root",
    children=[
        html.Div(
            id="header",
            children=[
                html.H4(children="Ataques terroristas globales desde 1970"),
                html.P(
                    id="description",
                    children="Información sobre más de 180.000 ataques terroristas\
                             Global Terrorism Database (GTD) es una base de datos de código abierto\
                             que incluye información sobre ataques terroristas en todo el mundo desde\
                             1970 hasta 2017. GTD incluye datos sistemáticos sobre incidentes\
                             terroristas nacionales e internacionales que han ocurrido durante\
                             este período de tiempo y ahora incluye más de 180.000 ataques.\
                             La base de datos es mantenida por investigadores del Consorcio\
                             Nacional para el Estudio del Terrorismo y Respuestas al Terrorismo\
                             (START), con sede en la Universidad de Maryland.",
                ),
                # TODO Codigo de los KPIs
            ]

        ),

        html.Div(
            id="app-container",
            children=[

                html.Div(
                    id="left-column",
                    children=[
                        html.Div(
                            id="heatmap-container",
                            children=
                            [
                                # TODO Mapa
                            ],
                        ),
                    ],
                ),
                html.Div(
                    id="graph-container",
                    style={'marginTop': 20},
                    children=
                    [
                        # TODO Selector y graficas
                    ],
                )

            ]
        )
    ]
)


# @app.callback(
#     Output("selected-data", "figure"),
#     [
#         Input("chart-dropdown", "value")
#     ],
# )
# def display_selected_data(chart_dropdown):
#
#     # TODO Callback del selector de graficas
#     # Tipo de graficas: px.bar()


if __name__ == '__main__':
    app.run_server(debug=True)
