# Python f-strings

An **f-string** (formatted string literal) is a string that can contain values  
of variables and expressions. You write it with the `f` prefix before the  
opening quote and put the expressions inside curly braces `{}`. When the line  
runs, Python evaluates each expression and inserts its value into the text.

f-strings were introduced in Python 3.6. They are the most readable and usually  
the fastest way to build text from values, and they are the recommended choice  
for new code.

## Three ways to format strings

Python offers three ways to insert values into a string. All three lines in the  
following example print the same text:

```python
name = "Peter"
age = 23

print("%s is %d years old" % (name, age))
print("{} is {} years old".format(name, age))
print(f"{name} is {age} years old")
```

```text
$ python formatting.py
Peter is 23 years old
Peter is 23 years old
Peter is 23 years old
```

- The `%` operator is the oldest method, inspired by the `printf()` function in  
  C. Placeholders such as `%s` (string) and `%d` (integer) are replaced by the  
  values in the tuple.
- The `str.format()` method was added in Python 3.0 and 2.6. It uses the same  
  format specifiers as f-strings, but the values are passed as arguments, away  
  from the place where they appear.
- f-strings, added in Python 3.6, put the expressions directly in the text,  
  which makes the code shorter and easier to read.

`str.format()` is still useful when the template is not known in advance, for  
example, when it is loaded from a file or a translation. An f-string is  
evaluated immediately where it is written, so it cannot serve as a reusable  
template.

You will meet the two older methods in existing code, so you should be able to  
read them. In new code, prefer f-strings. The rest of this chapter covers them  
in detail.

## The first f-string

```python
name = "John Doe"
age = 34

print(f"{name} is {age} years old")
```

```text
$ python first.py
John Doe is 34 years old
```

The `{name}` and `{age}` placeholders are replaced with the values of the  
variables. The number `34` is converted to text automatically, so you do not  
need to call `str()`.

Without the `f` prefix, the braces are ordinary characters:

```python
name = "John Doe"

print("Hello, {name}")
print(f"Hello, {name}")
```

```text
$ python no_prefix.py
Hello, {name}
Hello, John Doe
```

Forgetting the `f` is one of the most common beginner mistakes. Python does not  
report an error; it simply prints the braces.

## Expressions

The braces can contain any expression, not only a variable name. For example,  
you can do a calculation:

```python
bags = 3
apples_in_bag = 12

print(f"There are {bags * apples_in_bag} apples in total")
```

```text
$ python expressions.py
There are 36 apples in total
```

## Calling functions and methods

An expression inside the braces can also call a function or a method:

```python
name = "john doe"
numbers = [4, 9, 2, 7]

print(f"Name: {name.title()}")
print(f"Largest number: {max(numbers)}")
print(f"Number of items: {len(numbers)}")
```

```text
$ python functions.py
Name: John Doe
Largest number: 9
Number of items: 4
```

## Dictionaries and quotes

When you read a value from a dictionary, the key is a string, so the f-string  
contains quotes inside quotes. The simplest solution is to use the other type of  
quotes for the key:

```python
user = {"name": "John Doe", "occupation": "gardener"}

print(f"{user['name']} is a {user['occupation']}")
```

```text
$ python dicts.py
John Doe is a gardener
```

Since Python 3.12, you can also reuse the same type of quotes, as in  
`f"{user["name"]}"`. In older versions, this is a syntax error, so the first  
form is the safer choice.

## Multiline f-strings

The `f` prefix also works with triple-quoted strings that span several lines:

```python
name = "John Doe"
age = 34
occupation = "gardener"

msg = f"""name: {name}
age: {age}
occupation: {occupation}"""

print(msg)
```

```text
$ python multiline.py
name: John Doe
age: 34
occupation: gardener
```

## Printing curly braces

Because braces mark expressions, a literal brace must be doubled: `{{` produces  
`{` and `}}` produces `}`.

```python
name = "John"

print(f"Python uses {{}} to evaluate expressions in f-strings")
print(f"{{name}} prints the text, {name} prints the value")
```

```text
$ python braces.py
Python uses {} to evaluate expressions in f-strings
{name} prints the text, John prints the value
```

To put a quote character in the text, use the other type of quotes for the whole  
string, or escape the quote with a backslash:

```python
film = "Casablanca"

print(f"{film} was a 'great' film")
print(f'{film} was a \'great\' film')
```

```text
$ python quotes.py
Casablanca was a 'great' film
Casablanca was a 'great' film
```

## Format specifiers

So far, values have been inserted as they are. A **format specifier** controls  
how a value looks: the number of decimal places, the width, the alignment, and  
more. The specifier follows a colon inside the braces:

