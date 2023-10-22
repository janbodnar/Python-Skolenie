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


## The while statement

The `while` keyword is used to create a cycle. The statements inside the while loop are executed until  
the expression evaluates to `False`.

```python
#!/usr/bin/python

# while_kwd.py

numbers = [22, 34, 12, 32, 4]
mysum = 0

i = len(numbers)

while i != 0:

   i -= 1
   mysum = mysum + numbers[i]

print("The sum is:", mysum)
```

We want to calculate the sum of all values in the numbers list. We utilize the while loop.  
We determine the length of the list. The while loop is executed over and over again, until the `i` is equal  
to zero. In the body of the loop, we decrement the counter and calculate the sum of values.

## The break statement

The `break keyword` is used to interrupt the cycle if needed.

```python
#!/usr/bin/python

# break_kwd.py

import random

while True:

    val = random.randint(1, 30)
    print(val, end=" ")

    if val == 22:
        break

print()
```

In our example, we print random integer numbers. If the number equals to 22, the cycle is interrupted  
with the `break` keyword. The `while True` creates an endless cycle. The `break` is used to jump out of  
this endless cycle.  

## The continue statement 

The `continue` statement is used to interrupt the current cycle without jumping out of the whole cycle.  
It initiates a new cycle.


```python
#!/usr/bin/python

# continue_kwd.py

num = 0

while num < 1000:

      num = num + 1

      if num % 2 == 0:
         continue

      print(num, end=" ")

print()
```

In the example we print all numbers smaller than 1000 that cannot be divided by number 2 without a remainder.

## The for statement 

The `for/in` keywords are used to iterate over items of a collection in order that they appear in the container.

```python
#!/usr/bin/python

# for_kwd.py

lyrics = """
Are you really here or am I dreaming
I can't tell dreams from truth
for it's been so long since I have seen you
I can hardly remember your face anymore
"""


for i in lyrics:

    print(i, end=" ")
```

In the example, we have a lyrics variable having a strophe of a song. We iterate over the text and print  
the text character by character. The comma in the print statement prevents from printing each character  
on a new line.

The `for` statement has a rich syntax and it is covered in a separate section in a more detail.  

## Pattern match
Pattern matching is a powerful control flow construct that allows us to compare a value against  
a series of patterns and executing code based on which pattern matches. It is a much more  
advanced construct than the `if/else` statements.

```python
#!/usr/bin/python

grades = ['A', 'B', 'C', 'D', 'E', 'F', 'FX']

for grade in grades:

    match grade:
        case 'A' | 'B' | 'C' | 'D' | 'E' | 'F':
            print('passed')
        case 'FX':
            print('failed')
```

We have a list of grades. For A throug F grades, we pass the example.  
For the FX grade, we fail the exam.

```python
grades = ['A', 'B', 'C', 'D', 'E', 'F', 'FX']
```

We define a list of grades.

```python
for grade in grades:
```

First, we go over the list with a for loop.

```python
match grade:
    case 'A' | 'B' | 'C' | 'D' | 'E' | 'F':
        print('passed')
    case 'FX':
        print('failed')
```
        
In each for cycle, we match a value agains the given patterns. The first case branch  
matches against several values separated with |. In the second branch, we match  
agains single value 'FX'. 

```
$ ./main.py  
passed
passed
passed
passed
passed
passed
failed
```
