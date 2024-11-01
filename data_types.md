# Python data types

Computer programs, such as spreadsheets, text editors, calculators, or chat clients, work with data.  
Tools to work with various data types are essential part of a modern computer language.

## Definition

Data type is a set of values and the allowable operations on those values.  
Python has a great set of useful data types. Python's data types are built   
in the core of the language. They are easy to use and straightforward.

Python data types include:

- Booleans
- Strings
- Numbers
- Tuples
- Lists
- Sets
- Dictionaries
- None

Here is the data you provided in a markdown table format:

| Data Type | Class | Category | Kind | Mutable |
| --- | --- | --- | --- | --- |
| integers | int | numerics | Primitive | No |
| floats | float | numerics | Primitive | No |
| boolean | bool | booleans | Primitive | No |
| strings | str | text sequences | Primitive | No |
| ranges | range | sequences | Non-primitive | No |
| tuples | tuple | sequences | Non-primitive | No |
| lists | list | sequences | Non-primitive | Yes |
| dictionaries | dict | maps | Non-primitive | Yes |
| sets | set | sets | Non-primitive | Yes |
| frozen sets | frozenset | sets | Non-primitive | No |
| functions | function | functions | Non-primitive | Yes |
| NoneType | NoneType | nulls | --?-- | No |


## Booleans

In Python programming language, the Boolean datatype is a primitive datatype  
having one of two values: `True` or `False`. This is a fundamental data type.

Happy parents are waiting a child to be born. They have chosen a name for both possibilities.  
If it is going to be a boy, they might have chosen John. If it is going to be a girl,  
they might have chosen Victoria.

```python
#!/usr/bin/python

# kid.py

import random

male = False
male = bool(random.randint(0, 1))

if male:
   print("We will use name John")
else:
   print("We will use name Victoria")
```

The script uses a random integer generator to simulate our case.

```python
import random
```

Here we import the random module that is used to calculate random numbers.

```python
male = bool(random.randint(0, 1))
```

Here we use two functions. the randint function returns a random number from  
the given integer boundaries. In our case 0 or 1. The bool function converts  
the integers to boolean values.

```python
if male:
    print("We will use name John")
else:
    print("We will use name Victoria")
```

We print the name. The if keyword works with boolean values. If the male is `True`,  
we print the `"We will use name John"` to the console. If it has a `False` value, we print the other string.

The following script shows some common values that are considered to be True or False.

```python
#!/usr/bin/python

# bool_fun.py

print(bool(True))
print(bool(False))
print(bool("text"))
print(bool(""))
print(bool(' '))
print(bool(0))
print(bool())
print(bool(3))
print(bool(None))
```

The example prints nine boolean values.

```
$ ./bool_fun.py
True
False
True
False
True
False
False
True
False
```


## Numbers

In Python programming language, we have integer numbers, floating point numbers, and complex numbers.  
If we work with integers, we deal with discrete entities. We would use integers to count apples.  

```python
#!/usr/bin/python

# apples.py

# number of baskets
baskets = 16

# number of apples in a basket
apples_in_basket = 24

# we get the total number of apples
total = baskets * apples_in_basket

print("There are total of", total, "apples")
```

In our script, we count the total amount of apples. We use the multiplication operation.  

```
$ ./apples.py
There are total of 384 apples
```

Floating point numbers represent real numbers in computing. Real numbers measure continuous  
quantities. Let's say a sprinter for 100m ran 9.87s. What is his speed in km/h?  

```python
#!/usr/bin/python

# sprinter.py

# 100 m is 0.1 km

distance = 0.1

# 9.87 s is 9.87/60*60 h

time = 9.87 / 3600

speed = distance / time

print("The average speed of a sprinter is {0} km/h".format(speed))
```

To get the speed, we divide the distance by the time.

```python
print("The average speed of a sprinter is {0} km/h".format(speed))
```

We build the message with the format function and print it to the console.

