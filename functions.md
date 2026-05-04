# Functions

A function is a mapping of zero or more input parameters to zero or more output parameters.

The advantages of using functions are:

- code organization
- reducing duplication of code
- decomposing complex problems into simpler pieces
- improving clarity of the code
- reuse of code
- information hiding

Functions in Python are first-class citizens. It means that functions have equal  
status with other objects in Python. Functions can be assigned to variables, stored  
in collections, or passed as arguments. This brings additional flexibility to the language.  

[Function definition](#function-definition)  
[Kinds of functions](#kinds-of-functions)  
[Third-party functions](#third-party-functions)  
[Docstrings](#docstrings)  
[Instance, class, plain, inner functions](#instance-class-plain-inner-functions)    
[Functions are objects](#functions-are-objects)  
[Function scope](#function-scope)  
[Implicit arg value](#implicit-arg-value)   
[Unpacking](#unpacking)  
[Passing by reference](#passing-by-reference)  
[Global variables](#global-variables)  
[The pass keyword](#the-pass-keyword)  
[Returning values](#returning-values)  
[Arbitrary number of args](#arbitrary-number-of-args)  
[Nested functions](#nested-functions)  
[Passing functions as parameters](#passing-functions-as-parameters)  
[Function redefinition](#function-redefinition)  
[No function hoisting](#no-function-hoisting)  
[Collection of functions](#collection-of-functions)  
[Annotations](#annotations)  
<!--[Closures](#closures)  -->

## Function definition

Functions are defined with the `def` keyword.  

```python
#!/usr/bin/python

# fahrenheit.py

def cel_to_fahr(c):
    return c * 9/5 + 32

print(cel_to_fahr(100))
print(cel_to_fahr(0))
print(cel_to_fahr(30))
```

## Kinds of functions

- built-in readily available
- standard in modules
- custom

```python
#!/usr/bin/python

from math import sqrt

def cube(x):
    return x * x * x    
    
print(abs(-1))
print(cube(9))
print(sqrt(81))
```

## Third-party functions

Third-party functions defined in external modules.  
For instance, the `numpy` module.  

    $ pip install numpy


```python
#!/usr/bin/python

import numpy as np

# generate 10 random integers from 1 to 100
r_vals = np.random.randint(1, 100, 10)
print(r_vals)

# generate 1 random integer from 1 to 10
r_vals2 = np.random.randint(1, 10)
print(r_vals2)

# generate an array of random integers
r_vals3 = np.random.randint(5, size=(2, 4))
print(r_vals3)
```

## Docstrings

A docstring is a string literal placed as the first statement inside a function,  
class, or module. It describes what the function does, its parameters, its return  
value, and any exceptions it may raise. The conventions follow PEP 257.  

```python
#!/usr/bin/python

# docstrings.py

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return celsius * 9/5 + 32

# Accessing the docstring
print(celsius_to_fahrenheit.__doc__)

# The built-in help() function displays the docstring nicely.
help(celsius_to_fahrenheit)
```

Good docstrings make code more readable and enable tools like pydoc or IDE  
hints to provide instant documentation.  

## Instance, class, plain, inner functions

Functions defined inside classes are member functions. They are  
often called methods.  

```python
#!/usr/bin/python

class Info:

    def say(self):
        print('This is Info class')

class Some:

    @staticmethod
    def f():
        print ("f() static method")

def f():
    print ("f() plain function")

def g():
    def f():
        print ("f() inner function")
    f()


i = Info()
i.say()

Some.f()
f()
g()
```

`self` is a reference to the current instance of a class. It's how an  
object refers to itself, allowing each instance to access its own data  
and methods.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


c = Circle(5)
print("Area:", c.area())
print("Circumference:", c.circumference())

c2 = Circle(10)
print("Area of c2:", c2.area())
print("Circumference of c2:", c2.circumference())
```

`self` must be the first parameter in every instance method — it's a   
Python convention (you could name it anything, but self is universal)  
You never pass it manually — Python injects it automatically when you call `c.area()`  
It's not a keyword — it's just a strongly followed naming convention.


## Functions are objects 

Object attributes are accessed with the dot operator.  
The `object` is the mother of all objects in Python; every Python  
object implicitly derives from `object`.  

```python
#!/usr/bin/python

# functions in Python are objects

def f():
    """This function prints a message """
    return 'f() function'

print(isinstance(f, object))
print(id(f))
print(f())

print(f.__doc__)
print(f.__name__)
```

---

In Python, everything is an object.  

```python
#!/usr/bin/env python

import sys

def f():
    pass

print(type(1))
print(type(""))
print(type([]))
print(type({}))
print(type(()))
print(type(object))
print(type(f))
print(type(sys))
```

## Function scope 

Variables defined inside a function have a function scope. They are also  
called local variables.  

```python
#!/usr/bin/python

# a local variable is valid in the 
# function scope

name = "Jack"

def f():
   name = "Robert"
   print("Within function", name)

print("Outside function", name)
f()
```

## Implicit arg value 

```python
#!/usr/bin/python

def power(x, y=2):

    r = 1

    for i in range(y):
        r = r * x

    return r

print(power(3))
print(power(3, 3))
print(power(5, 5))
```

## Unpacking 

Unpacking is cutting an object (such as a list) into its elements.  
It is also called destructuring.  The _ operator is used to ignore the  
value. The * operator eagerly takes all elements until the next  
argument.  

Unpacking function return values

```python
#!/usr/bin/python

def fn():
    return [1, 2, 3, 4, 5, 6]

a, b, c, d, e, f = fn()
print(a, b, c, d, e, f)

a, *mid, b = fn()
print(a, mid, b)

a, b, c, _, _, _ = fn()
print(a, b, c)

a, b, *_ = fn()
print(a, b)

a, b, c, *d = fn()
print(a, b, c, d)

*a, b, c, d = fn()
print(a, b, c, d)
```

Unpacking function arguments

After the star operator, only keyword arguments can be used.  

```python
#!/usr/bin/python

def fn(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

def fn2(a, b, c, *d):
    print(a, b, c, d)

def fn3(a, b, c, *d, e, f):
    print(a, b, c, d, e, f)

fn(1, 2, 3, 4, 5, 6)
fn2(1, 2, 3, 4, 5, 6)
fn3(1, 2, 3, 4, e=5, f=6)
```
--- 

A list can be destructured into elements and passed to the function.  

```python
#!/usr/bin/python

def fn(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

def fn2(a, b, c, *d):
    print(a, b, c, d)

def fn3(a, b, c, *d, e, f):
    print(a, b, c, d, e, f)

vals = [1, 2, 3, 4, 5, 6]

fn(*vals)
fn2(*vals)
fn3(*vals, e=7, f=8)
```


The `**kwargs` defines a keyworded, variable-length argument list

```python
#!/usr/bin/python

def display(**user):

    for k, v in user.items():
        print(f'{k}: {v}')


display(name='Lary Jones', age=43, sex='M')
display(name='Jone Doe', occupation='gardener', age=35)
```

In Python, a function defined with only `**kwargs` like `def display(**user)`  
accepts any number of keyword arguments and stores them as a **dictionary**.  
Inside the function, `user.items()` is used to iterate over the dictionary,  
returning each key-value pair as `k` and `v`, which are then printed using an f-string.  

The real power here is **flexibility** — notice that the two calls to `display()` don't  
need to pass the same arguments. The first call passes `name`, `age`, and `sex`, while  
the second passes `name`, `occupation`, and `age`. The function handles both without  
any changes, because `**kwargs` doesn't care how many or which keyword arguments are  
passed — it simply captures whatever is given into a dictionary and works with it dynamically.  

--- 

```python
#!/usr/bin/python

def show(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

show(1, 2, 3, 4, 5, 6, name='John Doe', occupation='gardener', age=34)
```

In Python, functions can be made highly flexible using `*args` and `**kwargs`.  
When defining a function like `def show(a, *args, **kwargs)`, the regular parameter `a`  
captures the first positional argument, `*args` collects any additional positional  
arguments into a **tuple**, and `**kwargs` collects any keyword (named) arguments  
into a **dictionary**. So calling `show(1, 2, 3, name='John')` would  
give `a=1`, `args=(2, 3)`, and `kwargs={'name': 'John'}`. 

When it comes to positioning, the order strictly matters — regular parameters  
must come **first**, followed by `*args`, and finally `**kwargs` must always be  
**last**. Writing them in any other order, such as placing `**kwargs` before  
`*args`, will raise a `SyntaxError`. This ordering rule ensures Python can  
unambiguously separate plain values, extra positional values, and named values  
from one another when the function is called.

---

This code demonstrates using `**` to **unpack a dictionary** directly into  
a function call. The `display` function expects three named parameters —  
`name`, `occupation`, and `age` — and when called with `**u1`, Python unpacks  
the dictionary so that each key maps to its matching parameter by name. 

```python
#!/usr/bin/python

def display(name, occupation, age):

    print(f'{name}, {occupation}, {age}')

u1 = {'name': 'Lary Jones', 'occupation': 'driver', 'age': 45}
u2 = {'name': 'Jone Doe', 'occupation': 'gardener', 'age': 35}

display(**u1)
display(**u2)
```

This is essentially the reverse of `**kwargs` — instead of collecting keyword  
arguments into a dictionary inside the function, here you're spreading  
a dictionary out into keyword arguments at the call site. It's a clean and  
practical pattern when your data is already stored in a dictionary and matches  
the function's parameter names, saving you from having to write `display(name=u1['name'], occupation=u1['occupation'], age=u1['age'])` manually.


## Positional and keyword only

Python 3.8 introduced the / parameter to specify that all parameters before it  
must be passed positionally. Similarly, a single * marks the beginning of  
keyword-only parameters. This allows API designers to enforce a strict  
calling convention.  

```python
#!/usr/bin/python

# position_only_example.py

def describe_person(first, last, /, title='', *, age, city):
    """
    Print a person's description.
    first, last  -> positional-only (before /)
    title        -> optional, positional or keyword (between / and *)
    age, city    -> keyword-only, required (after *)
    """
    full = f"{title + ' ' if title else ''}{first} {last}"
    print(f"{full}, age {age}, from {city}")

# Valid calls
describe_person("Jane", "Doe", "Dr.", age=30, city="New York")  # title passed positionally
describe_person("John", "Smith", age=45, city="London")          # title omitted, uses default ''

# Invalid calls
# describe_person(first="Jane", last="Doe", age=30, city="NY")   # Error: first and last are positional-only
# describe_person("Jane", "Doe", 30, "NY")                       # Error: age and city must be passed as keywords
```

The function signature `def describe_person(first, last, /, title='', *, age, city)`  
demonstrates all three parameter zones in one definition. first and last sit   
before the /, making them positional-only — they cannot be passed by name. title    
sits between / and *, meaning it's flexible and can be passed either positionally    
or as a keyword, and since it has a default value of '' it's also optional.   
age and city come after the bare *, making them keyword-only — they must always    
be passed by name like age=30, and since they have no defaults, they are required.   
 
Using / and * together gives API designers precise control over how a function   
must be called, prevents accidental reliance on parameter names that might change   
in future versions, and makes the intended calling convention immediately visible   
from the signature itself.  


## Passing by reference 

In Python, mutable objects are passed by reference as function arguments.  
A list is passed by reference to the function. Therefore, the original list is  
modified inside a function.  

```python
#!/usr/bin/python

n = [1, 2, 3, 4, 5]

print('Original list:', n)

def f(x):

    x.pop()
    x.pop()
    x.insert(0, 0)
    print('Inside f():', x)

f(n)

print('After function call:', n)
```

## Global variables 

Global variables are defined in module.  
Global variables are automatically valid in functions.  
```python
#!/usr/bin/python

name = "Jack"

def f():
   print("Within function", name)

print("Outside function", name)
f()
```

---

 The `global` keyword allows us to modify the variable outside  
 of the current scope.

```python
#!/usr/bin/python

name = "Jack"

def f():
    
   global name 
   name = "Robert"
   print ("Within function", name)


print("Outside function", name)
f()
print("Outside function", name)
```

## The pass keyword 

The `pass` keyword is used to define functions that are not yet implemented.  

```python
#!/usr/bin/python

def f():
    pass

def g():
    pass
  
def h():
    return 'h fun'

print(f())
print(g())
print(h())

print(f.__name__)
print(g.__name__)
print(h.__name__)
```

## Returning values 

The `return` keyword is used to return values from functions.  
A function returns `None` if no keyword is defined.  

```python
#!/usr/bin/python

# returning.py

def showMessage(msg):

    print(msg)


def cube(x):

    return x * x * x


x = cube(3)
print(x)

showMessage("Computation finished.")
print(showMessage("Ready."))
```

---

We can return multiple values with tuples.  

```python
#!/usr/bin/python

n = [1, 2, 3, 4, 5]

def stats(x):

    mx = max(x)
    mn = min(x)
    ln = len(x)
    sm = sum(x)

    return mx, mn, ln, sm

mx, mn, ln, sm = stats(n) # deconstruction
print(stats(n))

print(mx, mn, ln, sm)
```

## Arbitrary number of args 

With `*` operator, function can accept arbitrary number of arguments.  

```python
#!/usr/bin/python

def do_sum(*args):
   '''Function returns the sum 
   of all values'''
   
   r = 0
   
   for i in args:
      r += i
      
   return r


print(do_sum.__doc__)
print(do_sum(1, 2, 3))
print(do_sum(1, 2, 3, 4, 5))
```


## Nested functions

Nested/inner functions are functions defined inside other functions.  

```python
#!/usr/bin/python

# nested functions are functions defined inside other
# functions

def myfun():
    print("inside myfun()")

    def greet():
        return "greeting message"

    def welcome():
        return "welcoming message"

    print(greet())
    print(welcome())
    print("inside myfun()")

myfun()
```

## Passing functions as parameters 

Functions can be passed to other functions as parameters. 

```python
#!/usr/bin/python

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(fun, x):

    res = fun(x)
    return res

x = 2

print(operate(inc, x))
print(x)

print(operate(dec, x))
print(x)
```

## Function redefinition

Python allows to redefine existing function definitions.  

```python
#!/usr/bin/python

# redefinition.py

from time import gmtime, strftime


def showMessage(msg):

    print(msg)


showMessage('Ready.')


def showMessage(msg):

    print(strftime('%H:%M:%S', gmtime()))
    print(msg)


showMessage('Processing.')
```

## No function hoisting 

Functions must be defined before being called. Python does not support  
function hoisting like JavaScript.  

```python
#!/usr/bin/python

def f1():
    print("f1()")


f1()
# f2()


def f2():
    print("f2()")
```

## Collection of functions

Python is flexible, it allows to store functions in collections.  

```python
#!/usr/bin/python

def f():
    pass

def g():
    pass
  
def h(f):
    print (id(f))
  
a = (f, g, h)

for i in a:
    print(i)
    
h(f)
h(g)
```

## Annotations

Python allows you to annotate the parameters and return value of a function with  
arbitrary expressions. When used to specify expected data types, they are called  
type hints (standardised in PEP 484). The Python runtime does not enforce  
type hints, but they serve as live documentation and are checked by static  
analysers like `mypy`.  

Enforce type checking in VS Code with `"python.analysis.typeCheckingMode": "basic"`. 

```python
#!/usr/bin/python

# annotations.py

def greet(name: str, times: int = 1) -> str:
    """Return a greeting repeated *times* times."""
    return (f"Hello, {name}!\n" * times).rstrip()

print(greet("Alice", 2))
print(greet("Bob"))          # uses default times=1

# Annotations are stored in the __annotations__ attribute
print(greet.__annotations__)  
```

Annotations can be any Python expression, not just types, though type hints are  
by far the most common use case. They improve code clarity and enable better  
autocompletion and linting in modern editors.  

<!--
## Closures 

A *closure* is a function that has access to variables in its outer (enclosing) function's scope,  
even after the outer function has returned. This concept is fundamental in functional programming  
languages and is often used to create self-contained functions with their own private state. 

Key characteristics of a closure:  

- Function: A closure is always a function.
- Access to Outer Variables: It has access to variables defined in its outer function's scope.  
- Persistence of State: The outer function's variables remain accessible even after the outer  
  function has finished executing.


```python
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def get_count():
        return count

    return increment, get_count

increment, get_count = create_counter()

for _ in range(5):
    increment()

print(get_count())  # Output: 5
```

Common Use Cases:

- Creating private variables: Closures can be used to create variables that are private  
  to a specific function or module.
- Implementing callbacks: Closures can be used to create functions that can be passed as  
  arguments to other functions, capturing specific state.  
- Decorators: Closures are often used to implement decorators, which are functions that  
  modify the behavior of other functions.  
- Memoization: Closures can be used to implement memoization techniques, which can improve  
  performance by caching the results of function calls.  
-->

