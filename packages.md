# Packages

A *package* is a collection of modules which have a common purpose. Package directories must have one special  
file called `__init__.py`. (Since Python 3.3, `__init__.py` is no longer required to define package directories.)  
A Python module is a single Python file.

When we deal with large projects containing hundreds or thousands of modules, using packages is crucial. For example,  
we could put all database related modules in a database package and user interface code in `ui` package. 

Built-in packages available in predefined directories; for instance, `/usr/lib/python3.5` on Debian Linux or  
`C:\Users\Jano\AppData\Local\Programs\Python\Python36-32\Lib\site-packages`.  

Third-party packages are installed into predefined directories such as `/usr/local/lib/python3.5/dist-packages`  
on Debian Linux or `C:\Users\Jano\AppData\Local\Programs\Python\Python36-32\libs` on Windows.  

## Python package management

Python packages are managed with the Python package manager `pip`.  

`$ sudo pip3 install arrow`  

For instance, the `arrow` library is installed with the above command.  

`$ sudo pip3 uninstall arrow`  

To uninstall arrow, we use the above command.

## Python package with empty __init__.py

In the first example, we create a simple package in Python.

```
$ tree
.
├── mymath
│   ├── __init__.py
│   └── mfuns.py
└── myprog.py
```

In our current working directory we have a mymath directory and a `myprog.py` script. The `mymath`  
contains the `__init__.py` file, which marks the `mymath` directory as a package directory.

The `mymath` directory has two files: the `__init__.py` file makes constants a Python package  
directory and the `mfuns.py` is a Python module.

The `__init__.py` is blank. It can contain some code but it can be also empty.  

```python
# mfuns.py

def mycube(x):

   return x * x * x 
```

In the `mfuns.py` module, we have a definition of a cube function.  

```python
#!/usr/bin/python

# myprog.py

from mymath.mfuns import mycube

print(mycube(3))
```

In the `myprog.py` program, we import the `mycube` function from th mymath.mfuns module.  
The module name and the package name is separated with a dot character.  

## Importing function in __init__.py

In the next example, we have some code in the `__init__.py` file.

```
$ tree
.
├── mymath
│   ├── __init__.py
│   └── mfuns.py
└── myprog.py
```

We have the same directory structure.

```python
# __init__.py

from .mfuns import mycube
```

In the `__init__.py` file, we import the `mycube` function. As a consequence, we do not have to  
specify the module name when we refer to the `mycube` function from the `mymath` package.

```python
# mfuns.py

def mycube(x):

   return x * x * x 
```

In the `mfuns.py` module, we have a definition of a cube function.  

```python
#!/usr/bin/python

# myprog.py

from mymath import mycube

print(mycube(3))
```

In the `myprog.py` program, we import the `mycube` function. This time we have omitted the module name.

## Package without __init__.py

Since Python 3.3 it is possible to define package directories without using the `__init__.py` file.

```
read.py
constants/
    data.py 
```

In our current working directory we have a constants directory and a `read.py` script.

```python
# data.py
colours = ('yellow', 'blue', 'red', 'orange', 'brown')
names = ('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
```

The `data.py` module has two tuples.

```python
#!/usr/bin/python

# read.py

from constants.data import colours
import constants.data as mydata

print(colours)
print(mydata.names)
```

In the `read.py` script we import the tuples and print them to the terminal.

```
$ ./read.py 
('yellow', 'blue', 'red', 'orange', 'brown')
('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
```

## The arrow package

The `arrow` is a third-party library for working with date and time in Python.

```
$ ls /usr/local/lib/python3.5/dist-packages/arrow
api.py  arrow.py  factory.py  formatter.py  __init__.py  
locales.py  parser.py  __pycache__  util.py
```

The library is installed in the arrow directory, under the dist-packages in Debian Linux.  
The library is installed with the pip package manager. As we can see, the library is a collection  
of Python modules.

## Python subpackages

We can also create subpackages. To access subpackages, we use the dot operator.

```
$ tree
.
├── constants
│ ├── __init__.py
│ ├── data.py
│ └── numbers
│     ├── __init__.py
│     └── myintegers.py
└── read.py
```

```python
from .data import names
```

This is the `__init__.py` file in the constants directory. We import the names tuple.  

```python
names = ('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
```

This is the `data.py` module in the constants directory. It contains the `names` tuple.  

```python
from .myintegers import myintegers
```

The `__init__.py` file in the numbers package has this one line.

```python
myintegers = (2, 3, 45, 6, 7, 8, 9)
```

The integers module defines a tuple of seven integers. This tuple will be accessed from the `read.py` script.
  
```python
#!/usr/bin/python

# read.py

from constants import names
from constants.numbers import myintegers

print(names)
print(myintegers)
```

This is the `read.py` program. We import the names tuple from the constants package and the `myintegers`  
tuple from the `constants.numbers` subpackage.

```
$ ./read.py 
('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
(2, 3, 45, 6, 7, 8, 9)
```
