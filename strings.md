# Strings in Python

A **string** is a piece of text: a sequence of characters such as letters,  
digits, spaces, and punctuation. Names, messages, file paths, and lines  
read from a file are all strings. In Python, strings have the type `str`.

This chapter goes from creating strings to working with them:

- creating strings: quotes, escape sequences, multiline and raw strings,  
  and Unicode,
- length, indexing, slicing, and looping over a string,
- why strings cannot be changed, and what that means for your code,
- combining strings and converting numbers to strings,
- comparing strings and searching in them,
- changing case and testing characters,
- cleaning and replacing text,
- splitting and joining strings,
- aligning text in columns,
- formatting strings.

The chapter ends with common mistakes and a hands-on example that cleans  
up messy data and prints it as a table.

## Creating Strings

### Single and Double Quotes

You create a string by writing text between quotes. Single and double  
quotes work the same way:

```python
# quotes.py

city = "Bratislava"
country = 'Slovakia'

print(city)
print(country)
print(type(city))
```

```text
$ python quotes.py
Bratislava
Slovakia
<class 'str'>
```

The quotes are not part of the string; they only mark where it starts and  
ends. PEP 8 does not prefer one style, but asks you to pick one and use it  
consistently. This course uses double quotes.

A string with no characters, `""`, is called the **empty string**.

### Quotes Inside a String

To put a quote character inside a string, the easiest way is to use the  
other kind of quotes around it. You can also put a backslash `\` in front  
of the quote:

```python
# quotes_inside.py

print("It's a sunny day.")
print('She said "hello" to me.')
print("She said \"hello\" to me.")
print('It\'s a sunny day.')
```

```text
$ python quotes_inside.py
It's a sunny day.
She said "hello" to me.
She said "hello" to me.
It's a sunny day.
```

The first two lines are easier to read, so prefer mixing quotes when you  
can.

### Escape Sequences

A backslash starts an **escape sequence**: a short code for a character  
that is hard to type or to see. The most common ones are:

| Escape sequence | Meaning |
| --- | --- |
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\uXXXX` | Unicode character with the hexadecimal code `XXXX` |
| `\N{name}` | Unicode character with the given name |

```python
# escapes.py

print("Name:\tAlice\nCity:\tPrague")
print("Folder: C:\\Users\\alice")
```

```text
$ python escapes.py
Name:   Alice
City:   Prague
Folder: C:\Users\alice
```

`\n` starts a new line, and `\t` moves the text to the next tab stop, so  
the values line up. Because the backslash has this special meaning, a real  
backslash must be written as `\\`.

### Multiline Strings

A string in **triple quotes**, `"""` or `'''`, can span several lines. The  
line breaks become part of the string:

```python
# multiline.py

poem = """Roses are red,
violets are blue,
strings in Python
are easy for you."""

print(poem)
```

```text
$ python multiline.py
Roses are red,
violets are blue,
strings in Python
are easy for you.
```

The text starts right after the opening quotes. If you press Enter after  
`"""`, the string begins with a newline character.

### Raw Strings

A **raw string** has an `r` before the opening quote. In a raw string, a  
backslash is an ordinary character and does not start an escape sequence.  
This is useful for Windows paths:

```python
# raw.py

print("C:\new\table")
print(r"C:\new\table")
```

```text
$ python raw.py
C:
ew      able
C:\new\table
```

In the normal string, `\n` became a new line and `\t` a tab, which ruined  
the path. The raw string keeps every backslash. Raw strings are also  
common in regular expressions, which use many backslashes.

### Unicode

Python strings are **Unicode**: they can hold characters from almost every  
writing system, as well as symbols and emoji. You can type such characters  
directly in your source file, because Python reads source files as UTF-8.  
You can also write them with an escape sequence.

```python
# unicode.py

greeting = "Dobrý deň"
print(greeting)
print(len(greeting))

print("Price: 25 \N{EURO SIGN}")
print("Price: 25 \u20ac")

print(ord("č"))
print(chr(269))
```

