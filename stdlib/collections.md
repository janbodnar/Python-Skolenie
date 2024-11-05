# Collections



| Module       | Description                                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------------------|
| deque        | A sequence-like collection that supports efficient addition and removal of items from either end of the sequence. |
| defaultdict  | A dictionary subclass for constructing default values for missing keys and automatically adding them to the dictionary. |
| namedtuple   | A factory function for creating subclasses of tuple that provides named fields, allowing access by name or index. |
| OrderedDict  | A dictionary subclass that maintains key-value pairs in the order they were inserted. |
| Counter      | A dictionary subclass for counting unique items in a sequence or iterable. |
| ChainMap     | A dictionary-like class that combines multiple mappings into a single object. |
| UserDict     | A wrapper class around a dictionary object that facilitates subclassing dict. |
| UserList     | A wrapper class around a list object that facilitates subclassing list. |
| UserString   | A wrapper class around a string object that facilitates subclassing string. |


## sum vals of keys

```python
animals1 = {'cats': 4, 'dogs': 8, 'horses': 12, 'donkeys': 2}
animals2 = {'cats': 1, 'dogs': 2, 'horses': 2}
summed_dict = {key: sum([animals1.get(key, 0), animals2.get(key, 0)])
               for key in {*animals1, *animals2}}

print(summed_dict)

animals3 = animals1.copy()

for k, v in animals2.items():

    if animals3.get(k, 0):
        animals3[k] += v

print(animals3)
```

## Counter

```python
from collections import Counter

vals = [1, 1, 1, 1, 2, 3, 3, 4, 3, 3, 4]

c = Counter(vals)
print(c)

words = ['sky', 'word', 'sky', 'sky', 'war', 'war', 'atom']
c = Counter(words)
print(c)
```

---

```python
from collections import Counter

animals1 = {'cats': 4, 'dogs': 8, 'horses': 12, 'donkeys': 2}
animals2 = {'cats': 1, 'dogs': 2, 'horses': 2}

c1 = Counter(animals1)
c2 = Counter(animals2)

c = c1 + c2
print(c)
print(dict(c))
```


## namedtuple

Python namedtuple is an immutable container type, whose values can be accessed with  
indexes and named attributes. It has functionality like tuples with additional features.  
A named tuple is created with the `collections.namedtuple` factory function.  

