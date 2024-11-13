# funcy 

The funcy library is a collection of practical functional programming tools for Python.  
It is inspired by functional programming languages like Clojure and libraries like  
Underscore.js. funcy provides a variety of utilities to make functional programming in  
Python more convenient and expressive.

## Filtering

```python
from funcy import filter

vals = [1, -3, 4, 0, -9, 11, 5, -6]

filtered = filter(lambda e: e > 0, vals)
print(list(filtered))


words = ['key', 'eye', 'norm', 'atom', 'rock', 'water']

filtered = filter(lambda e: len(e) == 3, words)
print(list(filtered))
```

## lmap, map 

`lmap` is a convenience for `list(map(...))`  

```python
from funcy import map, lmap

vals = [2, 4, 6]

res = map(lambda x: x * 2, vals)
print(list(res))

vals = [2, 4, 6]

res = lmap(lambda x: x * 2, vals)
print(res)
```

## distinct

```python
from funcy import distinct
 
 
words = ['sky', 'war', 'water', 'war', 'sky', 'cup', 'cup', 'atom']

distilled = distinct(words)
print(list(distilled))
```

## split

```python
from funcy import split

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens, odds = split(lambda e: e % 2 == 0, values)

print(list(evens))
print(list(odds))
```

## flatten 

```python
from funcy import flatten

nested_list = [[1, 2], [3, 4], [5]]
flat_list = flatten(nested_list)
```

## walk_values & walk_keys

```python
from funcy import walk_values, walk_keys

# Sample data with inconsistent text cases
data = {
    'Name': 'Alice',
    'Email': 'ALICE@EXAMPLE.COM',
    'City': 'NeW YoRk'
}

# Normalize the text to lowercase
normalized_values = walk_values(str.lower, data)
print("Normalized values:", normalized_values)

# Normalize the text to lowercase
normalized_keys = walk_keys(str.lower, data)
print("Normalized keys:", normalized_keys)
```

## split_by

```python
from collections import namedtuple
from funcy import split_by

City = namedtuple('City' , 'id, name population')

c1 = City(1, 'Bratislava', 432000)
c2 = City(2, 'Budapest', 1759000)
c3 = City(3, 'Prague', 1280000)
c4 = City(4, 'Warsaw', 1748000)
c5 = City(5, 'Los Angeles', 3971000)
c6 = City(6, 'Edinburgh', 464000)
c7 = City(7, 'Presov', 82930)
c8 = City(8, 'Kosice', 228000)
c9 = City(9, 'Zilina', 81220)

cities = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
cities.sort(key=lambda c: c.population)

low_pop, high_pop = split_by(lambda c: c.population < 1000_000, cities)
print(list(low_pop))
print(list(high_pop))
```

## select_keys & select_values

```python
from funcy import select_keys, select_values

animals = {'donkeys': 3, 'horses': 2, 'chickens': 15,
           'dogs': 2, 'cats': 5, 'elephants': 2}


res = select_values(lambda e: e > 2, animals)
print(res)

res = select_keys(lambda e: e.startswith('do'), animals)
print(res)


res = {k: v for k, v in filter(lambda e: e[1] > 2, animals.items())}
print(res)

res = {k: v for k, v in filter(
    lambda e: e[0].startswith('do'), animals.items())}
print(res)
```

## Function composition

```python
from funcy import rcompose, compose

def square(x):
    return x * x

def increment(x):
    return x + 1

def cube(x):
    return x * x * x


val = 5

fchain = rcompose(square, increment, cube)
print(fchain(val))
print(cube(increment(square(val))))

print('---------------------------------------------')

fchain = compose(square, increment, cube)
print(fchain(val))
print(square(increment(cube(val))))
```

## nth

```python
from funcy import nth, repeatedly
from argparse import ArgumentParser

aparser = ArgumentParser()

aparser.add_argument('-n', type=int, required=True)
args = aparser.parse_args()

n = args.n

with open('words.txt') as f:

    line = nth(n, repeatedly(f.readline))
    print(line)
```

## deck of cards

```python
from funcy import cycle, take, lmap

suits = ["♠", "♥", "♦", "♣"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

zdeck = zip(take(52, cycle(values)), cycle(suits))
print(lmap("".join, zdeck))
```

## group_by

```python
from funcy import group_by

users = [
    {'first_name': 'John', 'last_name': 'Doe', 'occupation': 'gardener'},
    {'first_name': 'Roger', 'last_name': 'Roe', 'occupation': 'driver'},
    {'first_name': 'Adam', 'last_name': 'Novak', 'occupation': 'teacher'},
    {'first_name': 'Paul', 'last_name': 'Novak', 'occupation': 'programmer'},
    {'first_name': 'Roman', 'last_name': 'Meszaros', 'occupation': 'programmer'},
    {'first_name': 'Tomas', 'last_name': 'Bruzik', 'occupation': 'driver'},
]

users.sort(key=lambda user: user['occupation'])
grouped = group_by(lambda user: user['occupation'], users)

for k, v in grouped.items():
        
    print('-----------------------------')
    print(k)
    print(v)
```

---

```python

from collections import namedtuple

from funcy import group_by
User = namedtuple('User', 'first_name last_name occupation')

users = [
    User('John', 'Doe', 'gardener'),
    User('Roger', 'Roe', 'driver'),
    User('Adam', 'Novak', 'teacher'),
    User('Paul', 'Novak', 'programmer'),
    User('Roman', 'Meszaros', 'programmer'),
    User('Tomas', 'Bruzik', 'driver'),
]

users.sort(key=lambda user: user.occupation)
grouped = group_by(lambda user: user.occupation, users)

for k, v in grouped.items():

    print('-----------------------------')
    print(k)
    for e in v:
        print(e)
```

## select & pluck

```python
from funcy import select, pluck

# List of user profiles
users = [
    {'name': 'Alice', 'active': True, 'email': 'alice@example.com'},
    {'name': 'Bob', 'active': False, 'email': 'bob@example.com'},
    {'name': 'Charlie', 'active': True, 'email': 'charlie@example.com'}
]

# Select active users
active_users = select(lambda u: u['active'], users)

# Extract emails of active users
emails = pluck('email', active_users)

print("Active Users:", active_users)
print("Emails of Active Users:", emails)
```






