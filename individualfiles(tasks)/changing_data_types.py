# changing datatypes to another data type if the data type is wrong in the data set:
import pandas as pd
import numpy as np

def fun(df,num,ot):
    print(df.head())
    print("numerical columns are")
    for i in range(len(num)):
        print("the column name is ",num[i],"contains null values :")
        print(df[num[i]].isna().sum())
        print("\n")
    print("other columns(object)")
    for i in range(len(ot)):
        print("the column name is ",num[i],"contains null values :")
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


data=df
def datatypescheck(data):
    i=0
    for col in data:
        print("index is ",i,"Data Type of column", col, "is", data[col].dtype)
        i=i+1
    print("\n")
    print("if any data type is not correct then enter the index and its type to change ")
    index=int(input("enter the index"))

    if index>i:
        print("your choice is out of bounds / please re enter your choice ")
        op=int(input("enter here:"))
        index=op

    print("enter the data type you that is correct for the column")
    dty=input("enter here :")

datatypescheck(data)

