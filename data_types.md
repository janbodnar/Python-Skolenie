# Python data types

Computer programs, such as spreadsheets, text editors, calculators, or chat clients, work with data.  
Tools to work with various data types are an essential part of a modern computer language.

## Definition

A data type is a set of values and the allowable operations on those values.  
Python has a great set of useful data types. Python's data types are built   
into the core of the language. They are easy to use and straightforward.

Python data types include:

- Booleans
- Strings
- Numbers
- Tuples
- Lists
- Sets
- Dictionaries
- None

Here is a summary of Python data types in a markdown table:

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
| NoneType | NoneType | nulls | — | No |


## Booleans

In Python programming language, the Boolean datatype is a primitive datatype  
having one of two values: `True` or `False`. This is a fundamental data type.  
Booleans are a subclass of integers — `True` behaves like `1` and `False` like `0`  
in numeric contexts, though they have their own `bool` type.

Happy parents are expecting a child. They have chosen a name for each possibility.  
If it is a boy, they might name him John. If it is a girl,  
they might name her Victoria.

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

Here we use two functions. The `randint` function returns a random number from  
the given integer boundaries — in our case 0 or 1. The `bool` function converts  
the integers to boolean values.

```python
if male:
    print("We will use name John")
else:
    print("We will use name Victoria")
```

We print the name. The if keyword works with boolean values. If the male is `True`,  
we print the `"We will use name John"` to the console. If it has a `False` value, we print the other string.

### Boolean operators

Python provides three logical operators: `and`, `or`, and `not`. They operate on  
boolean expressions and return boolean results. The `and` operator evaluates to  
`True` only if both operands are true. The `or` operator evaluates to `True` if at  
least one operand is true. The `not` operator inverts the boolean value.

```python
#!/usr/bin/python

# bool_ops.py

x = 5
y = 10

print(x > 3 and y < 20)   # True
print(x > 3 and y < 5)    # False
print(x > 10 or y > 5)    # True
print(not x > 3)          # False
```

Short‑circuit evaluation is used: if the first operand determines the result, the  
second is not evaluated. For `and`, if the left side is `False`, the right side is  
ignored. For `or`, if the left side is `True`, the right side is skipped.

### Truthiness and falsiness

Many objects in Python can be tested for truth value even if they are not  
explicitly `bool`. Values that are considered `False` in a boolean context:

- `None`
- `False`
- zero of any numeric type: `0`, `0.0`, `0j`
- any empty sequence: `''`, `()`, `[]`
- any empty mapping: `{}`
- instances of user‑defined classes that define a `__bool__` or `__len__` method returning `False` or `0`

Everything else is considered `True`.

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

### Boolean in arithmetic

Because `bool` is a subclass of `int`, `True` equals `1` and `False` equals `0`.  
This allows booleans to be used directly in arithmetic operations.

```python
#!/usr/bin/python

# bool_int.py

print(True + True)          # 2
print(True + False)         # 1
print(False * 100)          # 0
print(3 * True - 2)         # 1
```

While possible, using booleans as numbers often reduces code clarity.  
Explicit conversions are preferred in most situations.

### Comparison operators

Comparison operators return boolean values. They include:

| Operator | Meaning                  |
|----------|--------------------------|
| `==`     | equal                    |
| `!=`     | not equal                |
| `<`      | less than                |
| `>`      | greater than             |
| `<=`     | less than or equal       |
| `>=`     | greater than or equal    |
| `is`     | object identity          |
| `is not` | negated object identity  |
| `in`     | membership               |
| `not in` | negated membership       |

```python
#!/usr/bin/python

# comparisons.py

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)      # True  (same content)
print(a is b)      # False (different objects)
print(2 in a)      # True
print(5 not in a)  # True
```

## Numbers

In Python programming language, we have integer numbers, floating point numbers, and complex numbers.  
If we work with integers, we deal with discrete entities. We would use integers to count apples.  

### Integers

Integers (`int`) represent whole numbers without a fractional part. They have  
arbitrary precision — Python automatically handles numbers as large as the  
available memory allows.

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

In this script, we count the total number of apples using multiplication.  

