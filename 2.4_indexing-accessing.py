
# Label-Based Indexing with .loc
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
print("Original DataFrame:\n", df)
#select all rows for a specific column
print('\nResult:\n',df.loc[:,'A'])

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
# Select all rows for multiple columns, say list[]
print(df.loc[:,['A','C']])

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'],['A','C']])

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
# Select range of rows for all columns
print(df.loc['c':'e'])

# Integer Position-Based Indexing with .iloc

# Indexing with Brackets []
