"""
5. Consider the following sales data,
	Account number	Name	Sku	Category	Quantity	Unit price	Ext price
0	852659	Carroll PLC	QC-82856	Belt	13	44.48	578.24
1	654987	Heidenreich-Bosco	MJ-58694	Shoes	19	53.62	1018.78
2	258369	Kerluke	AS-58546	Shirt	12	24.16	289.92
3	741852	Waters-Walker	AS-46987	Shirt	5	82.68	413.40
4	693471	Waelchi-Fahey	AS-36987	Shirt	18	99.64	1793.52

a.	Summarise  the sales table for quick analysis.
b.	Print summary statistics for unit price 
c.	Print the data type used for each fields
d.	Create and print a data frame called customers, which only contains the name and ext price		
"""
import pandas as pd
df = pd.read_excel(r"C:\\Users\\user\\Python Programs\\April10\\prog5.xlsx")
print("Summary statistics:-\n")
print(df.describe())
print("\nSummary statistics for unit price\n")
print(df["Unit price"].describe())
print("\nData type for each field")
print(df.dtypes)
customers = df[["Name","Ext price"]]
print(customers)