```
$ ./sprinter.py
The average speed of a sprinter is  36.4741641337 km/h
```

This is the output of the `sprinter.py` script. Value `36.4741641337` is a floating point number.


The `math.isclose` function is used to determine whether two floating-point numbers are  
close to each other, within a specified tolerance. This is particularly useful for comparing  
floating-point numbers, which can often have small differences due to the imprecision of  
floating-point arithmetic.

```python
import math

a = 0.1 + 0.2
b = 0.3
tolerance = 1e-9

print(math.isclose(a, b, abs_tol=tolerance))  # Output: True
```


## Strings

String is a data type representing textual data in computer programs.

Strings in Python can be created using single quotes, double quotes, and triple quotes.  
When we use triple quotes, strings can span several lines without using the escape character.

```python
#!/usr/bin/python

# strings.py

a = "proximity alert"
b = 'evacuation'
c = """
requiem
for
a
tower
"""

print(a)
print(b)
print(c)
```

In our example we assign three string literals to a, b, and c variables.  
Then we print them to the console.

```
$ ./strings.py
proximity alert
evacuation

requiem
for
a
tower
```

When we work with strings, we can use escape sequences. Escape sequences are special   
characters that have a specific purpose when used within a string. 

```
print("   bbb\raaa") # prints aaabbb
```

The carriage return `\r` is a control character for end of line return to beginning of line.

```
#!/usr/bin/python

# strophe.py

print("Incompatible, it don't matter though\n'cos someone's bound to hear my cry")
print("Speak out if you do\nYou're not easy to find")
```

The new line is a control character which begins a new line of text.  

```
$ ./strophe.py
Incompatible, it don't matter though
'cos someone's bound to hear my cry
Speak out if you do
You're not easy to find
```

Next we examine the backspace control character.

```python
print("Python\b\b\booo") # prints Pytooo
```

The backspace control character \b moves the cursor one character back.  
In our case, we use three backspace characters to delete three letters 
and replace them with three o characters.

```
print("Towering\tinferno") # prints Towering        inferno
```

The horizontal tab puts a space between text.

```python
"Johnie's dog"
'Johnie\'s dog'
```

Single and double quotes can be nested. Or in case we use only single quotes,  
we can use the backslash to escape the default meaning of a single quote.

```
print("eagle has", len("eagle"), "characters")
```

We can use the len function to calculate the length of the string in characters.

If we append an r to the string, we get a raw string. The escape sequences are not interpreted.

```python
#!/usr/bin/python

# raw.py

print(r"Another world\n")
```

```
$ ./raw.py
Another world\n
```
We get the string with the new line character included.

In the next example, we show string multiplication and concatenation.

```python
#!/usr/bin/python

# strings2.py

print("eagle " * 5)
print("eagle " "falcon")

print("eagle " + "and " + "falcon")
```

The * operator repeats the string n times. In our case five times.  
Two string literals next to each other are automatically concatenated.  
We can also use the + operator to explicitly concatenate strings.

```
$ ./strings2.py
eagle eagle eagle eagle eagle
eagle falcon
eagle and falcon
```

Python has several built-in data types for working with collections of values: tuples, lists, sets, and dictionaries.

## Tuples

A *tuple* is an immutable sequence data type. The tuple can contain mixed data types.

```python
fruits = ("oranges", "apples", "bananas")
```

Tuples are created using round brackets. Here we have a tuple consisting of three fruit types.

```
fruits = "apples", "oranges", "bananas"
print(fruits)  # prints  ('apples', 'oranges', 'bananas')
```
The parentheses are not mandatory. We can omit them.

```python
#!/usr/bin/python

# tuples.py

first = (1, 2, 3)
second = (4, 5, 6)

print("len(first) : ", len(first))
print("max(first) : ", max(first))
print("min(first) : ", min(first))
print("first + second :", first + second)
print("first * 3 : ", first * 3)
print("1 in first : ", 1 in first)
print("5 not in second : ", 5 not in second)
```

