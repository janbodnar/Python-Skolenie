# Python Modules

A **module** is a file with Python code. Every file with the `.py` extension is  
a module: it can contain functions, classes, variables, and statements. Other  
programs can **import** the module and use what it defines.

Modules help in two ways:

- **Organization**: a long program becomes hard to read. When you split it into  
  several files, each file deals with one topic. For example, a web application  
  might keep database code in `db.py`, user login in `auth.py`, and settings in  
  `config.py`.
- **Reuse**: a function written once in a module can be used in many programs.  
  You do not have to copy it from file to file.

Python code is organized in levels:

- **Functions** group statements into a reusable unit of behavior.
- **Classes** group data and the functions that work with it.
- **Modules** are single `.py` files.
- **Packages** are directories that contain modules.

This chapter starts with modules that come with Python, then shows how to write  
your own modules and packages. A complete example of a small project is at the  
end.

## Using a module from the standard library

Python comes with hundreds of ready-made modules, called the **standard  
library**. For example, the `math` module contains mathematical functions. To  
use it, import it with the `import` statement:

```python
import math

print(math.sqrt(16))
print(math.pi)
print(math.floor(7.8))
```

```text
$ python using_math.py
4.0
3.141592653589793
7
```

After `import math`, the name `math` refers to the module. You reach the things  
inside it with a dot: `math.sqrt` is the `sqrt()` function from the `math`  
module, and `math.pi` is a variable with the value of π.

Imports are written at the top of the file, before the rest of the code.

A common mistake is to forget the module name before the function:

```python
import math

print(sqrt(16))
```

```text
$ python sqrt_error.py
Traceback (most recent call last):
  File "/home/user/project/sqrt_error.py", line 3, in <module>
    print(sqrt(16))
          ^^^^
NameError: name 'sqrt' is not defined
```

The `import math` statement makes only the name `math` available, not the names  
inside the module.

## Ways to import

The `import` statement has several forms. The following example uses three of  
them:

```python
import math
from math import sqrt, pi
import statistics as stats

print(math.floor(7.8))
print(sqrt(25))
print(pi)
print(stats.mean([4, 8, 6]))
```

```text
$ python import_styles.py
7
5.0
3.141592653589793
6
```

- `import math` imports the whole module. You write the module name before every  
  name from it, as in `math.floor()`.
- `from math import sqrt, pi` imports only the listed names. You use them  
  directly, without the `math.` prefix.
- `import statistics as stats` imports a module under a shorter name, an  
  **alias**. Some aliases are so common that everybody uses them, for example  
  `import numpy as np`.

The first form is usually the best choice. When you read `math.sqrt(25)`, you  
can see immediately where the function comes from. Use `from ... import` when  
you need only a few names many times.

A long list of imported names can be split over several lines with parentheses:

```python
from datetime import (
    date,
    datetime,
    timedelta,
)
```

### The wildcard import

The form `from math import *` imports all public names from a module. It looks  
convenient, but it is not recommended. You cannot see which names it creates,  
and a name in your code can quietly replace a name from the module, or the other  
way around:

```python
from math import *

e = 2.5    # overwrites math.e without warning

print(sqrt(49))
print(e)
```

```text
$ python star.py
7.0
2.5
```

The variable `e` now holds `2.5`, not Euler's number from the `math` module. In  
a larger program, such mistakes are hard to find. PEP 8, the Python style guide,  
recommends avoiding wildcard imports. They are fine for quick experiments in the  
interactive mode.

### Order of imports

PEP 8 recommends putting imports in three groups, separated by an empty line:

1. modules from the standard library
2. third-party modules installed with `pip`
3. your own modules

```python
import json
import math

import requests

import greetings
```

## Creating your own module

Any `.py` file you write is a module. Create a file named `greetings.py`:

```python
"""Functions for greeting people."""

GREETING = "Hello"


def greet(name):
    return f"{GREETING}, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"
```

The string on the first line is the module's **docstring**, a short description  
of the module.

In the same directory, create `main.py`, which imports the module. The module  
name is the file name without the `.py` extension:

```python
import greetings

print(greetings.greet("Alice"))
print(greetings.farewell("Bob"))
print(greetings.GREETING)
```

```text
$ python main.py
Hello, Alice!
Goodbye, Bob!
Hello
```

Your own module works exactly like `math`: after the import, you reach its  
functions and variables with a dot.

For now, keep both files in the same directory. The section *Where Python looks  
for modules* explains why this matters.

## Exploring a module

The built-in `dir()` function lists the names defined in a module. The docstring  
is stored in the `__doc__` attribute:

```python
import greetings

print(greetings.__doc__)
print(dir(greetings))
```

```text
$ python explore.py
Functions for greeting people.
['GREETING', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'farewell', 'greet']
```

