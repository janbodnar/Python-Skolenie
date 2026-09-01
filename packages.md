# Python Packages

A **package** is a collection of modules that share a common purpose. Packages  
help organize code into logical groups, making large projects manageable.  
A **module** is a single Python file (with a `.py` extension) containing  
functions, classes, and variables.

Package directories traditionally required a special file called `__init__.py`.  
Since Python 3.3, this file is **no longer required** to define package directories,  
though it's still commonly used for package initialization and to control what  
gets imported when using `from package import *`.

---

## Why Use Packages?

When dealing with large projects containing hundreds or thousands of modules,  
using packages is crucial for organization and maintainability. For example:

- Put all database-related modules in a `database` package  
- Place user interface code in a `ui` package  
- Group utility functions in a `utils` package  
- Organize test modules in a `tests` package  

This structure makes code easier to navigate, share, and reuse across projects.

---

## Package Locations

Python looks for packages and modules in specific directories:

### Built-in Packages

Predefined system directories contain Python's standard library:
- **Linux**: `/usr/lib/python3.x/`  
- **Windows**: `C:\Python3x\Lib\`  
- **macOS**: `/Library/Frameworks/Python.framework/Versions/3.x/lib/python3.x/`

### Third-Party Packages

External packages installed via `pip` are placed in:
- **Linux**: `/usr/local/lib/python3.x/dist-packages/` (system-wide) or  
  `~/.local/lib/python3.x/site-packages/` (user-specific)  
- **Windows**: `C:\Users\Username\AppData\Local\Programs\Python\Python3x\Lib\site-packages\`  

### Virtual Environment Packages

When using virtual environments, packages are installed in:  
`venv/lib/python3.x/site-packages/` (or `venv\Lib\site-packages\` on Windows)

---

## Python Package Management

Python packages are managed with the **Python Package Manager `pip`**, which  
installs, updates, and removes packages from PyPI (Python Package Index) or  
other repositories.

### Installing a Package

```bash
sudo pip install arrow
```

The `sudo` command may be required for system-wide installation. For user  
installation (without admin privileges), use:

```bash
pip install --user arrow
```

### Uninstalling a Package

```bash
sudo pip uninstall arrow
```

### Listing Installed Packages

```bash
pip list
```

### Generating Requirements Files

```bash
pip freeze > requirements.txt
```

### Installing from Requirements

```bash
pip install -r requirements.txt
```

---

## Package with Empty `__init__.py`

In the first example, we create a simple package structure:

```
$ tree
.
├── mymath
│   ├── __init__.py
│   └── mfuns.py
└── myprog.py
```

The `mymath` directory contains:
- `__init__.py` – marks `mymath` as a package directory (can be empty)  
- `mfuns.py` – a Python module with function definitions  

```python
# mfuns.py

def mycube(x):
    return x * x * x
```

The `mfuns.py` module defines a `mycube()` function that returns the cube of a number.

```python
# myprog.py

from mymath.mfuns import mycube

print(mycube(3))
```

In the `myprog.py` program, we import the `mycube` function from the `mymath.mfuns`  
module. The module name and package name are separated with a dot (`.`) character.

**Output:**

```
27
```

---

## Importing Functions in `__init__.py`

In the next example, we add code to the `__init__.py` file:

```
$ tree
.
├── mymath
│   ├── __init__.py
│   └── mfuns.py
└── myprog.py
```

We have the same directory structure, but now `__init__.py` contains code:

```python
# __init__.py

from .mfuns import mycube
```

In the `__init__.py` file, we import the `mycube` function. As a consequence, we  
don't need to specify the module name when referring to the `mycube` function  
from the `mymath` package.

```python
# mfuns.py

def mycube(x):
    return x * x * x
```

The `mfuns.py` module remains the same.

```python
# myprog.py

from mymath import mycube

print(mycube(3))
```

In the `myprog.py` program, we import `mycube` directly from the package,  
omitting the module name. This provides a cleaner interface for package users.

**Output:**

```
27
```

---

## Package Without `__init__.py`

Since Python 3.3, it's possible to define package directories without using the  
`__init__.py` file. These are called **namespace packages**.

```
read.py
constants/
    data.py
```

In our current working directory, we have a `constants` directory and a  
`read.py` script.

```python
# constants/data.py