Named tuples are essentially easy-to-create, immutable, lightweight object types. Named tuples  
can be used to make the code more clean and Pythonic. They are similar to records in other  
languages (C#, Java).

### Basic example

The following is a simple example with a namedtuple.

```python
#!/usr/bin/python

from collections import namedtuple


City = namedtuple('City' , 'name population')

c1 = City('Bratislava', 432000)
c2 = City('Budapest', 1759000)

print(c1)
print(c2)
```

The example create city namedtuples.

```python
from collections import namedtuple
```

First, we import the namedtuple type from the collections module.

```python
City = namedtuple('City' , 'name population')
```

We define the namedtuple. The first argument is the name for the namedtuple. The second argument  
are the field names. These can be specified in a string `'name population'` or in a list  
`['name', 'population']`.

```python
c1 = City('Bratislava', 432000)
c2 = City('Budapest', 1759000)
```

Here we create two namedtuple objects.

```
$ ./basic.py 
City(name='Bratislava', population=432000)
City(name='Budapest', population=1759000)
```


### Accessing attributes 

The namedtuples can be accessed using indexing and their named attributes.  

```python
#!/usr/bin/python

from collections import namedtuple


City = namedtuple('City' , 'name population')

c1 = City('Bratislava', 432000)
c2 = City('Budapest', 1759000)

print(c1[0])
print(c1[1])

print(c2.name)
print(c2.population)
```

In the example, we demonstrate both ways.

```
$ ./accessing.py 
Bratislava
432000
Budapest
1759000
```

### Unpacking

The unpacking is storing iterable elements into variables or function arguments.

```python
#!/usr/bin/python

from collections import namedtuple


City = namedtuple('City' , 'name population')

c1 = City('Bratislava', 432000)
c2 = City('Budapest', 1759000)

name, population = c1
print(f'{name}: {population}')

print('----------------------')

print(c2)
print(*c2, sep=': ')
```

In the example, we unpack our namedtuples.

```python
name, population = c1
```

Here we unpack the `c1` namedtuple into two variables.

```python
print(*c2, sep=': ')
```

Here we unpack the `c2` namedtuple with the `*` operator into print function arguments, which   
are joined with the given separator into the final output.

```
$ ./unpacking.py 
Bratislava: 432000
----------------------
City(name='Budapest', population=1759000)
Budapest: 1759000
```

```python
#!/usr/bin/python

from collections import namedtuple


City = namedtuple('City' , 'name population')

d = { 'name': 'Bratislava', 'population': 432000}

c = City(**d)
print(c)
```

With the `**` operator, we can unpack a dictionary into arguments of a namedtuple.  


### Sorting

In the following example, we sort a list of namedtuples.

```python
#!/usr/bin/python

from typing import NamedTuple


class City(NamedTuple):
    id: int
    name: str
    population: int


c1 = City(1, 'Bratislava', 432000)
c2 = City(2, 'Budapest', 1759000)
c3 = City(3, 'Prague', 1280000)
c4 = City(4, 'Warsaw', 1748000)
c5 = City(5, 'Los Angeles', 3971000)
c6 = City(6, 'Edinburgh', 464000)
c7 = City(7, 'Berlin', 3671000)

cities = [c1, c2, c3, c4, c5, c6, c7]

cities.sort(key=lambda e: e.name)

for city in cities:
    print(city)
```

With the help of the sort method and the lambda function, we sort cities by their name.

```
$ ./sorting.py 
City(id=7, name='Berlin', population=3671000)
City(id=1, name='Bratislava', population=432000)
City(id=2, name='Budapest', population=1759000)
City(id=6, name='Edinburgh', population=464000)
City(id=5, name='Los Angeles', population=3971000)
City(id=3, name='Prague', population=1280000)
City(id=4, name='Warsaw', population=1748000)
```

The cities are sorted by their names in ascending order.

### The _make helper

The `_make` is method that makes a new instance of a namedtuple from  
an existing sequence or iterable.

```python
#!/usr/bin/python

from collections import namedtuple


City = namedtuple('City' , 'name population')

c1 = City._make(('Bratislava', 432000))
c2 = City._make(('Budapest', 1759000))

print(c1)
print(c2)
```

The example creates `City` namedtuples from tuples with the help of the `_make` method.


### Read CSV data

Python namedtuples are helpful when we read CSV data.

```csv
Bratislava, 432000
Budapest, 1759000
Prague, 1280000
Warsaw, 1748000
Los Angeles, 3971000
New York, 8550000
Edinburgh, 464000
Berlin, 3671000
```

We have the `cities.csv` file.

```python
#!/usr/bin/python

from collections import namedtuple
import csv


City = namedtuple('City' , 'name population')

f = open('cities.csv', 'r')

with f:

    reader = csv.reader(f)
    
    for city in map(City._make, reader):
        print(city)
```

We use the `map` and the `_make` functions to create clean code.


```
$ ./read_csv.py 
City(name='Bratislava', population=' 432000')
City(name='Budapest', population=' 1759000')
City(name='Prague', population=' 1280000')
City(name='Warsaw', population=' 1748000')
City(name='Los Angeles', population=' 3971000')
City(name='New York', population=' 8550000')
City(name='Edinburgh', population=' 464000')
City(name='Berlin', population=' 3671000')
```

### Read SQLite database

In the following example, we use a namedtuple to read data from SQLite database.

```sql
--cities.sql

DROP TABLE IF EXISTS cities;
CREATE TABLE cities(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, 
  population INTEGER);

INSERT INTO cities(name, population) VALUES('Bratislava', 432000);
INSERT INTO cities(name, population) VALUES('Budapest', 1759000);
INSERT INTO cities(name, population) VALUES('Prague', 1280000);
INSERT INTO cities(name, population) VALUES('Warsaw', 1748000);
INSERT INTO cities(name, population) VALUES('Los Angeles', 3971000);
INSERT INTO cities(name, population) VALUES('New York', 8550000);
INSERT INTO cities(name, population) VALUES('Edinburgh', 464000);
INSERT INTO cities(name, population) VALUES('Berlin', 3671000);
```

These are SQL statements to create the cities table.

```
$ sqlite3 ydb.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .read cities.sql
```

With the sqlite3 command line tool, we generate the SQLite database and the cities table.

```python
#!/usr/bin/python

# read_sql.py

from typing import NamedTuple
import sqlite3 as sqlite


class City(NamedTuple):
    
    id: int
    name: str
    population: int


con = sqlite.connect('ydb.db')

with con:

    cur = con.cursor()

    cur.execute('SELECT * FROM cities')
    
    for city in map(City._make, cur.fetchall()):
        print(city)
```

We read all data from the `cities` table and transform each table row into a `City` namedtuple.

## OrderedDict

`OrderedDict` is a subclass of the dictionary that preserves the order of item insertion.  
When we iterate over an OrderedDict, the items are returned in the same order they were  
added. In contrast, a regular dictionary does not guarantee any specific order during iteration,  
resulting in arbitrary item retrieval.
