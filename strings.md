# Strings in Python

A **string** in Python is a sequence of characters. Strings are **immutable**—once defined,  
they cannot be changed. Many Python methods like `replace()`, `join()`, or `split()` appear  
to modify strings, but they actually create a new copy of the string, modify it, and return  
the modified copy to the caller.

---

## String Literals

Python strings can be created using **single quotes**, **double quotes**, or **triple quotes**.  
Triple quotes allow strings to span multiple lines without using escape characters.

```python
# string_literals.py

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

**Output:**

```
proximity alert
evacuation

requiem
for
a
tower
```

## Unicode in Python

In Python 3, **all strings are Unicode** by default. The `u'...'` prefix is optional and exists  
only for backward compatibility with Python 2. You can include Unicode characters directly in source code.

```python
# unicode.py

# Using Unicode escape sequences
text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

print(text)
```

**Output:**

```
Лев Николаевич Толстой:
Анна Каренина
```

You can also use Unicode characters directly in your source code:

```python
# unicode2.py

text = 'Лев Николаевич Толстой: Анна Каренина'
print(text)
```

**Note:** Python 3 assumes UTF-8 encoding by default, so no special encoding comment is needed.

---

## String Formatting

Python provides several ways to format strings. Here are the three main approaches:

```python
name = 'Peter'
age = 23

# Old-style % formatting
print('%s is %d years old' % (name, age))

# str.format() method (Python 3.0+)
print('{} is {} years old'.format(name, age))

# f-strings (Python 3.6+)
print(f'{name} is {age} years old')
```

**Output:**

```
Peter is 23 years old
Peter is 23 years old
Peter is 23 years old
```

**Formatting Options:**

| Method | Example | When to Use |
|--------|---------|-------------|
| `%`-formatting | `"%s is %d" % (name, age)` | Legacy code |
| `.format()` | `"{} is {}".format(name, age)` | Python 3.0–3.5 |
| f-strings | `f"{name} is {age}"` | Python 3.6+ (recommended) |

---

## Using Quotes Inside Strings

When you need to include quotes within a string, you have two options:

1. **Escape the quotes** with a backslash (`\`)
2. **Mix single and double quotes**

```python
# quotes.py

# Escaping quotes
print("He said, \"Which one is your favourite?\"")

# Mixing quote types
print('He said, "Which one is your favourite?"')

# Using single quotes inside double quotes (no escape needed)
print("Johnie's dog")

# Escaping single quotes
print('Johnie\'s dog')
```

**Output:**

```
He said, "Which one is your favourite?"
He said, "Which one is your favourite?"
Johnie's dog
Johnie's dog
```

---

## String Length

The `len()` function returns the number of characters in a string, including whitespace characters.

```python
# string_length.py

s1 = "Eagle"
s2 = "Eagle\n"    # Includes newline character
s3 = "Eagle  "    # Includes two spaces

print(len(s1))    # 5
print(len(s2))    # 6 (newline counts)
print(len(s3))    # 7 (spaces count)
```

**Output:**

```
5
6
7
```

---

## Stripping Whitespace Characters

The `strip()`, `lstrip()`, and `rstrip()` methods remove leading and/or trailing whitespace  
characters (spaces, tabs, newlines, etc.).

```python
# stripping.py

s = " Eagle  "

s2 = s.rstrip()   # Remove trailing spaces
s3 = s.lstrip()   # Remove leading spaces
s4 = s.strip()    # Remove both

print(f"'{s}' length: {len(s)}")     # ' Eagle  ' length: 8
print(f"'{s2}' length: {len(s2)}")   # ' Eagle' length: 6
print(f"'{s3}' length: {len(s3)}")   # 'Eagle  ' length: 7
print(f"'{s4}' length: {len(s4)}")   # 'Eagle' length: 5
```

**Output:**

```
' Eagle  ' length: 8
' Eagle' length: 6
'Eagle  ' length: 7
'Eagle' length: 5
```

---

## Escape Sequences

Escape sequences are special characters that begin with a backslash (`\`) and serve specific purposes within strings.

| Escape Sequence | Description |
|-----------------|-------------|
| `\n` | Newline |
| `\t` | Tab |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

```python
# strophe.py

print("Incompatible, it don't matter though\n'cos someone's bound to hear my cry")
print("Speak out if you do\nYou're not easy to find")
```

**Output:**

```
Incompatible, it don't matter though
'cos someone's bound to hear my cry
Speak out if you do
You're not easy to find
```

### The Backspace Control Character

```python
print("Python\b\b\booo")  # Output: Pytooo
```

The backspace control character `\b` moves the cursor one character back. In this case, we use three  
backspace characters to delete three letters and replace them with three 'o' characters.

### The Tab Character

```python
print("Towering\tinferno")  # Output: Towering        inferno
```

The horizontal tab inserts space between text.

### Raw Strings

If you prepend an `r` to the string, you get a **raw string** where escape sequences are not interpreted:

```python
# raw.py

