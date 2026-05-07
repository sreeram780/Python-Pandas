
# Dropping DataFrame Rows by Index Values

import pandas as pd
# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8]})
# Display original DataFrame
print("Original DataFrame:")
print(df)
# Drop the row with index 3
result = df.drop(3)
# Display the result
print("\nAfter dropping the row at index 3:")
print(result)