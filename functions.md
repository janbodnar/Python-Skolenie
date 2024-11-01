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
[Closures](#closures)  

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

Unpacking is cutting an object (such as a list) into its elements. It is also called destructuring.  
The _ operator is used to ignore the value. The * operator eagerly takes all elements until the next  
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

Unpacking keyworded arguments

The `**kwargs` defines a keyworded, variable-length argument list

```python
#!/usr/bin/python

def display(**user):

    for k, v in user.items():
        print(f'{k}: {v}')


display(name='Lary Jones', age=43, sex='M')
display(name='Jone Doe', occupation='gardener', age=35)
```
--- 

```python
#!/usr/bin/python

def show(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

show(1, 2, 3, 4, 5, 6, name='John Doe', occupation='gardener', age=34)
```

```python
#!/usr/bin/python

def display(name, occupation, age):

    print(f'{name}, {occupation}, {age}')

u1 = {'name': 'Lary Jones', 'occupation': 'driver', 'age': 45}
u2 = {'name': 'Jone Doe', 'occupation': 'gardener', 'age': 35}

display(**u1)
display(**u2)
```


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


