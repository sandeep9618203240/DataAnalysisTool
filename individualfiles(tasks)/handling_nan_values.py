import pandas as pd
import numpy as np
 
file = input("Enter the file name: ").strip('"\'')
df = pd.read_csv(file)

def handlingmissingvalues(data,colname,method):
    if method=="drop":
        data=data[colname].dropna()
    elif method=="mean":
        data=data[colname].fillna(data[colname].mean())
    elif method=="median":
        data=data[colname].fillna(data[colname].median())
    elif method=="mode":
        data=data[colname].fillna(data[colname].mode())
    elif method=="ffill":
        data=data[colname].fillna(method="ffill")
    return data

colname=input("please enter the valid column name")
method=input("please enter the method to handle missing values")
print(handlingmissingvalues(df,colname,method))