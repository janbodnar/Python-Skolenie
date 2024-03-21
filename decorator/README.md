# Python decorators


## Defining via a class

```python
class Power:
    def __init__(self, arg):
        self._arg = arg
        print(f'{arg} {type(arg)}')

    def __call__(self, *param_arg):
        """If there are decorator arguments, __call__() is only called once
        as part of the decoration process. You can only give it a single argument,
        which is the function object
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
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


The `__call__` method in the `Power` class serves two different purposes depending on the  
context in which it's used. This is why it can either return a wrapper function or the  
result of an expression.

1. **Returns a Wrapper Function**: When the `Power` class is used as a decorator with an  
  argument (like `@Power(3)`), the `__call__` method receives the decorated function as its  
  argument. In this case, it defines a wrapper function that takes two arguments, calls the  
  decorated function with these arguments, and returns the result raised to the power of  
  `self._arg`. This wrapper function is then returned by the `__call__` method and replaces  
  the original decorated function. This is why when you call `multiply_together(2, 2)`, you're  
  actually calling the wrapper function, which returns `64`.  

7. **Returns the Result of an Expression**: If the `Power` class is used as a decorator without  
  an argument (not demonstrated in the provided code), the `__call__` method would receive the arguments  
  of the decorated function. In this case, it calculates the result of the decorated function, raises it  
  to the power of `2`, and returns this value. This behavior is defined in the `else` block of  
  the `__call__` method.  

The ability to return different types of values based on the context is a powerful feature  
of Python, allowing for flexible and dynamic behavior. In the context of decorators, this allows the same  
class to be used as a decorator in multiple ways, either with or without arguments. The `__call__` method  
is central to this functionality, defining the behavior of the decorator when it's applied to a function.
