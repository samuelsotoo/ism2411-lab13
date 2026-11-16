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