```text
$ python unicode.py
Dobrý deň
9
Price: 25 €
Price: 25 €
269
č
```

Every Unicode character has a number, its **code point**. `ord()` returns  
the code point of a character, and `chr()` does the opposite. The letters  
`ý` and `ň` count as one character each, so the length is 9.

## Length, Indexing, and Slicing

### Length

The built-in `len()` function returns the number of characters in a  
string. Spaces and newline characters count as well:

```python
# length.py

print(len("Eagle"))
print(len("Eagle  "))
print(len("Eagle\n"))
print(len(""))
```

```text
$ python length.py
5
7
6
0
```

`\n` is written with two characters in the source code, but it is a single  
character in the string.

### Indexing

Each character in a string has a position, called its **index**. The  
first character has the index 0. Negative indexes count from the end, so  
`-1` is the last character:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

You get a single character with square brackets:

```python
# indexing.py

word = "Python"

print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
```

```text
$ python indexing.py
P
n
n
o
```

An index outside the string is an error:

```python
# index_error.py

word = "Python"
print(word[6])
```

```text
$ python index_error.py
Traceback (most recent call last):
  File ".../index_error.py", line 4, in <module>
    print(word[6])
          ~~~~^^^
IndexError: string index out of range
```

The string has six characters, so the last index is 5, not 6.

### Slicing

A **slice** returns a part of a string. You write it as  
`word[start:stop]`. The slice starts at the index `start` and stops  
*before* the index `stop`:

```python
# slicing.py

word = "Python"

print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
print(word[-3:])
```

```text
$ python slicing.py
Py
tho
Py
thon
hon
```

If you leave out `start`, the slice begins at the start of the string; if  
you leave out `stop`, it goes to the end. `word[:2]` is the first two  
characters, and `word[-3:]` the last three.

A third number, the **step**, takes every second, third, or *n*-th  
character. A negative step goes backwards, so `[::-1]` reverses a string:

```python
# step.py

word = "Python"

print(word[::2])
print(word[::-1])
print(word[1:100])
```

```text
$ python step.py
Pto
nohtyP
ython
```

Unlike an index, a slice never raises an error. `word[1:100]` simply stops  
at the end of the string.

### Looping over a String

A `for` loop goes through a string one character at a time:

```python
# loop.py

word = "Rome"

for letter in word:
    print(letter)
```

```text
$ python loop.py
R
o
m
e
```

## Strings Cannot Be Changed

Strings are **immutable**: after a string is created, its characters  
cannot be changed. Trying to assign to an index is an error:

```python
# immutable.py

word = "cat"
word[0] = "b"
```

```text
$ python immutable.py
Traceback (most recent call last):
  File ".../immutable.py", line 4, in <module>
    word[0] = "b"
    ~~~~^^^
TypeError: 'str' object does not support item assignment
```

Instead, you build a new string and assign it to the name:

```python
# new_string.py

word = "cat"
word = "b" + word[1:]
print(word)
```

```text
$ python new_string.py
bat
```

The same rule applies to string **methods**. A method is a function that  
belongs to an object; you call it with a dot, as in `name.upper()`. String  
methods never change the original string. They return a new one, which  
you must store or use:

```python
# method_result.py

name = "alice"

name.upper()
print(name)

name = name.upper()
print(name)
```

```text
$ python method_result.py
alice
ALICE
```

The first call to `upper()` created `"ALICE"`, but the result was thrown  
away, so `name` still refers to `"alice"`. Keep this in mind for every  
method in the rest of the chapter.

## Combining Strings

### Joining and Repeating

The `+` operator joins two strings, and the `*` operator repeats a string,  
as the Operators chapter shows:

```python
# combine.py

first_name = "Anna"
last_name = "Novak"

full_name = first_name + " " + last_name
print(full_name)
print("=" * len(full_name))
```

```text
$ python combine.py
Anna Novak
==========
```

`+` does not add spaces for you; the `" "` in the middle does that.  
Two string literals written next to each other are also joined:  
`"Hello, " "world"` is the same as `"Hello, world"`. This is handy for  
splitting a long text over several lines.

