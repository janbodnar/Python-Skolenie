# Enum type


An *enumeration* is a set of symbolic names bound to unique, constant values. Enumerations  
can be used to create simple custom data types which include things such as seasons, weeks,  
types of weapons in a game, planets, grades, or days. By convention, enumeration names begin  
with an uppercase letter and are singular.  

The enum module is used for creating enumerations in Python. Enumerations are created with the  
class keyword or with the functional API.  

Enumeration is a data type introduced in Python 3.4.

## Simple example

We have a  `Season` enumeration which has four distinct values: `SPRING`, `SUMMER`, `AUTUMN`,  
and `WINTER`. 

```python
from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


seas = Season.SPRING
print(seas)

if seas == Season.SPRING:
    print("Spring")

print(list(Season))
```

To access a member, we specify the enumeration name followed by a dot and the member name.  

```python
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
````

The `Season` enumeration is created with the class keyword. We inherit from the `enum.Enum`  
base class. We explicity set numbers to the enumeration values.  

```python
seas = Season.SPRING
print(seas)
```

An enumeration value is assigned to a variable and it is printed to the console.  

```python
if seas == Season.SPRING:
    print("Spring")
```

The `Season.SPRING` is used in an if expression.  

```python
print(list(Season))
```

With the list built-in function, we get the list of all possible values for the `Season` enum.  


## Basic functionality 

The next example presents some other basic functionality of a Python enum.

```python
from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


seas = Season.SPRING

print(seas)
print(isinstance(seas, Season))
print(type(seas))
print(repr(seas))

print(Season['SPRING'])
print(Season(1))
```

Again, we deal with a Season enumeration created with the class.

```python
print(seas)
```

Here we print a human readable string representation of a `Season` member.  

```python
print(isinstance(seas, Season))
```

With the isinstance method, we check if the variable has a value of `Season` type.  

```python
print(type(seas))
```

The type function prints the type of the variable.

```python
print(repr(seas))
```

The `repr` function provides more information about the enum.

```python
print(Season['SPRING'])
print(Season(1))
```

Member of an enumeration can be accessed by item name and index.


## Functional API

```python
from enum import Enum

Season = Enum('Season', 'SPRING SUMMER AUTUMN WINTER', start=1)

seas = Season.SUMMER
print(seas)

if seas == Season.SUMMER:
    print("Summer")
```

```python
Season = Enum('Season', 'SPRING SUMMER AUTUMN WINTER', start=1)
```

Here the values are specified in a string, separated by space. The `start`  
provides the initial value.


## Enumeration

In this example, we create a `Season` enum where the values are set in   
a list of strings.

```python
from enum import Enum


Season = Enum('Season', ['SPRING', 'SUMMER', 'AUTUMN', 'WINTER'], start=5)

for season in Season:
    print(season)

for season in Season:
    print(season.name, season.value)
```

```python
for season in Season:
    print(season)
```

We iterate over enum members in a for loop.

```python
for season in Season:
    print(season.name, season.value)
```

Here we print their names and values.

## Automatic values

Python enum values can be automatically set with the auto function.

```python
from enum import Enum, auto


class Season(Enum):
    SPRING = auto()
    SUMMER = auto()
    AUTUMN = auto()
    WINTER = auto()


for season in Season:
    print(season.value)
```

We have a `Season` enum where its members get a value with `auto` function.


## Unique member values

The member values of a Python enum can be enforced to be unique with the `@unique`  
decorator.

```python
from enum import Enum, unique

@unique
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 3
    # WINTER = 4


for season in Season:
    print(season)
```

The example fails with the `ValueError: duplicate values found in <enum 'Season'>: WINTER -> AUTUMN error`,   
because the `AUTUMN` and `WINTER` members have the same value. If we comment out the @unique decorator, the  
example prints three members; the `WINTER` is ignored.  

## The __members__ attribute

The special attribute `__members__` is a read-only ordered mapping of names to members.

```python
from enum import Enum


Season = Enum('Season', [('SPRING', 1), ('SUMMER', 2), 
    ('AUTUMN', 3), ('WINTER', 4)])


for name, member in Season.__members__.items():
    print(name, member)
```

In the example, we use the `__members__` property. The enumeration members are created with a list of  
tuples using functional API.

## The enum.Flag

The `enum.Flag` is a base class for creating enumerated constants that can be combined using the  
bitwise operations without losing their Flag membership.

```python
from enum import Flag, auto


class Perm(Flag):
    EXECUTE = auto()
    WRITE = auto()
    READ = auto()


print(list(Perm))
print(Perm.READ | Perm.WRITE)
```

The example shows how the Flag can be used on permissions.

## Static method 

```python
from enum import Enum
import random


class Day(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

    @staticmethod
    def random_day():
        return random.choice(list(Day))


rdays = [Day.random_day() for _ in range(10)]

for e in rdays:
    print(e)
```

We define a Day enumeration. The `random_day` static method returns a random choice from the  
keys of the enumeration.

```python
rdays = [Day.random_day() for _ in range(10)]
```

With a list comprehension, we create a list of ten random days.

## Coin toss

We have a coin with two enum values: `HEADS` and `TAILS`.

```python
from enum import Enum
import random


class Coin(Enum):
    HEADS = 0
    TAILS = 1

    @staticmethod
    def toss():
        return random.choice(list(Coin))


for _ in range(15):
    print(f'{Coin.toss()}', end=' ')
```

In the example, we toss a coin fifteen times.

## Pattern matching

The `match/case` keywords can be used with enums to create concise code.

```python
from enum import Enum
import random


class Day(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

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

In the example, we define a `Day` enumeration.

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

We check the four chosen values and print their corresponding string representations. For each option,  
we have a specific case arm.

## Practical examples 

### Pick males/females

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

### Determine weekdays

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



