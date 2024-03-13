# Python fstrings


Python f-string is the newest Python syntax to do string formatting. It is available since Python 3.6.  
Python f-strings provide a faster, more readable, more concise, and less error prone way  
of formatting strings in Python.

The f-strings have the `f` prefix and use `{}` brackets to evaluate values.  
#!/usr/bin/python

name = 'John Doe'
occupation = 'gardener'
age = 34

msg = f'''name: {name}
age: {age}
occupation: {occupation}'''

print(msg)
Format specifiers for types, padding, or aligning are specified after the colon character;  
for instance: `f'{price:.3}'`, where price is a variable name. 

## String formatting

The following example summarizes string formatting options in Python.

```python
#!/usr/bin/python

name = 'Peter'
age = 23

print('%s is %d years old' % (name, age))
print('{} is {} years old'.format(name, age))
print(f'{name} is {age} years old')
```

The example formats a string using two variables.

```python
print('%s is %d years old' % (name, age))
```

This is the oldest option. It uses the % operator and classic string format specifies such as `%s` and `%d`.

```python
print('{} is {} years old'.format(name, age))
```

Since Python 3.0, the `format` function was introduced to provide advance formatting options.

```python
print(f'{name} is {age} years old')
```

Python f-strings are available since Python 3.6. The string has the `f` prefix and uses `{}` to evaluate variables.

```
$ python formatting_string.py
Peter is 23 years old
Peter is 23 years old
Peter is 23 years old
```

## Python f-string expressions

We can put expressions between the `{}` brackets.

```python
#!/usr/bin/python

bags = 3
apples_in_bag = 12

print(f'There are total of {bags * apples_in_bag} apples')
```

The example evaluates an expression inside f-string.

```
$ python expressions.py
There are total of 36 apples
```

## Python f-string dictionaries

We can work with dictionaries in f-strings.

```python
#!/usr/bin/python

user = {'name': 'John Doe', 'occupation': 'gardener'}

print(f"{user['name']} is a {user['occupation']}")
```

The example evaluates a dictionary in an f-string.

```
$ python dicts.py
John Doe is a gardener
```

## Python f-string debug

Python 3.8 introduced the self-documenting expression with the `=` character.

```python
#!/usr/bin/python

import math

x = 0.8

print(f'{math.cos(x) = }')
print(f'{math.sin(x) = }')
```

The example outputs the Sine and Cosine functions in the debug mode.

```
$ python debug.py
math.cos(x) = 0.6967067093471654
math.sin(x) = 0.7173560908995228
```

## Multiline f-string

We can work with multiline strings.

```python
#!/usr/bin/python

name = 'John Doe'
occupation = 'gardener'
age = 34

msg = f'''name: {name}
age: {age}
occupation: {occupation}'''

print(msg)
```

The example presents a multiline f-string.  

```
$ python main.py
name: John Doe
age: 34
occupation: gardener
```

## Calling functions

We can also call functions in f-strings.

```python
#!/usr/bin/python

def mymax(x, y):

    return x if x > y else y

a = 3
b = 4

print(f'Max of {a} and {b} is {mymax(a, b)}')
```

The example calls a custom function in the f-string.

```
$ python main.py
Max of 3 and 4 is 4
```

## F-string objects

Python f-string accepts objects as well; the objects must have either `__str__` or `__repr__`   
magic functions defined.

```python
#!/usr/bin/python

class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __repr__(self):
        return f"{self.name} is a {self.occupation}"

u = User('John Doe', 'gardener')

print(f'{u}')
```

The example evaluates an object in the f-string.

```
$ python main.py
John Doe is a gardener
```

## The __format__ method

The `__format` method gives us more control over how an object is formatted within  
an f-string. It allows us to define custom formatting behavior based on the format  
specifier provided within the f-string.  

```python
#!/usr/bin/python

from dataclasses import dataclass

@dataclass
class User:
    name: str
    occupation: str

    def __format__(self, spec):
        return f'User(name={self.name}{spec} occupation={self.occupation})'


u1 = User('John Doe', 'gardener')
u2 = User('Roger Roe', 'driver')
u3 = User('Lucia Smith', 'teacher')

print(f'{u1:-}')
print(f'{u2:;}')
print(f'{u3:#}')
```

