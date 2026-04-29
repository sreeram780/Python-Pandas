# Series[start:stop:step]: It selects elements from start to end with specified step value.
# Series[start:stop]: It selects items from start to stop with step 1.
# Series[start:]: It selects items from start to the rest of the object with step 1.
# Series[:stop]: It selects the items from the beginning to stop with step 1.
# Series[:]: It selects all elements from the series object.

# Slicing a Series by Position
# Example: Slicing range of values from a Series
import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
# Display the Original series
print('Original Series:',s, sep='\n')
# Slice the range of values
result = s[1:3]
# Display the output
print('Values after slicing the Series:', result, sep='\n')

# Example: Slicing the First Three Elements from a Series
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the first three element
print(s[:3])