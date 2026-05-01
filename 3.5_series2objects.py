# Method	Description
# to_list()	Converts the Series into a Python list.
# to_numpy()	Converts the Series into a NumPy array.
# to_dict()	Converts the Series into a dictionary.
# to_frame()	Converts the Series into a DataFrame.
# to_string()	Converts the Series into a string representation for display.

import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3])
# Convert Series to a Python list
result = s.to_list()
print("Output:",result)
print("Output Type:", type(result))