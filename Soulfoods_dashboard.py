import pandas as pd
import os
import glob

file =glob.glob(os.path.join("data",'*.csv'))
df =pd.concat((pd.read_csv(f) for f in file), ignore_index=True)
print(len(df))
df = df[df["product"]=="pink morsel"]
df["price"] = (df["price"].str.replace("$","").astype(float))
df["sales"]=df["quantity"]*df["price"]
df = df[["sales","date","region"]]
df.to_csv("sales_data.csv",index=False)