This example shows several basic operations with tuples. The `len` function returns the number  
of elements in the first tuple. The max function returns the maximum value and the min the minimum value.  
The addition operator adds two tuples, the multiplication operator multiplies the tuple.  
The in operator determines if the value is in the tuple.

```
$ ./tuples.py
len(first) :  3
max(first) :  3
min(first) :  1
first + second : (1, 2, 3, 4, 5, 6)
first * 3 :  (1, 2, 3, 1, 2, 3, 1, 2, 3)
1 in first :  True
5 not in second :  False
```

Next we do some indexing.

```python
#!/usr/bin/python

# tuples2.py

five = (1, 2, 3, 4, 5)

print("five[0] : ", five[0])
print("five[-1] : ", five[-1])
print("five[-2] : ", five[-2])
print("five[:] : ", five[:])
print("five[0:4] : ", five[0:4])
print("five[1:2] : ", five[1:2])
print("five[:2] : ", five[:2])
print("five[:-1] : ", five[:-1])
print("five[:9] : ", five[:9])
```

To get a value from a tuple, we use square brackets `[]`. Note that we count indexes from 0.  
If there are five objects in a tuple, the indexes are 0...4. If we use a negative index,  
we get a value from the end of the tuple. So index -1 gets the last element, -2 gets the last but one element.

Python enables to create slices from tuples. For this we use the : delimiter.  
For instance, `[0:4]` gives `(1, 2, 3, 4)`. Note that the last element is not included.

We can omit one or both indexes in a slice. The `[:4]` gives `(1, 2, 3, 4)`. It goes from the first element.  
The `[0:]` gives `(1, 2, 3, 4, 5)`. This time, the last element is included.  
If we go out of bounds, we simply get all elements in the tuple.

```
$ ./tuples2.py
five[0] :  1
five[-1] :  5
five[-2] :  4
five[:] :  (1, 2, 3, 4, 5)
five[0:4] :  (1, 2, 3, 4)
five[1:2] :  (2,)
five[:2] :  (1, 2)
five[:-1] :  (1, 2, 3, 4)
five[:9] :  (1, 2, 3, 4, 5)
```

Tuples can contain several mix data types.

```python
#!/usr/bin/python

# tuples_mix.py

mix = (1, 2, "solaris", (1, 2, 3))

print("mix[1] :", mix[1])
print("mix[2] :", mix[2])
print("mix[3] :", mix[3])
print("mix[3][0] :", mix[3][0])
print("mix[3][1] :", mix[3][1])
print("mix[3][2] :", mix[3][2])
```

In our example, we have put numbers, a string, and a tuple into the mix tuple.

```
$ ./tuples_mix.py
mix[1] : 2
mix[2] : solaris
mix[3] : (1, 2, 3)
mix[3][0] : 1
mix[3][1] : 2
mix[3][2] : 3
```

To get the elements from the nested tuple, we use two square brackets.

We have an exception when we work with tuples containing one element.  
Parentheses are also used in expressions. How do we distinguish between an expression  
and a one element tuple? The creators of the Python programming language decided  
to use a comma to denote that we are using a tuple.

```python
#!/usr/bin/python

# tuple_one.py

print((3 + 7))
print((3 + 7, ))
```

In the first case we have and expression. We print number 10 to the console.  
In the second case we deal with a tuple. We print a tuple containing number 10.

```
$ ./tuple_one.py
10
(10,)
```

## Lists

A list is a mutable sequence data type. It can contain mixed data types.  
A list and a tuple share many common features. Because a list is a modifiable data type,  
it has some additional operations. A whole chapter is dedicated to the Python list.

```python
actors = ["Jack Nicholson", "Antony Hopkins", "Adrien Brody"]
```

The list is created using the square brackests `[]`.

```python
#!/usr/bin/python

# simple_list.py

num = [0, 2, 5, 4, 6, 7]

print(num[0])
print(num[2:])
print(len(num))
print(num + [8, 9])
```

