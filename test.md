# Priklady 13.11.24

## Select users

```python
import sqlite3
from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    city: str
    salary: int

users = []

con = sqlite3.connect('test.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM users ORDER BY salary DESC LIMIT 30")

    rows = cur.fetchall()

    for row in rows:
        user = User(row[0], row[1], row[2], row[3], row[4])
        users.append(user)


print(len(users))

for user in users:
    print(user)
```



## Generate test users

```sql
CREATE TABLE users (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, city TEXT, salary INT);
```

```python
from faker import Faker

file_name = 'users.csv'
faker = Faker()

with open(file_name, 'w') as f:

    for idx in range(1, 10_000):
        first_name = faker.first_name()
        last_name = faker.last_name()
        city = faker.city()
        salary = faker.random_int(850, 5000)

        line = f'{idx},{first_name},{last_name},{city},{salary}\n'
        f.write(line)
```



## Show database row

Take id from script argument.  

```python
import sqlite3
import sys

argv = sys.argv
uid = int(argv[1])

con = sqlite3.connect('test.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT name, population FROM cities WHERE id=:id", {"id": uid})

    row = cur.fetchone()
    print(row[0], row[1])
```


## Filtering data

```python
import sqlite3
from dataclasses import dataclass

@dataclass
class City:
    id: int
    name: str
    population: int

cities = []

con = sqlite3.connect('test.db')

with con:    
    
    cur = con.cursor()    
    # cur.execute("SELECT * FROM cities WHERE population < 500000")
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        # city = City(row[0], row[1], row[2])
        city = City(*row)
        cities.append(city)


small_cities = [city for city in cities if city.population < 500_000]

for small_city in small_cities:
    print(small_city)
```



## Fetch one row

```python
import sqlite3

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT * FROM cities WHERE id = 3')
    
    res = cur.fetchone()
    
    print(res)
    print(f'{res[0]} {res[1]} {res[2]}')
```


## Read JSON data from file

```python
from dataclasses import dataclass
import json

@dataclass
class Product:
    id: int
    name: str
    price: int
    quantity: int


products = []

fname = "products.json"
with open(fname) as f:

    data = json.load(f)
    # print(data)

    for e in data["products"]:
        product = Product(int(e['id']), e['name'], float(e['price']), int(e['quantity']))
        products.append(product)

        # print(e)


# print(products)
for product in products:
    print(product)
```


## Opakovanie

```python

# calculate sum
vals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

mysum = 0

for nested in vals:
    mysum += sum(nested)

print(mysum)


# generate a list of 100 random numbers and calculate its sum

import random

random_vals = []

for _ in range(100):
    r = random.randint(0, 100)
    random_vals.append(r)

print(len(random_vals))
print(sum(random_vals))



# generate list of words starting with c or w
data = """
sky
down
cup
blue
python
dark
war
water
roam
club
"""

fields = data.splitlines()[1:]
# fields.pop(0)

words_w_c = [field for field in fields if field.startswith(('w', 'c'))]
print(words_w_c)
```
