## The csv module 

## CSV 

CSV (Comma Separated Values) is a very popular import and export data format  
used in spreadsheets and databases. Each line in a CSV file is a data record.  
Each record consists of one or more fields, separated by commas. While CSV is a  
very simple data format, there can be many differences, such as different  
delimiters, new lines, or quoting characters.  


## Python csv module

The `csv` module implements classes to read and write tabular data in CSV  
format. The `csv` module's reader and writer objects read and write sequences.
Programmers can also read and write data in dictionary form using the  
`DictReader` and `DictWriter` classes.  

## CSV methods

The following table shows basic csv methods:

| Method | Description |
|---|---|
| csv.reader | Returns a reader object which iterates over lines of a CSV file |
| csv.writer | Returns a writer object which writes data into CSV file |
| csv.register_dialect | Registers a CSV dialect |
| csv.unregister_dialect | Unregisters a CSV dialect |
| csv.get_dialect | Returns a dialect with the given name |
| csv.list_dialects | Returns all registered dialects |
| csv.field_size_limit | Returns the current maximum field size allowed by the parser |



## Using csv module

```python
import csv
```

To use Python CSV module, we import csv.

## Python CSV reader

The `csv.reader` method returns a reader object which iterates over lines in the  
given CSV file.  

```
$ cat numbers.csv
16,6,4,12,81,6,71,6
```

The `numbers.csv` file contains numbers.

```python
import csv

with open('numbers.csv', 'r') as f:

    reader = csv.reader(f)

    for row in reader:

        for e in row:
            print(e)
```

In the code example, we open the `numbers.csv` for reading and read its contents.  

```python
reader = csv.reader(f)
```

We get the reader object.

```python
for row in reader:
   
    for e in row:
        print(e)
```

With two for loops, we iterate over the data.


## Using different delimiter

The csv.reader method allows to use a different delimiter with its delimiter attribute.

```
$ cat items.csv
pen|cup|bottle
chair|book|tablet
```

The `items.csv` contains values separated with `|` character.

```python
#!/usr/bin/python

import csv

with open('items.csv', 'r') as f:

    reader = csv.reader(f, delimiter="|")

    for row in reader:

        for e in row:
            print(e)
```

The code example reads and displays data from a CSV file that uses a `|`  
delimiter.  


## The DictReader

The `csv.DictReader` class operates like a regular reader but maps the  
information read into a dictionary. The keys for the dictionary can be passed in  
with the fieldnames parameter or inferred from the first row of the CSV file.  

```
$ cat values.csv
min,avg,max
1, 5.5, 10
2, 3.5, 5
```

The first line of the file consists of dictionary keys.

```python
import csv

with open('values.csv', 'r') as f:

    reader = csv.DictReader(f)

    for row in reader:
        print(row['min'], row['avg'], row['max'])
```

The example reads the values from the `values.csv` file using the  
`csv.DictReader`.

```python
for row in reader:
    print(row['min'], row['avg'], row['max'] )
```

The row is a Python dictionary and we reference the data with the keys.  

## Python CSV writer

The `csv.writer` method returns a writer object which converts the user's data  
into delimited strings on the given file-like object.  

```python
import csv

nms = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

with open('numbers2.csv', 'w') as f:

    writer = csv.writer(f)

    for row in nms:
        writer.writerow(row)
```

The script writes numbers into the `numbers2.csv` file. The `writerow` method  
writer a row of data into the specified file.  

```
$ cat numbers2.csv
1,2,3,4,5,6
7,8,9,10,11,12
```

It is possible to write all data in one shot. The `writerows` method writes all  
given rows to the CSV file.  

```python
import csv

nms = [[1, 2, 3], [7, 8, 9], [10, 11, 12]]

with open('numbers3.csv', 'w') as f:

    writer = csv.writer(f)
    writer.writerows(nms)
```

The code example writes three rows of numbers into the file using the  
`writerows` method.  

## CSV DictWriter

The `csv.DictWriter` class operates like a regular writer but maps Python  
dictionaries into CSV rows. The fieldnames parameter is a sequence of keys that  
identify the order in which values in the dictionary passed to the `writerow`  
method are written to the CSV file.  

```python
#!/usr/bin/python

import csv

with open('names.csv', 'w') as f:

    fnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fnames)

    writer.writeheader()
    writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name' : 'Robert', 'last_name': 'Brown'})
    writer.writerow({'first_name' : 'Julia', 'last_name': 'Griffin'})
```

The example writes the values from Python dictionaries into the CSV file using
the `csv.DictWriter`.  

```python
writer = csv.DictWriter(f, fieldnames=fnames)
```

New `csv.DictWriter` is created. The header names are passed to the fieldnames  
parameter.  

```
writer.writeheader()
```

The `writeheader` method writes the headers to the CSV file.

```python
writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})
```

The Python dictionary is written to a row in a CSV file.

```
$ cat names.csv
first_name,last_name
John,Smith
Robert,Brown
Julia,Griffin
```

## Custom CSV dialect

A custom dialect is created with the `csv.register_dialect` method.

```python
import csv

csv.register_dialect("hashes", delimiter="#")

with open('items3.csv', 'w') as f:

    writer = csv.writer(f, dialect="hashes")
    writer.writerow(("pens", 4))
    writer.writerow(("plates", 2))
    writer.writerow(("bottles", 4))
    writer.writerow(("cups", 1))
```

The program uses a (#) character as a delimiter. The dialect is specified with 
 the dialect option in the `csv.writer` method.

```python
$ cat items3.csv
pens#4
plates#2
bottles#4
cups#1
```

## Generate fake CSV data

In the next example, we create a new CSV file which is filled with fake data.  
Fake data is useful for testing.  

We use the `faker` module to generate fake data.  

```python
from faker import Faker
import csv

faker = Faker()

with open('users.csv', 'w', newline='') as f:

    fieldnames = ['id', 'first_name', 'last_name', 'occupation']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(1, 101, 1):
        
        _id = i
        fname = faker.first_name()
        lname = faker.last_name()
        occupation = faker.job()

        writer.writerow({'id': _id, 'first_name': fname, 
            'last_name': lname, 'occupation': occupation})
```

The example creates 100 users. The users are written to the `users.csv` file in  
CSV format.  