As we have stated previously, we can use the same operations on lists as on tuples.

```
$ ./list_simple.py
0
[5, 4, 6, 7]
6
[0, 2, 5, 4, 6, 7, 8, 9]
```

Next we sort a list.

```python
#!/usr/bin/python

# list_sorting.py

numbers = [4, 3, 6, 1, 2, 0, 5]

print(numbers)
numbers.sort()
print(numbers)
```

In our script we have a list of numbers. To sort those numbers, we use the built-in sort function.

```
$ ./list_sorting.py
[4, 3, 6, 1, 2, 0, 5]
[0, 1, 2, 3, 4, 5, 6]
```

The reverse function will sort the elements of a list in reverse order.

```python
numbers.reverse()   #  [5, 4, 3, 2, 1, 0]
```

Counting elements in a list is done with the count method.

```python
#!/usr/bin/python

# list_counting_elements.py

numbers = [0, 0, 2, 3, 3, 3, 3]

print("zero is here",  numbers.count(0), "times")
print("one is here",   numbers.count(1), "times")
print("two is here",   numbers.count(2), "time")
print("three is here", numbers.count(3), "times")
```

The script counts number occurrences in a list.

```
$ ./list_counting_elements.py
zero is here 2 times
one is here 0 times
two is here 1 time
three is here 4 times
```

Next, we deal with inserting and deleting items from the list.

```python
#!/usr/bin/python

# list_modify.py

names = []

names.append("Frank")
names.append("Alexis")
names.append("Erika")
names.append("Ludmila")

print(names)

names.insert(0, "Adriana")
print(names)

names.remove("Frank")
names.remove("Alexis")
del names[1]
print(names)

del names[0]
print(names)
```

In our example we first create an empty names list. We use the append function  
to append new items to the list. The elements are appended in the consecutive way.  
The insert function inserts new elements at a given position. The existing elements  
are not deleted, they are relocated. The remove function removes a specific item  
from the list. If we want to delete an item based on the index, we use the `del` keyword.

```
$ ./list_modify.py
['Frank', 'Alexis', 'Erika', 'Ludmila']
['Adriana', 'Frank', 'Alexis', 'Erika', 'Ludmila']
['Adriana', 'Ludmila']
['Ludmila']
```

There following program presents additional two functions.

```python
#!/usr/bin/python

# list_modify2.py

first = [1, 2, 3]
second = [4, 5, 6]

first.extend(second)
print(first)

first[0] = 11
first[1] = 22
first[2] = 33
print(first)

print(first.pop(5))
print(first)
```

The `extend` method appends a whole list to another list. To modify an element in a list,  
we can use the assignment operator. The `pop` method takes an item from the list and returns it.

```
$ ./list_modify2.py
[1, 2, 3, 4, 5, 6]
[11, 22, 33, 4, 5, 6]
6
[11, 22, 33, 4, 5]
```
In the following example, we find out indexes of elements.

```python
#!/usr/bin/python

# list_index.py

numbers = [0, 1, 2, 3, 3, 4, 5]

print(numbers.index(1))
print(numbers.index(3))
```

To find an index in a list, we use the index method. If there are more occurrences  
of an element, the method returns the index of the first element.

```
$ ./list_index.py
1
3
```

Next we do some transformations.

```python
#!/usr/bin/python

# list_transform.py

first = [1, 2, 3]
second = (4, 5, 6)

print(tuple(first))
print(list(second))

print(first)
print(second)
```

We can use tuple function to create a tuple from a list and list function to create  
a list from a tuple. Note that the original objects are not modified;  
the functions only return those transformed collections.

```
$ ./list_transform.py
(1, 2, 3)
[4, 5, 6]
[1, 2, 3]
(4, 5, 6)
```

## Sets

A *set* is an unordered collection of data with no duplicate elements. A set supports  
operations like union, intersection, or difference; similar as in Mathematics.

### Newer syntax

