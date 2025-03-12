import pandas as pd
import numpy as np

def fun(df,num,ot):
    print(df.head())
    for i in range(len(num)):
        print(df[num[i]].isna().sum())
    for i in range(len(ot)):
        print(df[ot[i]].isna().sum())
    
        
    
file = input("Enter the file name: ").strip('"\'')
df = pd.read_csv(file)
numericals=[]
others=[]
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        numericals.append(col)
    else:
        others.append(col)
fun(df,numericals,others)