Besides `GREETING`, `farewell`, and `greet`, the list contains names with two  
underscores on both sides. Python creates them automatically for every module.  
For example, `__file__` holds the path to the module's file.

In the interactive mode, you can also call `help(greetings)` to read the  
documentation of a module, including the docstrings of its functions.

## The `__name__` variable

Every module has a name, stored in its `__name__` variable. For an imported  
module, it is the module name. The file that you run directly is special: its  
`__name__` is always `"__main__"`.

```python
import greetings
import math

print(__name__)
print(greetings.__name__)
print(math.__name__)
```

```text
$ python show_name.py
__main__
greetings
math
```

### The main guard

When Python imports a module, it runs all the code in the file, from top to  
bottom. This becomes a problem when a module also contains code to test itself.  
Look at this `prices.py` module:

```python
"""Helper functions for working with prices."""

VAT_RATE = 0.20


def add_vat(price):
    return round(price * (1 + VAT_RATE), 2)


print(add_vat(10))
print(add_vat(24.99))
```

The two `print()` calls at the end check that `add_vat()` works. Now another  
program, `invoice.py`, imports the module:

```python
import prices

print("Total:", prices.add_vat(100))
```

```text
$ python invoice.py
12.0
29.99
Total: 120.0
```

The test output appears in the invoice, too. The fix is to put the test code  
under the condition `if __name__ == "__main__":`. The condition is true only  
when the file is run directly:

```python
"""Helper functions for working with prices."""

VAT_RATE = 0.20


def add_vat(price):
    return round(price * (1 + VAT_RATE), 2)


if __name__ == "__main__":
    print(add_vat(10))
    print(add_vat(24.99))
```

```text
$ python prices.py
12.0
29.99
$ python invoice.py
Total: 120.0
```

This condition is called the **main guard**. Thanks to it, one file can serve  
both as a module that others import and as a script that you run. You will see  
it in most Python programs.

## Where Python looks for modules

When Python executes `import greetings`, it searches for the module in this  
order:

1. The `sys.modules` dictionary of modules that are already imported. A module  
   is loaded only once; a second `import` reuses it.
2. Built-in modules compiled into the interpreter, such as `sys`.
3. The directories listed in `sys.path`, one by one. The first matching file  
   wins.

You can print `sys.path` to see the directories:

```python
import sys

for path in sys.path:
    print(path)
```

The output depends on your system and on where Python is installed. On Linux, it  
may look like this:

```text
$ python search_path.py
/home/user/project
/usr/local/lib/python315.zip
/usr/local/lib/python3.15
/usr/local/lib/python3.15/lib-dynload
/usr/local/lib/python3.15/site-packages
```

The first directory is the directory of the script you run. That is why  
`main.py` finds `greetings.py` in the same directory. The other directories  
contain the standard library and, in `site-packages`, modules installed with  
`pip`. You can add more directories with the `PYTHONPATH` environment variable.

When Python does not find a module, it raises `ModuleNotFoundError`:

```text
$ python -c "import requests"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```

Check the spelling of the name. If the module is a third-party package, install  
it first, for example with `pip install requests`.

### Do not name your files after existing modules

Because the script's directory is searched first, your own file can hide a  
module from the standard library. Suppose you are practicing with random numbers  
and save the program as `random.py`:

```python
import random

print(random.randint(1, 6))
```

```text
$ python random.py
Traceback (most recent call last):
  File "/home/user/project/random.py", line 1, in <module>
    import random
  File "/home/user/project/random.py", line 3, in <module>
    print(random.randint(1, 6))
          ^^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'randint' (consider renaming '/home/user/project/random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
```

The statement `import random` imported the file itself, not the standard  
`random` module. Since Python 3.13, the error message explains the problem. The  
fix is to rename the file, for example to `dice.py`. Avoid names such as  
`math.py`, `random.py`, `json.py`, `test.py`, or the names of packages you have  
installed.

## Private names and `__all__`

A name that starts with an underscore, such as `_clean`, is **private** by  
convention. It tells other programmers that the name is meant for use inside the  
module only. Python does not forbid using it, but the wildcard import skips it:

```python
"""Simple text helpers."""


def shout(text):
    return _clean(text).upper() + "!"


def whisper(text):
    return _clean(text).lower() + "..."


def _clean(text):
    return text.strip()
```

```python
from textutils import *

print(shout("  hello  "))
print(whisper("  GOOD NIGHT "))
print(_clean("  text  "))
```

```text
$ python use_textutils.py
HELLO!
good night...
Traceback (most recent call last):
  File "/home/user/project/use_textutils.py", line 5, in <module>
    print(_clean("  text  "))
          ^^^^^^
NameError: name '_clean' is not defined
```