```
$ ./apples.py
There are total of 384 apples
```

#### Integer literals

You can write integers in several bases:

```python
decimal = 255         # decimal (base 10)
binary  = 0b11111111  # binary (base 2)
octal   = 0o377       # octal (base 8)
hexa    = 0xFF        # hexadecimal (base 16)

print(decimal, binary, octal, hexa)  # 255 255 255 255
```

Underscores can be used as visual separators in large numbers: `1_000_000` is the  
same as `1000000`.

#### Integer operations

Standard arithmetic operators work as expected:

```python
#!/usr/bin/python

# int_operations.py

x = 17
y = 5

print(x + y)         # addition: 22
print(x - y)         # subtraction: 12
print(x * y)         # multiplication: 85
print(x / y)         # true division (always returns float): 3.4
print(x // y)        # floor division (integer, rounded towards minus infinity): 3
print(x % y)         # modulo (remainder): 2
print(x ** y)        # exponentiation: 1419857
print(abs(-x))       # absolute value: 17
print(pow(x, y))     # equivalent to x ** y
print(divmod(x, y))  # returns (quotient, remainder) as tuple: (3, 2)
```

Bitwise operators are also available:

```python
a = 0b1100   # 12
b = 0b1010   # 10

print(bin(a & b))   # AND:      0b1000 (8)
print(bin(a | b))   # OR:       0b1110 (14)
print(bin(a ^ b))   # XOR:      0b0110 (6)
print(bin(~a))      # NOT:      -0b1101 (two's complement)
print(bin(a << 2))  # left shift:  0b110000 (48)
print(bin(a >> 2))  # right shift: 0b11 (3)
```

#### Type conversion and rounding

Integers can be constructed from other types with the `int()` function.  
Floats are truncated toward zero.

```python
print(int(9.99))        # 9
print(int(-3.7))        # -3
print(int("42"))        # 42
print(int("101", 2))    # 5 (binary string)
```

#### Very large integers

Python handles arbitrarily large integers seamlessly:

```python
big = 2**1000
print(big)
print(len(str(big)), "digits")
```

No overflow errors occur unless memory is exhausted.

### Floats

Floating-point numbers (`float`) represent real numbers using double-precision (64-bit)  
encoding as defined by the IEEE 754 standard. They can express very large (≈1.8×10³⁰⁸)  
and very small (≈2.2×10⁻³⁰⁸) values, but with finite precision — meaning not every decimal  
number can be stored exactly in binary. This is the fundamental trade-off that makes floats  
fast and memory-efficient while occasionally surprising in arithmetic comparisons.

Floating-point numbers are used whenever a value measures a continuous quantity — distance,  
temperature, speed, weight, or time. For example, if a sprinter runs 100 m in 9.87 s, we can  
compute their average speed in km/h:

```python
#!/usr/bin/python
# sprinter.py

# 100 m is 0.1 km
distance = 0.1
# 9.87 s converted to hours
time = 9.87 / 3600

speed = distance / time
print(f'The average speed of a sprinter is {speed} km/h')
```

```
$ ./sprinter.py
The average speed of a sprinter is 36.47416413373962 km/h
```

The result `36.47416413373962` is a float. To present it more cleanly, you can  
control decimal precision directly in the f-string without changing the stored value:

```python
print(f'The average speed of a sprinter is {speed:.2f} km/h')
# The average speed of a sprinter is 36.47 km/h
```

#### Scientific notation

Floats can be written using scientific notation with `e` or `E`, which is  
convenient for very large or very small values:

```python
tiny = 1.5e-3    # 0.0015
huge = 6.022E23  # Avogadro's number: 6.022e+23
print(tiny, huge)
```

Python also displays floats in scientific notation automatically when the value  
is extreme enough:

```python
print(1.5e-320)  # 1.5e-320
print(1.8e308)   # inf  (exceeds the max representable float)
```

#### Floating-point precision and `math.isclose`

Because floats are stored in binary, some decimal values cannot be represented  
exactly. The classic example is `0.1 + 0.2`:

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 == 0.3) # False
```

This is not a Python bug — it is an inherent property of IEEE 754 arithmetic.  
The workaround is to compare floats within a tolerance using `math.isclose`:

```python
import math

