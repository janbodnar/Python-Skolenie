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

## merge_with

```python
from funcy import merge_with

# Sales data for different stores and online
store1_sales = {
    'Product A': 120,
    'Product B': 80
}
store2_sales = {
    'Product A': 150,
    'Product C': 60
}
online_sales = {
    'Product B': 110,
    'Product C': 90
}

# Merge sales data, summing up sales for each product
total_sales = merge_with(sum, store1_sales, store2_sales, online_sales)

print(total_sales)
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

City = namedtuple('City' , 'id name population')

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

## count_by

The `count_by` function counts numbers of occurrences of values of f on elements of seq.  
Returns defaultdict(int) of counts.  


```python
from dataclasses import dataclass
from funcy import count_by

@dataclass
class User:
    name: str
    age: int
    occupation: str

users = [
    User(name='Alice', age=25, occupation='pilot'),
    User(name='Bob', age=30, occupation='driver'),
    User(name='Charlie', age=35, occupation='teacher'),
    User(name='David', age=40, occupation='teacher'),
    User(name='Paul', age=44, occupation='teacher'),
    User(name='Eva', age=25, occupation='driver'),
    User(name='Frank', age=30, occupation='teacher'),
    User(name='Mary', age=31, occupation='accountant')
]


# Count users by age group
occupation_counts = count_by(lambda user: user.occupation, users)

print(dict(occupation_counts))
```



The next example demonstrates how count_by can be used to categorize and count users by age  
group, providing a clear breakdown of the user distribution across different age categories.  

```python
from dataclasses import dataclass
from funcy import count_by

@dataclass
class User:
    name: str
    age: int
    email: str

# List of user profiles
users = [
    User(name='Alice', age=25, email='alice@example.com'),
    User(name='Bob', age=30, email='bob@example.com'),
    User(name='Charlie', age=35, email='charlie@example.com'),
    User(name='David', age=40, email='david@example.com'),
    User(name='Eva', age=25, email='eva@example.com'),
    User(name='Frank', age=30, email='frank@example.com')
]

# Define age groups
def age_group(user):
    if user.age < 30:
        return 'Under 30'
    elif user.age < 40:
        return '30-39'
    else:
        return '40 and above'

# Count users by age group
age_group_counts = count_by(age_group, users)

print("User counts by age group:", age_group_counts)
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

## chunks 

The `chunks` function divides the list of tasks into chunks, each with a length equal to  
the number of employees.  

The `zip` function to pair each employee with a corresponding chunk of tasks.  


```python
from dataclasses import dataclass
from funcy import chunks
from pprint import pprint

@dataclass
class Employee:
    name: str

@dataclass
class Task:
    description: str

# List of employees
employees = [
    Employee(name='Alice'),
    Employee(name='Bob'),
    Employee(name='Charlie')
]

# List of tasks
tasks = [
    Task(description='Task 1'),
    Task(description='Task 2'),
    Task(description='Task 3'),
    Task(description='Task 4'),
    Task(description='Task 5'),
    Task(description='Task 6'),
    Task(description='Task 7'),
    Task(description='Task 8')
]

# Distribute tasks to employees in chunks
task_chunks = list(chunks(len(employees), tasks))

# Assign tasks to employees using zip
assigned_tasks = list(zip([employee.name for employee in employees], task_chunks))

# Convert the list of tuples to a dictionary for better readability
assigned_tasks_dict = dict(assigned_tasks)

# Print the assigned tasks
pprint(assigned_tasks_dict)
```