print(r"Another world\n")
```

**Output:**

```
Another world\n
```

With a raw string, `\n` is treated as literal backslash and 'n' characters, not as a newline.  
Raw strings are useful for file paths and regular expressions.

---

## Comparing Strings

Use the `==` operator for equality and `!=` for inequality. These operators return boolean  
values (`True` or `False`).

```python
# comparing.py

print("12" == "12")      # True
print("17" == "9")       # False
print("aa" == "ab")      # False

print("abc" != "bce")    # True
print("efg" != "efg")    # False
```

**Output:**

```
True
False
False
True
False
```

**Lexicographic Comparison:**

Strings can also be compared using `<`, `>`, `<=`, `>=`, which compare character by character  
based on Unicode code points.

```python
print("apple" < "banana")   # True (a < b)
print("Apple" < "apple")    # True (A < a in Unicode)
```

---

## Accessing String Elements

Strings support indexing to access individual characters and slicing to access substrings.

```python
# string_elements.py

s = "Eagle"

# Positive indexing (0-based)
print(s[0])    # E (first character)
print(s[4])    # e (fifth character)

# Negative indexing (from end)
print(s[-1])   # e (last character)
print(s[-2])   # l (second from last)

# Slicing [start:end] (end is exclusive)
print(s[0:4])  # Eagl (characters 0-3)
print(s[1:3])  # ag (characters 1-2)
print(s[:])    # Eagle (full string)
print(s[::2])  # Egl (every second character)
```

**Output:**

```
E
e
e
l
Eagl
ag
Eagle
```

### Iterating Through a String

```python
# traverse.py

s = "ZetCode"

for char in s:
    print(char, end=" ")  # Note: This produces a space after each character
```

**Output:**

```
Z e t C o d e
```

---

## Basic String Operations

### Multiplication and Concatenation

```python
# add_multiply.py

# String repetition
print("eagle " * 5)

# Automatic concatenation of adjacent literals
print("eagle " "falcon")

# Explicit concatenation with +
print("eagle " + "and " + "falcon")
```

**Output:**

```
eagle eagle eagle eagle eagle
eagle falcon
eagle and falcon
```

### String Length

```python
# eagle.py

word = 'eagle'
print(f"{word} has {len(word)} characters")  # eagle has 5 characters
```

### Type Conversion

Python does not implicitly convert between strings and numbers. You must use explicit conversion:

```python
# string_number.py

# String to integer
print(int("12") + 12)                    # 24

# Integer to string
print("There are " + str(22) + " oranges.")  # There are 22 oranges.

# String to float
print(float("22.33") + 22.55)            # 44.88
```

**Output:**

```
24
There are 22 oranges.
44.88
```

---

## Replacing Substrings

The `replace()` method replaces occurrences of a substring within a string. Since strings  
are immutable, it returns a new string.

```python
# replacing.py

a = "I saw a wolf in the forest. A lonely wolf."

# Replace all occurrences
b = a.replace("wolf", "fox")
print(b)  # I saw a fox in the forest. A lonely fox.

# Replace only the first occurrence (count parameter)
c = a.replace("wolf", "fox", 1)
print(c)  # I saw a fox in the forest. A lonely wolf.
```

**Syntax:** `replace(old, new[, count])`

---

## Splitting and Joining Strings

### Splitting with `split()` and `rsplit()`

The `split()` method divides a string into a list using a separator. `rsplit()`  
does the same but from the right.

```python
# splitting.py

nums = "1,5,6,8,2,3,1,9"

# Split all
print(nums.split(","))        # ['1', '5', '6', '8', '2', '3', '1', '9']

# Split with max splits
print(nums.split(",", 5))     # ['1', '5', '6', '8', '2', '3,1,9']

# Split from the right
print(nums.rsplit(",", 3))    # ['1,5,6,8,2', '3', '1', '9']
```

### Joining with `join()`

The `join()` method concatenates strings from an iterable with the separator string.

```python
# split_join.py

nums = "1,5,6,8,2,3,1,9"
parts = nums.split(",")       # ['1', '5', '6', '8', '2', '3', '1', '9']

joined = ':'.join(parts)      # 1:5:6:8:2:3:1:9
print(joined)
```

### The `partition()` Method

The `partition()` method splits a string at the first occurrence of a separator and  
returns a tuple of three parts: before, separator, and after.

```python
# partition.py