colours = ('yellow', 'blue', 'red', 'orange', 'brown')
names = ('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
```

The `data.py` module defines two tuples.

```python
# read.py

from constants.data import colours
import constants.data as mydata

print(colours)
print(mydata.names)
```

In the `read.py` script, we import the tuples using two different approaches:  
- Direct import with `from ... import ...`  
- Module alias with `import ... as ...`

**Output:**

```
('yellow', 'blue', 'red', 'orange', 'brown')
('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
```

**Note:** While `__init__.py` is optional, it's still recommended for most  
packages to provide explicit initialization and control over package imports.

---

## The `arrow` Package (Third-Party Example)

The `arrow` library is a third-party package for working with dates and times  
in Python. It provides a more human-friendly API than the standard `datetime`  
module.

```
$ ls /usr/local/lib/python3.5/dist-packages/arrow/
api.py  arrow.py  factory.py  formatter.py  __init__.py  
locales.py  parser.py  __pycache__  util.py
```

The library is installed in the `arrow` directory under `dist-packages` on  
Debian Linux. As we can see, the library is a collection of Python modules  
working together as a cohesive package.

### Basic Usage of `arrow`

```python
import arrow

# Get current time
now = arrow.now()
print(now)

# Parse a date string
date = arrow.get('2024-01-15', 'YYYY-MM-DD')
print(date)

# Format dates
formatted = now.format('YYYY-MM-DD HH:mm:ss')
print(formatted)
```

---

## Python Subpackages

We can also create **subpackages** – packages nested within other packages.  
To access subpackages, we use the dot operator.

```
$ tree
.
├── constants
│   ├── __init__.py
│   ├── data.py
│   └── numbers
│       ├── __init__.py
│       └── myintegers.py
└── read.py
```

### Package Files

**`constants/__init__.py`**

```python
from .data import names
```

The `__init__.py` file in the `constants` directory imports the `names` tuple.

**`constants/data.py`**

```python
names = ('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
```

The `data.py` module defines the `names` tuple.

**`constants/numbers/__init__.py`**

```python
from .myintegers import myintegers
```

The `__init__.py` file in the `numbers` subpackage imports the `myintegers` tuple.

**`constants/numbers/myintegers.py`**

```python
myintegers = (2, 3, 45, 6, 7, 8, 9)
```

The `myintegers.py` module defines a tuple of seven integers.

**`read.py`**

```python
from constants import names
from constants.numbers import myintegers

print(names)
print(myintegers)
```

In the `read.py` program, we import:
- The `names` tuple from the `constants` package  
- The `myintegers` tuple from the `constants.numbers` subpackage  

**Output:**

```
('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
(2, 3, 45, 6, 7, 8, 9)
```

---

## Relative Imports

Within a package, you can use **relative imports** to import modules from the  
same package without specifying the full absolute path.

### Relative Import Syntax

| Syntax | Meaning |
|--------|---------|
| `.` | Current directory (same package) |
| `..` | Parent directory (one level up) |
| `...` | Grandparent directory (two levels up) |

### Example

```
mypackage/
    __init__.py
    module1.py
    subpackage/
        __init__.py
        module2.py
```

**`module2.py` (inside subpackage)**

```python
# Relative import from same package
from . import module1

# Relative import from parent package
from .. import module1

# Absolute import (recommended)
from mypackage import module1
```

**Important Notes on Relative Imports:**

1. Relative imports only work **inside a package**  
2. They cannot be used in scripts run directly (`__name__ == "__main__"`)  
3. The script must be run as a module: `python -m mypackage.module`  
4. Python 3 requires explicit relative imports (using `.` or `..`)  

For more details, see:  
[Relative imports in Python 3](https://stackoverflow.com/questions/16981921/relative-imports-in-python-3)

---

## Package Structure Best Practices

### Recommended Structure

```
project_name/
    README.md
    setup.py
    requirements.txt
    project_name/
        __init__.py
        main.py
        module1.py
        module2.py
        subpackage/
            __init__.py
            module3.py
    tests/
        __init__.py
        test_module1.py
        test_module2.py
```

### Guidelines

1. **Use descriptive names** for packages and modules  
2. **Keep `__init__.py` minimal** – typically for package initialization  
3. **Document public interfaces** in `__init__.py`  
4. **Avoid circular imports** – restructure if they occur  
5. **Use relative imports** within packages for maintainability  
6. **Place tests** in a separate `tests/` directory  
7. **Include a `setup.py`** for distribution (or use `pyproject.toml`)  

---

## `__init__.py` Usage Patterns

### Pattern 1: Empty File (Package Marker)

```python
# __init__.py
# No content - just marks package directory
```

### Pattern 2: Import Key Functions

```python
# __init__.py
from .core import main_function, helper_function
from .utils import utility_function

__all__ = ['main_function', 'helper_function', 'utility_function']
```

### Pattern 3: Package Initialization

```python
# __init__.py
import logging

# Configure logging for the package
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# Package metadata
__version__ = '1.0.0'
__author__ = 'Your Name'
```

### Pattern 4: Control `from package import *`

```python
# __init__.py
__all__ = ['module1', 'module2', 'public_function']
```

---

## Common Import Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError` | Module not installed or not in PATH | Install with `pip` or add to `sys.path` |
| `ImportError: attempted relative import beyond top-level` | Using relative import in top-level script | Use absolute imports or run as module |
| `ImportError: cannot import name` | Circular import or name not defined | Restructure code to avoid circularity |
| `ValueError: attempted relative import in non-package` | Running a script that uses relative imports | Use `python -m package.module` |

---

## Creating Distributable Packages

To share your package with others:

### 1. Create `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
        'numpy',
    ],
    author="Your Name",
    description="A sample Python package",
)
```

### 2. Build the Package

```bash
python setup.py sdist bdist_wheel
```

### 3. Install Locally

```bash
pip install -e .  # Editable (development) install
```

### 4. Upload to PyPI

```bash
pip install twine
twine upload dist/*
```

---

## Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)  
- [Creating a Python Package](https://packaging.python.org/tutorials/packaging-projects/)  
- [Python Import System Documentation](https://docs.python.org/3/reference/import.html)  
- [PEP 420 – Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)  
- [pip Documentation](https://pip.pypa.io/)  

---

*Packages are essential for organizing Python code in large projects.  
Understanding how to create, import, and distribute packages enables you  
to build maintainable and shareable software.*
