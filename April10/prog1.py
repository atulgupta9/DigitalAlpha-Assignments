"""
1. Given sales dataset and perform the following operations on it,
a. print the name of columns
b. print 10 rows and 10 columns in the data set
c. plot any graph to represent the total profit.
d. print the item_type with total cost grater than 1000000
"""
import pandas as pd

df = pd.read_csv(r"C:\\Users\\user\\Python Programs\\April10\\100 Sales Records.csv")

print("Columns are:-")
for column in df.columns:
    print(column,end=",")

print("\n\nPrinting 10 rows and 10 columns from the data set")
print(df.iloc[0:10,0:10])


df[["Total Profit"]].plot()




itemList = df[["Item Type","Total Cost"]]
itemList.columns = ["Item Type","TotalCost"]
dfNew= itemList.query("TotalCost>1000000")

print("\n\nPrinting the item_type with total cost greater than 1000000")
for val in dfNew["Item Type"].values:
    print(val,end=",")