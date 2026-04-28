# class pandas.Series(data, index, dtype, name, copy)
# Create an Empty Series
#import the pandas library and aliasing as pd
import pandas as pd
s = pd.Series()

# Display the result
print('Resultant Empty Series:\n',s)

# Create a Series from ndarray
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print("Output:\n",s)

# Create a Series from Python Dictionary
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','x','a'])
print(s)

# Create a Series from Scalar
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)