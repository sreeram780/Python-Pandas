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