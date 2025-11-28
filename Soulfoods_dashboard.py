import pandas as pd
from dash import html,Dash,dcc
import plotly.express as px
import os
import glob

app= Dash()

#file =glob.glob(os.path.join("data",'*.csv'))
#df =pd.concat((pd.read_csv(f) for f in file), ignore_index=True)
#print(len(df))
#df = df[df["product"]=="pink morsel"]
#df["price"] = (df["price"].str.replace("$","").astype(float))
#df["sales"]=df["quantity"]*df["price"]
#df = df[["sales","date","region"]]
#df.to_csv("sales_data.csv",index=False)

df = pd.read_csv("sales_data.csv")
fig = px.line(df,x="date",y="sales",color="region")

app.layout = html.Div([
    html.Div([html.H1("Sales Data Per Region (2018-2022)"),dcc.Graph(figure=fig)]),
])
app.run(debug=True)

