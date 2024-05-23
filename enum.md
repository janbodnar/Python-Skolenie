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

```pythnon
print(list(Season))
```

With the list built-in function, we get the list of all possible values for the `Season` enum.  