### Converting Between Strings and Numbers

Python does not mix strings and numbers on its own. `"3" + 4` raises a  
`TypeError`. You convert values yourself with `int()`, `float()`, and  
`str()`:

```python
# convert.py

quantity = int("3")
price = float("2.50")
total = quantity * price

print(total)
print("Total: " + str(total))
```

```text
$ python convert.py
7.5
Total: 7.5
```

`int()` and `float()` turn text into numbers, which is needed whenever the  
numbers come from user input or a file. `str()` turns any value into  
text. In practice, an f-string such as `f"Total: {total}"` is usually  
simpler than `str()` and `+`.

## Comparing and Searching

### Comparing Strings

`==` checks whether two strings are equal, and `!=` whether they differ.  
The comparison is exact, so upper and lower case matter:

```python
# compare.py

print("apple" == "apple")
print("apple" == "Apple")
print("apple".lower() == "Apple".lower())
print("apple" < "banana")
```

```text
$ python compare.py
True
False
True
True
```

To compare text regardless of case, convert both sides to lowercase  
first. The `<` and `>` operators compare strings alphabetically, character  
by character; the Operators chapter explains the details.

### Checking for a Substring

A **substring** is a part of a string. The `in` operator checks whether a  
string contains a substring, and `startswith()` and `endswith()` check the  
beginning and the end:

```python
# contains.py

sentence = "I saw a wolf in the forest. A lonely wolf."

print("wolf" in sentence)
print("fox" not in sentence)
print(sentence.startswith("I saw"))
print(sentence.endswith("."))
print(sentence.count("wolf"))
```

```text
$ python contains.py
True
True
True
True
2
```

`count()` returns how many times the substring occurs. When you only need  
a yes or no answer, `in` is the simplest and most readable choice.

### Finding the Position

`find()` returns the index where a substring starts, or `-1` if it is not  
there. `rfind()` searches from the right and returns the last occurrence:

```python
# find.py

sentence = "I saw a wolf in the forest. A lonely wolf."

print(sentence.find("wolf"))
print(sentence.rfind("wolf"))
print(sentence.find("wolf", 10))
print(sentence.find("fox"))
```

```text
$ python find.py
8
37
37
-1
```

The optional second argument is the index where the search starts, so  
`find("wolf", 10)` skips the first wolf.

`index()` and `rindex()` work like `find()` and `rfind()`, but raise an  
error when the substring is missing:

```python
# index_method.py

sentence = "I saw a wolf in the forest. A lonely wolf."
print(sentence.index("fox"))
```

```text
$ python index_method.py
Traceback (most recent call last):
  File ".../index_method.py", line 4, in <module>
    print(sentence.index("fox"))
          ~~~~~~~~~~~~~~^^^^^^^
ValueError: substring not found
```

Use `index()` when the substring must be there and a missing one means a  
bug. Use `find()` when a missing substring is a normal situation that you  
check for.

## Changing Case and Testing Characters

### Changing Case

These methods return a copy of the string with a different case:

```python
# case.py

name = "john SMITH"

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.swapcase())
```

```text
$ python case.py
JOHN SMITH
john smith
John Smith
John smith
JOHN smith
```

- `upper()` and `lower()` change all letters.
- `title()` starts every word with a capital letter.
- `capitalize()` starts only the first word with a capital letter and  
  makes the rest lowercase.
- `swapcase()` turns upper case into lower case and the other way round.

`title()` treats every non-letter as the end of a word, so  
`"it's john's book".title()` gives `"It'S John'S Book"`. For text with  
apostrophes, check the result.

### Testing Characters

Methods whose names start with `is` check what kind of characters a string  
contains. They return `True` or `False`:

| Method | Returns `True` when all characters are |
| --- | --- |
| `isalpha()` | letters |
| `isdigit()` | digits |
| `isalnum()` | letters or digits |
| `isspace()` | whitespace, such as spaces, tabs, or newlines |
| `isupper()` | uppercase (ignoring non-letters) |
| `islower()` | lowercase (ignoring non-letters) |

