# Pattern matching

*Pattern matching* is performed using the `match` and `case` keywords. It was introduced  
in Python 3.10 under the name **structural pattern matching**.

Pattern matching is a powerful control flow construct that allows you to compare a value  
against a series of patterns and then execute code based on which pattern matches. It is  
far more advanced than traditional `if/else` chains or the classic `switch` statements  
found in other languages.

In `if/else` or `switch` statements, each individual condition is called a *branch*;  
in pattern matching, the term **arm** is used instead.

## Matching literal values

In the first example, we match against simple literal values.

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

We have a list of languages. We iterate through the list and greet each language by v
printing the corresponding word for "hello".

```python
for lang in langs:
    match lang:
```

The `match` keyword is followed by the value we are matching (the *subject*) and a colon.

```python
case 'russian':
    print('привет')
```

Each arm begins with the keyword `case`, followed by a pattern, and then a colon.  
If the pattern matches the subject, the indented block is executed.

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

## Multiple options in a single arm

You can combine several literal patterns into one arm using the `|` (OR) operator.

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

We have a list of grades. For grades `A` through `F`, the exam is passed. For the  
`FX` grade, the exam is failed.

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

## The wildcard pattern `_`

The wildcard character `_` matches any value but does not bind it to a name. It is typically  
used as a default case for values that do not match any specific pattern.

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

We implement the factorial function using `match/case`.

```python
match n:
    case 0 | 1:
        return 1
    case _:
        return n * factorial(n - 1)
```

For values `0` and `1`, we return `1`. For any other value, we recursively call `factorial`.  
The wildcard pattern `_` matches everything not already matched.

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

## Guards (conditional arms)

Guards allow you to attach an `if` condition to an arm. The arm is only chosen if 
the pattern matches **and** the guard expression evaluates to `True`.

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

The example picks a random integer. Using `match/case` with guards, we  
determine whether the value is negative, zero, or positive.

```python
case n if n < 0:
    print(f"{n}: negative value")
```

This arm is executed only if `n` is less than zero. Notice that the variable `n` is  
bound before the guard is evaluated.

## Matching objects (data classes)

Pattern matching works seamlessly with Python objects, especially data classes.

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

We define three data classes: `Cat`, `Dog`, and `Person`. With `match/case` we  
check the type of each object.

```python
case Cat(name) | Dog(name):
    print(f'{name} is a pet')
```

This arm matches either a `Cat` or a `Dog` and extracts the `name` attribute.

```python
case Person(name):
    print(f'{name} is a human')
```

This arm matches a `Person` object.

```python
case _:
    print(f'unknown')
```

For any other value (like the string `'Jupiter'`), we use the wildcard.

```
$ ./objects.py 
Missy is a pet
Jasper is a pet
Ace is a pet
Peter is a human
unknown
```

### Matching objects with positional patterns

You can also define **positional patterns** for your classes by setting  
`__match_args__`. This allows you to match without naming the attributes explicitly.

```python
#!/usr/bin/python

# positional_match.py

from dataclasses import dataclass

@dataclass
class Point:
    __match_args__ = ('x', 'y')
    x: int
    y: int

def describe(point):
    match point:
        case Point(0, 0):
            print("Origin")
        case Point(0, y):
            print(f"On Y-axis at y={y}")
        case Point(x, 0):
            print(f"On X-axis at x={x}")
        case Point(x, y):
            print(f"Point at ({x}, {y})")

describe(Point(0, 0))
describe(Point(0, 5))
describe(Point(3, 0))
describe(Point(2, 7))
```

The `__match_args__` tuple tells the pattern matcher which attributes to use  
for positional matching. This makes the syntax more concise.

## Matching sequences (lists, tuples)

Pattern matching can deconstruct sequences like lists and tuples, including  
variable-length sequences.

```python
#!/usr/bin/python

# sequences.py

records = [
    ("Alice", "Engineering", 85000),
    ("Bob", "Sales", 62000),
    ("Charlie", "Engineering", 91000),
    ("Diana", "HR", 55000),
]

for record in records:
    match record:
        case (name, "Engineering", salary):
            print(f"{name} works in Engineering and earns ${salary}")
        case (name, dept, salary) if salary < 60000:
            print(f"{name} from {dept} earns less than $60k")
        case (name, dept, _):
            print(f"{name} works in {dept}")
```

