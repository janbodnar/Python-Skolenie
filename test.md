# Priklady 13.11.24

## The split function

```python
from funcy import split

values = [1, 2, 3, -4, 5, -6, 7, 8, 9, -10]

negs, pos = split(lambda e: e < 0, values)

print(list(negs))
print(list(pos))
```


## Today in Hebrew

```python
from hdate import HDate
from datetime import datetime

# Get today's date in Gregorian calendar
today_gregorian = datetime.today().date()

# Convert the current date to Hebrew calendar
today_hebrew = HDate(today_gregorian)

print(today_hebrew.hebrew_date)
```


## Year in days

```python
from datetime import date, datetime

# Define the initial date
d0 = date(1978, 11, 18)

# Get the current date
td = datetime.today().date()  # Convert datetime to date
print(td)

# Calculate the difference
delta = td - d0
print(delta.days)
```


## Yougest, oldest 

```python
#!/usr/bin/python

from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    email: str
    dob: datetime


users = (
    User('John Doe', 'john.doe@example.com', datetime(1985, 8, 21)),
    User('Roger Roe', 'roger.roe@example.com', datetime(1998, 2, 11)),
    User('Paul Anka', 'paul.anka@example.com', datetime(1977, 9, 5)),
    User('Lucia Smith', 'lucia.smith@example.com', datetime(2001, 2, 2)),
    User('Jane Miller', 'jane.miller@example.com', datetime(1967, 5, 15)),
)

oldest = users[0]

for user in users:
    if user.dob < oldest.dob:
        oldest = user

print('The oldest user:', oldest)


yougest = users[0]

for user in users:
    if user.dob > yougest.dob:
        yougest = user

print('The youngest user:', yougest)
```



## Clean data

```python
import re

# Sample data
data = """
    John Doe, 123-456-7890
    Jane Smith, 987.654.3210
    Alice   Johnson, (555)555-5555
"""

# List of words with white spaces
words_with_spaces = ["   hello  ", "  world ", "   foo   ", "   bar"]

# Clean data: remove extra white spaces and unify phone number formats
def clean_data(data):
    # Remove extra white spaces
    data = re.sub(r'\s+', ' ', data)
    # Unify phone number formats to xxx-xxx-xxxx
    data = re.sub(r'\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})', r'\1-\2-\3', data)
    return data

# Clean words list: strip leading and trailing white spaces
clean_words = [word.strip() for word in words_with_spaces]

# Cleaned data
cleaned_data = clean_data(data)

# Print results
print("Cleaned Data:")
print(cleaned_data)
print("\nCleaned Words List:")
print(clean_words)
```


## List Python files in current directory

```python
import os 

files = os.listdir('.')
# print(files)

python_files = [file for file in files if file.endswith('py')]
print(python_files)

for file in files:

    if file.endswith('py'):
        print(file)
```




## Recap

1. Calculate total sales

```python
{
    "products": [
        {
            "id": 1,
            "name": "Laptop",
            "price": 999.99,
            "quantity": 10,
            "category": "Electronics"
        },
        {
            "id": 2,
            "name": "Smartphone",
            "price": 499.99,
            "quantity": 25,
            "category": "Electronics"
        },
        {
            "id": 3,
            "name": "Coffee Maker",
            "price": 79.99,
            "quantity": 5,
            "category": "Home Appliances"
        },
        {
            "id": 4,
            "name": "Headphones",
            "price": 199.99,
            "quantity": 15,
            "category": "Electronics"
        },
        {
            "id": 5,
            "name": "Blender",
            "price": 49.99,
            "quantity": 20,
            "category": "Home Appliances"
        },
        {
            "id": 6,
            "name": "Electric Kettle",
            "price": 29.99,
            "quantity": 30,
            "category": "Home Appliances"
        },
        {
            "id": 7,
            "name": "Tablet",
            "price": 299.99,
            "quantity": 8,
            "category": "Electronics"
        },
        {
            "id": 8,
            "name": "Smartwatch",
            "price": 199.99,
            "quantity": 12,
            "category": "Electronics"
        },
        {
            "id": 9,
            "name": "Camera",
            "price": 599.99,
            "quantity": 7,
            "category": "Electronics"
        },
        {
            "id": 10,
            "name": "Microwave Oven",
            "price": 89.99,
            "quantity": 10,
            "category": "Home Appliances"
        }
    ]
}
```

Solution:

```python
import json
from decimal import Decimal 


file_name = 'products.json'

with open(file_name, 'r') as f:
    data = json.load(f)

    products = data['products']


total_sales = sum(Decimal(product['price']) * Decimal(product['quantity']) for product in products)
print(f"The total potential sales value is: ${total_sales:.2f}")

total_sales_float = 0.0

# Use a for loop to calculate the sum of all potential sales
for product in products:
    total_sales_float += product['price'] * product['quantity']

print(f"The total potential sales value (float) is: ${total_sales_float:.2f}")
```



2. 
How much is 100 Eur in US dollars and CZ. 

`https://nbs.sk/export/sk/exchange-rate/2024-11-13/csv`

```python
import requests
import csv
import io
from decimal import Decimal

url = 'https://nbs.sk/export/sk/exchange-rate/2024-11-13/csv'

resp = requests.get(url)
content = resp.content.decode('utf8')

csv_file = io.StringIO(content) # Create a CSV reader object 
reader = csv.DictReader(csv_file, delimiter=';')

amount_eur = 100

for row in reader:
    usd = Decimal(row['USD'].replace(",", "."))
    czk = Decimal(row['CZK'].replace(",", "."))

    print(f'{amount_eur} eur is {usd * amount_eur} dollars')
    print(f'{amount_eur} eur is {czk * amount_eur} czech crowns')
```

```python
import csv
from decimal import Decimal

with open('exchange-rate.csv', 'r') as f:

    reader = csv.DictReader(f, delimiter=';')

    amount_eur = 100

    for row in reader:
        usd = Decimal(row['USD'].replace(",", "."))
        czk = Decimal(row['CZK'].replace(",", "."))

        print(f'{amount_eur} eur is {usd * amount_eur} dollars')
        print(f'{amount_eur} eur is {czk * amount_eur} czech crowns')
```


3. 
Transform top 20 earning users from database into JSON otput.


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
