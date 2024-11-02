# Pandas 

## Simple

```python
import pandas as pd

data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)
```

## Series 

A `Series` is a one-dimensional array-like object in the Pandas library, capable of holding any  
data type (e.g., integers, strings, floating-point numbers, etc.). It is essentially a labeled array,  
where each element in the array is associated with an index label.

```python
import pandas as pd

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
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
