# Pattern match

*Pattern matching* is done with `match/case` keywords. It was introduced in Python 3.10 under the name  
structural pattern matching.

*Pattern matching* is a powerful control flow construct that allows us to compare a value against a series  
of patterns and then execute code based on which pattern matches. It is a much more advanced construct  
than the `if/else` statements or the classic switch statements.

In `if/else` or switch statements, each individual condition is called a branch; in pattern matching,  
the term arm is used instead.

## Pattern match literals

In the first example, we match againts simple literal values.

```python
#!/usr/bin/python

# literals.py

langs = ['russian', 'slovak', 'german',
         'swedish', 'hungarian', 'french', 'spanish']

print('say hello')

for lang in langs:
    match lang:
        case 'russian':
            print('привет')
        case 'hungarian':
            print('szia')
        case 'french':
            print('salut')
        case 'spanish':
            print('hola')
        case 'slovak':
            print('ahoj')
        case 'german':
            print('hallo')
        case 'swedish':
            print('Hallå')
```

We have a list of languages. We go through the list and say hello for each language.  

```python
for lang in langs:
    match lang:
```

The `match` keywords is followed by the option we are matching and a colon.  

```python
case 'russian':
    print('привет')
```

Each arm is started with a case, an option, and a colon.  

```
$ ./literals.py 
say hello
привет
ahoj
hallo
Hallå
szia
salut
hola
```

## Multiple options

We can have multiple options for a single line with `|`.

```python
#!/usr/bin/python

# grades.py

grades = ['A', 'B', 'C', 'D', 'E', 'F', 'FX']

for grade in grades:

    match grade:
        case 'A' | 'B' | 'C' | 'D' | 'E' | 'F':
            print('passed')
        case 'FX':
            print('failed')
```

We have a list of grades. For A throug F grades, we pass the example. For the FX grade, we fail the exam.

```
$ ./grades.py 
passed
passed
passed
passed
passed
passed
failed
```

## Wildcards 

We can use the wildcard character `_` for values that do not match any specific pattern, or it also can  
be utilized for all other patterns. 

```python
#!/usr/bin/python

# factorial.py

def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n - 1)


for i in range(17):
    print(i, factorial(i))
```

We create a factorial function with `match/case`.  

```python
match n:
    case 0 | 1:
        return 1
    case _:
        return n * factorial(n - 1)
```

For values 0 and 1, we return 1. For all other values, we recursively call the `factorial` function.  

```
$ ./factorial.py 
0 1
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 3628800
11 39916800
12 479001600
13 6227020800
14 87178291200
15 1307674368000
16 20922789888000
```

## Guards

Guards in the form of if conditions can be executed on an arm.

```python
#!/usr/bin/python

# guards.py

import random

n = random.randint(-5, 5)

match n:
    case n if n < 0:
        print(f"{n}: negative value")
    case n if n == 0:
        print(f"{n}: zero")
    case n if n > 0:
        print(f"{n}: positive value")
```

The example chooses a random integer. With `match/case` we determine, if the value is negative, zero, or positive.  

```python
case n if n < 0:
    print(f"{n}: negative value")
```

This arm is executed if the `n` is less than zero.  

## Matching objects

We can use pattern matching on Python objects.

```python
from dataclasses import dataclass

# objects.py

@dataclass
class Cat:
    name: str

@dataclass
class Dog:
    name: str

@dataclass
class Person:
    name: str

data = [Cat('Missy'), Dog('Jasper'), Dog('Ace'), Person('Peter'), 'Jupiter']

for e in data:
    match e:
        case Cat(name) | Dog(name):
            print(f'{name} is a pet')
        case Person(name):
            print(f'{name} is a human')
        case _:
            print(f'unknown')
```

We have three classes: `Cat`, `Dog`, and `Person`. With `match/case` we check, what type of class we have.  

```python
case Cat(name) | Dog(name):
    print(f'{name} is a pet')
```

This arm checks either for a cat or for a dog.

```python
case Person(name):
    print(f'{name} is a human')
```

This arm checks for a person object.

```python
case _:
    print(f'unknown')
```
  
For an object that we cannot identify, we use the wildcard.  

```
$ ./objects.py 
Missy is a pet
Jasper is a pet
Ace is a pet
Peter is a human
unknown
```

In the next example, we work with `Point` objects.

