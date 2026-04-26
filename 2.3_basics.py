import pandas as pd
import numpy as np

# Create a Series with random numbers
s = pd.Series(np.random.randn(4))

# Exploring attributes
print("Data type of Series:", s.dtype)
print("Index of Series:", s.index)
print("Values of Series:", s.values)
print("Shape of Series:", s.shape)
print("Number of dimensions of Series:", s.ndim)
print("Size of Series:", s.size)
print("Is Series empty?:", s.empty)

import pandas as pd
import numpy as np

# Create a DataFrame with random numbers
df = pd.DataFrame(np.random.randn(3, 4), columns=list('ABCD'))
print("DataFrame:")
print(df)

print("Results:")
print("Data types:", df.dtypes)
print("Index:", df.index)
print("Columns:", df.columns)
print("Values:")
print(df.values)
print("Shape:", df.shape)
print("Number of dimensions:", df.ndim)
print("Size:", df.size)
print("Is empty:", df.empty)

import pandas as pd
import numpy as np
# Create a Series with random numbers
s = pd.Series(np.random.randn(10))
print("Series:")
print(s)
# Using basic methods
print("First 5 elements of the Series:\n", s.head())
print("\nLast 3 elements of the Series:\n", s.tail(3))
print("\nDescriptive statistics of the Series:\n", s.describe())

import pandas as pd
import numpy as np
# Create a Dictionary of series
data = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
        'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
        'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# Create a DataFrame
df = pd.DataFrame(data)
print("Our data frame is:\n")
print(df)
# Using basic methods
print("\nFirst 5 rows of the DataFrame:\n", df.head())
print("\nLast 3 rows of the DataFrame:\n", df.tail(3))
print("\nInfo of the DataFrame:")
df.info()
print("\nDescriptive statistics of the DataFrame:\n", df.describe())