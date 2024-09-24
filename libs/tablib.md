# tablib

The tablib library is designed to make working with tabular data (like CSV,  
XLSX, JSON, and more) more efficient and flexible. It provides a consistent  
interface for handling these different data formats.  

It allowing use to easily:

- Create and manipulate tabular data: Define and modify data structures using  
  Python lists or dictionaries.
- Convert between formats: Seamlessly transform data between CSV, XLSX, JSON,  
  and other supported formats.
- Export and import data: Save data to files or load data from existing files.  
- Customize output: Control the appearance of exported data, such as column  
  headers, formatting, and more.

A tablib *Dataset* is a Python object that represents a collection of tabular  
data. It provides a structured way to store and manipulate data in a consistent  
format.

```python
import tablib

ds = tablib.Dataset()

ds.headers = ['first_name', 'last_name', 'occupation']
ds.append(['John', 'Doe', 'gardener'])
ds.append(['Adam', 'Brown', 'programmer'])
ds.append(['Tom', 'Holland', 'teacher'])
ds.append(['Ken', 'Roberts', 'driver'])

print(ds)
ds.wipe()
print(ds)
```

The example creates a simple dataset.

```python
ds = tablib.Dataset()
```

We create an empty dataset.

```python
ds.headers = ['first_name', 'last_name', 'occupation']
```

We create four headers for the dataset.

```python
ds.append(['John', 'Doe', 'gardener'])
ds.append(['Adam', 'Brown', 'programmer'])
ds.append(['Tom', 'Holland', 'teacher'])
ds.append(['Ken', 'Roberts', 'driver'])
```

Using `append` method, we add four rows to the dataset.

```python
print(ds)
```

We print the contents of the dataset.

```python
ds.wipe()
```

The `wipe` method removes the data from the dataset.


## Getting rows

We can retrieve rows via indexing operation or the `get` method.

```python
import tablib

ds = tablib.Dataset()

ds.headers = ['first_name', 'last_name', 'occupation']
ds.append(['John', 'Doe', 'gardener'])
ds.append(['Adam', 'Brown', 'programmer'])
ds.append(['Tom', 'Holland', 'teacher'])
ds.append(['Ken', 'Roberts', 'driver'])

print(ds[0])
print(ds[-1])

print(ds.get(1))
print(ds.get(-2))
```

The example builds a dataset and retrieves four rows.


## Getting columns

The `get_col` method returns the column from the Dataset at the given index.

```python
import tablib

ds = tablib.Dataset()

ds.headers = ['first_name', 'last_name', 'occupation']
ds.append(['John', 'Doe', 'gardener'])
ds.append(['Adam', 'Brown', 'programmer'])
ds.append(['Tom', 'Holland', 'teacher'])
ds.append(['Ken', 'Roberts', 'driver'])

print(ds.get_col(0))
print(ds.get_col(2))
```

In the example, we print the first and the last columns.

## Adding a new column

The `append_col` adds a column to the dataset.

```python
import tablib

ds = tablib.Dataset()

ds.headers = ['first_name', 'last_name', 'occupation']
ds.append(['John', 'Doe', 'gardener'])
ds.append(['Adam', 'Brown', 'programmer'])
ds.append(['Tom', 'Holland', 'teacher'])
ds.append(['Ken', 'Roberts', 'driver'])

ds.append_col([980, 1230, 2310, 1100], header='salary')

print(ds)
```

In the example, we add a new column salary to the dataset.

## Sorting data

The `sort` function is used to sort the data in the dataset. The function  
returns a new sorted dataset; the original dataset is not modified.  

```python
import tablib

ds = tablib.Dataset()

ds.headers = ['first_name', 'last_name', 'occupation']
ds.append(['John', 'Doe', 'gardener'])
ds.append(['Adam', 'Brown', 'programmer'])
ds.append(['Tom', 'Holland', 'teacher'])
ds.append(['Ken', 'Roberts', 'driver'])

ds.append_col([980, 1230, 2310, 1100], header='salary')

sorted_ds = ds.sort('last_name')
print(sorted_ds)

print()

sorted_ds = ds.sort(3, reverse=True)
print(sorted_ds)
```

The example sorts the data by last name and salary.

```python
sorted_ds = ds.sort('last_name')
print(sorted_ds)
```

We sort the data by the last_name column. The function returns a new sorted  
dataset.

```python
sorted_ds = ds.sort(3, reverse=True)
print(sorted_ds)
```

We sort the data by salary in descending order. This time we provide the column  
index.


## Formatting columns

With `add_formatter`, we can format a column.

```python
import tablib
import datetime

ds = tablib.Dataset()
ds.headers = ['Name', 'Age', 'Height', 'Birthdate']

ds.append(['John Doe', 34, 174.5, datetime.date(1990, 1, 1)])
ds.append(['Roger Roe', 25, 182.7, datetime.date(1995, 5, 15)])

ds.add_formatter('Height', lambda v: f'${v:.2f}')
ds.add_formatter('Birthdate', lambda v: v.strftime('%Y-%m-%d'))
print(ds)
```

The example formats the Height and Birthdate columns.

## Exporting dataset

The export method exports the dataset into the specified format. The supported  
formats include CSV, YAML, XLSX, JSON, and Pandas dataframe.  

```python
import tablib

ds = tablib.Dataset()

ds.headers = ['first_name', 'last_name', 'occupation']
ds.append(['John', 'Doe', 'gardener'])
ds.append(['Adam', 'Brown', 'programmer'])
ds.append(['Tom', 'Holland', 'teacher'])
ds.append(['Ken', 'Roberts', 'driver'])

ds.append_col([980, 1230, 2310, 1100], header='salary')

fname = 'users.csv'

with open(fname, 'w', newline='') as f:
    f.write(ds.export('csv'))

fname = 'users.xlsx'

with open(fname, 'wb') as f:
    f.write(ds.export('xlsx'))
```
We export the dataset into CSV and XLSX formats.

```python
with open(fname, 'w', newline='') as f:
    f.write(ds.export('csv'))
```

In order not to have additional empty lines, we set the newline option for the  
CSV format to empty character.  

```python
with open(fname, 'wb') as f:
    f.write(ds.export('xlsx'))
```

For the XLSX format, we open a file in the 'wb' mode.

## The load function

The `load` function loads the data into the dataset.

```python
import tablib

ds = tablib.Dataset()

fname = 'users.csv'
with open(fname, 'r') as f:

    ds.load(f)

print(ds)
```

We load the rows fromt he `users.csv` file into the dataset.
