

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


def change_m(x):
    if "M" in x:
        return x.replace("M", "000")
    else:
        return x


def change_dollar(x):
    if "$" in x:
        return x.replace("$", "000")
    elif "Everyone" in x:
        return 0
    else:
        return x


df["Price"] = df["Price"].apply(change_dollar)
df["Price"] = pd.to_numeric(df["Price"])
df["Reviews"] = df["Reviews"].apply(change_m)
df["Reviews"] = pd.to_numeric(df["Reviews"])

fig = px.histogram(df, x="Rating", range_x=[0.8, 5.2])
fig2 = px.box(df, x="Category", y="Rating", color="Category", range_y=[0.8, 5.2])
fig3 = px.scatter(df, x="Price", y="Category")


app.layout = html.Div(children=[
    html.H1(children='Dashboard aplicaciones Android'),

    html.Div(children='''
        Primera app de aprendizaje con Dash
    '''),

    html.Div([
            html.Div([
                html.P(
                       "Filter for paind or free apps",
                        className="control_label",
                        ),
                dcc.Dropdown(
                    id='id_free_paid',
                    options=[
                        {'label': 'Free', 'value': 'Free'},
                        {'label': 'Paid', 'value': 'Paid'}
                    ],
                    value=['Free', 'Paid'],
                    multi=True
                ),
                html.P(
                       "Reviews slider",
                        className="control_label",
                        ),
                dcc.RangeSlider(
                    id='id_reviews_slider',
                    count=1,
                    min=df["Reviews"].min(),
                    max=df["Reviews"].max(),
                    step=1,
                    value=[df["Reviews"].min(), df["Reviews"].max()]
                ),
                dcc.Graph(
                    id='example-graph3',
                    figure=fig3
                )

            ], className="five columns"),

            html.Div([

                dcc.Graph(
                    id='example-graph',
                    figure=fig
                ),

                dcc.Graph(
                    id='example-graph-box',
                    figure=fig2)

                ], className="seven columns")
        ])
])


@app.callback(
    Output('example-graph', 'figure'),
    Output('example-graph-box', 'figure'),
    [Input('id_free_paid', 'value'),
     Input('id_reviews_slider', 'value')])
def update_graphs_selector(selected_type, reviews):
    filtered_df = df[df["Type"].isin(selected_type)]
    filtered_df = filtered_df[filtered_df["Reviews"] >= reviews[0]]
    filtered_df = filtered_df[filtered_df["Reviews"] <= reviews[1]]

    fig = px.histogram(filtered_df, x="Rating", range_x=[0.8, 5.2])
    fig2 = px.box(filtered_df, x="Category", y="Rating", color="Category", range_y=[0.8, 5.2])

    fig.update_layout()
    fig2.update_layout()

    return fig, fig2

if __name__ == '__main__':
    app.run_server(debug=True)