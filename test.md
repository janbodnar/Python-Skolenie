# Samples

## Read CSV from internet resource

```python

import requests
import csv
from io import StringIO
from dataclasses import dataclass


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str


url = 'https://webcode.me/users.csv'
resp = requests.get(url)

content = resp.content.decode('utf8')
f = StringIO(content)

users = []

for user in csv.DictReader(f):

    u = User(**user)
    users.append(u)
    # print(user)

# for u in users:
#     print(u)

names_w_a = [u for u in users if u.last_name.startswith('W') or u.last_name.startswith('A')]

print(len(names_w_a))

for user in names_w_a:
    print(user)
```




## Calculate age

```python
import csv
from dataclasses import dataclass
from datetime import date
from dateutil.relativedelta import relativedelta

@dataclass
class User:
    name: str
    occupation: str
    dob: str

def get_age(val: str):
    born = date.fromisoformat(val.strip())
    today = date.today()
    age = relativedelta(today, born)
    return age.years


users = []

fname = 'users.csv'
with open(fname) as f:

    reader = csv.reader(f)

    for row in reader:
        if row:
            u = User(*row)
            users.append(u)

print(users)

for u in users:

    print(f'{u.name} is {u.occupation}, age: {get_age(u.dob)}')
```



## Filter users

```python
import csv
from dataclasses import dataclass
import argparse


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str

ws = []


parser = argparse.ArgumentParser()
parser.add_argument('-fn', type=str, required=True, help="provide first name of user")
parser.add_argument('-ln', type=str, required=True, help="provide last name of user")

args = parser.parse_args()

first_name = args.fn
last_name = args.ln

with open('users.csv') as f:

    # reader = csv.reader(f)
    reader = csv.DictReader(f)

    for row in reader:
        if row['first_name'] == first_name and row['last_name'] == last_name:

            # u = User(row['id'], row['first_name'], row['last_name'], row['occupation'])
            u = User(**row)

            ws.append(u)

print(ws)
print(len(ws))
```




```python
import csv
from dataclasses import dataclass
import argparse


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str

ws = []


parser = argparse.ArgumentParser()
parser.add_argument('-fn', type=str, required=True, help="provide first name of user")
parser.add_argument('-ln', type=str, required=True, help="provide last name of user")

args = parser.parse_args()

first_name = args.fn
last_name = args.ln

with open('users.csv') as f:

    reader = csv.reader(f)

    for row in reader:
        if row[1] == first_name and row[2] == last_name:

            # u = User(row[0], row[1], row[2], row[3])
            u = User(*row)

            ws.append(u)

print(ws)
print(len(ws))
```


## Read first 100 lines of CSV data

```python
from dataclasses import dataclass

@dataclass
class Person:
    id: int
    first_name: str
    last_name: str
    occupation: str

fname = 'users.csv'

users = []

i = 0
with open(fname) as f:

    reader = csv.DictReader(f)

    for row in reader:
        user = Person(row['id'], row['first_name'], row['last_name'], row['occupation'])
        users.append(user)
        i += 1

        if i >= 101:
            break


print(len(users))

for user in users:
    print(user)
```



## Read data from CSV file

Data in `data.csv`

```
1, 2, 3, 4, 5
6, 7, 8, 9, 10
```


```python
import csv

fname = 'data.csv'
values = []

with open(fname) as f:

    reader = csv.reader(f)

    for row in reader:
        values.extend(row)

print(values)

data = [int(e) for e in values]
print(data)

print(sum(data))
print(max(data))
print(min(data))
print(len(data))
```


## Split string

```python
data = '1,2,3,4,5,6,7,8,9,10'

# split/int/sum

parts = data.split(',')
print(parts)

vals = [int(e) for e in parts]
print(vals)
print(sum(vals))

print(sum([int(e) for e in data.split(',')]))
```



```python
words = ['war', 'water', 'cup', 'atom', 'cloud', 'sky']

words_w_c = [word for word in words if word.startswith('w') or word.startswith('c')]
print(words_w_c)
```


```python
a = [9, 2, 18, 14, 22, 11, 7, 19, 23]

b1 = [e for e in a if e > 10 if e < 20]
b2 = [e for e in a if e > 10 and e < 20]
b3 = [e for e in a if 10 < e < 20]

print(b1, b2, b3)
```




```python
a = [-4, 2, 0, -1, 12, -3]

b = [e for e in a if e > 0]
print(b)

vals = [1, 2, 3, 4, 5, 6, 7]

evens = [e for e in vals if e % 2 == 0]
print(evens)

odds = [e for e in vals if e % 2 == 1]
print(odds)


words = ['sky', 'cup', 'war', 'twin', 'forest']

words_3 = [word for word in words if len(word) == 3]
print(words_3)
```


```python
#!/usr/bin/python

class User:

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setOccupation(self, occupation):
        self.occupation = occupation

    def getOccupation(self):
        return self.occupation

data = [
    ['John Doe', 'gardener'],
    ['Roger Roe', 'driver'],
    ['Lucia Smith', 'teacher']
]


for e in data:
    user = User(e[0], e[1])
    print(user.getName(), user.getOccupation())
```














```python
words = ['sky', 'word', 'cup', 'letter', 'water']
vals = [1, 2, 3, 4, 5]
# for loop, len, fstring

def startw(e:str):
    return e.startswith('w')

def times5(e):
    return e * 5

for word in words:
    print(f'{word} has {len(word)} ascii characters')

# filter slov na w
# map -> prenasob 5

filtered = list(filter(startw, words))
print(filtered)

multiplied = list(map(times5, vals))
print(multiplied)
```










