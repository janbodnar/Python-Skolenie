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
