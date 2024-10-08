# Python decorators

A **Python decorator** is a callable that takes a function as input, modifies or  
extends its behavior, and returns the modified function. Decorators provide a  
syntax-friendly way to enhance or alter the functionality of functions or methods  
without changing their source code. They are prefixed with an `@` symbol and  
placed immediately before the function definition.  

## Simple example 

```python
def enclose(fun):
    def wrapper():
        print("------------------------------")
        fun()
        print("------------------------------")

    return wrapper


def myfun():
    print("myfun")


enc = enclose(myfun)
enc()
```

The `enclose` function is a decorator which extends the decorated function by  
adding star symbols to its output.


Python allows to use the `@` symbol to mark the method to be decorated with  
a decorator. Functionally, the example is equivalent to the previous one. Only  
different syntax is used.  

```python
def enclose(fun):

    def wrapper():

        print("------------------------------")
        fun()
        print("------------------------------")

    return wrapper

@enclose
def myfun():
    print("myfun")

myfun()
```



## Timing decorator 

```python
import time
import math
import sys

sys.set_int_max_str_digits(maxdigits=90000)

def timer(func):

    def wrapper(*args, **kwargs):

        begin = time.time()

        f = func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

        return f

    return wrapper


@timer
def factorial(num):

    return math.factorial(num)

f = factorial(4580)
print(f)
```


## Multiple decorators

Decorators can be stacked.  

```python
def strong(fun):

    def wrapper():
        return f'<strong>{fun()}</strong>'
    return wrapper

def em(fun):

    def wrapper():
        return f'<em>{fun()}</em>'

    return wrapper


@strong
@em
def message():
    return 'This is some message'


print(message())
```

## Defining via a class

```python
class Power:
    def __init__(self, arg):
        self._arg = arg
        print(f'{arg} {type(arg)}')

    def __call__(self, *param_arg):
        if len(param_arg) == 1:

            def wrapper(a, b):
                retval = param_arg[0](a, b)
                return retval**self._arg

            return wrapper
        else:
            expo = 2
            retval = self._arg(param_arg[0], param_arg[1])
            return retval**expo


@Power(4)
def multiply_together(a, b):
    return a * b

print(multiply_together(2, 2))
```


## Explanation

### The __init__ method 

The `__init__` method in the `Power` class is a special method in Python,  
known as a constructor. It is automatically called when an instance of the  
class is created. It is used to initialize the attributes of the class.  

In this case, the `__init__` method takes one argument `arg`, which can be  
either a function or a number, depending on how the `Power` class is used:  

1. **As a Decorator with an Argument**: When the `Power` class is used as a  
decorator with an argument (like `@Power(3)`), the argument passed to  
`__init__` is the number `3`. This number is stored in `self._arg` and is  
used as the exponent in the `__call__` method.  

2. **As a Decorator without an Argument**: If the `Power` class is used as a  
decorator without an argument (not demonstrated in the provided code), the  
function to be decorated would be passed to `__init__`. In this case,  
`self._arg` would be a function, which is why the `__call__` method can call  
`self._arg(param_arg[0], param_arg[1])` in the `else` block.  

This flexibility in the `__init__` method allows the `Power` class to be used  
as a decorator in multiple ways, either with or without arguments. The type  
of `self._arg` determines the behavior of the `__call__` method, which in  
turn defines the behavior of the decorated function.  


### The __call__ method

The `__call__` method in the `Power` class serves two different purposes depending  
on the context in which it's used. This is why it can either return a wrapper function  
or the result of an expression.

1. **Returns a Wrapper Function**: When the `Power` class is used as a decorator with an  
  argument (like `@Power(3)`), the `__call__` method receives the decorated function as its  
  argument. In this case, it defines a wrapper function that takes two arguments, calls the  
  decorated function with these arguments, and returns the result raised to the power of  
  `self._arg`. This wrapper function is then returned by the `__call__` method and replaces  
  the original decorated function. This is why when you call `multiply_together(2, 2)`,  
  you're actually calling the wrapper function, which returns `64`.  

7. **Returns the Result of an Expression**: If the `Power` class is used as a decorator without  
  an argument (not demonstrated in the provided code), the `__call__` method would receive the  
  arguments of the decorated function. In this case, it calculates the result of the decorated  
  function, raises it to the power of `2`, and returns this value. This behavior is defined in  
  the `else` block of the `__call__` method.  

The ability to return different types of values based on the context is a powerful feature  
of Python, allowing for flexible and dynamic behavior. In the context of decorators, this allows the same  
class to be used as a decorator in multiple ways, either with or without arguments. The `__call__` method  
is central to this functionality, defining the behavior of the decorator when it's applied to a function.
