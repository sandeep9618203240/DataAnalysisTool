import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter the file name: ").strip('"\'')
df = pd.read_csv(file)

numericals=[]
others=[]   
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        numericals.append(col)
    else:
        others.append(col)


def centratendencies(data,nums,cats):
    print("central tendencies")
    print("enter the column name to get the central tendencies")
    colname = input("")
    if colname in nums:
        print("mean: ",data[colname].mean())
        print("median: ",data[colname].median())
        print("mode: ",data[colname].mode())
    else:
        print("mode: ",data[colname].mode())
        print("count: ",data[colname].count())
        print("unique: ",data[colname].unique())
        print("top: ",data[colname].top())
        print("freq: ",data[colname].freq())
    print("\n")
    return


centratendencies(df,numericals,others)
# def measureofdispersion(data,nums,cats):
