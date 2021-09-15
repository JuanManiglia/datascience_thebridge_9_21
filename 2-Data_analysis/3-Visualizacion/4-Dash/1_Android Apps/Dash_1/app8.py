

# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.GRID, external_stylesheets])

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

df = df[df['Reviews'] >= 1000000]

fig1 = px.scatter(df, x="Reviews", y="Rating",
                  color='Category', hover_data=['App'])

df_bars = df.groupby(['Category', 'Installs'])['App'].count().reset_index().sort_values('App', ascending=False)

fig2 = px.bar(df_bars, x="Category", y="App", color="Installs")


app.layout = html.Div(
        [
            dbc.Row(dbc.Col(html.H1(children='Dashboard aplicaciones Android'))),
            dbc.Row([
                    dbc.Col(dcc.Dropdown(
                        id='id_free_paid',
                        options=[
                            {'label': 'Free', 'value': 'Free'},
                            {'label': 'Paid', 'value': 'Paid'}
                        ],
                        value=['Free', 'Paid'],
                        multi=True
                    )),
                    dbc.Col(dcc.RangeSlider(
                        id='id_reviews_slider',
                        count=1,
                        min=df["Reviews"].min(),
                        max=df["Reviews"].max(),
                        step=1,
                        value=[df["Reviews"].min(), df["Reviews"].max()]
                    ))
            ]),

            dbc.Row([
                dbc.Col(
                        dcc.Graph(
                                id='scatter',
                                figure=fig1
                                )
                ),
                dbc.Col(
                        dcc.Graph(
                                id='bars',
                                figure=fig2
                                )
                )
            ])
        ]
)


@app.callback(
    Output('scatter', 'figure'),
    Output('bars', 'figure'),
    [Input('id_free_paid', 'value'),
     Input('id_reviews_slider', 'value')])
def update_graphs_selector(selected_type, reviews):
    filtered_df = df[df["Type"].isin(selected_type)]
    filtered_df = filtered_df[filtered_df["Reviews"] >= reviews[0]]
    filtered_df = filtered_df[filtered_df["Reviews"] <= reviews[1]]

    fig = px.scatter(filtered_df, x="Reviews", y="Rating",
                      color='Category', hover_data=['App'])

    df_bars = filtered_df.groupby(['Category', 'Installs'])['App'].count().reset_index().sort_values('App', ascending=False)
    fig2 = px.bar(df_bars, x="Category", y="App", color="Installs")

    fig.update_layout()
    fig2.update_layout()

    return fig, fig2


if __name__ == '__main__':
    app.run_server(debug=True)