A module can also list its public names explicitly in the `__all__` variable.  
Then the wildcard import brings in only the names from this list:

```python
"""Simple text helpers."""

__all__ = ["shout"]


def shout(text):
    return _clean(text).upper() + "!"


def whisper(text):
    return _clean(text).lower() + "..."


def _clean(text):
    return text.strip()
```

```python
from textutils import *

print(shout("hello"))
print(whisper("good night"))
```

```text
$ python use_all.py
HELLO!
Traceback (most recent call last):
  File "/home/user/project/use_all.py", line 4, in <module>
    print(whisper("good night"))
          ^^^^^^^
NameError: name 'whisper' is not defined
```

`__all__` affects only the wildcard import. An explicit import, such as `from  
textutils import whisper`, still works. `__all__` also tells the readers of the  
module which names form its public interface.

## Packages

When a project grows, even modules need to be organized. A **package** is a  
directory that contains modules and a file named `__init__.py`. The file may be  
empty; it marks the directory as a package.

Let's create a package named `shop` with the `prices.py` module from the  
previous sections:

```text
project/
    main.py
    shop/
        __init__.py
        prices.py
```

A module inside a package is imported with a dotted name, `package.module`. All  
three forms of the import work:

```python
import shop.prices

print(shop.prices.add_vat(50))
```

```python
from shop import prices

print(prices.add_vat(50))
```

```python
from shop.prices import add_vat

print(add_vat(50))
```

Each of these programs prints `60.0`. Run them from the `project` directory, so  
that Python finds the `shop` package there.

### Relative imports

Modules inside a package often use each other. Add a `cart.py` module to the  
package:

```text
project/
    main.py
    shop/
        __init__.py
        cart.py
        prices.py
```

```python
"""A simple shopping cart."""

from .prices import add_vat


class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append((name, price))

    def subtotal(self):
        total = 0
        for name, price in self.items:
            total += price
        return total

    def total(self):
        return add_vat(self.subtotal())


if __name__ == "__main__":
    cart = Cart()
    cart.add("Book", 15.0)
    print(cart.total())
```

The line `from .prices import add_vat` is a **relative import**. The dot means  
"the current package", so `.prices` is the `prices` module next to `cart.py`.  
Two dots mean the parent package, as in `from ..models import User`. You can  
also write the absolute form, `from shop.prices import add_vat`.

Relative imports work only inside a package. If you run the file directly,  
Python does not know which package it belongs to:

```text
$ python shop/cart.py
Traceback (most recent call last):
  File "/home/user/project/shop/cart.py", line 3, in <module>
    from .prices import add_vat
ImportError: attempted relative import with no known parent package
```

To run a module that is part of a package, use the `-m` option with the dotted  
module name, from the `project` directory:

```text
$ python -m shop.cart
18.0
```

### The `__init__.py` file

Python runs `__init__.py` when the package is first imported. Besides marking  
the directory as a package, it can make the most important names available  
directly from the package:

```python
"""A small package for an online shop."""

from .cart import Cart
from .prices import add_vat
```

Users of the package can now write `from shop import Cart` instead of `from  
shop.cart import Cart`.

A directory without `__init__.py` can also be imported; Python treats it as a  
**namespace package**. Namespace packages are meant for large projects that are  
split across several directories. For your own packages, always create  
`__init__.py`.

## The `__pycache__` directory

After you import a module, you will find a new directory named `__pycache__`  
next to it:

```text
$ ls shop/__pycache__
__init__.cpython-315.pyc
prices.cpython-315.pyc
```

When Python imports a module, it first compiles the source code to **bytecode**,  
a form that the interpreter runs faster. It saves the bytecode to a `.pyc` file,  
so that the next import can skip the compilation. The file name contains the  
Python version, here `cpython-315` for CPython 3.15. When you change the source  
file, Python compiles it again automatically.

The script that you run directly is not cached, only imported modules. You can  
delete `__pycache__` at any time; Python creates it again. Do not add it to  
version control: put `__pycache__/` in the `.gitignore` file.

## Handling a missing module

Some programs can work without an optional third-party module. Because a missing  
module raises `ModuleNotFoundError`, you can catch it with `try` and `except`:

```python
try:
    import numpy
except ModuleNotFoundError:
    numpy = None

if numpy is None:
    print("numpy is not installed")
    print("Install it with: pip install numpy")
else:
    print("numpy version:", numpy.__version__)
```

```text
$ python optional.py
numpy is not installed
Install it with: pip install numpy
```

If `numpy` is installed, the program prints its version instead.

## Importing a module by its name

The `import` statement needs the module name written in the code. When the name  
is known only while the program runs, for example when it comes from a  
configuration file, use the `import_module()` function from the `importlib`  
module:

```python
import importlib

module_name = "math"
module = importlib.import_module(module_name)

print(module.sqrt(81))
```

```text
$ python by_name.py
9.0
```

This technique is used, for example, by programs that load plugins.

## Lazy imports

Python 3.15 added **lazy imports**. When an import is marked with the `lazy`  
soft keyword, Python does not load the module at once, but only when the program  
uses it for the first time:

```python
import sys

lazy import json

print("json" in sys.modules)
print(json.dumps({"name": "Alice"}))
print("json" in sys.modules)
```

```text
$ python lazy.py
False
{"name": "Alice"}
True
```

The first line of the output shows that the `json` module is not loaded yet. It  
is loaded when `json.dumps()` is called. Lazy imports make programs start faster  
when they import many modules but use only some of them in a typical run. In  
older versions of Python, `lazy import` is a syntax error.

## Common mistakes

- **Forgetting the module prefix**: after `import math`, write `math.sqrt()`,  
  not `sqrt()`.
- **Naming a file after a module**: a file named `random.py` or `json.py` hides  
  the standard module of the same name.
- **Running a package module directly**: a module with relative imports must be  
  run with `python -m package.module`.
- **Circular imports**: when module `a` imports module `b` and `b` imports `a`,  
  one of them is only partly loaded at the time of the import, and Python may  
  raise an `ImportError`. Move the shared code to a third module that both of  
  them import.
- **Wildcard imports**: `from module import *` hides where names come from and  
  can overwrite your own names.

## A complete example

The following small project puts the parts of this chapter together. It prints a  
receipt for a shopping cart.

```text
receipt/
    main.py
    shop/
        __init__.py
        cart.py
        prices.py
```

The `prices.py` module calculates the price with VAT:

```python
"""Helper functions for working with prices."""

VAT_RATE = 0.20


def add_vat(price):
    return round(price * (1 + VAT_RATE), 2)
```

The `cart.py` module defines the shopping cart. It uses a relative import to get  
`add_vat()` from its sibling module:

```python
"""A simple shopping cart."""

from .prices import add_vat


class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append((name, price))

    def subtotal(self):
        total = 0
        for name, price in self.items:
            total += price
        return total

    def total(self):
        return add_vat(self.subtotal())
```

The `__init__.py` file makes the public names available directly from the `shop`  
package and lists them in `__all__`:

```python
"""A small package for an online shop."""

from .cart import Cart
from .prices import add_vat

__all__ = ["Cart", "add_vat"]
```

The `main.py` script uses the package. Its code is in the `main()` function,  
which runs only when the file is executed directly:

```python
"""Print a receipt for a shopping cart."""

from shop import Cart


def print_receipt(cart):
    for name, price in cart.items:
        print(f"{name:<16}{price:>8.2f}")
    print("-" * 24)
    print(f"{'Subtotal':<16}{cart.subtotal():>8.2f}")
    print(f"{'Total with VAT':<16}{cart.total():>8.2f}")


def main():
    cart = Cart()
    cart.add("Python book", 29.90)
    cart.add("Notebook", 3.50)
    cart.add("Pen", 1.20)
    print_receipt(cart)


if __name__ == "__main__":
    main()
```

Run the program from the `receipt` directory:

```text
$ python main.py
Python book        29.90
Notebook            3.50
Pen                 1.20
------------------------
Subtotal           34.60
Total with VAT     41.52
```

Thanks to the main guard, another program can import `main` and call  
`print_receipt()` with its own cart, without printing this receipt.

## Summary

| Topic | Example |
| --- | --- |
| Import a module | `import math` |
| Import selected names | `from math import sqrt, pi` |
| Import with an alias | `import statistics as stats` |
| Wildcard import (avoid) | `from math import *` |
| List names in a module | `dir(math)` |
| Module name | `__name__` |
| Main guard | `if __name__ == "__main__":` |
| Module search path | `sys.path` |
| Private name | `_clean` |
| Public names for `*` | `__all__ = ["shout"]` |
| Import from a package | `from shop.prices import add_vat` |
| Relative import | `from .prices import add_vat` |
| Run a module in a package | `python -m shop.cart` |
| Import by name | `importlib.import_module("math")` |
| Lazy import (3.15+) | `lazy import json` |

## References

- [Python Tutorial: Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Language Reference: The import system](https://docs.python.org/3/reference/import.html)
- [Python Language Reference: The import statement](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
- [The Python Standard Library](https://docs.python.org/3/library/index.html)
- [importlib](https://docs.python.org/3/library/importlib.html)
- [PEP 8: Imports](https://peps.python.org/pep-0008/#imports)
- [PEP 810: Explicit lazy imports](https://peps.python.org/pep-0810/)
