# Python Data Types

Programs work with data: prices in a shop, names in a contact list, scores  
in a game. Every value in Python has a **data type**, which says what kind  
of value it is and what you can do with it. You can add two numbers, make  
a string uppercase, or append an item to a list, but you cannot make a  
number uppercase.

The built-in `type()` function shows the type of any value:

```python
# show_types.py

print(type(42))
print(type(3.14))
print(type(True))
print(type(None))
print(type("hello"))
print(type([1, 2, 3]))
print(type((1, 2)))
print(type({"name": "Alice"}))
print(type({1, 2, 3}))
```

```text
$ python show_types.py
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'set'>
```

This chapter gives an overview of these built-in types, from simple values  
to collections:

- numbers: integers and floating-point numbers,
- booleans,
- `None`,
- strings,
- lists,
- tuples,
- dictionaries,
- sets,
- mutable and immutable types,
- converting between types.

Strings and several operators have their own chapters; this chapter shows  
only the essentials and points to them.

## Numbers

### Integers

An **integer**, type `int`, is a whole number without a decimal point:  
`0`, `42`, `-7`. Use integers for things that you count, such as apples,  
people, or points.

```python
# apples.py

baskets = 16
apples_per_basket = 24

total = baskets * apples_per_basket
print("Total apples:", total)
```

```text
$ python apples.py
Total apples: 384
```

Python integers have no size limit. They can grow as large as the memory  
of the computer allows:

```python
# big_number.py

print(2 ** 100)
print(1_000_000 * 1_000_000)
```

```text
$ python big_number.py
1267650600228229401496703205376
1000000000000
```

`**` is the power operator. Underscores in `1_000_000` make long numbers  
easier to read; Python ignores them. The Lexical Structure chapter shows  
how to write integers in binary, octal, and hexadecimal.

### Floating-Point Numbers

A **floating-point number**, type `float`, has a decimal point: `3.14`,  
`0.5`, `-2.0`. Use floats for things that you measure, such as distance,  
weight, or time.

```python
# sprinter.py

distance = 0.1           # 100 m in kilometres
time = 9.87 / 3600       # 9.87 s in hours

speed = distance / time
print(speed)
print(f"Speed: {speed:.2f} km/h")
```

```text
$ python sprinter.py
36.474164133738604
Speed: 36.47 km/h
```

The `:.2f` in the f-string shows the number with two decimal places; the  
stored value does not change. Very large or very small floats can be  
written in **scientific notation**: `6.022e23` means 6.022 × 10²³, and  
`1.5e-3` means 0.0015.

When you mix integers and floats, the result is a float. The `/` operator  
always returns a float, even when the division is exact:

```python
# mixing.py

print(7 + 0.5)
print(10 / 2)
print(10 // 3)
```

```text
$ python mixing.py
7.5
5.0
3
```

`//` is floor division, which returns a whole number. The Operators  
chapter explains all arithmetic operators.

### Floats Are Not Exact

A computer stores floats in binary, and many decimal fractions, such as  
0.1, have no exact binary form. Python stores the nearest possible value,  
which leads to tiny errors:

```python
# precision.py

import math

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))
```

```text
$ python precision.py
0.30000000000000004
False
True
```

This is not a bug in Python; every language that uses standard floats  
behaves the same way. Never compare floats with `==`. Use  
`math.isclose()`, which checks whether two numbers are close enough.

For money and other values that must be exact, use the `Decimal` type from  
the `decimal` module. Create decimals from strings, not from floats:

```python
# money.py

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))
print(Decimal(0.1))
```

```text
$ python money.py
0.3
0.1000000000000000055511151231257827021181583404541015625
```

`Decimal(0.1)` receives the inexact float and keeps its error, as the long  
second line shows. The string `"0.1"` is converted exactly.

### Rounding

The built-in `round()` function rounds a number to a given number of  
decimal places. Without the second argument, it returns an integer:

```python
# rounding.py

price = 19.876

print(round(price, 2))
print(round(price))
print(round(2.5))
print(round(3.5))
```

```text
$ python rounding.py
19.88
20
2
4
```

The last two lines may surprise you. When a number is exactly halfway,  
`round()` goes to the nearest *even* number, so `2.5` becomes `2` and `3.5`  
becomes `4`. This is called **banker's rounding**, and it avoids always  
rounding up. To always round down or up, use `math.floor()` or  
`math.ceil()`.