Newer syntax uses `{}` to define sets, older uses the `set` function. 

```python
set1 = {'a', 'b', 'c', 'c', 'd'}
set2 = {'a', 'b', 'x', 'y', 'z'}

print("set1: " , set1)
print("set2: " , set2)
print("intersection: ", set1 & set2)
print("union: ", set1 | set2)
print("difference: ", set1 - set2)
print("symmetric difference: ", set1 ^ set2)
```

In our example we have two sets. We use the set function to create sets.  
The intersection operation returns elements that are both in set1 and set2.  
The union operation returns all elements from both sets. The difference returns elements  
that are in the set1 but not is set2. And finally, the symmetric difference returns elements  
that are in set1 or set2, but not in both.


```
$ ./sets.py
set1:  {'a', 'c', 'b', 'd'}
set2:  {'x', 'b', 'z', 'a', 'y'}
intersection:  {'a', 'b'}
union:  {'d', 'z', 'x', 'b', 'a', 'y', 'c'}
difference:  {'c', 'd'}
symmetric difference:  {'x', 'd', 'z', 'y', 'c'}
```

Next we introduce some other operations with sets.

```python
#!/usr/bin/python

set1 = {1, 2}
set1.add(3)
set1.add(4)

set2 = {1, 2, 3, 4, 6, 7, 8}
set2.remove(8)

print(set1)
print(set2)

print("Is set1 subset of set2 ? :", set1.issubset(set2))
print("Is set1 superset of set2 ? :", set1.issuperset(set2))

set1.clear()
print(set1)
```

The `add` method adds an item to the set. The `remove` method removes an item from a set.  
The `clear` method removes all items from the set. The set1 is superset of set2 if every  
element in set2 is also in set1. The set1 is a subset of set2 if every element in set1 is also in set2.

```
$ ./sets2.py
{1, 2, 3, 4}
{1, 2, 3, 4, 6, 7}
Is set1 subset of set2 ? : True
Is set1 superset of set2 ? : False
set()
```

If we need an immutable set, we can create a frozen set with the frozenset function.

```python
fs = frozenset(['a', 'b', 'c'])
```

This line creates a frozen set from a list.

Find common and different functionality for bytes, strings and lists and tuples.  

```python
print(set(dir(bytes)) - set(dir(str)))
print(set(dir(list)) & set(dir(tuple)))
```


## Dictionaries

A Python dictionary is a group of key-value pairs. The elements in a dictionary are indexed  
by keys. Keys in a dictionary are required to be unique. Because of the importance  
of the dictionary data type, a whole chapter covers the dictionary in this Python tutorial.

```python
#!/usr/bin/python

# dictionary_simple.py

words = { 'girl': 'Maedchen', 'house': 'Haus', 'death': 'Tod' }

print(words['house'])

print(words.keys())
print(words.values())
print(words.items())

print(words.pop('girl'))
print(words)

words.clear()
print(words)
```

Our first example shows some basic usage of the dictionary data type. We print a specific value,  
keys and values of the dictionary. The items method returns a list of dictionarie's (key, value) pairs as tuples.

```
$ ./dictionary_simple.py
Haus
['house', 'girl', 'death']
['Haus', 'Maedchen', 'Tod']
[('house', 'Haus'), ('girl', 'Maedchen'), ('death', 'Tod')]
Maedchen
{'house': 'Haus', 'death': 'Tod'}
{}
```

looping  

```python
#!/usr/bin/python

# looping.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway" }

for key in domains:
    print(key)

for val in domains.values():
    print(val)

for k, v in domains.items():
    print(f'{k}: {v}')
```

## None

There is another special data type — None. This data type means non existent, not known, or empty.

```python
#!/usr/bin/python

# none.py

def function():
    pass

print(function())
```

In our example, we define a function. Functions will be covered later in the tutorial.  
The function does nothing. It does not explicitly return any value. Such a function will implicitly return `None`.  

```
$ ./none.py
None
```