```python
# testing.py

print("2026".isdigit())
print("20.26".isdigit())
print("Anna".isalpha())
print("Anna Lee".isalpha())
print("R2D2".isalnum())
print("".isdigit())
```

```text
$ python testing.py
True
False
True
False
True
False
```

`"20.26"` contains a dot, and `"Anna Lee"` a space, so the tests fail. An  
empty string always returns `False`.

You can combine these methods with a loop to count types of characters:

```python
# char_count.py

sentence = "There are 22 apples"

letters = 0
digits = 0
spaces = 0

for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print("letters:", letters)
print("digits:", digits)
print("spaces:", spaces)
```

```text
$ python char_count.py
letters: 14
digits: 2
spaces: 3
```

## Cleaning and Replacing

### Removing Whitespace

Text from users and files often has extra spaces or a newline at the ends.  
`strip()` removes **whitespace** (spaces, tabs, and newlines) from both  
ends, `lstrip()` only from the left, and `rstrip()` only from the right.  
The brackets in this example show where the string starts and ends:

```python
# strip.py

name = "   Alice  "

print("[" + name + "]")
print("[" + name.strip() + "]")
print("[" + name.lstrip() + "]")
print("[" + name.rstrip() + "]")
```

```text
$ python strip.py
[   Alice  ]
[Alice]
[Alice  ]
[   Alice]
```

Whitespace inside the string is not touched. You can also pass the  
characters to remove: `"...Hello!!!".strip(".!")` gives `"Hello"`.

### Removing a Prefix or Suffix

`removeprefix()` and `removesuffix()` remove a given text from the start  
or the end of a string, if it is there (Python 3.9+):

```python
# prefix.py

file_name = "report.txt"
print(file_name.removesuffix(".txt"))

title = "Mr. Novak"
print(title.removeprefix("Mr. "))
print(title.removeprefix("Mrs. "))
```

```text
$ python prefix.py
report
Novak
Mr. Novak
```

When the prefix is not there, the string is returned unchanged.

### Replacing Text

`replace(old, new)` replaces every occurrence of `old` with `new`. An  
optional third argument limits the number of replacements:

```python
# replace.py

sentence = "I saw a wolf in the forest. A lonely wolf."

print(sentence.replace("wolf", "fox"))
print(sentence.replace("wolf", "fox", 1))

phone = "0905 123 456"
print(phone.replace(" ", ""))
```

```text
$ python replace.py
I saw a fox in the forest. A lonely fox.
I saw a fox in the forest. A lonely wolf.
0905123456
```

Replacing with an empty string `""` deletes the text, here all the spaces  
in a phone number.

## Splitting and Joining

### Splitting a String

`split()` cuts a string into a list of parts. Without an argument, it  
splits at any run of whitespace. With an argument, it splits at exactly  
that separator:

```python
# split.py

sentence = "The quick  brown fox"
print(sentence.split())
print(sentence.split(" "))

record = "Alice,30,Prague"
print(record.split(","))
```

```text
$ python split.py
['The', 'quick', 'brown', 'fox']
['The', 'quick', '', 'brown', 'fox']
['Alice', '30', 'Prague']
```

There are two spaces between "quick" and "brown". `split()` treats them as  
one gap, but `split(" ")` sees an empty word between them. To split text  
into words, call `split()` without an argument.

The second argument, `maxsplit`, limits the number of cuts. `rsplit()`  
does the same, starting from the right:

```python
# maxsplit.py

path = "home/alice/docs/report.txt"

print(path.split("/", 1))
print(path.rsplit("/", 1))
```

```text
$ python maxsplit.py
['home', 'alice/docs/report.txt']
['home/alice/docs', 'report.txt']
```

`rsplit("/", 1)` is a quick way to separate a folder from a file name.

### Splitting into Lines and at the First Separator

`splitlines()` splits text into lines. `partition()` splits at the first  
occurrence of a separator and always returns three parts: the text before,  
the separator itself, and the text after.

```python
# lines.py

text = "first line\nsecond line\nthird line"
print(text.splitlines())

setting = "timeout = 30"
print(setting.partition("="))
```

