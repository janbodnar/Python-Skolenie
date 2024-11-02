# Pandas 


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