s = "1 + 2 + 3 = 6"
result = s.partition("=")
print(result)  # ('1 + 2 + 3 ', '=', ' 6')
```

---

## String Case Conversion

Python provides several methods to convert string case:

| Method | Description |
|--------|-------------|
| `.upper()` | Converts all characters to uppercase |
| `.lower()` | Converts all characters to lowercase |
| `.swapcase()` | Swaps case (upper ↔ lower) |
| `.title()` | Capitalizes first letter of each word |
| `.capitalize()` | Capitalizes first letter only |

```python
# convert_case.py

a = "ZetCode"

print(a.upper())      # ZETCODE
print(a.lower())      # zetcode
print(a.swapcase())   # zETcODE
print(a.title())      # Zetcode

# Additional examples
text = "hello world"
print(text.capitalize())  # Hello world
```

---

## String Testing Methods

Several methods check character properties:

| Method | Description |
|--------|-------------|
| `.isalpha()` | All characters are alphabetic |
| `.isdigit()` | All characters are digits |
| `.isspace()` | All characters are whitespace |
| `.isalnum()` | All characters are alphanumeric |
| `.isupper()` | All characters are uppercase |
| `.islower()` | All characters are lowercase |

```python
# letters.py

sentence = "There are 22 apples"

alphas = sum(1 for c in sentence if c.isalpha())
digits = sum(1 for c in sentence if c.isdigit())
spaces = sum(1 for c in sentence if c.isspace())

