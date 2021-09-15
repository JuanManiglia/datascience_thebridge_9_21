

# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("data/googleplaystore.csv")

fig = px.histogram(df, x="Rating", range_x=[0.8, 5.2])
fig2 = px.box(df, x="Category", y="Rating", color="Category", range_y=[0.8, 5.2])

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div(children=[
    html.H1(children='Dashboard aplicaciones Android'),

    html.Div(children='''
        Primera app de aprendizaje con Dash
    '''),

    dcc.Dropdown(
        id='id_free_paid',
        options=[
            {'label': 'Free', 'value': 'Free'},
            {'label': 'Paid', 'value': 'Paid'}
        ],
        value=['Free', 'Paid'],
        multi=True
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Graph(
        id='example-graph-box',
        figure=fig2
    ),
    dcc.Markdown(children=markdown_text)
])

@app.callback(
    Output('example-graph', 'figure'),
    Output('example-graph-box', 'figure'),
    [Input('id_free_paid', 'value')])
def update_graphs_selector(selected_type):
    filtered_df = df[df["Type"].isin(selected_type)]

    fig = px.histogram(filtered_df, x="Rating", range_x=[0.8, 5.2])
    fig2 = px.box(filtered_df, x="Category", y="Rating", color="Category", range_y=[0.8, 5.2])

    fig.update_layout()
    fig2.update_layout()

    return fig, fig2


if __name__ == '__main__':
    app.run_server(debug=True)