# Opakovanie

```python
# genrate a list of cubes using list comprehension
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter all numbers
data = ['test', 3.0, 5, True, (1, 2), 3.14, None, {'us': 'United States'}, 
        [1, 2, 3], 'hello', 42]

# clean the words, remove leading and trailing spaces, and filter out empty strings
words = [' blue', '\nred', '',  'green', '\t\tyellow', 'purple\n', 
         'sky', 'pawn', 'rock\n', '  ', 'paper', '\t\tscissors']

# using list comprehension, generate a list of random numbers 
# from 1, 100 
# print first 10 and last 10 numbers

# calculate the sum of all numbers in the list
data2 = '1,2,3,4,5,6,7,8,9,10'

# filter users youger than 30 years old
# filter users with last name starting with 'W'
from collections import namedtuple

User = namedtuple('User', ['first_name', 'last_name', 'age', 'email'])

users = [
    User('John', 'Doe', 34, 'john.doe@example.com'),
    User('Jane', 'Smith', 28, 'jane.smith@example.com'),
    User('Alice', 'Johnson', 45, 'alice.johnson@example.com'),
    User('Bob', 'Brown', 50, 'bob.brown@example.com'),
    User('Charlie', 'Davis', 22, 'charlie.davis@example.com'),
    User('Emily', 'Wilson', 30, 'emily.wilson@example.com'),
    User('Frank', 'White', 27, 'frank.white@example.com'),
    User('Grace', 'Hall', 38, 'grace.hall@example.com'),
    User('Henry', 'Lewis', 29, 'henry.lewis@example.com'),
    User('Ivy', 'Young', 40, 'ivy.young@example.com'),
    User('Jack', 'Martin', 33, 'jack.martin@example.com'),
    User('Karen', 'King', 26, 'karen.king@example.com'),
    User('Leo', 'Scott', 35, 'leo.scott@example.com'),
    User('Mia', 'Turner', 24, 'mia.turner@example.com'),
    User('Nathan', 'Adams', 37, 'nathan.adams@example.com'),
    User('Olivia', 'Baker', 31, 'olivia.baker@example.com'),
    User('Paul', 'Carter', 42, 'paul.carter@example.com'),
    User('Quinn', 'Flores', 23, 'quinn.flores@example.com'),
    User('Ryan', 'Hill', 48, 'ryan.hill@example.com'),
    User('Sophia', 'Reed', 29, 'sophia.reed@example.com')
]
```




## Riesenia

```python
##

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vals_cubed = [x**3 for x in vals]
print(vals_cubed)

# filter all numbers
data = ['test', 3.0, 5, True, (1, 2), 3.14, None, {'us': 'United States'}, 
        [1, 2, 3], 'hello', 42]

data_nums = [x for x in data if type(x) == int or type(x) == float]
# data_nums = [x for x in data if type(x) in (int, float)]

print(data_nums)

words = [' blue', '\nred', '',  'green', '\t\tyellow', 'purple\n', 
         'sky', 'pawn', 'rock\n', '  ', 'paper', '\t\tscissors']

words_cleaned = [word.strip() for word in words if word.strip()]
print(words_cleaned)
```















```python
import sys
from faker import Faker

filename = sys.argv[1]
n = int(sys.argv[2])

faker = Faker()

with open(filename, 'w') as fd:

    headers = 'id,first_name,last_name,email,city\n'
    fd.write(headers)

    for uid in range(1, n+1):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        city = faker.city()
        row = f'{uid},{first_name},{last_name},{email},{city}\n'

        fd.write(row)
```


```python

import sys

vals = sys.argv[1:]
print(vals)

total = sum(int(val) for val in vals)
print(total)
```



## Generate fake users.csv file

```python

from faker import Faker

faker = Faker()
filename = "users.csv"

with open(filename, 'w') as fd:

    headers = 'id,first_name,last_name,email,city\n'
    fd.write(headers)

    for uid in range(1, 100_001):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        city = faker.city()
        row = f'{uid},{first_name},{last_name},{email},{city}\n'

        fd.write(row)
```



## Write to file