We define a data object with a custom `__format__` method.  


## Python f-string escaping characters

The following example shows how to escape certain characters in f-strings.

```python
#!/usr/bin/python

print(f'Python uses {{}} to evaludate variables in f-strings')
print(f'This was a \'great\' film')
```

To escape a curly bracket, we double the character. A single quote is escaped with a backslash character.
```python
$ python escaping.py
Python uses {} to evaludate variables in f-strings
This was a 'great' film
```

## Python f-string format datetime

The following example formats datetime.

```python
#!/usr/bin/python

import datetime

now = datetime.datetime.now()

print(f'{now:%Y-%m-%d %H:%M}')
print(f'{now:%A}')
print(f'{now:%a}')
print(f'{now:%B}')
print(f'{now:%j}')
print(f'{now:%w}')
```

The example displays a formatted current datetime. The datetime format specifiers follow the `:` character.

```
$ python format_datetime.py
2023-03-24 15:12
Friday
Fri
March
083
5
```

## Python f-string format floats

Floating point values have the `f` suffix. We can also specify the precision: the number of decimal places.  
The precision is a value that goes right after the dot character.

```python
#!/usr/bin/python

val = 12.3

print(f'{val:.2f}')
print(f'{val:.5f}')
```

The example prints a formatted floating point value.

```
$ python format_floats.py
12.30
12.30000
```

The output shows the number having two and five decimal places.

## Python f-string percentage

We display a decimal value as percentage using the % format specifier.

```python
#!/usr/bin/python

val = 1/7.0

print(f'{val}')
print(f'{val:.2%}')
```

In the program, we display the 1/7 value as a percentage with two decimal places.

```
$ python percentage.py 
0.14285714285714285
14.29%
```

## Python f-string format width

The width specifier sets the width of the value. The value may be filled with spaces or other characters  
if the value is shorter than the specified width.

```python
#!/usr/bin/python

for x in range(1, 11):
    print(f'{x:02} {x*x:3} {x*x*x:4}')
```

The example prints three columns. Each of the columns has a predefined width. The first column uses  
0 to fill shorter values.

```python
$ python format_width.py
01   1    1
02   4    8
03   9   27
04  16   64
05  25  125
06  36  216
07  49  343
08  64  512
09  81  729
10 100 1000
```

## Python f-string justify string

By default, the strings are justified to the left. We can use the `>` character to justify the strings  
to the right. The `>` character follows the colon character. The `<` justifies to the left; this can  
be omitted. The `^` centers the string.

```python
#!/usr/bin/python

words = ['sky', 'fork', 'small', 'cup', 'car', 'war']

for word in words:
    print(f'|{word:>20}|')

for word in words:
    print(f'|{word:^20}|')

for word in words:
    print(f'|{word:<20}|')
```

We have a list of words. The words are aligned to the right, center, and left.  
Each of the outputs has twenty characters.  

```
$ python main.py
|                 sky|
|                fork|
|               small|
|                 cup|
|                 car|
|                 war|
|        sky         |
|        fork        |
|       small        |
|        cup         |
|        car         |
|        war         |
|sky                 |
|fork                |
|small               |
|cup                 |
|car                 |
|war                 |
```
      
## Numeric notations

Numbers can have various numeric notations, such as decadic or hexadecimal.

```python
#!/usr/bin/python

val = 300

# hexadecimal lower
print(f'{val:x}')

# hexadecimal upper
print(f'{val:X}')

# octal
print(f'{val:o}')

# binary
print(f'{val:b}')

# scientific
print(f'{val:e}')
The example prints a value in various notations.
```

```
$ python format_notations.py
12c
12C
454
100101100
3.000000e+02
```

## Thousands separator

We can format numbers with underscore and command thousands separators.  

```python
#!/usr/bin/python

val = 1_200_400_001

print(val)
print(f'{val:_}')
print(f'{val:,}')
```

A big integer is printed in formats where thousand groups are separated with 
`_` and `,`.

```
$ python main.py
python main.py
1200400001
1_200_400_001
1,200,400,001
```

