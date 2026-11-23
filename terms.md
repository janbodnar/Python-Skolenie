# Python Terms

This chapter explains words that you will meet in the Python documentation  
and in the rest of this course. Each term is explained in plain language  
and shown in a short program with its output. The examples were checked  
with Python 3.15.

The chapter covers these topics:

- how Python runs your code, and the two kinds of errors,
- objects, names, and types,
- how Python manages memory,
- Python Enhancement Proposals (PEPs),
- version numbers and the release cycle.

You do not need to remember everything on the first reading. Come back to  
this chapter when one of the terms appears later in the course.

## How Python Runs Your Code

An **interpreter** is a program that reads your source code and runs it.  
When you type `python greet.py`, the program called `python` is the  
interpreter, and `greet.py` is your **script**. The interpreter that you  
installed from python.org is called **CPython**, because it is written in  
the C language. The Introduction chapter lists other implementations.

Running a script happens in two steps:

1. **Compiling.** Python reads the whole file and checks that it is valid  
   Python. It translates the code into **bytecode**, a list of simple  
   instructions that are quicker to run than the original text.
2. **Running.** Python executes the bytecode, one instruction after  
   another, from the top of the file to the bottom.

Both steps happen in memory, in a fraction of a second, so you normally do  
not notice them. You do notice them when something goes wrong, because each  
step has its own kind of error.

### Errors Before the Program Starts

A **syntax error** means that the code breaks the grammar rules of Python,  
for example a missing colon. Python finds it in the first step, so not a  
single line of the program runs:

```python
# syntax_error.py

print("this never runs")

if True
    print("broken")
```

```text
$ python syntax_error.py
  File ".../syntax_error.py", line 5
    if True
           ^
SyntaxError: expected ':'
```

The error is on line 5, but the `print()` call on line 3 did not run  
either. Python refuses to start a program that it cannot read completely.  
`IndentationError` belongs to the same group.

### Errors While the Program Runs

Other errors appear only when Python reaches the line that causes them.  
Everything before that line has already run:

```python
# name_error.py

print("start")
print(total)
print("end")
```

```text
$ python name_error.py
start
Traceback (most recent call last):
  File ".../name_error.py", line 4, in <module>
    print(total)
          ^^^^^
NameError: name 'total' is not defined
```

The word `start` was printed, then the program stopped at line 4, because  
no variable named `total` exists. Such an error is called an **exception**.  
The report that Python prints is a **traceback**. Read it from the bottom  
up: the last line names the exception and the reason, and the lines above  
show the file, the line number, and the code that failed. The `^` marks  
point at the exact problem. `TypeError` and `NameError` are common  
exceptions of this kind.

### Going Further

The `dis` module shows the bytecode of a function, and the Modules chapter  
explains the `.pyc` files where Python stores the bytecode of imported  
modules. The instruction names in the bytecode change between Python  
versions, and you never need to read bytecode to write good programs.

## Objects, Names, and Types

### Objects

Every value in Python is an **object**: a number, a piece of text, a list,  
even `True`. Each object has a **type**, which says what kind of value it  
is and what you can do with it. The built-in `type()` function shows it:

```python
# objects.py

print(type(42))
print(type(3.5))
print(type("Alice"))
print(type([10, 20, 30]))
print(type(True))
```

```text
$ python objects.py
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'bool'>
```

`int` is a whole number, `float` a number with a decimal point, `str` a  
string of text, `list` an ordered collection, and `bool` a truth value.  
The word `class` in the output is another word for type.

### Names and Dynamic Typing

A variable is a **name** that refers to an object. As the Lexical  
Structure chapter shows, an assignment **binds** the name to an object.  
Assigning to the same name again simply binds it to a different object.

The type belongs to the object, not to the name. This is why Python is  
called **dynamically typed**: one name can refer to an `int` now and to a  
`str` later.

```python
# dynamic.py

age = 30
print(type(age))

age = "thirty"
print(type(age))
```

```text
$ python dynamic.py
<class 'int'>
<class 'str'>
```

In a **statically typed** language such as C or Java, each variable has a  
fixed type, and the program would not even compile after this change.

### Two Names for One Object

Because names only refer to objects, two names can refer to the same  
object. A change made through one name is visible through the other:

