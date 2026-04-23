# class pandas.Index(data=None, dtype=None, copy=False, name=None, tupleize_cols=True)
# data: The data for the index, which can be an array-like structure (like a list or numpy array) or another index object.
# dtype: It specifies the data type for the index values, If not provided, Pandas will decide the data type based on the index values.
# copy: It is a boolean parameter (True or False), which, specifies to create a copy of the input data.
# name: This parameter gives a label to the index.
# data: It is also a boolean parameter (True or False), When True, it tries to create MultiIndex if possible.

# NumericIndex
import pandas as pd
# Generate some data for DataFrame
data = {
   'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
   'Age': [32, 28, 45, 38],
   'Gender': ['Male', 'Female', 'Male', 'Female'],
   'Rating': [3.45, 4.6, 3.9, 2.78]
}
# Creating the DataFrame
df = pd.DataFrame(data)
# Display the DataFrame
print(df)
print("\nDataFrame Index Object Type:",df.index.dtype)
print()
# CategoricalIndex
# Creating a CategoricalIndex
categories = pd.CategoricalIndex(['a','b', 'a', 'c'])
df = pd.DataFrame({'Col1': [50, 70, 90, 60], 'Col2':[1, 3, 5, 8]}, index=categories)
print("Input DataFrame:\n",df)
print("\nDataFrame Index Object Type:",df.index.dtype)
print()

# MultiIndex
# IntervalIndex
import pandas as pd
# Creating a IntervalIndex
interval_idx = pd.interval_range(start=0, end=4)
# Creating a DataFrame with IntervalIndex
df = pd.DataFrame({'Col1': [1, 2, 3, 4], 'Col2':[1, 3, 5, 8]}, index=interval_idx)
print("Input DataFrame:\n",df)
print("\nDataFrame Index Object Type:",df.index.dtype)
print()
# DatetimeIndex
# TimedeltaIndex
# PeriodIndex