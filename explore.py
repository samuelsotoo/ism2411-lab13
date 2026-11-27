# Self-Assessment Questions:
# Question 1 - boolean filter checks each row against a condition and keeps only the rows where it's True. In Exercise 2, df['region'] == 'South' kept just the South rows, and the 50 NaN rows got left out.
# Question 2 - df["revenue"] gives a Series (one column). df[["revenue"]] gives a DataFrame (a table with one column). It matters when I need a DataFrame, like for .shape or selecting multiple columns in Exercise 7.
# Question 3 - Because I can write the steps once as code and rerun them on any data, and it handles big data (like our 5,000 rows) fast without clicking around. Plus the code shows exactly what I did, so someone else can check it or repeat it, which you can't really do with Excel clicks.




"--- Exercise 1 ---"

import pandas as pd; 
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

"--- Exercise 2 ---"

south = df[df['region'] == 'South']
print(len(south))
print(south.head())

"--- Exercise 3 ---"

df.sort_values('revenue', ascending=False).head(5)
print(df.sort_values('revenue', ascending=False).head(5))

"--- Exercise 4 ---"

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())

"--- Exercise 5 ---"

df['per_unit'] = df['revenue'] / df['quantity']
print(df[['per_unit']].head())
print(df['per_unit'].mean())

"--- Exercise 6 ---"

print(df['region'].unique()) 
print(df['region'].value_counts())

"--- Exercise 7 ---"

df_small = df[['region', 'product', 'revenue']]
print(df_small.shape) 

"--- Exercise 8 ---"

import os

df.to_csv('data/explored.csv', index=False)

print(os.path.exists('data/explored.csv'))
print(os.path.getsize('data/explored.csv'))

with open('data/explored.csv') as f:
    print(f.readline())