Python also has a type for **complex numbers**, such as `3 + 4j`, used in  
engineering and science. You will not need it in this course.

## Booleans

A **boolean**, type `bool`, has only two values: `True` and `False`.  
Comparisons produce booleans, and `if` statements and `while` loops use  
them to make decisions:

```python
# booleans.py

age = 20
is_adult = age >= 18

print(is_adult)
print(type(is_adult))
print(is_adult and age < 65)
print(not is_adult)
```

```text
$ python booleans.py
True
<class 'bool'>
True
False
```

`and`, `or`, and `not` combine booleans. The Operators chapter explains  
them, together with short-circuit evaluation.

### Truthy and Falsy Values

Python can treat any value as true or false. The `bool()` function shows  
how a value is treated:

```python
# truthy.py

print(bool(0))
print(bool(3))
print(bool(""))
print(bool(" "))
print(bool([]))
print(bool([0]))
print(bool(None))
```

```text
$ python truthy.py
False
True
False
True
False
True
False
```

The **falsy** values are `False`, `None`, zero (`0`, `0.0`), and empty  
collections (`""`, `[]`, `()`, `{}`, `set()`). Everything else is  
**truthy**, including the string `" "` with one space and the list `[0]`  
with one item. This lets you write `if names:` to check that a list is not  
empty.

Booleans are a special kind of integer: `True` counts as `1` and `False`  
as `0`. That is why `sum([True, False, True])` returns `2`, which is a  
handy way to count how many conditions are true.

## None

`None` means "no value". It is the only value of the type `NoneType`. Use  
it for something that is missing or not known yet:

```python
# none.py

middle_name = None

print(middle_name)
print(type(middle_name))

if middle_name is None:
    print("No middle name")
```

```text
$ python none.py
None
<class 'NoneType'>
No middle name
```

There is only one `None` object, so check for it with `is None` or  
`is not None`, as PEP 8 recommends, rather than with `==`.

`None` is not the same as `0`, `False`, or an empty string. A price of `0`  
means "free"; a price of `None` means "unknown". That is why `is None` is  
better than `if not price:`, which would treat both cases the same.

Functions that do their work without computing a result return `None`.  
`print()` is one of them:

```python
# print_result.py

result = print("Hello")
print(result)
```

```text
$ python print_result.py
Hello
None
```

## Strings

A **string**, type `str`, is text: a sequence of characters in single or  
double quotes. Strings support indexing, slicing, and many methods:

```python
# string_basics.py

name = "Alice"

print(len(name))
print(name[0])
print(name.upper())
print(name + " Smith")
```

```text
$ python string_basics.py
5
A
ALICE
Alice Smith
```

Strings are **immutable**: their characters cannot be changed, and methods  
such as `upper()` return a new string. The Strings chapter covers strings  
in detail.

## Lists

A **list**, type `list`, is an ordered collection of values in square  
brackets. It is the most common collection in Python. A list can grow and  
shrink, and its items can be changed.

### Creating and Reading a List

Lists use the same indexing and slicing as strings. The first item has the  
index 0, and `-1` is the last item:

```python
# list_basics.py

fruits = ["apple", "banana", "cherry"]

print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[1:])
print(len(fruits))
print("banana" in fruits)
```

```text
$ python list_basics.py
['apple', 'banana', 'cherry']
apple
cherry
['banana', 'cherry']
3
True
```

A list can hold values of any type, even mixed types, but in practice the  
items of one list are usually of the same kind. An empty list is written  
as `[]`.

### Changing a List

Unlike a string, a list can be changed in place:

```python
# list_change.py

fruits = ["apple", "banana", "cherry"]

fruits[1] = "blueberry"
fruits.append("date")
fruits.insert(0, "avocado")
print(fruits)

fruits.remove("cherry")
last = fruits.pop()
print(last)
print(fruits)
```

```text
$ python list_change.py
['avocado', 'apple', 'blueberry', 'cherry', 'date']
date
['avocado', 'apple', 'blueberry']
```