## Frequency

```
The Battle of Thermopylae was fought between an alliance of Greek city-states,
led by King Leonidas of Sparta, and the Persian Empire of Xerxes I over the
course of three days, during the second Persian invasion of Greece.
```


```python
filename = 'termopyly.txt'

with open(filename) as f:
    content = f.read()

freq = {}
for c in content:
    freq[c] = freq.get(c, 0) + 1

print(freq)

for k, v in freq.items():
    print(f'{k} is there {v} times')
```

---

```python
freq = {}

filename = 'termopyly.txt'
with open(filename) as f:

    content = f.read()

    for c in content:

        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1


print(freq)

for k, v in freq.items():
    print(f'{k} is there {v} times')
```

## Read CSV data

```
1,2,3,4,5,6,7,8,9,10
11,12,13,14,15,16,17
18,19,20,21,22,23,24
```

```python
import csv

values = []

with open('vals.csv') as f:
    reader = csv.reader(f)

    for row in reader:
        values.extend(row)

        # print(row)
        # lines.extend(row)
        # for e in row:
        #     lines.append(e)

    print(sum(map(lambda e: int(e), values)))
```

## map fun

```python
def twice(e: int):
    return e * 2

def cube(e: int):
    # return e * e * e
    # return e ** 3
    return pow(e, 3)

vals = [-2, 0, 3, 2, 6, -9, 11, -7, -5]

# doubled = list(map(twice, vals))
# print(doubled)
#
# cubed = list(map(cube, vals))
# print(cubed)

doubled = list(map(lambda e: e * 2, vals))
print(doubled)

cubed = list(map(lambda e: e ** 3, vals))
print(cubed)
```



```python
words = ['sky', 'war', 'water', 'cup', 'ocean', 'owl']

data = list(filter(lambda e: e.startswith('w'), words))
print(data)

data = list(filter(lambda e: e.startswith('w') or e.startswith('o'), words))
print(data)

data = list(filter(lambda e: len(e) == 3, words))
print(data)
```



```python
def starts_w(e):
    return e.startswith('w')

def starts_w_o(e):
    return e.startswith('w') or e.startswith('o')

words = ['sky', 'war', 'water', 'cup', 'ocean', 'owl']

data = list(filter(starts_w, words))
print(data)

data = list(filter(starts_w_o, words))
print(data)
```


```python
vals = (1, 2, 3, 7, 8, 11, 12, -6, -21, 22)
evens = []
odds = []

for val in vals:
    if val % 2 == 0:
        evens.append(val)
        
print(evens)

for val in vals:
    if val % 2 == 1:
        odds.append(val)

print(odds)
```



```python
nums = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

for i in nums:
    for e in i:
        for f in e:
            print(f)
```



```python
data = '1-2-3-4-5-6-7-8-9-10'
mysum = 0

substrings = data.split('-')
print(substrings)

for val in substrings:
    mysum += int(val)

print(mysum)
```


```python
words = ['sky', 'cup', 'blue', 'bottom', 'war', 'atom', 'water', 'car']
words_w = []
words_w_c = []

for word in words:
    if word.startswith('w'):
        words_w.append(word)

print(words_w)


for word in words:
    if word.startswith('w') or word.startswith('c'):
        words_w_c.append(word)

print(words_w_c)
```


```python

words = ['sky', 'blue', 'bottom', 'war', 'atom', 'water', 'car']

for word in words:
    print(word)

for word in words:
    print(word, end=' ')

print()

for word in words:
    print(word.capitalize(), end=' ')
```


```python
age_s = input('Enter your age: ')
age = int(age_s)

if age < 18:
    print('minor')
# elif age >= 18 and age < 70:
elif 18 <= age < 70:
    print('adult')
else:
    print('senior')
```


```python
vals = [1, 2, -3, -4, 0, 2, 1, 9, 11, -22]

maximum = max(vals)
minimum = min(vals)
n = len(vals)
mysum = sum(vals)

print(f'maximum is {maximum}')
print(f'minimum is {minimum}')
print(f'length is {n}')
print(f'the sum is {mysum}')
```

```python
words = ['sky', 'top', 'warm', 'clear', 'war', 'by', 'net', 'falcon', 'cup']
words_w = []

for word in words:
    if word.startswith('w') or word.startswith('c'):
        words_w.append(word)

print(words)
print(words_w)
```

```python
words = ['sky', 'top', 'warm', 'clear', 'war', 'by', 'net', 'falcon']
words_w = []

for word in words:
    if word.startswith('w'):
        words_w.append(word)

print(words)
print(words_w)
```

```python
words = ['sky', 'top', 'clear', 'by', 'net', 'falcon']
words_3 = []

for word in words:
    if len(word) == 3:
        words_3.append(word)

print(words)
print(words_3)
```


```python
mix = (1, 2, 3, (1, 2, 3, (1, 2, 3, (11, 12, 13))))
print(mix[3][3][3][2])
```


```python
i = 10

while i > 0:
    print('falcon')
    # i += 1
    i = i - 1
```

```python
vals = [-2, 3, 0, 4, -6, 0, 9]

for e in vals:
    if e < 0:
        print(f'{e} is negative')
    elif e == 0:
        print(f'{e} is zero')
    else:
        print(f'{e} is positive')
```



```python
import random


for i in range(5):
    r = random.randint(1, 100)
    msg = f'vygenerovane nahodne cislo: {r}'
    print(msg)
```