```text
{expression:format_specifier}
```

### Decimal places

The `f` type displays a number as a decimal number with a fixed number of  
decimal places. The number after the dot is the **precision**:

```python
price = 12.3456

print(f"{price}")
print(f"{price:.2f}")
print(f"{price:.0f}")
print(f"Total: {price * 3:.2f} EUR")
```

```text
$ python floats.py
12.3456
12.35
12
Total: 37.04 EUR
```

The value is rounded, not cut off. The variable itself does not change; only its  
text representation does.

### Percentages

The `%` type multiplies the value by 100 and adds a percent sign:

```python
passed = 17
total = 20
ratio = passed / total

print(f"{ratio}")
print(f"{ratio:.0%}")
print(f"{1 / 7:.2%}")
```

```text
$ python percentage.py
0.85
85%
14.29%
```

### Thousands separators

A comma or an underscore groups digits of large numbers by thousands:

```python
population = 5_400_000
budget = 1234567.891

print(f"{population}")
print(f"{population:,}")
print(f"{population:_}")
print(f"{budget:,.2f}")
```

```text
$ python thousands.py
5400000
5,400,000
5_400_000
1,234,567.89
```

The last line combines the thousands separator with two decimal places.

### Width

A number in the specifier sets the minimum **width** of the result in  
characters. Shorter values are padded with spaces; longer values are never cut.  
A leading `0` pads numbers with zeros instead:

```python
for x in range(1, 11):
    print(f"{x:02} {x * x:3} {x * x * x:4}")
```

```text
$ python width.py
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

The example prints three columns with widths of 2, 3, and 4 characters. The  
first column is padded with zeros.

### Alignment and fill characters

By default, strings are aligned to the left and numbers to the right. The `<`,  
`>`, and `^` characters align a value to the left, to the right, or to the  
center:

```python
words = ["sky", "fork", "small"]

for word in words:
    print(f"|{word:<10}|{word:^10}|{word:>10}|")
```

```text
$ python align.py
|sky       |   sky    |       sky|
|fork      |   fork   |      fork|
|small     |  small   |     small|
```

Each column is ten characters wide. A **fill character** placed before the  
alignment character replaces the default spaces:

```python
title = "Menu"

print(f"{title:*^20}")
print(f"{'Soup':.<15}{3.5:>5.2f}")
print(f"{'Steak':.<15}{14.9:>5.2f}")
```

```text
$ python fill.py
********Menu********
Soup........... 3.50
Steak..........14.90
```

Alignment and width are useful for printing simple tables:

```python
items = [("Apples", 3, 0.45), ("Bread", 1, 1.99), ("Milk", 2, 1.15)]

print(f"{'Item':<10}{'Qty':>5}{'Price':>8}")

for name, qty, price in items:
    print(f"{name:<10}{qty:>5}{price:>8.2f}")
```

```text
$ python table.py
Item        Qty   Price
Apples        3    0.45
Bread         1    1.99
Milk          2    1.15
```

Each item in the list holds a name, a quantity, and a price. The `for` loop  
takes them out into the `name`, `qty`, and `price` variables. The header and  
the rows use the same widths, so the columns line up.

### Number systems

The `b`, `o`, `x`, and `X` types display an integer in binary, octal, or  
hexadecimal. The `#` option adds the usual prefix, such as `0x`. The `e` type  
uses scientific notation:

```python
val = 300

print(f"{val:b}")       # binary
print(f"{val:o}")       # octal
print(f"{val:x}")       # hexadecimal, lowercase
print(f"{val:X}")       # hexadecimal, uppercase
print(f"{val:#x}")      # hexadecimal with the 0x prefix
print(f"{val:e}")       # scientific notation
```

```text
$ python notations.py
100101100
454
12c
12C
0x12c
3.000000e+02
```

### Dates and times

Dates and times use their own format codes, the same as the `strftime()` method.  
For example, `%Y` is the year, `%m` the month, and `%d` the day:

```python
from datetime import datetime

meeting = datetime(2026, 3, 24, 15, 12)

print(f"{meeting:%Y-%m-%d %H:%M}")
print(f"{meeting:%d.%m.%Y}")
print(f"{meeting:%A, %B %d}")
```

```text
$ python dates.py
2026-03-24 15:12
24.03.2026
Tuesday, March 24
```

For the current date and time, use `datetime.now()` instead of a fixed date.

### Overview of format specifiers

