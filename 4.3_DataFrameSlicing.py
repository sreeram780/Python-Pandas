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