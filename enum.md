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

