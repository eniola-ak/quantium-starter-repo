import pandas as pd
from dash import html, Dash, dcc, Output, Input
import plotly.express as px

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv("sales_data.csv")
df = df.sort_values(by=['date'], ascending=True)
colors ={"background": "#111111", "text": "#7FDBFF"}

app.layout = html.Div([
    html.Div([html.H1("Pink Morsels Sales Data", id ="header-one"),html.H4("Sales data Per Region (2018-2022)"),dcc.RadioItems(id="radio",
                                                                          options=[{"label":"North", "value":"north"},
                                                                                   {"label":"South", "value":"south"},
                                                                                   {"label":"East", "value":"east"},
                                                                                   {"label":"West", "value": "west"},
                                                                                   {"label":"All", "value": "All"}],value="All",inline=True), dcc.Graph(id="sales-graph")])
])

@app.callback(Output("sales-graph", "figure"),Input("radio","value"))

def update_graph(value):
    dff = df if value == "All" else df[df["region"]==value]
    fig = px.line(dff,x="date",y="sales",color="region")
    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"]
    )
    return fig
if __name__ == "__main__":
    app.run(debug=True)
