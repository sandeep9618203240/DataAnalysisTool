import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = input("Enter the file name: ").strip('"\'')
df = pd.read_csv(file)


numericals=[]
others=[]
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        numericals.append(col)
    else:
        others.append(col)


def univariate_analysis(data,column,type):
    numericals=[]
    others=[]
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            numericals.append(col)
        else:
            others.append(col)
    if column in numericals:
        if type=='hist':
            plt.hist(data[column])
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title('Histogram of '+column)
            plt.show()
        elif type=='box':
            sns.boxplot(data[column])
            plt.title('Boxplot of '+column)
            plt.show()
        elif type=='kde':
            sns.kdeplot(data[column],shade=True)
            plt.title('KDE plot of '+column)
            plt.show()
        elif type=='line':
            plt.plot(data[column])
            plt.title('Line plot of '+column)
            plt.show()
    else:
        if type=='count':
            sns.countplot(data[column])
            plt.title('Count plot of '+column)
            plt.show()
        elif type=='pie':
            data[column].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title('Pie chart of '+column)
            plt.show()
        elif type=='bar':
            data[column].value_counts().plot.bar()
            plt.title('Bar chart of '+column)
            plt.show()
        elif type=='violin':
            sns.violinplot(data[column])


column = input("Enter the column name: ").strip('"\'')
type = input("Enter the type of plot: ").strip('"\'')
univariate_analysis(df,column,type)
        
def bivariate_analysis(df,colulmn1,column2,type):
    if type=='scatter':
        plt.scatter(df[colulmn1],df[column2])
        plt.xlabel(colulmn1)
        plt.ylabel(column2)
        plt.title('Scatter plot between '+colulmn1+' and '+column2)
        plt.show()
    elif type=='line':
        plt.plot(df[colulmn1],df[column2])
        plt.xlabel(colulmn1)
        plt.ylabel(column2)
        plt.title('Line plot between '+colulmn1+' and '+column2)
        plt.show()
    elif type=='box':
        sns.boxplot(df[colulmn1],df[column2])
        plt.title('Box plot between '+colulmn1+' and '+column2)
        plt.show()
    elif type=='bar':
        df.groupby(colulmn1)[column2].mean().plot.bar()
        plt.title('Bar plot between '+colulmn1+' and '+column2)
        plt.show()
    elif type=='violin':
        sns.violinplot(df[colulmn1],df[column2])
        plt.title('Violin plot between '+colulmn1+' and '+column2)
        plt.show()


colulmn1 = input("Enter the first column name: ").strip('"\'')
column2 = input("Enter the second column name: ").strip('"\'')
type = input("Enter the type of plot: ").strip('"\'')
bivariate_analysis(df,colulmn1,column2,type)

