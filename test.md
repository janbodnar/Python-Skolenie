# Priklady

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
