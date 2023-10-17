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
followed by an expression that evaluates to a boolean value.  If the boolean value is true, then the  
block is executed. In our case, the string *The r variable is positive* is printed to the terminal.  
If the random value is negative, nothing is done. 