- `fruits[1] = "blueberry"` replaces the item at index 1.
- `append()` adds an item to the end, and `insert()` at a given index.
- `remove()` deletes the first item with the given value.
- `pop()` removes the last item and returns it, so you can still use it.  
  `pop(0)` removes the first item instead.

The `del` statement removes an item by its index: `del fruits[0]`.

### Sorting and Other Operations

```python
# list_sort.py

scores = [72, 95, 88, 61]

print(sorted(scores))
print(scores)

scores.sort(reverse=True)
print(scores)

print(max(scores), min(scores), sum(scores))
print(scores.count(88), scores.index(88))
```

```text
$ python list_sort.py
[61, 72, 88, 95]
[72, 95, 88, 61]
[95, 88, 72, 61]
95 61 316
1 1
```

There are two ways to sort:

- `sorted(scores)` returns a new sorted list and leaves the original  
  unchanged.
- `scores.sort()` sorts the list itself and returns `None`.

`reverse=True` sorts from the largest to the smallest. `max()`, `min()`,  
and `sum()` work on any list of numbers. `count()` returns how many times  
a value occurs, and `index()` returns the position of its first  
occurrence.

## Tuples

A **tuple**, type `tuple`, is like a list that cannot be changed. You  
write it with parentheses, or simply with commas. Use a tuple for a fixed  
group of values that belong together, such as the two coordinates of a  
point or the parts of a date.

```python
# tuples.py

point = (3, 7)
birthday = (1990, 5, 17)

print(point[0])
print(len(birthday))

x, y = point
print(x, y)
```

```text
$ python tuples.py
3
3
3 7
```

Tuples support indexing and slicing like lists. The line `x, y = point` is  
called **unpacking**: it assigns the items of the tuple to several names  
at once.

A tuple cannot be changed after it is created:

```python
# tuple_immutable.py

point = (3, 7)
point[0] = 5
```

```text
$ python tuple_immutable.py
Traceback (most recent call last):
  File ".../tuple_immutable.py", line 4, in <module>
    point[0] = 5
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

This is a feature, not a limitation. When you pass a tuple to other code,  
you know that it cannot be modified by accident.

### A Tuple with One Item

It is the comma, not the parentheses, that creates a tuple. Parentheses  
alone only group an expression:

```python
# one_item.py

print(type((10)))
print(type((10,)))
print((10,))
```

```text
$ python one_item.py
<class 'int'>
<class 'tuple'>
(10,)
```

To create a tuple with one item, add a comma after it: `(10,)`. An empty  
tuple is written as `()`.

## Dictionaries

A **dictionary**, type `dict`, stores pairs of **keys** and **values**.  
You look up a value by its key, just as you look up a word in a real  
dictionary to find its meaning. Dictionaries are written with curly  
braces and a colon between each key and value.

### Reading and Changing a Dictionary

```python
# dict_basics.py

ages = {"Alice": 30, "Bob": 25}

print(ages["Alice"])

ages["Carol"] = 35
ages["Bob"] = 26
print(ages)

del ages["Alice"]
print(ages)
print(len(ages))
print("Bob" in ages)
```

```text
$ python dict_basics.py
30
{'Alice': 30, 'Bob': 26, 'Carol': 35}
{'Bob': 26, 'Carol': 35}
2
True
```

- `ages["Alice"]` returns the value for the key `"Alice"`.
- Assigning to a new key adds a pair; assigning to an existing key  
  replaces its value. Each key appears only once.
- `del` removes a pair.
- `in` checks the keys, not the values.

Dictionaries remember the order in which the keys were added (Python  
3.7+). An empty dictionary is written as `{}`.

### Missing Keys

Looking up a key that does not exist is an error:

```python
# dict_missing.py

ages = {"Alice": 30, "Bob": 25}
print(ages["Dave"])
```

```text
$ python dict_missing.py
Traceback (most recent call last):
  File ".../dict_missing.py", line 4, in <module>
    print(ages["Dave"])
          ~~~~^^^^^^^^
KeyError: 'Dave'
```

When a key may be missing, use the `get()` method. It returns `None`, or a  
default value that you choose, instead of raising an error:

```python
# dict_get.py

ages = {"Alice": 30, "Bob": 25}

print(ages.get("Alice"))
print(ages.get("Dave"))
print(ages.get("Dave", 0))
```

```text
$ python dict_get.py
30
None
0
```

### Looping over a Dictionary

A `for` loop over a dictionary goes through its keys. The `items()` method  
gives you each key together with its value:

```python
# dict_loop.py

