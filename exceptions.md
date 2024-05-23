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


