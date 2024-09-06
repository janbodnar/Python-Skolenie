# Priklady


## Download PDF file 

```python
import requests

url = 'https://static.realpython.com/python-basics-sample-chapters.pdf'

resp = requests.get(url)
content = resp.content

file_name = 'python-basics.pdf'

with open(file_name, 'wb') as f:
    f.write(content)
```


## ZIP Python files

```python
import os 
import zipfile

files = os.listdir('.')
files_to_zip = list(filter(lambda file: file.endswith('py') , files))

with zipfile.ZipFile('myarchive.zip', 'w') as zip:

    for file in files_to_zip:
        zip.write(file)
```



## JSON

using urllib3  

```python
#!/usr/bin/python

import json
import urllib3

http = urllib3.PoolManager()

url = 'https://webcode.me/users.json'

resp = http.request('GET', url)
text = resp.data.decode("utf-8")

data = json.loads(text)
print(type(data))

for user in data['users']:
    print(user)
```

using requests 

```python
import json
import requests

url = 'https://webcode.me/users.json'

resp = requests.get(url)
text = resp.content.decode("utf-8")

data = json.loads(text)

for user in data['users']:
    print(user)
```



## list directory

```python
import os 

# content = os.listdir('.')
content = os.listdir(r'C:\Users\bodnar\Documents\pyprogs')
# print(content)

for file in content:
    if file.endswith('py'):
        print(file)

py_files = list(filter(lambda file: file.endswith('py'), content))
print(py_files)
```


## filter words

```python
def has_3_letters(word):

    return len(word) == 3


words = ['sky', 'letter', 'pet', 'cup', 'morning']

# words_3 = list(filter(has_3_letters, words)) 
words_3 = list(filter(lambda word: len(word) == 3, words)) 
print(words_3)

# words_3 = []

# for word in words:
#     if len(word) == 3:
#         words_3.append(word)

# print(words_3)
```


## lambda & median

```python
#!/usr/bin/python

import math, statistics

# salaries = [980, 890, 1000, 1050, 7000, 9000]
# print(sorted(salaries))

# print(statistics.mean(salaries))
# print(statistics.median(salaries))

import statistics

from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    name: str
    price: int

cars = [
    Car("Audi", 52642), Car("Mercedes", 57127), Car("Skoda", 9000),
    Car("Volvo", 29000), Car("Bentley", 350000), Car("Citroen", 21000),
    Car("Hummer", 41400), Car("Volkswagen", 21601)
]

prices = []

for car in cars:

    prices.append(car.price)

print(prices)
print(statistics.median(prices))


def get_min_price(car):

    return car.price

# n = min(cars, key=lambda c: c.price)
n = min(cars, key=get_min_price)
print(n)

n = max(cars, key=lambda c: c.price)
print(n)
```



## map function

```python
#!/usr/bin/python

def upper_word(word):
    return word.upper()


words = ['sky', 'tool', 'pen']


# words_upper = list(map(upper_word, words))
words_upper = list(map(lambda e: e.upper(), words))

print(words_upper)
```


## sort by age

```python
import csv
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta

User = namedtuple('User', 'first_name last_name country date_of_birth job')

users = []
file_name = 'users.csv'

def calculate_age(dob_str):
    # dob = datetime.strptime(dob_str, "%Y-%m-%d")
    dob = datetime.fromisoformat(dob_str)
    today = datetime.today()
  
    age = relativedelta(today, dob)
    
    return age.years


def by_age(u):

    age = calculate_age(u.date_of_birth)
    return age <= 30


with open(file_name, 'r') as f:

    reader = csv.reader(f)
    next(reader) # skips header

    for row in reader:
        users.append(User(*row))
 

users_20_24 = list(filter(by_age, users))

print(users_20_24)
```
