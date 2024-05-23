# Exceptions 

Errors detected during code execution are called `excepitons`.  

- full disk
- logical errors 
- syntax error
- unsufficient permissions


## Handling exceptions 

```python
try:
   # do something

except ValueError:
   # handle ValueError exception

except (IndexError, ZeroDivisionError):
   # handle multiple exceptions
   # IndexError and ZeroDivisionError

except:
   # handle all other exceptions

finally:
   # cleanup resources
```

## ValueError 

Value error is raised when invalid value is received.  

```python
try:
    x = int(input("Please enter a number: "))
    y = int(input("Please enter another number: "))

    print(f'addition: {x + y}')
    print(f'multiplication: {x * y}')

except ValueError:
    print("invalid number")
```