```text
$ python lines.py
['first line', 'second line', 'third line']
('timeout ', '=', ' 30')
```

The result of `partition()` is a tuple, so `setting.partition("=")[2]` is  
the value, `" 30"`.

### Joining Strings

`join()` is the opposite of `split()`. You call it on the separator, and  
pass it a list of strings:

```python
# join.py

colors = ["red", "green", "blue"]

print(", ".join(colors))
print(" | ".join(colors))
print("".join(colors))
```

```text
$ python join.py
red, green, blue
red | green | blue
redgreenblue
```

The syntax may look backwards at first: the separator comes first, the  
list second. `join()` is the usual way to build one string from many  
parts; it is clearer and faster than adding them one by one with `+`.

## Aligning Text

`ljust()`, `rjust()`, and `center()` pad a string with spaces to a given  
width, so text lines up in columns. `zfill()` pads a number with zeros on  
the left:

```python
# align.py

print("Price list".center(20, "-"))
print("apple".ljust(12) + "1.20".rjust(8))
print("banana".ljust(12) + "0.50".rjust(8))
print("watermelon".ljust(12) + "12.90".rjust(8))
print("7".zfill(3))
```

```text
$ python align.py
-----Price list-----
apple           1.20
banana          0.50
watermelon     12.90
007
```

Text is usually aligned to the left and numbers to the right, so the  
decimal points line up. The optional second argument of `center()`,  
`ljust()`, and `rjust()` is the fill character. f-strings can align text  
in the same way; see the f-strings chapter.

## Formatting Strings

To build a string from text and values, use an **f-string**: put `f`  
before the opening quote and the values in curly braces.

```python
# formatting.py

name = "Peter"
age = 23
height = 1.8

print(f"{name} is {age} years old and {height:.2f} m tall.")
```

```text
$ python formatting.py
Peter is 23 years old and 1.80 m tall.
```

The `:.2f` after `height` shows the number with two decimal places. The  
f-strings chapter explains f-strings and these **format specifiers** in  
detail.

In older code you will also see two other ways to format strings. You  
should be able to read them, but prefer f-strings in new code:

| Style | Example |
| --- | --- |
| f-string (Python 3.6+) | `f"{name} is {age}"` |
| `str.format()` | `"{} is {}".format(name, age)` |
| `%` operator | `"%s is %d" % (name, age)` |

## Common Mistakes

### Forgetting to Store the Result of a Method

Methods return a new string and leave the original unchanged, as shown in  
the section on immutability. A call such as `name.strip()` on its own line  
does nothing useful. Write `name = name.strip()`.

### Backslashes in Windows Paths

In a normal string, the backslashes in a Windows path can form escape  
sequences. If a backslash is followed by a character that is not a valid  
escape, Python warns you:

```python
# path_warning.py

path = "C:\data\new"
print(path)
```

```text
$ python path_warning.py
.../path_warning.py:3: SyntaxWarning: "\d" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\d"? A raw string is also an option.
  path = "C:\data\new"
C:\data
ew
```

`\d` is not an escape sequence, so Python keeps it but warns (Python  
3.12+; older versions accepted it silently). `\n`, however, is valid and  
became a new line. Use a raw string, `r"C:\data\new"`, or forward slashes,  
`"C:/data/new"`, which also work on Windows.

### Using `rstrip()` to Remove a Suffix

`strip()`, `lstrip()`, and `rstrip()` take a *set of characters*, not a  
word. They remove any of those characters, in any order:

```python
# rstrip_suffix.py

file_name = "report.txt"

print(file_name.rstrip(".txt"))
print(file_name.removesuffix(".txt"))
```

```text
$ python rstrip_suffix.py
repor
report
```

`rstrip(".txt")` kept removing `t`, `x`, and `.` from the right, and also  
took the last `t` of "report". Use `removesuffix()` to remove an exact  
ending.

### Using `find()` as a Condition

`find()` returns `-1` when the substring is missing and `0` when it is at  
the very start. In an `if` statement, `0` counts as false and `-1` as  
true, which is the opposite of what you want:

```python
# find_condition.py

sentence = "I saw a wolf."

if sentence.find("I"):
    print("found with find()")

if "I" in sentence:
    print("found with in")
```

```text
$ python find_condition.py
found with in
```

`"I"` is at index 0, so the first condition is false. Use `in` to check  
whether a substring is present.

### Joining Numbers

`join()` accepts only strings. A number in the list is an error:

```python
# join_numbers.py

scores = [90, 85, 77]
print(", ".join(scores))
```

```text
$ python join_numbers.py
Traceback (most recent call last):
  File ".../join_numbers.py", line 4, in <module>
    print(", ".join(scores))
          ~~~~~~~~~^^^^^^^^
TypeError: sequence item 0: expected str instance, int found
```

Convert the numbers first, for example with a loop that appends  
`str(score)` to a new list.

## Hands-On: Cleaning a Shopping List

Data from a file or a form is rarely tidy. This program takes a shopping  
list with extra spaces and inconsistent capitals, cleans it, computes the  
prices, and prints an aligned table.

```python
# shopping.py

data = """
  apple, 1.20 , 4
BANANA,0.50,6
  cherry tomatoes , 2.80, 1
"""

lines = data.strip().splitlines()

print("Item".ljust(18) + "Qty".rjust(4) + "Total".rjust(8))
print("-" * 30)

total = 0

for line in lines:
    parts = line.split(",")
    name = parts[0].strip().title()
    price = float(parts[1])
    quantity = int(parts[2])

    cost = price * quantity
    total += cost

    print(name.ljust(18) + str(quantity).rjust(4) + f"{cost:.2f}".rjust(8))

print("-" * 30)
print("Total".ljust(22) + f"{total:.2f}".rjust(8))
```

```text
$ python shopping.py
Item               Qty   Total
------------------------------
Apple                4    4.80
Banana               6    3.00
Cherry Tomatoes      1    2.80
------------------------------
Total                    10.60
```

The program uses most of the chapter:

- `strip()` removes the empty lines around the data, and `splitlines()`  
  turns it into a list of lines,
- `split(",")` cuts each line into a name, a price, and a quantity,
- `strip()` and `title()` clean the name,
- `float()` and `int()` convert the text to numbers; they ignore the  
  spaces around the digits,
- `ljust()` and `rjust()` align the columns, and an f-string rounds the  
  prices to two decimal places.

## Summary

| Term or method | Meaning |
| --- | --- |
| String (`str`) | An immutable sequence of characters |
| Escape sequence | A code starting with `\`, such as `\n` for a new line |
| Raw string | `r"..."`; backslashes are ordinary characters |
| Code point | The Unicode number of a character; see `ord()` and `chr()` |
| `len(s)` | The number of characters |
| `s[i]` | The character at index `i`; `-1` is the last one |
| `s[start:stop:step]` | A slice; `stop` is not included |
| Immutable | A string cannot be changed; methods return a new string |
| `in`, `startswith()`, `endswith()` | Check for a substring |
| `find()`, `index()`, `count()` | Find the position of a substring or count it |
| `upper()`, `lower()`, `title()` | Change the case |
| `isdigit()`, `isalpha()`, ... | Test the kind of characters |
| `strip()`, `removeprefix()`, `replace()` | Clean and replace text |
| `split()`, `splitlines()`, `partition()` | Split a string into parts |
| `sep.join(list)` | Join strings with a separator |
| `ljust()`, `rjust()`, `center()` | Pad a string to a width |
| f-string | `f"{value}"`; the recommended way to format strings |

## References

- [Built-in Types: Text Sequence Type — `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Built-in Types: String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [The Python Tutorial: Text](https://docs.python.org/3/tutorial/introduction.html#text)
- [Lexical Analysis: String and Bytes Literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)
- [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
- [PEP 498: Literal String Interpolation](https://peps.python.org/pep-0498/)
- [PEP 616: String Methods to Remove Prefixes and Suffixes](https://peps.python.org/pep-0616/)