a = 0.1 + 0.2
b = 0.3

print(math.isclose(a, b, rel_tol=1e-9))           # True (relative tolerance)
print(math.isclose(a, b, abs_tol=1e-9))           # True (absolute tolerance)
```

`rel_tol` (default `1e-9`) scales the tolerance relative to the size of the  
numbers — useful for large values. `abs_tol` sets a fixed margin — better when  
comparing values near zero.

For financial or exact decimal arithmetic, use the `decimal` module instead, which avoids  
binary rounding entirely by passing values as strings:

```python
from decimal import Decimal

a = Decimal('0.1') + Decimal('0.2')
b = Decimal('0.3')

print(a)        # 0.3
print(a == b)   # True
```

Notice that strings are passed to `Decimal` rather than float literals. If you write  
`Decimal(0.1)`, Python first creates the imprecise float and then converts it, carrying  
the rounding error along:

```python
print(Decimal(0.1))   # 0.1000000000000000055511151231257827021181583404541015625
print(Decimal('0.1')) # 0.1
```


#### Rounding

The built-in `round()` function rounds a float to a given number of decimal places.  
If the second argument is omitted, it returns an `int`:

```python
pi = 3.1415926535

print(round(pi, 4))  # 3.1416
print(round(pi, 2))  # 3.14
print(round(pi))     # 3

print(round(2.5))    # 2  — banker's rounding: ties go to the nearest even number
print(round(3.5))    # 4
```

Banker's rounding (round half to even) is the IEEE 754 default and reduces cumulative  
bias in large datasets. If you need ceiling, floor, or truncation instead:

```python
import math

print(math.floor(3.9))   # 3  — always rounds down
print(math.ceil(3.1))    # 4  — always rounds up
print(math.trunc(-3.9))  # -3 — strips the decimal, toward zero
print(int(-3.9))         # -3 — same as trunc
```

#### Special floating-point values

The `float` type can represent three special values: `inf`, `-inf`, and `nan`.  
These arise from mathematical edge cases and overflow:

```python
import math

pos_inf = float('inf')
neg_inf = float('-inf')
nan     = float('nan')

print(1e309)              # inf  (overflow)
print(-1e309)             # -inf
print(1 / pos_inf)        # 0.0
print(pos_inf + 1)        # inf
print(pos_inf - pos_inf)  # nan

print(math.isinf(pos_inf))  # True
print(math.isnan(nan))      # True
```

`nan` is particularly unusual — it is not equal to anything, including itself:

```python
print(nan == nan)       # False
print(nan is nan)       # True  (same object, but value comparison always fails)
```

Always use `math.isnan()` to test for `nan` rather than `==`.

#### Type conversion

Floats can be created from integers, strings, booleans, or other numeric types:

```python
print(float(42))           # 42.0
print(float(True))         # 1.0
print(float("  -3.14\n")) # -3.14  (strips surrounding whitespace)
print(float("1e-4"))       # 0.0001
```

Passing a non-numeric string raises a `ValueError`:

```python
float("hello")  # ValueError: could not convert string to float: 'hello'
```

#### Implicit and explicit conversion with integers

When an integer and a float are used together in an expression, Python automatically   
promotes the integer to a float to avoid losing precision:

```python
result = 3 + 4.5   # 7.5 — result is a float
print(type(result)) # <class 'float'>
```

Going the other direction requires an explicit cast. Keep in mind that `int()` always  
truncates toward zero — it does not round:

```python
print(int(7.9))   #  7  — truncated, not rounded
print(int(-7.9))  # -7  — truncated toward zero, not -8
print(round(7.9)) #  8  — rounded
```

Use `round()` when you want true rounding, and `int()` only when truncation is intentional.

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

In our example, we assign three string literals to the variables `a`, `b`, and `c`.  
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

The carriage return `\r` is a control character that moves the cursor to the beginning of the current line.

```python
#!/usr/bin/python

# strophe.py

