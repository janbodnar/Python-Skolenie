# Control flow

When a Python program is run, the code is executed from top to bottom. The flow of the  
program can be altered with various keywords, including if/else, for, while, and match.

The control flow structures can be used to executed code conditionally or multiple times.

## The if statement

The if statement has the following general form:

```python
if expression:
    statements

```

The `if` keyword is used to check if an expression is true. If it is true, a statement is  
then executed. The statement can be a single statement or a compound statement. A compound  
statement consists of multiple statements enclosed by the block.  

```python
#!/usr/bin/python

import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
```

A random number is generated. If the number is greater than zero, we print a message to the terminal.

```python
r = random.randint(-5, 5)
```

We generate a random integer between -5 .. 5.

```
if r > 0:
    print('The r variable is positive')
```

Using the `if` keyword, we check if the generated number is greater than zero. The `if` keyword is  
followed by an expression that evaluates to a boolean value.  If the boolean value is `True` then the  
block is executed. In our case, the string *The r variable is positive* is printed to the terminal.  
If the random value is negative, nothing is done. 

# The else statement

We can use the `else` keyword to create a simple branch. If the expression following the `if` keyword  
evaluates to `False`, the block following the `else` keyword is automatically executed.

```python
#!/usr/bin/python

import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
else:
    print('The r variable is negative or zero')
```

Either the block following the `if` keyword is executed or the block following the `else` keyword. 

# The elif statement

We can create multiple branches using the `elif` keyword. It tests for another condition if and only if  
the previous condition was not met. Note that we can use multiple `elif` keywords in our tests. 

```python
#!/usr/bin/python

import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
elif r == 0:
    print('The r variable is zero')
else:
    print('The r variable is negative')
```

If the first condition evaluates to `True`, e.g. the entered value is less than zero, the first block  
is executed and the remaining two blocks are skipped. If the first condition is not met, then the  
second condition following the if else keywords is checked. If the second condition evaluates to `True`,  
the second block is executed. If not, the third block following the else keyword is executed.  
The `else` block is always executed if the previous conditions were not met.











