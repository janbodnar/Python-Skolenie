# Pandas 

## Simple

```python
import pandas as pd

data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)
```

## No index

Sometimes, displaying index is not necessary. 

```python
import pandas as pd

df = pd.read_csv("military_spending.csv")
print(df.to_string(index=False))
```

No header and no index:

```python
import pandas as pd 
  
df = pd.read_csv("military_spending.csv") 

print(df.head(4).to_string(header=False, index=False))
```

## The index, values & column properties

- *index*: Provides access to the row labels of the DataFrame.
- *values*: Returns a NumPy array representation of the DataFrame's values.
- *columns*: Returns the column labels of the DataFrame.


```python
import pandas as pd

data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

print(f'Index: {df.index}')
print(f'Columns: {df.columns}')
print(f'Values: {df.values}')
```

## Change index

```python
import pandas as pd

data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df.index = df.index + 1

print(df)
```

## Custom index

```python
import pandas as pd

data = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

frame = pd.DataFrame(data)
print(frame)

print('------------------------------')

frame.index = ["BR", "RU", "IN", "CH", "SA"]
print(frame)
```

## The write_csv function

The `to_csv` function in pandas is used to export a `DataFrame` or `Series` to a  
CSV (Comma-Separated Values) file. This function allows you to specify various  
parameters to control the output format and the details of how the data is  
written to the file.


```python
import pandas as pd 

data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

df.to_csv("users.csv", index=False) 
```


## Counting

```python
import pandas as pd

file_name = 'military_spending.csv'
df = pd.read_csv(file_name)

print(df.count())
print(f'Number of columns: {len(df.columns)}')
print(df.shape)
```

Rows: 

```python
import pandas as pd

file_name = 'employees.csv'
df = pd.read_csv(file_name)

print(df.shape[0])
print(len(df))
print(df.count().max())
```


## Series 

A `Series` is a one-dimensional array-like object in the Pandas library, capable  
of holding any data type (e.g., integers, strings, floating-point numbers,  
etc.). It is essentially a labeled array, where each element in the array is  
associated with an index label.


```python
import pandas as pd

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
```

From dictionary:

```python
import pandas as pd

data = {'coins' : 22, 'pens' : 3, 'books' : 28}
s = pd.Series(data)

print(s)
```


Using numpy array.

```python
import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)

print(s)
```

Retrieving data:

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

print(s.iloc[0])
print('-----------------------')

print(s[1:4])
print('-----------------------')

print(s[['a','c','d']])
```

## Random sample

```python
import pandas as pd

df = pd.read_csv("military_spending.csv")

print(df.sample(3))
```

## The describe function

The `describe` function in pandas is a convenient method used to generate  
summary statistics of a DataFrame or Series. It provides a quick overview of the  
central tendency, dispersion, and shape of the dataset's distribution, including  
statistics like count, mean, standard deviation, minimum, quartiles, and  
maximum.  

```python
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
s2 = pd.Series([12, 23, 31, 14, 11, 61, 17, 18])

data = {'Vals 1': s1, 'Vals 2': s2}
df = pd.DataFrame(data)

print(df.describe())
```

```python
import pandas as pd

# Sample DataFrame with categorical data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salaries': [900, 1200, 980, 2300, 1230],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Gender': ['F', 'M', 'M', 'M', 'F']
}
df = pd.DataFrame(data)

# Get summary statistics for categorical data
# O stands of object data types
categorical_summary = df.describe(include=['O'])
print(categorical_summary)
```

## Sum & max 

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0, 1200, 2), columns=['A'])
print(df)
# df.index = df.index + 1

print(sum(df['A']))
print(max(df['A']))
```

## Head & tail

```python
import pandas as pd 
  
df = pd.read_csv("military_spending.csv") 

print(df.head(4))

print('*******************************************')

print(df.tail(4))
```

## The iloc function

The `iloc` function in pandas is used for integer-location based indexing and  
selection. It allows you to select and manipulate rows and columns in a  
`DataFrame` using their integer positions.  

```python
import pandas as pd

file_name = 'employees.csv'
df = pd.read_csv(file_name)

# integer-location based indexing for selection by position.
# Multiple row and column selections using iloc and DataFrame


print(df.iloc[1]) # select second row

print(df.iloc[0:6])  # first six rows of dataframe
print('--------------------------------------')

print(df.iloc[:, 0:2])  # first two columns of data frame with all rows
print('--------------------------------------')

# 1st, 4th, 7th, 25th row + 1st 6th 8th column
print(df.iloc[[0, 3, 6, 24], [0, 5, 7]])
print('--------------------------------------')

# first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).
print(df.iloc[:5, 5:8])
print('--------------------------------------')
```


## The loc function

The `loc` function in pandas is used for label-based indexing and selection. It    
allows you to select and manipulate rows and columns in a `DataFrame` using  
their labels. This makes it very flexible for selecting data based on row and  
column names rather than their integer positions.  

