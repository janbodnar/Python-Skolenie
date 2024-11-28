# Priklady

https://api.api-ninjas.com/v1/quotes?category=happiness

## Docker 

```
We've detected that you have an incompatible version of Windows.
Docker Desktop requires Windows 10 Pro/Enterprise/Home version 19044 or above.
```

## Select random user from CSV file

```python
import csv
import random
from dataclasses import dataclass

@dataclass
class Person:
    id: int
    first_name: str
    last_name: str
    address: str

def read_csv(file_path: str):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [Person(int(row[0]), row[1], row[2], row[3]) for row in reader]

# Read the CSV file and create a list of Person objects
people = read_csv('users.csv')

# Print the list of Person objects
# for person in people:
#     print(person)

print(random.choice(people))
```



## Fetch users as JSON

```python
import requests
from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str

def fetch_users(url: str):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    
    users = [User(**user_data) for user_data in data['users']]
    return users

# URL to fetch data from
url = 'https://webcode.me/users.json'

# Fetch and print users
users = fetch_users(url)
for user in users:
    print(user)
```

## Total sales

```python
import json
from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: Decimal
    quantity: int

products = []

fname = 'products.json'
with open(fname) as f:
    data = json.load(f)
    rows = data['products']

    for product in rows:
        p = Product(
            int(product['id']),
            product['name'],
            Decimal(product['price']),
            int(product['quantity'])
        )
        products.append(p)

total_sales = sum(p.price * p.quantity for p in products)
print(f"Total sales: {total_sales}")
```


## Decimal

```python
import json
from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: Decimal
    quantity: int

products = []

fname = 'products.json'
with open(fname) as f:
    data = json.load(f)
    rows = data['products']

    for product in rows:
        p = Product(
            int(product['id']),
            product['name'],
            Decimal(product['price']),
            int(product['quantity'])
        )
        products.append(p)

print(products)
```



## Dataclass

```python
import json
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    quantity: int


products = []


fname = 'products.json'
with open(fname) as f:

    data = json.load(f)
    rows = data['products']

    for product in rows:
        # print(product)
        p = Product(int(product['id']), product['name'], float(product['price']), int(product['quantity']))
        # p = Product(**product)
        products.append(p)

    
print(products)
```


## requests kniznica

```python
import requests

url = 'https://webcode.me'

# resp = requests.get(url)

# content = resp.content.decode('utf8')
# print(content)

resp = requests.head(url)

headers = resp.headers
print(type(headers))
print(headers)

print(headers['Server'])
print(headers['Last-Modified'])
print(headers['Date'])
```


## Faker kniznica

```python

from faker import Faker

faker = Faker()

file_name = 'users.csv'

with open(file_name, 'w') as f:

    for i in range(1, 501):

        idx = i
        first_name = faker.first_name()
        last_name = faker.last_name()
        city = faker.city()
        
        row = f'{idx},{first_name},{last_name},{city}\n'

        f.write(row)


print('file created OK')
```




## Opakovanie

```python

# calculate sum
vals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

mysum = 0

# for val in vals:
#     mysum += sum(val)

for nested in vals:
    for val in nested:
        mysum += val

print(mysum)


# generate a list of 100 random numbers 0-100 and calculate its sum
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

lines = data.splitlines()[1:]

words_c_w = [line for line in lines if line.startswith('w') or line.startswith('c')]
print(words_c_w)


# words_c_w = []
# for line in lines:
#     if line.startswith('w') or line.startswith('c'):
#         words_c_w.append(line)

# print(words_c_w)
```
