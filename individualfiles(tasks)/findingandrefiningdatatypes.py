import pandas as pd
import numpy as np
 
file = input("Enter the file name: ").strip('"\'')
df = pd.read_csv(file)


data=df
def datatypescheck(data):
    i=0
    for col in data:
        print("index is ",i,"Data Type of column", col, "is", data[col].dtype)
        i=i+1
    print("\n")
    print("if any data type is not correct then enter the index and its type to change ")
    index=int(input("enter the index"))
    # if index>i:
    #     print("your choice is out of bounds / please re enter your choice ")
    #     op=int(input("enter here:"))
    #     index=op
    print("enter the data type you that is correct for the column")
    dty=input("enter here :")
    change_type(dty,index,data)
    
    # if index

def check_index(index,data):
    if index>len(data.columns):
        print("your choice is out of bounds / please re enter your choice ")
        op=int(input("enter here:"))
        index=op
        if index<=len(data.columns):
            return index
        else:
            check_index(index,data)
    return index

def change_type(dt,index,data):
    ind=check_index(index,data)
    cname=data.columns[ind]
    # if dt in ["int","str", "bool","float","datetime","object"] :
    #     if dt=="int":
    #         data[cname]=data[cname].astype(dt)
    if dt in ["int", "str", "bool", "float", "datetime", "object"]:
        if dt == "datetime":
            data[cname] = pd.to_datetime(data[cname])  # Convert to datetime
        else:
            data[cname] = data[cname].astype(dt)  # Convert to specified type
    else:
        raise ValueError("❌ Invalid data type")
    print(data.dtypes)
   


datatypescheck(data)




