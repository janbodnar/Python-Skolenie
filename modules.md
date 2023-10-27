# Modules

A *module* is a file containing Python code. Python modules have the `.py` extension.  

Python code can be managed using:  

- functions
- classes
- modules
- packages

Python modules are used to organize Python code. For example, database related code is placed  
inside a database module, security code in a security module etc. Smaller Python scripts can have  
one module. But larger programs are split into several modules. Modules are grouped together  
to form packages.  

## Python module names

A module name is the file name with the `.py` extension. When we have a file called `empty.p`y, empty  
is the module name. The `__name__` is a variable that holds the name of the module being referenced.  
The current module, the module being executed (called also the main module) has a special name: `'__main__'`.  
With this name it can be referenced from the Python code. 

We have two files in the current working directory: `empty.py` and `test_empty.py`. The second module is the  
main module, which is executed. It imports the first module. Modules are imported using the import keyword.  

```python
"""
An empty module
"""
```

This is `empty.py` module. 

```python
#!/usr/bin/python

# test_empty.py

import empty
import sys

print(__name__)
print(empty.__name__)
print(sys.__name__)
```

In this code example we import two modules: the built-in module `sys` and one custom  
module `empty`. We print the names of modules to the console.  

```
$ ./test_empty.py
__main__
empty
sys
```

The name of the module, which is being executed is always `'__main__'`. Other modules are named after  
the file name. Modules can be imported into other modules using the `import` keyword.  

## Python locating modules

When a module is imported the interpreter first searches for a built-in module with that name.  
If not found, it then searches in a list of directories given by the variable `sys.path`.  
The `sys.path` is a list of strings that specifies the search path for modules. It consists of the  
current working directory, directory names specified in the `PYTHONPATH` environment variable,  
and some additional installation dependent directories. If the module is not found, an `ImportError`  
is raised.

```python
#!/usr/bin/python

# locating_modules.py

import sys
import textwrap

sp = sorted(sys.path)
dnames = ', '.join(sp)

print(textwrap.fill(dnames))
```

The script prints all directories from `sys.path` variable.

```python
import textwrap
```

The `textwrap` module is used for easy formatting of paragraphs.  

```python
sp = sorted(sys.path)
```

We retrieve a list of directories from the `sys.path` variable and sort them.

```python
dnames = ', '.join(sp)
```

We make a string out of the list.

```
$ ./locating_modules.py
/home/jano/.local/lib/python3.10/site-packages, /home/jano/tmp/py,
/usr/lib/python3.10, /usr/lib/python3.10/lib-dynload,
/usr/lib/python3/dist-packages, /usr/lib/python310.zip,
/usr/local/lib/python3.10/dist-packages
```

## Python import keyword

The `import` keyword can be used in several ways.

```python
from module import *
```

This imports all Python definitions into the namespace of another module.  
There is one exception. Objects beginning with underscore character `_` are not imported.  
They are expected to be used only internally by the module being imported. This way of  
importing modules is not recommended.  

```python
#!/usr/bin/python

# everything.py

from math import *

print(cos(3))
print(pi)
```

This import construct has imported all definitions from the built-in `math` module. We can call   
the math functions directly, without referencing the math module.  

```
$ ./everything.py
-0.9899924966004454
3.141592653589793
```

The use of this import construct may result in namespace pollution. We may have several objects  
of the same name and their definitions can be overridden. 

```python
#!/usr/bin/python

# pollution.py

from math import *

pi = 3.14

print(cos(3))
print(pi)
```

The example prints 3.14 to the console. Which may not be what we wanted. The namespace pollution  
may become critical in larger projects. 

## Python objects that are not imported

The following example shows definitions that are not being imported using this import construct.  

```python
#!/usr/bin/python

# names.py

"""
names is a test module
"""

_version = 1.0

names = ["Paul", "Frank", "Jessica", "Thomas", "Katherine"]

def show_names():

    for i in names:
       print(i)

def _show_version():

    print(_version)
```

This is the `names.py` module. It has a private variable and public and a private functions.  

```python
#!/usr/bin/python

# test_names.py

from names import *

print(locals())

show_names()
```

The `_version` variable and the `_show_version` function are not imported into the `test_names`  
module. We do not see them in the namespace. The `locals` function give us all the definitions  
available in the module.  

## Importing specific objects

With the from and `import` keywords, it is possible to import only some objects.  

```python
from module import fun, var
```

This import construct imports only specific objects from a module. This way we import only  
definitions that we need.

```python
#!/usr/bin/python

# import_specific.py

from math import sin, pi

print(sin(3))
print(pi)
```

We import two objects from the math module. There is no way how we could reference other  
definitions such as a `cos` function.