```python
# shared.py

prices = [10, 20, 30]
backup = prices

backup.append(40)
print(prices)
print(prices is backup)
```

```text
$ python shared.py
[10, 20, 30, 40]
True
```

`backup = prices` does not copy the list. It gives the same list a second  
name, so appending through `backup` also changes `prices`. The `is`  
operator, explained in the Operators chapter, confirms that both names  
refer to one object. To get a real copy, use `prices.copy()`.

### Strong Typing

Dynamic typing does not mean that Python ignores types. Python is also  
**strongly typed**: it does not silently turn a value of one type into  
another type. Joining text and a number is a common beginner mistake:

```python
# str_int.py

age = 30
print("Age: " + age)
```

```text
$ python str_int.py
Traceback (most recent call last):
  File ".../str_int.py", line 4, in <module>
    print("Age: " + age)
          ~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```

The `+` operator can add two numbers or join two strings, but it does not  
know what to do with one of each. Some languages would guess and turn the  
number into text; Python refuses to guess. You decide by converting the  
value yourself, with `"Age: " + str(age)`, or by using an f-string,  
`f"Age: {age}"`.

### Duck Typing

Many functions do not care about the type of their argument, only about  
what the argument can do. The `len()` function accepts anything that has a  
length:

```python
# lengths.py

print(len("Python"))
print(len([10, 20, 30]))
print(len({"apples": 3, "pears": 5}))
print(len(42))
```

```text
$ python lengths.py
6
3
2
Traceback (most recent call last):
  File ".../lengths.py", line 6, in <module>
    print(len(42))
          ~~~^^^^
TypeError: object of type 'int' has no len()
```

A string, a list, and a dictionary are different types, but each has a  
length, so `len()` works for all of them. A number has no length, so the  
last call fails. This style is called **duck typing**, after the saying  
"if it walks like a duck and quacks like a duck, it is a duck."

## Memory Management

A program needs memory for every object it creates. In some languages, the  
programmer must reserve memory and then free it again by hand. In Python,  
this happens automatically. The rule is simple: **an object lives as long  
as something refers to it.** When nothing refers to it any more, Python  
frees its memory.

### Reference Counting

A **reference** is anything that points to an object: a name, an item in a  
list, an argument passed to a function. CPython counts the references to  
every object. When the **reference count** drops to zero, the object is  
deleted at once. The `sys.getrefcount()` function shows the count:

```python
# refcount.py

import sys

prices = [10, 20, 30]
print(sys.getrefcount(prices))

backup = prices
print(sys.getrefcount(prices))

del backup
print(sys.getrefcount(prices))
```

```text
$ python refcount.py
2
3
2
```

The list has one name, `prices`, but the count is 2. Passing the list to  
`getrefcount()` creates one more, temporary reference, so the result is  
always one higher than you might expect. The second name `backup` raises  
the count to 3, and the `del` statement, which removes a name, lowers it  
back to 2. Focus on how the number changes, not on its exact value.

### The Garbage Collector

Reference counting has one weak spot. When objects refer to each other,  
or an object refers to itself, the count never reaches zero. This is  
called a **reference cycle**:

```python
# cycle.py

import gc

team = ["Alice", "Bob"]
team.append(team)
print(team)

del team
print(gc.collect())
```

```text
$ python cycle.py
['Alice', 'Bob', [...]]
1
```

The list contains itself; Python prints the inner copy as `[...]`. After  
`del team`, no name refers to the list, but the list still refers to  
itself, so its count stays at 1. To clean up such objects, Python has a  
**garbage collector**. It runs automatically from time to time, finds  
groups of objects that the program can no longer reach, and frees them.  
`gc.collect()` runs it immediately and returns the number of objects it  
found; here it found the one list. You rarely need to call it yourself.

### Memory Leaks

A **memory leak** is memory that a program keeps although it no longer  
needs it. Python frees unreachable objects, so leaks in Python programs  
usually come from objects that are still reachable by mistake. A typical  
example is a list or dictionary at the top of a module that the program  
keeps adding to and never empties. If the memory use of a long-running  
program only grows, look for such collections first.

### Going Further