```python
#!/usr/bin/python

import pandas as pd

data = {'Items': ['coins', 'pens', 'books'], 'Quantity': [22, 28, 3]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])

print(df.loc['A'])
print('-------------------------------')
print(df.loc[['A', 'B'], ['Items']])
```

```python
import pandas as pd

data = {'Items': ['coins', 'pens', 'books'], 'Quantity': [22, 28, 3]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df.loc[[True, False, True], ['Items', 'Quantity']])
```

```python
import pandas as pd

file_name = 'employees.csv'
df = pd.read_csv(file_name)

data = df.loc[(df['Salary'] > 10000) & (df['Salary'] < 50000)]
print(data.iloc[:, [0, 1, 4, 5, 7]].head())
```



## Read CSV string

```python
import pandas
from io import StringIO

data = '''
1,2,3,4,5
6,7,8,9,10
'''

mysum = 0

csv_file = StringIO(data)

df = pandas.read_csv(csv_file, header=None)
print(df.head())
print(df.values.sum())
print((df > 1).values.all())
```

## The to_dict function

The `to_dict` function in pandas is used to convert a `DataFrame` or `Series`  
into a dictionary. This function allows you to transform your data into various  
dictionary formats, depending on your needs.  

The `orient` parameter specifies the format of the resulting dictionary. For
`DataFrame`, the options include:

- *dict*: Default. Each column becomes a key, with the column values as the  
  corresponding dictionary values.
- *list*: Each column becomes a key, with the column values stored as lists.
- *series*: Each column becomes a key, with the column values stored as Series.
- *split*: Returns a dictionary with three keys: 'index', 'columns', and 'data'.
- *records*: Each row becomes a dictionary, and the list of these dictionaries  
  is returned.
- *index*: Each row becomes a dictionary, with row indexes as keys.

```python
import pandas as pd 

data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

print('list')
print(df.to_dict(orient='list'))

print('************************************')

print('series')
print(df.to_dict(orient='series'))

print('************************************')

print('dict')
print(df.to_dict(orient='dict'))

print('************************************')

print('split')
print(df.to_dict(orient='split'))

print('************************************')

print('records')
print(df.to_dict(orient='records'))

print('************************************')

print('index')
print(df.to_dict(orient='index'))
```


## Sorting 

The `sort_values` function in pandas is used to sort a `DataFrame` or `Series`  
by the values of one or more columns. It allows you to specify the sorting order  
(ascending or descending) and various other parameters to customize the sorting  
behavior.  

```python
import pandas as pd

s1 = pd.Series([2, 1, 4, 5, 3, 8, 7, 6])
s2 = pd.Series([12, 23, 31, 14, 11, 61, 17, 18])

data = {'Col 1': s1, 'Col 2': s2}
df = pd.DataFrame(data)

print(df.sort_values('Col 1', ascending=True))
print('------------------------------------')
print('Sorted')

print(df.sort_values('Col 2', ascending=False))
```

Renaming the sorted column:  

```python
import pandas as pd

file_name = 'military_spending.csv'
df = pd.read_csv(file_name)
df.rename(columns={' Amount (Bn. $)': 'Amount_Bn_$'}, inplace=True)
          
sorted_df = df.sort_values('Amount_Bn_$', ascending=False)
print(sorted_df)
```

Sorting by column index:

```python
import pandas as pd

file_name = 'military_spending.csv'
df = pd.read_csv(file_name)
          
sorted_df = df.sort_values(by=df.columns[2], ascending=False)
print(sorted_df)
```


## Sorting by multiple fields

```python
import pandas as pd

s1 = pd.Series([1, 2, 1, 2, 2, 1, 2, 2])
s2 = pd.Series(['A', 'A', 'B', 'A', 'C', 'C', 'C', 'B'])

data = {'Col 1': s1, 'Col 2': s2}
df = pd.DataFrame(data)

print(df.sort_values(['Col 1', 'Col 2'], ascending=[True, False]))
```

## Index

In pandas, an `Index` is an immutable array that holds the labels for a `Series`  
or `DataFrame`. It is a core part of pandas' data structures and is used for  
aligning data, selecting data, and performing various data manipulation tasks.  
The index can be thought of as the "address" of each data point in the pandas  
object.  

```python
import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Viewing the index
print("Original Index:", df.index)

# Setting a column as the index
df = df.set_index('A')
print("\nDataFrame with 'A' as index:\n", df)

# Resetting the index
df = df.reset_index()
print("\nDataFrame with reset index:\n", df)

# Renaming the index
df.index = ['a', 'b', 'c']
print("\nDataFrame with renamed index:\n", df)
df = df.rename(index={'a': 'x', 'b': 'y', 'c': 'z'})
print("\nDataFrame with renamed index labels:\n", df)

# Sorting by index
df = df.sort_index()
print("\nDataFrame sorted by index:\n", df)

# Selecting data by index
selected_data = df.loc['x']
print("\nSelected data for index 'x':\n", selected_data)
```