```python
filename = "words2.txt"

with open(filename, 'w') as fd:

    fd.write('atom\n')
    fd.write('new\n')
    fd.write('small\n')
```


## Append to file

```python

filename = "words2.txt"

with open(filename, 'a') as fd:

    fd.write('cup\n')
    fd.write('cloud\n')
```


## reading files

```python
filename = "words.txt"

with open(filename, 'r') as fd:

    # content = fd.read()
    # print(content.split())

    # lines = fd.readlines()
    # print(lines)

    for line in fd:
        print(line.strip())
```



## dataclasses and namedtuples

```python

from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str
    salary: int


u = User(1, 'Roger', 'Roe', 'driver', 1780)

print(u.last_name)
print(u.salary)

print(u)


# from collections import namedtuple
#
# User = namedtuple('User', 'id first_name last_name occupation salary')
#
# u1 = User(1, "John", "Doe", "gardener", 2300)
# print(u1)
```






## Rectangle

```python
import sys

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def area(self):

        return self.width * self.height


# print(sys.argv)


width = sys.argv[1]
height = sys.argv[2]


r = Rectangle(int(width), int(height))
print(r.area())
print(r.get_width(), r.get_height())

r.set_height(40)
print(r.area())
```



```python
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def area(self):

        return self.width * self.height

w = input("Enter width:")
h = input("Enter height:")

r = Rectangle(int(w), int(h))
print(r.area())
print(r.get_width(), r.get_height())

r.set_height(40)
print(r.area())
```



## Objects

```python


class Cat:

    def __init__(self, name, age):

        self.name = name
        self.age = age

missy = Cat('Missy', 3)
lucky = Cat('Lucky', 4)
mercy = Cat('Mercy', 1)

print(missy.name, missy.age)
print(lucky.name, lucky.age)
print(mercy.name, mercy.age)

# procedural style:

# cat_name1 = 'Missy'
# cat_age1 = 3
# 
# cat_name2 = 'Lucky'
# cat_age2 = 4
# 
# cat_name3 = 'Mercy'
# cat_age3 = 1
```







The `words.txt` file:

```
smart
war
abyss
ocean
park
water
ram
new
cup
pen
dog
cat
chair
```

```python
# transform to lowercase using list comprehension
words = ["skY", "NEW", "Output", "blue", "SMart", 'oceaN']

# filter even vals using list comprehension
vals = [3, 4, 2, 1, 9, 11, 10, 8, 7, 6, 3]

# using a list comprehension, generate a list of random values
# between 1 .. 100. 

# calculate sum
data = "1;2;3;4;5;6,7;8;9;10"

# filter out words with length 3 and ending in 't'
words2 = ["sky", "war", "put", "out", "ocean", 'os', 'season', 'arch']

# read words.txt into a list and sort it
```

## Riesenia

```python
# transform to lowercase using list comprehension
words = ["skY", "NEW", "Output", "blue", "SMart", 'oceaN']

words2 = [word.lower() for word in words]
print(words2)

# filter even vals using list comprehension
vals = [3, 4, 2, 1, 9, 11, 10, 8, 7, 6, 3]

evens = [val for val in vals if val % 2 == 0]
print(evens)

# using a list comprehension, generate a list of 100 random values
# between 1 .. 100. 
import random

randvals = [random.randint(1, 101) for _ in range(100)]
print(randvals)

# filter out words with length 3 and ending in 't'
words2 = ["sky", "war", "put", "out", "ocean", 'os', 'season', 'arch']
# words3 = [word for word in words2 if len(word) == 3 and word.endswith('t')]
words3 = [word for word in words2 if len(word) == 3 and word[-1] == 't']

print(words3)

# read words.txt into a list and sort it
filename = 'words.txt'
with open(filename, 'r') as fd:

    lines = fd.readlines()
    lines_cleaned = [line.strip() for line in lines]

    print(lines_cleaned)

# calculate sum
data = "1;2;3;4;5;6,7;8;9;10"

data2 = data.replace(',', ';')
print(data2)

fields = data2.split(';')
print(fields)

print(sum(int(field) for field in fields))

# vals = [int(field) for field in fields]
# print(vals)
# 
# print(sum(vals))
```