Later, when you write your own classes, you will meet related tools: the  
`__del__` method runs when an object is deleted, the `weakref` module  
creates references that do not keep an object alive, and the `tracemalloc`  
module shows which lines of code allocate the most memory.

## Python Enhancement Proposals (PEPs)

A **Python Enhancement Proposal**, or **PEP**, is a document that proposes  
a change to Python and explains the reasons for it. New language features  
are discussed and decided through PEPs. Each PEP has a number, and all of  
them are published at [peps.python.org](https://peps.python.org/).

A PEP goes through several stages. It starts as a *Draft*, the community  
discusses it, and it is either *Accepted* or *Rejected*. An accepted  
feature PEP becomes *Final* once the feature is part of a Python release.  
Even rejected PEPs are useful, because they record why an idea was not  
chosen.

A few PEPs that you will meet in this course:

- PEP 8, the Style Guide for Python Code, which all examples in this  
  course follow,
- PEP 20, The Zen of Python, a list of design principles,
- PEP 484, which introduced type hints,
- PEP 572, which added the assignment expression `:=`,
- PEP 634, which introduced the `match` statement.

When you want to know *why* a feature looks the way it does, read the  
Motivation and Rejected Ideas sections of its PEP.

### The Zen of Python

The Introduction chapter quoted a few lines of PEP 20. Python ships the  
full text, and you can print it with the `-m this` option:

```text
$ python -m this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

These are principles, not rules that the interpreter checks. You have  
already seen one at work: "In the face of ambiguity, refuse the temptation  
to guess" is why `"Age: " + 30` raises a `TypeError`.

## Version Numbers and the Release Cycle

### The Three Parts

A Python version has three numbers, **MAJOR.MINOR.MICRO**. In `3.15.2`:

- **3** is the major version. It changes only for very large, incompatible  
  changes. The last one was the move from Python 2 to Python 3 in 2008.
- **15** is the minor version. A new one comes out every October and  
  brings new features. It may also remove old features that were marked  
  for removal in earlier versions.
- **2** is the micro version. It only fixes bugs and security problems,  
  so upgrading from 3.15.1 to 3.15.2 is normally safe.

Before a minor version is final, there are test releases with a letter in  
the number: `a` for alpha, `b` for beta, and `rc` for release candidate.  
For example, `3.16.0b2` is the second beta of Python 3.16. Do not use them  
for real work.

### Support and End of Life

Each minor version is supported for five years:

- **Bugfix** support for about two years. New micro releases fix bugs and  
  security problems.
- **Security** support for three more years. Only security problems are  
  fixed.
- **End of life** after that. The version gets no fixes at all, and you  
  should upgrade.

At the time of writing, the supported versions are:

| Version | Status | First release | End of life |
| --- | --- | --- | --- |
| 3.16 | in development | 2027-10 (planned) | 2032-10 |
| 3.15 | bugfix | 2026-10-09 | 2031-10 |
| 3.14 | bugfix | 2025-10-07 | 2030-10 |
| 3.13 | security | 2024-10-07 | 2029-10 |
| 3.12 | security | 2023-10-02 | 2028-10 |
| 3.11 | security | 2022-10-24 | 2027-10 |

This table will age. The current status is always at  
[devguide.python.org/versions](https://devguide.python.org/versions/).

### Checking the Version

On the command line, `python --version` prints the version. Inside a  
program, use the `platform` and `sys` modules:

```python
# version.py

import platform
import sys

print(platform.python_version())
print(sys.version_info.major)
print(sys.version_info.minor)
print(sys.version_info >= (3, 10))
```

```text
$ python version.py
3.15.2
3
15
True
```

`platform.python_version()` returns the version as a string, which is good  
for printing. `sys.version_info` holds the parts as integers, and it can  
be compared with a tuple such as `(3, 10)`. Use the comparison when your  
program needs a feature from a particular version.

### Going Further

PEP 602 describes the yearly release schedule, and PEP 387 explains how  
long a feature must stay in Python after it is marked for removal. The  
"What's New" page of each release lists the removed features.

## Common Mistakes

### Comparing Version Numbers as Floats

A version is not a decimal number. Read as a float, `3.10` is 3.1, which is  
smaller than 3.9:

```python
# version_compare.py

print(3.10 > 3.9)
print("3.10" > "3.9")
print((3, 10) > (3, 9))
```

```text
$ python version_compare.py
False
False
True
```

Strings do not work either: they are compared character by character, and  
the character `"1"` comes before `"9"`. Only the tuple of integers gives  
the right answer, because `10` is greater than `9`. `sys.version_info`  
compares in the same way.

### `del` Removes a Name, Not an Object

`del` removes one name. If another name still refers to the object, the  
object stays alive:

```python
# del_alias.py

prices = [10, 20, 30]
backup = prices

del prices
print(backup)
```

```text
$ python del_alias.py
[10, 20, 30]
```

The list still exists, because `backup` refers to it. Python frees the  
object only when the last reference is gone.

### Type Hints Do Not Check Types

You can write the intended type after a name, separated by a colon. This  
note is called a **type hint**. Python stores it but does not enforce it:

```python
# annotations.py

age: int = "thirty"
print(age)
print(type(age))
```

```text
$ python annotations.py
thirty
<class 'str'>
```

The hint says `int`, but Python accepts a string without complaint.  
Separate tools such as mypy and pyright read type hints and report such  
mistakes before you run the program. Python itself checks types only when  
an operation runs.

## Hands-On: Inspect the Running Interpreter

This program combines the ideas of the chapter. It reports the interpreter  
and its version, shows dynamic typing, and follows a reference count.

```python
# runtime_report.py

import gc
import platform
import sys

print("implementation:", platform.python_implementation())
print("version:", platform.python_version())
print("at least 3.10:", sys.version_info >= (3, 10))

value = 42
print("type of value:", type(value))
value = "forty-two"
print("type of value:", type(value))

prices = [10, 20, 30]
backup = prices
print("reference count:", sys.getrefcount(prices))
del backup
print("reference count:", sys.getrefcount(prices))

print("garbage collector on:", gc.isenabled())
```

```text
$ python runtime_report.py
implementation: CPython
version: 3.15.2
at least 3.10: True
type of value: <class 'int'>
type of value: <class 'str'>
reference count: 3
reference count: 2
garbage collector on: True
```

The version line differs on other machines. The name `value` refers first  
to an `int` and then to a `str`. The reference count drops by one after  
`del backup`, and `gc.isenabled()` confirms that the automatic garbage  
collector is running, which is the normal state.

## Summary

| Term | Meaning |
| --- | --- |
| Interpreter | A program that runs Python code; CPython is the standard one |
| Script | A file of Python code that you run with `python file.py` |
| Bytecode | Simple instructions that Python compiles your code into before running it |
| Syntax error | Invalid code, found before the program starts |
| Exception | An error that happens while the program runs |
| Traceback | Python's report of an exception; read it from the bottom up |
| Object | Any value in Python; every object has a type |
| Name | A variable; it refers to an object |
| Dynamic typing | Types belong to objects, so a name can refer to any type |
| Strong typing | Python does not silently convert between unrelated types |
| Duck typing | What matters is what an object can do, not its type |
| Reference count | The number of references to an object; at zero, the object is freed |
| Garbage collector | Frees groups of objects that refer only to each other |
| Memory leak | Memory kept although the program no longer needs it |
| PEP | A document that proposes a change to Python and explains why |
| MAJOR.MINOR.MICRO | Python's version format, for example `3.15.2` |
| End of life | The point when a version receives no more fixes |

## References

- [The Python Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [The Python Language Reference: Data model](https://docs.python.org/3/reference/datamodel.html)
- [The Python Language Reference: Execution model](https://docs.python.org/3/reference/executionmodel.html)
- [Glossary](https://docs.python.org/3/glossary.html)
- [`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html)
- [`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)
- [`platform` — Access to underlying platform's data](https://docs.python.org/3/library/platform.html)
- [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
- [PEP 0: Index of Python Enhancement Proposals](https://peps.python.org/pep-0000/)
- [PEP 8: Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 20: The Zen of Python](https://peps.python.org/pep-0020/)
- [PEP 387: Backwards Compatibility Policy](https://peps.python.org/pep-0387/)
- [PEP 602: Annual Release Cycle for Python](https://peps.python.org/pep-0602/)
- [Python Developer's Guide: Status of Python versions](https://devguide.python.org/versions/)
