# Priklady


## Read XML

Using xml module.  

```python
import xml.etree.ElementTree as ET
import requests
import io

url = 'https://webcode.me/users.xml'

resp = requests.get(url)
content = resp.content.decode('utf8')

data = io.StringIO(content)

tree = ET.parse(data)
root = tree.getroot()

# Define the namespace
namespace = {'ns': 'zetcode.com'}

# print(root)

for user in root.findall("ns:user", namespace):
    # print(user)
    first_name = user.find("ns:firstname", namespace).text
    last_name = user.find("ns:lastname", namespace).text
    occupation = user.find("ns:occupation", namespace).text
    print(first_name, last_name, occupation)
```


## Read CSV data

```python
import csv

file_name = 'numbers.csv'

values = []

with open(file_name, 'r') as f:

    reader = csv.reader(f)

    for row in reader:
        for e in row:
            values.append(int(e))
        # row2 = [int(e) for e in row]
        # values.append(row2)

print(values)            
print(len(values))
print(sum(values))
```

## Find user by id in CSV file

```python
import csv

# Read the CSV data into a list
data = []
with open('users.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        data.append(row)

# Function to find a row by id
def find_row_by_id(data, id):
    for row in data:
        if row[0] == id:  # Assuming the id is in the first column
            return row
    return None

# Get user input for the id
user_id = input("Enter the id: ")

# Find the row
result = find_row_by_id(data, user_id)

# Print the result
if result:
    print("Row found:", result)
else:
    print("No row found with id:", user_id)
```



## GTP4All

```python
import requests

# Define the API endpoint
url = "http://localhost:4891/v1/chat/completions"

# Define the payload (data to be sent in the POST request)
payload = {
    "model": "llama 3 8B Instruct",
    "messages": [{"role": "user", "content": "What is Python language?"}],
    "max_tokens": 55,
    "temperature": 0.28
}

# Define the headers (if needed)
headers = {
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Print the response (JSON format)
print(response.json())
```







## Docker 

```
We've detected that you have an incompatible version of Windows.
Docker Desktop requires Windows 10 Pro/Enterprise/Home version 19044 or above.
```

## Datclass vs classic class

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:

    name: str
    age: int

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # def getAge(self):
    #     return self.age

    # def setAge(self, age):
    #     self.age = age

    # def getName(self):
    #     return self.name

    # def setName(self, name):
    #     self.name = name

    # def __eq__(self, other): 
    #     if isinstance(other, Person): 
    #         return self.name == other.name and self.age == other.age 
    #     return False

    # def __str__(self):
    #     return f'{self.name} {self.age}'

p = Person('John Doe', 34)

print(p)
print(p.age)
print(p.name)
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