print(f"Total characters: {len(sentence)}")
print(f"Alphabetic: {alphas}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
```

**Output:**

```
Total characters: 19
Alphabetic: 14
Digits: 2
Spaces: 3
```

---

## String Justification

The `ljust()`, `rjust()`, and `center()` methods align strings within a specified width.

| Method | Description |
|--------|-------------|
| `.ljust(width)` | Left-justifies the string |
| `.rjust(width)` | Right-justifies the string |
| `.center(width)` | Centers the string |

```python
# teams1.py

print("Ajax Amsterdam" " - " "Inter Milano " "2:3")
print("Real Madrid" " - " "AC Milano " "3:3")
print("Dortmund" " - " "Sparta Praha " "2:1")
```

**Output:**

```
Ajax Amsterdam - Inter Milano 2:3
Real Madrid - AC Milano 3:3
Dortmund - Sparta Praha 2:1
```

### Improving Output with Justification

```python
# teams2.py

teams = {
    0: ("Ajax Amsterdam", "Inter Milano"),
    1: ("Real Madrid", "AC Milano"),
    2: ("Dortmund", "Sparta Praha")
}

results = ("2:3", "3:3", "2:1")

for i in teams:
    line = (teams[i][0].ljust(16) +
            "-".ljust(5) +
            teams[i][1].ljust(16) +
            results[i].ljust(3))
    print(line)
```

**Output:**

```
Ajax Amsterdam  -    Inter Milano    2:3
Real Madrid     -    AC Milano       3:3
Dortmund        -    Sparta Praha    2:1
```

---

## Advanced String Formatting

### Basic Formatting with `%`

```python
# oranges.py

print('There are %d oranges in the basket' % 32)
print('There are {0} oranges in the basket'.format(32))
```

**Output:**

```
There are 32 oranges in the basket
There are 32 oranges in the basket
```

### Multiple Values

```python
# fruits.py

print('There are %d oranges and %d apples in the basket' % (12, 23))
print('There are {0} oranges and {1} apples in the basket'.format(12, 23))
```

**Output:**

```
There are 12 oranges and 23 apples in the basket
There are 12 oranges and 23 apples in the basket
```

### Formatting Different Types

```python
# height.py

print('Height: %f %s' % (172.3, 'cm'))
print('Height: {0:f} {1:s}'.format(172.3, 'cm'))
```

**Output:**

```
Height: 172.300000 cm
Height: 172.300000 cm
```

### Controlling Decimal Places

```python
# height2.py

height = 172.3

# Old-style
print("Height: %.2f cm" % height)  # Height: 172.30 cm

# str.format()
print("Height: {:.2f} cm".format(height))  # Height: 172.30 cm

# f-string
print(f"Height: {height:.2f} cm")  # Height: 172.30 cm
```

**Output:**

```
Height: 172.30 cm
Height: 172.30 cm
Height: 172.30 cm
```

### Numeric Formatting

```python
# various.py

# Hexadecimal
print("%x" % 300)      # 12c
print("%#x" % 300)     # 0x12c (adds 0x prefix)

# Octal
print("%o" % 300)      # 454

# Scientific notation
print("%e" % 300000)   # 3.000000e+05
```

**Output:**

```
12c
0x12c
454
3.000000e+05
```

### Binary and Other Formats with `.format()`

```python
# various2.py

# Hexadecimal
print("{:x}".format(300))      # 12c
print("{:#x}".format(300))     # 0x12c

# Binary
print("{:b}".format(300))      # 100101100

# Octal
print("{:o}".format(300))      # 454

# Scientific
print("{:e}".format(300000))   # 3.000000e+05
```

**Output:**

```
12c
0x12c
100101100
454
3.000000e+05
```

### Column Formatting with Width Specifiers

The width specifier defines the minimal width of the object. If the object is  
smaller than the width, it is filled with spaces.

```python
# columns2.py

for x in range(1, 11):
    print('%2d %3d %4d' % (x, x*x, x*x*x))
```

**Output:**

```
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Using `.format()`:

```python
# columns3.py

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
```

**Output:**

```
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

---

## Finding Substrings

Python provides four methods for finding substrings:

| Method | Search Direction | Return on Not Found |
|--------|-----------------|---------------------|
| `.find(sub[, start[, end]])` | Beginning to end | Returns `-1` |
| `.rfind(sub[, start[, end]])` | End to beginning | Returns `-1` |
| `.index(sub[, start[, end]])` | Beginning to end | Raises `ValueError` |
| `.rindex(sub[, start[, end]])` | End to beginning | Raises `ValueError` |

**Note:** The `start` and `end` parameters are positional, not keyword arguments.  
Use `a.find("wolf", 10, 20)` rather than `a.find("wolf", start=10, end=20)`.

### Using `find()` and `rfind()`

```python
# substrings.py

a = "I saw a wolf in the forest. A lone wolf."

print(a.find("wolf"))          # 8 (first occurrence)
print(a.find("wolf", 10, 20))  # -1 (not found in range)
print(a.find("wolf", 15))      # 35 (second occurrence)
print(a.rfind("wolf"))         # 35 (search from end)
```

**Output:**

```
8
-1
35
35
```

### Using `index()` and `rindex()`

```python
# substrings2.py

a = "I saw a wolf in the forest. A lone wolf."

try:
    print(a.index("wolf"))   # 8
    print(a.rindex("wolf"))  # 35
    print(a.rindex("fox"))   # Raises ValueError
except ValueError as e:
    print("Could not find substring")
```

**Output:**

```
8
35
Could not find substring
```

### Checking for Substrings with `in` and `not in`

```python
text = "Hello, world!"

print("world" in text)      # True
print("Python" in text)     # False
print("world" not in text)  # False
```

---

## Common String Methods Summary

| Method | Description | Example |
|--------|-------------|---------|
| `len(s)` | Returns string length | `len("Hello")` → `5` |
| `s.upper()` | Converts to uppercase | `"hi".upper()` → `"HI"` |
| `s.lower()` | Converts to lowercase | `"HI".lower()` → `"hi"` |
| `s.strip()` | Removes leading/trailing whitespace | `" hi ".strip()` → `"hi"` |
| `s.replace(old, new[, count])` | Replaces substrings | `"hi".replace("i","ello")` → `"hello"` |
| `s.split(sep[, maxsplit])` | Splits into list | `"a,b".split(",")` → `["a","b"]` |
| `sep.join(list)` | Joins list elements | `",".join(["a","b"])` → `"a,b"` |
| `s.startswith(prefix)` | Checks prefix | `"Hello".startswith("He")` → `True` |
| `s.endswith(suffix)` | Checks suffix | `"Hello".endswith("lo")` → `True` |
| `s.find(sub[, start[, end]])` | Finds substring index | `"Hi".find("i")` → `1` |
| `s.count(sub)` | Counts occurrences | `"aaa".count("a")` → `3` |

---

## Best Practices

1. **Use f-strings** for readability in modern code (Python 3.6+)
2. **Prefer `with` statements** for file I/O (automatic resource cleanup)
3. **Use raw strings (`r"..."`)** for file paths and regex patterns
4. **Check for substrings with `in`** instead of `find()` for simple checks
5. **Use `.strip()`** to clean user input
6. **Prefer `join()` over `+`** for concatenating many strings (performance)


## Additional Resources

- [Python String Documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [PEP 498 – Literal String Interpolation (f-strings)](https://www.python.org/dev/peps/pep-0498/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)


*Strings are fundamental to Python programming. Mastering string operations enables efficient text processing, 
data parsing, and user interaction in any Python application.*