| Specifier | Meaning | Example | Result |
| --- | --- | --- | --- |
| `.2f` | Two decimal places | `f"{3.14159:.2f}"` | `3.14` |
| `.1%` | Percentage | `f"{0.256:.1%}"` | `25.6%` |
| `,` | Thousands separator | `f"{1234567:,}"` | `1,234,567` |
| `5` | Minimum width | `f"\|{42:5}\|"` | `\|   42\|` |
| `05` | Width, padded with zeros | `f"{42:05}"` | `00042` |
| `<` `^` `>` | Left, center, right alignment | `f"\|{'ab':^6}\|"` | `\|  ab  \|` |
| `*^6` | Fill character and alignment | `f"{'ab':*^6}"` | `**ab**` |
| `+` | Always show the sign | `f"{42:+}"` | `+42` |
| `b` `o` `x` | Binary, octal, hexadecimal | `f"{255:x}"` | `ff` |
| `e` | Scientific notation | `f"{1500:e}"` | `1.500000e+03` |

The parts of a specifier are written in a fixed order: fill and alignment, sign,  
width, thousands separator, precision, and type. For example, `*>12,.2f` means:  
fill with `*`, align to the right, width 12, thousands separator, two decimal  
places, decimal notation.

```python
amount = 1234.5

print(f"{amount:*>12,.2f}")
```

```text
$ python combined.py
****1,234.50
```

## Variable format specifiers

A format specifier can itself contain expressions in braces. This lets you  
choose the width or the precision while the program runs:

```python
value = 3.14159265

for precision in range(1, 5):
    print(f"{value:.{precision}f}")

width = 12
print(f"|{'Python':^{width}}|")
```

```text
$ python nested.py
3.1
3.14
3.142
3.1416
|   Python   |
```

## Debugging with `=`

Adding `=` after an expression prints both the expression and its value. This is  
handy for quick debugging. The feature is available since Python 3.8.

```python
x = 10
y = 3

print(f"{x = }, {y = }")
print(f"{x / y = }")
print(f"{x / y = :.2f}")
```

```text
$ python debug.py
x = 10, y = 3
x / y = 3.3333333333333335
x / y = 3.33
```

The last line shows that `=` can be combined with a format specifier.

## Objects in f-strings

When an f-string inserts an object, it uses the object's string representation,  
the same text that `str()` returns. For your own classes, you define this text  
with the `__str__` method:

```python
class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __str__(self):
        return f"{self.name} is a {self.occupation}"


user = User("John Doe", "gardener")

print(f"{user}")
```

```text
$ python objects.py
John Doe is a gardener
```

The `!r` conversion uses `repr()` instead of `str()`. For strings, `repr()` adds  
quotes, which makes it easy to see empty strings or extra spaces:

```python
name = "  John "

print(f"[{name}]")
print(f"[{name!r}]")
```

```text
$ python conversion.py
[  John ]
['  John ']
```

## The `__format__` method

The format specifier is passed to the object's `__format__` method. By defining  
this method, a class can support its own format specifiers. In the following  
example, a temperature can be displayed in degrees Celsius with `c` or in  
degrees Fahrenheit with `f`:

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __format__(self, spec):
        if spec == "f":
            return f"{self.celsius * 9 / 5 + 32:.1f} °F"
        return f"{self.celsius:.1f} °C"


temp = Temperature(21.5)

print(f"{temp}")
print(f"{temp:c}")
print(f"{temp:f}")
```

```text
$ python custom_format.py
21.5 °C
21.5 °C
70.7 °F
```

When the braces contain no specifier, `__format__` receives an empty string, and  
the example falls back to degrees Celsius.

## Summary

| Feature | Example |
| --- | --- |
| Variable | `f"{name}"` |
| Expression | `f"{price * 2}"` |
| Function or method call | `f"{name.upper()}"` |
| Dictionary value | `f"{user['name']}"` |
| Literal braces | `f"{{}}"` |
| Decimal places | `f"{price:.2f}"` |
| Percentage | `f"{ratio:.1%}"` |
| Thousands separator | `f"{population:,}"` |
| Width and alignment | `f"{word:>10}"` |
| Fill character | `f"{word:*^10}"` |
| Date format | `f"{date:%d.%m.%Y}"` |
| Variable specifier | `f"{value:.{precision}f}"` |
| Debugging | `f"{x = }"` |
| `repr()` conversion | `f"{name!r}"` |

## References

- [Python Tutorial: Fancier Output Formatting](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
- [Python Language Reference: f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
- [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
- [strftime() and strptime() format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
- [PEP 498: Literal String Interpolation](https://peps.python.org/pep-0498/)
- [PEP 701: Syntactic formalization of f-strings](https://peps.python.org/pep-0701/)