Tuples are matched positionally. The first arm extracts `name` and `salary` when  
the department is exactly `"Engineering"`. The second arm uses a guard to filter  
low salaries. The third arm uses a wildcard `_` to ignore the salary.

### Variable‑length sequence patterns

You can use `*rest` to match an arbitrary number of items.

```python
#!/usr/bin/python

# star_pattern.py

def process_first_two(items):
    match items:
        case [first, second, *rest]:
            print(f"First: {first}, Second: {second}, Rest: {rest}")
        case [first, *rest]:
            print(f"Only first: {first}, Rest: {rest}")
        case _:
            print("Empty list")

process_first_two([10, 20, 30, 40])
process_first_two([5])
process_first_two([])
```

## Using the `as` pattern

The `as` keyword lets you capture the entire matched value in a variable, even 
while destructuring parts of it.

```python
#!/usr/bin/python

# as_pattern.py

def inspect_command(cmd):
    match cmd.split():
        case ["quit"]:
            print("Exiting...")
        case ["load", filename] as whole:
            print(f"Loading file '{filename}' (full command: {whole})")
        case _:
            print("Unknown command")

inspect_command("load data.txt")
```

## Matching enums

Pattern matching is especially clean when working with enumerations.

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
            print("wednesday")
        case Day.Thursday:
            print("thursday")
        case Day.Friday:
            print("friday")
        case Day.Saturday:
            print("saturday")
        case Day.Sunday:
            print("sunday")
```

We define a `Day` enumeration, select four random days, and print their names.

```python
from enum import Enum
import random

Day = Enum("Day", "Monday Tuesday Wednesday Thursday Friday Saturday Sunday")

days = [
    Day.Monday,
    Day.Tuesday,
    Day.Wednesday,
    Day.Thursday,
    Day.Friday,
    Day.Saturday,
    Day.Sunday,
]

sample = random.sample(days, 4)

for day in sample:
    match day:
        case Day.Saturday | Day.Sunday:
            print(f"{day} is a weekend")
        case _:
            print(f"{day} is a weekday")
```


## Matching maps (dictionaries)

Dictionaries can be matched by their keys, and you can extract values.

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
        case {'name': name, 'cols': cols}:
            print(f'favourite colours of {name}:')
            for col in cols:
                print(col)
```

The pattern `{'name': name, 'cols': cols}` matches any dictionary that has at least  
the keys `'name'` and `'cols'`. It binds the corresponding values to the  
variables `name` and `cols`.

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

> **Note**: Dictionary patterns do **not** require every key in the dictionary
> to be specified. Missing keys are simply ignored. If you want to match an
> exact set of keys, you can add `**rest` to capture any extra items.

## Nested patterns

Patterns can be nested arbitrarily. This allows you to destructure complex  
data structures in a single match.

```python
#!/usr/bin/python

# nested.py

data = [
    ("user", {"id": 1, "role": "admin"}),
    ("user", {"id": 2, "role": "editor"}),
    ("guest", {"token": "abc123"}),
]

for item in data:
    match item:
        case ("user", {"role": "admin", "id": user_id}):
            print(f"Admin user with id {user_id}")
        case ("user", {"role": "editor"}):
            print("Editor user")
        case ("guest", {"token": token}):
            print(f"Guest with token {token}")
        case _:
            print("Unknown item")
```

Here we match a tuple whose second element is a dictionary, and we further  
match inside that dictionary.

## Summary

Python’s structural pattern matching (`match/case`) is a versatile tool that  
goes far beyond simple value equality. It can:

- Match literals, sequences, mappings, and objects.
- Capture sub‑values into variables.
- Combine patterns with `|` (OR).
- Use guards to add extra conditions.
- Use wildcards (`_`) to ignore parts or provide a fallback.
- Nest patterns to destructure complex data.

When you need to inspect the shape and content of data, pattern matching often  
produces much clearer and more maintainable code than a cascade of `if/else` statements.