print("Incompatible, it don't matter though\n'cos someone's bound to hear my cry")
print("Speak out if you do\nYou're not easy to find")
```

The new line is a control character that begins a new line of text.  

```
$ ./strophe.py
Incompatible, it don't matter though
'cos someone's bound to hear my cry
Speak out if you do
You're not easy to find
```

Next, we examine the backspace control character.

```python
print("Python\b\b\booo") # prints Pytooo
```

The backspace control character `\b` moves the cursor one character back.  
In this case, we use three backspace characters to delete three letters  
and replace them with three `o` characters.

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

Tuples can contain several mixed data types.

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

In the first case we have an expression — we print the number 10 to the console.  
In the second case we have a tuple — we print a tuple containing the number 10.

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

The list is created using square brackets `[]`.

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
$ ./simple_list.py
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

The script counts the number of occurrences in a list.

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

In our example, we first create an empty names list. We use the `append` function  
to add new items to the list consecutively.  
The `insert` function inserts new elements at a given position — the existing elements  
are not deleted, they are shifted. The `remove` function removes a specific item  
from the list. To delete an item by its index, we use the `del` keyword.

```
$ ./list_modify.py
['Frank', 'Alexis', 'Erika', 'Ludmila']
['Adriana', 'Frank', 'Alexis', 'Erika', 'Ludmila']
['Adriana', 'Ludmila']
['Ludmila']
```

The following program presents two additional functions.

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
In the following example, we find the indexes of elements in a list.

```python
#!/usr/bin/python

# list_index.py

numbers = [0, 1, 2, 3, 3, 4, 5]

print(numbers.index(1))
print(numbers.index(3))
```

To find an index in a list, we use the `index` method. If there are multiple occurrences  
of an element, the method returns the index of the first one.

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

We can use the `tuple` function to create a tuple from a list and the `list` function to create  
a list from a tuple. Note that the original objects are not modified —  
the functions only return the transformed collections.

```
$ ./list_transform.py
(1, 2, 3)
[4, 5, 6]
[1, 2, 3]
(4, 5, 6)
```

## Sets

A *set* is an unordered collection of data with no duplicate elements. A set supports  
operations like union, intersection, or difference — similar to those in mathematics.

### Creating sets

Sets can be created using curly braces `{}` or the `set()` constructor. 

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

In this example, we have two sets created with curly brace syntax.  
The intersection operation returns elements that are both in set1 and set2.  
The union operation returns all elements from both sets. The difference returns elements  
that are in set1 but not in set2. Finally, the symmetric difference returns elements  
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
The `clear` method removes all items from the set. A set is a superset of another if it contains  
every element of the other set. A set is a subset of another if all its elements are contained in the other set.

```
$ ./sets2.py
{1, 2, 3, 4}
{1, 2, 3, 4, 6, 7}
Is set1 subset of set2 ? : True
Is set1 superset of set2 ? : False
set()
```

If we need an immutable set, we can create a `frozenset` with the `frozenset()` function.

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
keys and values of the dictionary. The `items` method returns a list of the dictionary's (key, value) pairs as tuples.

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

Looping  

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

There is another special data type — `None`. This data type represents a nonexistent, unknown, or empty value.  
It is the sole value of the `NoneType` class. `None` is a built‑in constant that represents the  
absence of a value, a null, or a placeholder.  

`None` is falsy — when used in a boolean context, it evaluates to `False`. However, it is  
distinct from other falsy values like `0`, `False`, `""`, or empty collections.

### Functions without a return value

If a function does not end with an explicit `return` statement, it returns `None` automatically.

```python
#!/usr/bin/python

# none.py

def function():
    pass

print(function())    # None
```

In our example, we define a function. The function does nothing. It does not explicitly  
return any value. Such a function will implicitly return `None`.  

### Uses of `None`

`None` is commonly used to:

- initialize variables that will later hold a meaningful value
- serve as a default argument for function parameters (but see the note on mutable defaults below)
- indicate that a search or lookup operation found nothing
- mark the absence of a result

```python
#!/usr/bin/python

# none_initialization.py

data = None

# ... later in the code ...
if some_condition:
    data = [1, 2, 3]

