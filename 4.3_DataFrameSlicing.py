# Slicing DataFrame Rows by Position
import pandas as pd
# Create a Pandas DataFrame
df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']], columns=['col1', 'col2'])
# Display the DataFrame
print("Input DataFrame:")
print(df)
# Slice rows based on position
result = df.iloc[1:3, :]
print("Output:")
print(result)

# Create a DataFrame with labeled indices
df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']], columns=['col1', 'col2'], index=['r1', 'r2', 'r3', 'r4'])
# Display the DataFrame
print("Original DataFrame:")
print(df)
# Slice rows and columns by label
result = df.loc['r1':'r3', 'col1']
print("Output:")
print(result)

# Column Slicing using iloc[]
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
# Slice a single column
col_A = df.iloc[:, 0]
print("Slicing a single column A using iloc[]:")
print(col_A)
# Slice multiple columns
cols_AB = df.iloc[:, 0:2]
print("Slicing multiple columns A and B using iloc[]:")
print(cols_AB)

# Column Slicing Using loc[]
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
# Slice a single column by label
col_A = df.loc[:, 'A']
print("Slicing a single column A using loc[]:")
print(col_A)
# Slice multiple columns by label
cols_AB = df.loc[:, 'A':'B']
print("Slicing Multiple columns A and B using loc[]:")
print(cols_AB)

# Modifying Values After Slicing
# Create a DataFrame
df = pd.DataFrame([['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']],
                  columns=['col1', 'col2'])
# Display the Original DataFrame
print("Original DataFrame:", df, sep='\n')
# Modify a subset of the DataFrame using iloc
df.iloc[1:3, 0] = ['x', 'y']
# Display the modified DataFrame
print('Modified DataFrame:',df, sep='\n')

# modified DataFrame
import pandas as pd
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})
# Display original DataFrame
print("Original DataFrame:")
print(df)
# Rename column 'A' to 'aa'
df = df.rename(columns={'A': 'aa'})
# Display modified DataFrame
print("Modified DataFrame:")
print(df)

# Renaming Row Labels in a DataFrame
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]}, index=['x', 'y', 'z'])
# Display original DataFrame
print("Original DataFrame:")
print(df)
# Rename the multiple row labels
df = df.rename(index={'x': 'r1', 'y':'r2', 'z':'r3'})
# Display modified DataFrame
print("Modified DataFrame:")
print(df)