```python
#!/usr/bin/python

# points.py

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int


def check(p):
    match p:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x, y) if y == 0:
            print(f"on x axis")
        case Point(x, y) if x == 0:
            print(f"on y axis")
        case Point(x, y) if x > 0 and y > 0:
            print("Q I")
        case Point(x, y) if x < 0 and y > 0:
            print("Q II")
        case Point(x, y) if x < 0 and y < 0:
            print("Q III")
        case Point(x, y) if x > 0 and y < 0:
            print("Q IV")
        case _:
            print("Not a point")


points = [Point(3, 0), Point(0, 0), Point(-4, -5), Point(-4, 0), Point(0, 5),
          Point(4, 8), Point(-5, 3), Point(6, -4)]

for p in points:
    check(p)
```

Depending on the coordinates, we assign the point objects to the origin, x and y axis,  
or one of the four quadrants.  

```
$ ./points.py 
on x axis
Origin
Q III
on x axis
on y axis
Q I
Q II
Q IV
```

## Matching enums

Pattern matching can be effectively used with enums.  

```python
#!/usr/bin/python

# enums.py

from enum import Enum
import random


Day = Enum('Day', 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday')


days = [Day.Monday, Day.Tuesday, Day.Wednesday,
        Day.Thursday, Day.Friday, Day.Saturday, Day.Sunday]


res = random.sample(days, 4)

for e in res:

    match e:
        case Day.Monday:
            print("monday")
        case Day.Tuesday:
            print("tuesday")
        case Day.Wednesday:
            print("wednesay")
        case Day.Thursday:
            print("thursday")
        case Day.Friday:
            print("friday")
        case Day.Saturday:
            print("saturday")
        case Day.Sunday:
            print("sunday")
```

In the example, we define a Day enumeration.

```python
days = [Day.Monday, Day.Tuesday, Day.Wednesday,
    Day.Thursday, Day.Friday, Day.Saturday, Day.Sunday]

res = random.sample(days, 4)
```

We randomly choose four days from a list.

```python
for e in res:

    match e:
        case Day.Monday:
            print("monday")
        case Day.Tuesday:
            print("tuesday")
        case Day.Wednesday:
            print("wednesay")
        case Day.Thursday:
            print("thursday")
        case Day.Friday:
            print("friday")
        case Day.Saturday:
            print("saturday")
        case Day.Sunday:
            print("sunday")
```

We check the four chosen values and print their corresponding string representations.  

```
$ ./enums.py 
friday
monday
thursday
tuesday
```

## Matching tuples

In the following example, we match tuples.

```python
#!/usr/bin/python

# tuples.py

users = [
    ('John', 'Doe', 'gardener'),
    ('Jane', 'Doe', 'teacher'),
    ('Roger', 'Roe', 'driver'),
    ('Martin', 'Molnar', 'programmer'),
    ('Robert', 'Kovac', 'shopkeeper'),
    ('Tomas', 'Novy', 'programmer'),
]


for user in users:
    match user:
        case (fname, lname, 'programmer'):
            print(f'{fname} {lname} is a programmer')
        case (fname, lname, 'teacher'):
            print(f'{fname} {lname} is a teacher')
        case (fname, lname, 'gardener'):
            print(f'{fname} {lname} is a gardener')
        case _:
            print(user)
```

We have a list of tuples. Each tuple is a person and his profession. We match against the profession.  

```python
case (fname, lname, 'programmer'):
    print(f'{fname} {lname} is a programmer')
```

This arm binds the name of the person to fname and lname variables and matches against  
the 'programmer' value.

```
$ ./tuples.py
John Doe is a gardener
Jane Doe is a teacher
('Roger', 'Roe', 'driver')
Martin Molnar is a programmer
('Robert', 'Kovac', 'shopkeeper')
Tomas Novy is a programmer
```

## Matching maps 

In the next example, we do pattern matching with maps.  

```python
#!/usr/bin/python

# maps.py

users = [
    {'name': 'Paul', 'cols': ['red', 'blue', 'salmon']},
    {'name': 'Martin', 'cols': ['blue']},
    {'name': 'Lucia', 'cols': ['pink', 'brown']},
    {'name': 'Jan', 'cols': ['blue', 'green']},
]

for user in users:
    match user:
        case {'name':name, 'cols': cols}:
            print(f'favourite colours of {name}:')
            for col in cols:
                print(col)
```

We have a list of users represented as maps.  

```python
case {'name':name, 'cols': cols}:
    print(f'favourite colours of {name}:')
    for col in cols:
        print(col)
```

The case arm matches against a map and prints each user's favourite colours.  

```
$ ./maps.py 
favourite colours of Paul:
red
blue
salmon
favourite colours of Martin:
blue
favourite colours of Lucia:
pink
brown
favourite colours of Jan:
blue
green
```