```python
#!/usr/bin/python

# imnames.py

from names import _version, _show_version

print(_version)
_show_version()
```

We could also import definitions beginning with an underscore. But this is a bad practice. 

```
$ ./imnames.py
1.0
1.0
```

## Python import module

The last construct is most widely used.

```python
import module
```

It prevents the namespace pollution and enables to access all definitions from a module.  

```python
#!/usr/bin/python

# impmod.py

import math

pi = 3.14

print(math.cos(3))
print(math.pi)
print(math.sin(3))
print(pi)
```

In this case, we reference the definitions via the module name. As we can see, we are able to use  
both `pi` variables. Our definition and the one from the `math` module.

```
$ ./impmod.py
-0.9899924966004454
3.141592653589793
0.1411200080598672
3.14
```

## Python aliasing modules

We can create an alias for the module with the as keyword.  

```python
#!/usr/bin/python

# importas.py

import math as m

print(m.pi)
print(m.cos(3))
```

We can change the name through which we can reference the module. To do this, we use  
the `as` keyword.

```
$ ./importas.py
3.14159265359
-0.9899924966
ImportError
```

An `ImportError` is raised if a module cannot be imported.  

```

#!/usr/bin/python

# importerror.py

try:
    import empty2
except ImportError as e:
    print('Failed to import:', e)
```

We have not created an `empty2` module. Therefore an exception is raised. 

```
$ ./importerror.py
Failed to import: No module named empty2
```

# Executing Python modules

Modules can be imported into other modules or they can be also executed. Module authors  
often create a testing suite to test the module. Only if the module is executed as a script,  
the `__name__` attribute equals to `'__main__'`.

We demonstrate this on a `fibonacci` module. Fibonacci numbers is a sequence of numbers,  
where each is the sum of its two immediate predecessors. 

```python
#!/usr/bin/python

# fibonacci.py

"""
A module containing the fibonacci
function.
"""

def fib(n):

    a, b = 0, 1

    while b < n:

        print(b, end=" ")
        (a, b) = (b, a + b)


# testing

if __name__ == '__main__':
    fib(500)
```

The module can be normally imported as usual. The module can be also executed.  

```
$ ./fibonacci.py
1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

If we do import the `fibonacci` module, the test is not executed automatically.  

```
>>> import fibonacci as fib
>>> fib.fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

The `fibonacci module` is imported and the `fib` function is executed.

## Python dir function

The built-in `dir` function gives a sorted list of strings containing the names
defined by a module.


```python
#!/usr/bin/python

# dirfun.py

"""
This is dirfun module
"""

import math, sys

version = 1.0

names = ["Paul", "Frank", "Jessica", "Thomas", "Katherine"]

def show_names():

   for i in names:
      print(i)

print(dir())
```

In this module, we import two system modules. We define a variable, a list and a function.  

```python
print(dir())
```

The `dir` function returns all the names available in the current namespace of the module.  

```
$ ./dirfun.py
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', 'math', 'names', 'show_names', 'sys', 'version']
```

We can see some built-in names like `'__file__'` or `'__name__'` and all the others that we have  
defined and imported. 

## Python globals function

The `globals` function returns a dictionary that represents the current global namespace. It is  
a dictionary of global names and their values. It is the dictionary of the current module.  

```python
#!/usr/bin/python

# globalsfun.py

import textwrap

version = 1.0

def myfun():
    pass

gl = globals()
gnames = ', '.join(gl)

print(textwrap.fill(gnames))
```

We use the globals function to print all the global names of the current module.

```
$ ./globalsfun.py
textwrap, __package__, version, __builtins__, __name__, __spec__,
__doc__, gl, __cached__, myfun, __loader__, __file__
These are the global names of the current module.
```

## Python __module__ attribute

The `__module__` class attribute has the name of the module in which the class is defined.   

```python
"""
module animals
"""

# animals.py

class Cat:
    pass

class Dog:
    pass
```

This are the contents of the `animals.py` file. We have two classes.

```python
#!/usr/bin/python

# mclass.py

from animals import Cat

class Being:
    pass

b = Being()
print(b.__module__)

c = Cat()
print(c.__module__)
```

In this code we use the `__module__` attribute.

```python
from animals import Cat
```

From the `animals` module, we import the `Cat` class.

```python
class Being:
    pass
```

In the current module, we define a class `Being`. 

```python
b = Being()
print(b.__module__)
```

An instance of the `Being` class is created. We print the name of its module.

```python
c = Cat()
print(c.__module__)
```

We create an object from the `Cat` class. We also print the module where it was defined.  

```
$ ./mclass.py
__main__
animals
```

The current module's name is `'__main__'`. And the Cat's module name is animals.