capitals = {
    "Slovakia": "Bratislava",
    "Czechia": "Prague",
    "Austria": "Vienna",
}

for country in capitals:
    print(country)

for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")
```

```text
$ python dict_loop.py
Slovakia
Czechia
Austria
The capital of Slovakia is Bratislava.
The capital of Czechia is Prague.
The capital of Austria is Vienna.
```

`items()` returns pairs, and `country, capital` unpacks each pair, just  
like the tuple unpacking shown earlier. `keys()` and `values()` return  
only the keys or only the values.

## Sets

A **set**, type `set`, is a collection of *unique* values. Adding a value  
that is already there has no effect. Sets are written with curly braces,  
like dictionaries, but without the colons.

### Removing Duplicates

The most common use of a set is to remove duplicates or to check quickly  
whether a value is present:

```python
# sets.py

visits = [3, 1, 3, 2, 1, 3]

unique = set(visits)
print(unique)
print(len(unique))

unique.add(4)
unique.add(1)
print(unique)
print(2 in unique)
```

```text
$ python sets.py
{1, 2, 3}
3
{1, 2, 3, 4}
True
```

The list had six items, but only three different values. Adding `1` again  
changed nothing.

A set has no order and no indexes, so `unique[0]` is an error. The order  
in which a set prints its items is not guaranteed and can differ from run  
to run, especially for strings. Use `sorted()` when you need a fixed  
order.

### Set Operations

Sets support the operations known from mathematics. The following example  
compares the students of two courses:

```python
# set_operations.py

python_course = {"Alice", "Bob", "Carol"}
java_course = {"Bob", "Dave"}

print(sorted(python_course & java_course))
print(sorted(python_course | java_course))
print(sorted(python_course - java_course))
```

```text
$ python set_operations.py
['Bob']
['Alice', 'Bob', 'Carol', 'Dave']
['Alice', 'Carol']
```

- `&`, the **intersection**, returns the students in both courses.
- `|`, the **union**, returns the students in at least one course.
- `-`, the **difference**, returns the students in the Python course only.

`sorted()` returns the result as a sorted list, so the output is always  
the same. Python also has a `frozenset` type, a set that cannot be  
changed.

## Mutable and Immutable Types

Some types can be changed after they are created; they are **mutable**.  
Others cannot; they are **immutable**. An operation on an immutable value  
always creates a new value.

| Type | Example | Mutable | Ordered | Duplicates |
| --- | --- | --- | --- | --- |
| `int`, `float`, `bool` | `42`, `3.14`, `True` | No | — | — |
| `NoneType` | `None` | No | — | — |
| `str` | `"hello"` | No | Yes | Yes |
| `tuple` | `(3, 7)` | No | Yes | Yes |
| `list` | `[1, 2, 3]` | Yes | Yes | Yes |
| `dict` | `{"a": 1}` | Yes | Yes (3.7+) | Unique keys |
| `set` | `{1, 2, 3}` | Yes | No | No |

The difference matters when two names refer to the same object, as the  
Python Terms chapter shows. Changing a list through one name changes it  
for the other name too. To work on an independent copy, use `copy()`:

```python
# copy_list.py

original = ["apple", "banana"]
shared = original
copied = original.copy()

shared.append("cherry")

print(original)
print(copied)
```

```text
$ python copy_list.py
['apple', 'banana', 'cherry']
['apple', 'banana']
```

Only immutable values can be dictionary keys or set items. A string or a  
tuple works as a key; a list does not, because it could change after it  
was added.

## Converting Between Types

The name of each type also works as a function that converts a value to  
that type:

```python
# conversions.py

print(int("25") + 5)
print(float("2.5") * 2)
print(str(3.5) + " kg")
print(int(7.9))
print(list("abc"))
print(tuple([1, 2, 3]))
print(set([1, 1, 2]))
print(list(range(5)))
```

```text
$ python conversions.py
30
5.0
3.5 kg
7
['a', 'b', 'c']
(1, 2, 3)
{1, 2}
[0, 1, 2, 3, 4]
```

Converting text to a number is needed whenever the number comes from user  
input or a file. Note that `int(7.9)` returns `7`: `int()` cuts off the  
decimal part instead of rounding. Use `round()` to round.

## Common Mistakes

### Storing the Result of a List Method

List methods such as `append()` and `sort()` change the list in place and  
return `None`. Assigning their result replaces your list with `None`:

```python
# append_none.py