if data is None:
    print("Data not yet available")
else:
    print("Data is ready")
```

### Testing for `None` – the identity operator

Because `None` is a singleton (there is only ever one instance of `NoneType`), the correct way  
to check for it is by identity using the `is` operator, not by equality with `==`.

```python
x = None

# Recommended way
if x is None:
    print("x is None")

# Works, but less precise (and can be overridden if == is overloaded)
if x == None:
    print("x equals None")
```

The same `is` operator is used for checking non‑null: `if x is not None:`.

### Difference from other falsy values

Even though `None` is falsy, it is not the same as `0`, `False`, or an empty string.  
You should check for `None` explicitly when the absence of a value has a special meaning.

```python
value = 0

if value is None:
    print("No value")
else:
    print("value is zero")   # This will be printed, correctly distinguishing 0 from None
```

### Methods that return `None`

Many Python methods that modify an object in place return `None` (rather than the modified object).  
This is an important pattern — do not chain these methods thinking they return the original object.

```python
names = ["Alice", "Bob", "Charlie"]

result = names.append("David")
print(result)        # None
print(names)         # ['Alice', 'Bob', 'Charlie', 'David']

# A common mistake:
# names = names.append("Eve")  # This would set names to None!
```

Other methods like `sort()`, `reverse()`, and `extend()` also return `None`.

### `None` as default argument – careful with mutables

Using `None` as a default value for mutable parameters (like lists or dictionaries)  
is a common idiom  to avoid unwanted sharing across function calls.

Default arguments are part of the function object, not re‑evaluated each call.
This makes them: a) faster, b) predictable, c) consistent with how Python treats objects.
But it also means you must avoid mutable defaults unless you want shared state.

```python
def append_safely(item, lst=None):
    if lst is None:
        lst = []    # fresh list per call
    lst.append(item)
    return lst

print(append_safely(1))          # [1]
print(append_safely(2))          # [2]  (not [1, 2])

# WRONG: using a mutable default value
def append_unsafely(item, lst=[]):
    lst.append(item)
    return lst

data = [-1, 0]

print(append_unsafely(1, data))       # [-1, 0, 1, 1]  (data is modified)
print(append_unsafely(2, data))       # [-1, 0, 1, 1, 2]  (data is modified again)
print(append_unsafely(3))             # [3]  (unexpectedly, the default list is modified)
print(append_unsafely(4))             # [3, 4]  (unexpectedly, the default list is modified again)
```

Without the `None` sentinel, using `target_list=[]` would reuse the same list object across  
multiple calls, causing the list to accumulate items unexpectedly.

### `None` in data structures

`None` can be stored inside lists, dictionaries, or tuples to signal missing or optional data.

```python
user_info = {
    "name": "John",
    "email": None,          # email not provided
    "age": 30
}

for key, val in user_info.items():
    if val is None:
        print(f"{key}: not set")
    else:
        print(f"{key}: {val}")
```

### Comparison with `null` in other languages

`None` in Python is similar to `null` in Java or JavaScript, but it is a true object with a type.  
Python’s `None` cannot be accidentally used as a number (as `null` might in some languages) because  
Python is strongly typed and operations like `None + 1` will raise a `TypeError`.

```python
try:
    result = None + 1
except TypeError as e:
    print(e)   # unsupported operand type(s) for +: 'NoneType' and 'int'
```

### Checking for `None` in expressions

You can use the ternary operator to provide a fallback value when something might be `None`:

```python
name = None
display_name = name or "Guest"
print(display_name)   # Guest
```

However, this trick also catches other falsy values like empty strings.  
A more precise approach uses `if`/`else` or the `a if a is not None else b` pattern:

```python
name = ""
display_name = name if name is not None else "Guest"
print(display_name)   # (prints empty string, not "Guest")
```

### `None` is a singleton – implications

`None` is always the same object in memory, regardless of where it is referenced.

```python
a = None
b = None
print(a is b)   # True
print(id(a) == id(b))  # True
```

This is why the `is` test is both correct and efficient.

The section now provides a thorough understanding of `None`, its behaviour, and common usage patterns.
