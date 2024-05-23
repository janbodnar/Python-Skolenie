# Exceptions 

Errors detected during code execution are called `exceptions`.  

- full disk
- logical errors 
- syntax error
- unsufficient permissions


`Warnings` are alerts generated during code compilation or execution. Unlike exceptions,  
warnings do not halt program execution. They indicate potential problems but allow the  
program to continue.

Warnings can arise from issues like deprecated functions, unused variables, or type  
mismatches. Developers should review and address warnings to improve code quality, but they  
don't require immediate action.  


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

## List of basic exceptions 



- `ZeroDivisionError:` - raised when division or modulo operation is performed with zero  
  as the divisor  
- `NameError:` - raised when a local or global name is not found  
- `IndentationError:` - raised when there is incorrect indentation in the code  
- `IOError:` - raised when an input/output operation fails (e.g., file not found)  
- `EOFError:` - raised when the end of the file is reached unexpectedly  
- `TypeError:` - raised when an operation or function is applied to an object of inappropriate type  
- `ValueError:` - raised when a built-in operation or function receives an argument of the  
  correct type but an inappropriate value  
- `IndexError:` - raised when a sequence subscript is out of range  
- `KeyError:` - raised when a dictionary key is not found  
- `AttributeError:` - raised when an attribute reference or assignment fails  
- `ImportError:` - raised when an import statement fails to find the specified module  
- `AssertionError:` - raised when an assert statement fails  
- `RuntimeError:` - raised when an error occurs that doesn’t belong to any specific category  
- `MemoryError:` - raised when an operation runs out of memory  
- `FileNotFoundError:` A specific type of IOError - raised when a file is not found  
- `PermissionError:` - raised when trying to perform an operation without the required permissions  
- `OverflowError:` - raised when an arithmetic operation exceeds the limits of the data type  
- `RecursionError:` - raised when the maximum recursion depth is exceeded  
- `SystemExit:` - raised when the `sys.exit()` function is called  
- `KeyboardInterrupt:` - raised when the user interrupts the program (e.g., by pressing `Ctrl+C`)  


## Returning errors 

Some programming languages, including C, Go and Rust, do not work with exceptions.  
They work with errors that are returned from functions.  

```go
package main

import (
    "fmt"
    "io/ioutil"
    "log"
)

func main() {

    content, err := ioutil.ReadFile("thermopylae.txt")

     if err != nil {
          log.Fatal(err)
     }

    fmt.Println(string(content))
}
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

## Exception object 

We can receive information about the exception from the exception object.  

```python
try:
    x = int(input("Please enter a number: "))
    y = int(input("Please enter another number: "))

    print(f'addition: {x + y}')
    print(f'multiplication: {x * y}')

except ValueError as e:
    print("invalid number")
    print(e)
```

## ZeroDivisionError 

`ZeroDivisionError` is thrown when we try to divide by zero.   

```python
def input_numbers():

    a = float(input("Enter numerator:"))
    b = float(input("Enter denominator:"))
    return a, b

x, y = input_numbers()

try:
    print(f"{x} / {y} is {x/y}")

except ZeroDivisionError:

    print("Cannot divide by zero")
```

Rather than catching the exception, we can fix the code by  
adding the `if b == 0` condition.   

```python
import sys

def input_numbers():

    a = float(input("Enter numerator:"))
    b = float(input("Enter denominator:"))

    if b == 0:
        print('cannot divide by zero')
        sys.exit(1)

    return a, b


x, y = input_numbers()


print(f"{x} / {y} is {x/y}")
```

## IndexError 

`IndexError` is handled by fixing the logical error in the application.  

```python
import random

words = ['sky', 'word', 'blue', 'cop', 'atom', 'car']

r_idx = random.randint(0, len(words))
rword = words[r_idx]

print(f'random word: {rword}')
```

We pass `len(words) - 1)` into the function.  

## ImportError 

```python
import sys

try:
    import requests
except ImportError:
    print('please install requests library')
    sys.exit(1)

url = 'https://webcode.me'
resp = requests.get(url)

content = resp.content.decode('utf8')
print(content)
```

## OverFlowError

`OverFlowError` - result is too large to be represented.  

```python
try:
    f = 3.0

    for _ in range(100):
        f = f ** 2
        print(f)

except OverflowError as err:
    print('Overflowed after', f, err)
```

## Raising exceptions 

Exceptions can be raised by programmers with the `raise` keyword.  

```python
def read_age():

    age = int(input("Enter your age: "))

    if age < 0 or age > 130:
        raise ValueError("Invalid age")

    return age


try:
    val = read_age()
    print(f"Your age is {val}")

except ValueError as e:
    print(e)
```

## Custom exception 

Custom exceptions can be created by inheriting from the base `Exception` class.  

```python
class InvalidAgeError(Exception):
    def __init__(self, value):
        self.par = value

    def __str__(self):
        return f"InvalidAgeError: {self.par}"


def read_age():

    age = int(input("Enter your age: "))

    if age < 0 or age > 130:
        raise InvalidAgeError(f"{age} is not a valid human age")

    return age


try:
    val = read_age()
    print(f"Your age is {val}")

except InvalidAgeError as e:
    print(e)
```

## Multiple exceptions 

Multiple exceptions can be handled by multiple `catch` arms.  

```python
class InvalidAgeError(Exception):
    def __init__(self, value):
        self.par = value

    def __str__(self):
        return f"InvalidAgeError: {self.par}"


def read_age():

    age = int(input("Enter your age: "))

    if age < 0 or age > 130:
        raise InvalidAgeError(f"{age} is not a valid human age")

    return age


try:
    val = read_age()
    print(f"Your age is {val}")

except InvalidAgeError as e:
    print(e)

except ValueError:
    print('invalid integer value')
```

## The finally clause

The `finally` clause is used to clean up resources at the end. It is always  
executed.  

```python
f = None

try:

    f = open('data.txt', 'r')
    lines = f.readlines()

    for line in lines:
        print(line.rstrip())

except IOError:

    print('Error opening file')

finally:

    if f:
        f.close()
```

## The with statement

The `with` statement is used for managing resources, especially in the context of exception handling  
and ensuring proper resource cleanup.

It is used with  used with file streams, locks, sockets or subprocesses.  

```python
with open('data.txt', 'r') as f:

    lines = f.readlines()

    for line in lines:
        print(line.rstrip())
```

## One exception caught

By default, only the first exception can be caught. Raising multiple exceptions, the program  
will finish after handling the first exception. The rest will never be raised.   

```python
import random

exceptions = [IndexError(), FileNotFoundError(), ImportError(), TypeError()]
random.shuffle(exceptions)

try:
    for e in exceptions:
        raise e
except ImportError:
    print('ZeroDivisionError')
except FileNotFoundError:
    print('FileNotFoundError')
except IndexError:
    print('IndexError')
except TypeError:
    print('TypeError')
```

In concurrent programming, where our program performs multiple tasks simultaneously, it becomes  
essential to handle all exceptions that may occur. Each concurrent task can raise its own exceptions.  
Starting from Python 3.11, the language introduces `ExceptionGroup` objects and a special except* clause  
to facilitate handling all exceptions.

```python
import random

exceptions = [IndexError(), FileNotFoundError(), ImportError(), TypeError()]
random.shuffle(exceptions)

try:
    raise ExceptionGroup("Errors Occurred", exceptions)
except* ImportError:
    print('ZeroDivisionError')
except* FileNotFoundError:
    print('FileNotFoundError')
except* IndexError:
    print('IndexError')
except* TypeError:
    print('TypeError')
```