names = ["Alice", "Bob"]
names = names.append("Carol")
print(names)
```

```text
$ python append_none.py
None
```

Write `names.append("Carol")` on its own line. This is the opposite of  
string methods, which return a new string that you must store.

### Creating an Empty Set with `{}`

Empty curly braces create an empty dictionary, not a set:

```python
# empty_set.py

print(type({}))
print(type(set()))
```

```text
$ python empty_set.py
<class 'dict'>
<class 'set'>
```

Use `set()` to create an empty set.

### Converting a Decimal String with `int()`

`int()` accepts only strings that contain a whole number:

```python
# int_decimal.py

print(int("3.5"))
```

```text
$ python int_decimal.py
Traceback (most recent call last):
  File ".../int_decimal.py", line 3, in <module>
    print(int("3.5"))
          ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '3.5'
```

Convert such a string with `float("3.5")`. If you need an integer, convert  
the float afterwards: `int(float("3.5"))` or `round(float("3.5"))`.

### Comparing Floats with `==`

As shown in the section on floats, `0.1 + 0.2 == 0.3` is `False`. Use  
`math.isclose()` to compare floats, and `Decimal` for money.

## Hands-On: A Class Gradebook

This program uses most of the types from this chapter. A dictionary maps  
each student's name (a string) to a list of scores (integers). The  
program computes averages (floats), decides who passed (booleans), and  
remembers the best student in a tuple that starts as `None`.

```python
# gradebook.py

grades = {
    "Alice": [92, 88, 95],
    "Bob": [75, 64, 81],
    "Carol": [58, 49, 66],
}
pass_mark = 60

best = None
failed = []

print(f"{'Name':<8}{'Average':>8}  Result")

for name, scores in grades.items():
    average = sum(scores) / len(scores)
    passed = average >= pass_mark

    if not passed:
        failed.append(name)

    if best is None or average > best[1]:
        best = (name, average)

    result = "pass" if passed else "fail"
    print(f"{name:<8}{average:>8.1f}  {result}")

print()
print(f"Best student: {best[0]} ({best[1]:.1f})")
print("Failed:", ", ".join(failed))
```

```text
$ python gradebook.py
Name     Average  Result
Alice       91.7  pass
Bob         73.3  pass
Carol       57.7  fail

Best student: Alice (91.7)
Failed: Carol
```

- `grades.items()` gives each name with its list of scores.
- `sum(scores) / len(scores)` divides two integers with `/`, so the  
  average is a float.
- `average >= pass_mark` produces a boolean.
- `best` starts as `None`, because no student has been seen yet. The  
  first student always replaces it, and later only a higher average does.
- The tuple `(name, average)` keeps two values that belong together.
- The f-string format `<8` aligns text to the left and `>8.1f` aligns a  
  number to the right with one decimal place; see the f-strings chapter.

## Summary

| Type | Example | Use it for |
| --- | --- | --- |
| `int` | `42` | Whole numbers, counting |
| `float` | `3.14` | Measured values; not exact |
| `Decimal` | `Decimal("0.10")` | Money and exact decimal values |
| `bool` | `True`, `False` | Results of comparisons and conditions |
| `NoneType` | `None` | A missing or unknown value; test with `is None` |
| `str` | `"hello"` | Text; immutable |
| `list` | `[1, 2, 3]` | An ordered collection that can change |
| `tuple` | `(3, 7)` | A fixed group of values; immutable |
| `dict` | `{"Alice": 30}` | Looking up values by key |
| `set` | `{1, 2, 3}` | Unique values, removing duplicates, set operations |

Mutable types (`list`, `dict`, `set`) can be changed in place; immutable  
types (numbers, `str`, `tuple`, `None`) cannot.

## References

- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [The Python Tutorial: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [The Python Tutorial: Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html)
- [`math` — Mathematical functions](https://docs.python.org/3/library/math.html)
- [The Python Language Reference: Data model](https://docs.python.org/3/reference/datamodel.html)
