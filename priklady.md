# Priklady 22.10.2024


## List Python files


```python 
import sys
import os

# list all Python files 


if len(sys.argv) != 2:
    
    print('Usage: list_files.py dir_name')
    sys.exit(1)

dir_name = sys.argv[1]

gfiles = os.walk(dir_name)

for (root, dir, files) in gfiles:

    for file in files:

        if file.endswith('py'):
            print(file)
```


```python
import os
from functools import partial
import sys

filetype = sys.argv[1]
data = os.listdir(os.curdir)
# print(data)

def isFileType(filetype, filename):

    # print(filetype)
    # print(filename)

    return os.path.isfile(filename) and filename.endswith('.{}'.format(filetype))

files = filter(partial(isFileType, filetype), os.listdir(os.curdir))

for myfile in files:
    print(myfile)
```

## Scan directory

```python
import os

for file in os.scandir('.'):

    line = ''

    if file.is_file():
        line += 'f'
    elif file.is_dir():
        line += 'd'
    elif file.is_symlink():
        line += 'l'

    line += '\t'

    print("{}{}".format(line, file.name))
```

## Pick males/females

pick males/femals from a list of users using list comprehension, records, and  
enumeration.  

```python
from dataclasses import dataclass
from enum import Enum
from collections import namedtuple

Sex = Enum('Sex', ['MALE', 'FEMALE'])


# @dataclass(frozen=True)
# class User:
#     name: str
#     occupation: str
#     sex: Sex

User = namedtuple('User', 'name occupation sex')

users = [User('John Doe', 'gardener', Sex.MALE),
         User('Roger Roe', 'driver', Sex.MALE),
         User('Peter Novak', 'teacher', Sex.MALE),
         User('Lucia Novak', 'teacher', Sex.FEMALE)]

males = [u for u in users if u.sex == Sex.MALE]
females = [u for u in users if u.sex == Sex.FEMALE]

print(males)
print(females)

print(type(males[0]))

for u in males:
    print(u)
```

## Create sequence 

```python
import numpy

# create sequence of values from 100 to 1000

# 1
vals = numpy.linspace(100, 1000, 900, dtype=int)
print(vals)

# 2
vals2 = []

for i in range(100, 1001):
    vals2.append(i)

print(vals2)

# 3

i = 0
start = 100
step = 1
end = 1000
vals3 = []

while i + start <= end:

    vals3.append(start + i)
    i += 1

print(vals3)

# 4

def seq():

    start = 100
    end = 1000

    while start <= end:

        yield start
        start += 1

vals4 = []

for e in seq():
    vals4.append(e)

print(vals4)
```


## Determine weekdays

Determine weekdays from date strings.  

```python
from dateutil import parser
from enum import Enum

data = ['2023-12-23', '2023-5-2', '2023-1-2', '2023-1-1',
        '2023-11-3', '2023-1-23', '2023-8-3', '2023-9-13']

Day = Enum(
    'Day', 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday', start=0)

print(Day.Monday)
print(Day.Tuesday)

print('------------------')

for ds in data:

    dt = parser.parse(ds)
    wd = dt.date().weekday()

    match Day(wd):
        case Day.Monday:
            print('it is', Day.Monday.name)
        case Day.Tuesday:
            print('it is', Day.Tuesday.name)
        case Day.Wednesday:
            print('it is', Day.Wednesday.name)
        case Day.Thursday:
            print('it is', Day.Thursday.name)
        case Day.Friday:
            print('it is', Day.Friday.name)
        case Day.Saturday:
            print('it is', Day.Saturday.name)
        case Day.Sunday:
            print('it is', Day.Sunday.name)
```


## Nacitanie CSV data

Tento priklad stahune data z CSV suboru na webe.  

Pouzivame:

- dataclass
- requests modul

```python
from dataclasses import dataclass
import requests

@dataclass(frozen=True)
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str

url = 'https://webcode.me/users.csv'

resp = requests.get(url)
content = resp.content.decode('utf8')

lines = content.splitlines()

users = []

for line in lines[1:-1]:
    fields = line.split(',', 3)
    fields_cleaned = fields[0], fields[1], fields[2], fields[3].replace('"', '')

    u = User(*fields_cleaned)
    users.append(u)


for user in users:
    print(user)
```

## Generator

```python
def countdown():

    num = 0
    print('Starting')

    while True:
        yield num
        num -= 1


max_iter = 3000
i = 0
for val in countdown():
    print(val)       
    i += 1
    if i >= max_iter:
        break 
```

## French deck

```python
import collections
from random import choice


Card = collections.namedtuple('Card', ['suit', 'rank'])


class FrenchDeck:

    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = ["heart", "clubs", "spades", "diamond"]

    def __init__(self):
        self.total = [Card(suit, rank)
                           for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.total)

    def __getitem__(self, index):
        return self.total[index]


deck = FrenchDeck()
print(deck[0])
# print(deck[2:7])
# print(deck[-2])
print(len(deck))
print(choice(deck))
```


## Functional list

```python
class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take.'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list 
        # values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    # def __iter__(self):
    #     return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)

    def head(self, n=5):
        # get the first element
        return self.values[:n]

    def tail(self, n=5):
        # get all elements after the first
        return self.values[-n:]

    def init(self):
        # get elements up to the last
        return self.values[:-1]

    def last(self):
        # get last element
        return self.values[-1]

    def drop(self, n):
        # get all elements except first n
        return self.values[n:]

    def take(self, n):
        # get first n elements
        return self.values[:n]


fl = FunctionalList([1, 2, 3, 4, 5, 6, 7, 8])
fl.append(9)
fl.append(10)
fl.append(11)

print(fl.head())
print(fl.tail())

print(len(fl))

for e in fl:
    print(e, end=' ')

print()
```


## Pouch

```python
import collections

Coin = collections.namedtuple('coin', ['rank'])

# a gold coin equals to two silver and six bronze coins


class Pouch:

    def __init__(self):
        self.bag = []

    def add(self, coin):

        self.bag.append(coin)

    def __eq__(self, other):

        val1, val2 = self.__evaluate(other)

        if val1 == val2:
            return True
        else:
            return False

    def __lt__(self, other):

        val1, val2 = self.__evaluate(other)
        # print(val1, val2)

        if val1 < val2:
            return True
        else:
            return False

    def __gt__(self, other):

        val1, val2 = self.__evaluate(other)
        # print(val1, val2)

        if val1 > val2:
            return True
        else:
            return False

    def __str__(self):

        return str(self.bag)

    def __evaluate(self, other):

        val1 = 0
        val2 = 0

        for coin in self.bag:

            if coin.rank == 'g':
                val1 += 6

            if coin.rank == 's':
                val1 += 3

            if coin.rank == 'b':
                val1 += 1

        for coin in other.bag:

            if coin.rank == 'g':
                val2 += 6

            if coin.rank == 's':
                val2 += 3

            if coin.rank == 'b':
                val2 += 1

        return val1, val2


pouch1 = Pouch()

pouch1.add(Coin('g'))
pouch1.add(Coin('g'))
pouch1.add(Coin('s'))

pouch2 = Pouch()

pouch2.add(Coin('g'))
pouch2.add(Coin('s'))
pouch2.add(Coin('s'))
pouch2.add(Coin('b'))
pouch2.add(Coin('b'))
pouch2.add(Coin('b'))

print(pouch1)
print(pouch2)

if pouch1 == pouch2:
    print('Pouches have equal value')

elif pouch1 > pouch2:
    print('Pouch 1 is more valueable than Pouch 2')
else:
    print('Pouch 2 is more valueable than Pouch 1')

```