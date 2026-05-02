#import the pandas library and aliasing as pd
import pandas as pd
df = pd.DataFrame()
print(df)

# Create a DataFrame from Lists
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

# Create a DataFrame from Dict of ndarrays / Lists
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)

# indexed DataFrame using arrays
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

# Create a DataFrame from List of Dicts
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)