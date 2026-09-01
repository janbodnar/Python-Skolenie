# Conditionals

Conditional statements allow us to execute a block of code only if a certain condition is met.  
When a Python program is run, the code is executed from top to bottom. Conditional statements  
alter the flow of the program based on the evaluation of expressions. The `if`, `elif`, and  
`else` keywords are used to create conditional branches.

A more advanced conditional construct is *pattern matching*, created with the `match` and  
`case` keywords; it is covered in a separate chapter.

## The if statement

The `if` statement has the following general form:

```python
if expression:
    statements
```

The `if` keyword is used to check whether an expression evaluates to `True`. If it does,  
the indented block is executed. The block can contain a single statement or multiple  
statements.

```python
import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
```

A random number is generated. If the number is greater than zero, a message is printed  
to the terminal.

```python
r = random.randint(-5, 5)
```

We generate a random integer between -5 and 5.

```python
if r > 0:
    print('The r variable is positive')
```

Using the `if` keyword, we check whether the generated number is greater than zero. The  
`if` keyword is followed by an expression that evaluates to a boolean value. If the value  
is `True`, the block is executed; in our case, the string *The r variable is positive* is  
printed to the terminal. If the random value is negative or zero, nothing is done.

## The else statement

We can use the `else` keyword to create a simple branch. If the expression following the  
`if` keyword evaluates to `False`, the block following the `else` keyword is executed  
instead.

```python
import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
else:
    print('The r variable is negative or zero')
```

Either the block following the `if` keyword is executed or the block following the  
`else` keyword — never both.

## The elif statement

We can create multiple branches using the `elif` keyword. It tests another condition if  
and only if the previous conditions were not met. Note that we can use multiple `elif`  
keywords in our tests.

```python
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

If the first condition evaluates to `True`, the first block is executed and the remaining  
blocks are skipped. If the first condition is not met, the second condition following the  
`elif` keyword is checked. If the second condition evaluates to `True`, the second block  
is executed. If not, the block following the `else` keyword is executed. The `else` block  
is always executed if none of the previous conditions were met.

## Chained comparisons

Python allows chaining comparison operators. A chained comparison `a < b < c` is equivalent  
to `a < b and b < c`; however, the middle expression is evaluated only once.

```python
x = 12

if 0 <= x <= 10:
    print('The x is between 0 and 10')
else:
    print('The x is outside the 0..10 range')
```

The condition `0 <= x <= 10` is a single expression that tests whether the `x` value is  
within the given range.

## Nested conditionals

Conditional statements can be nested inside other conditional statements. The inner `if`  
is evaluated only when the outer condition is true.

```python
age = 25
has_licence = True

if age >= 18:
    if has_licence:
        print('The person can drive')
    else:
        print('The person is adult but has no licence')
else:
    print('The person is too young to drive')
```

The outer `if` checks whether the person is adult. If so, the inner `if` verifies whether  
they have a driving licence. Deeply nested conditionals quickly become hard to read; in  
many cases they can be rewritten with the `and` operator or with `elif` branches.

## Truthiness

The condition of an `if` statement does not have to be an explicit boolean value. In  
Python, every value is considered either *truthy* or *falsy*. The following values are  
falsy:

- `None`
- `False`
- numeric zero: `0`, `0.0`, `0j`
- empty collections: `''`, `[]`, `()`, `{}`, `set()`

All other values are truthy.

```python
name = ''

if name:
    print(f'The name is: {name}')
else:
    print('The name is empty')
```

An empty string is falsy; therefore, the `else` branch is executed. Testing collections  
directly in conditions is a common Python idiom:

```python
users = []

if not users:
    print('There are no users')
```

The `not` keyword negates the condition. An empty list is falsy, so the message is  
printed.

## The conditional expression

The conditional expression (sometimes called the *ternary operator*) is a terse way to  
assign a value based on a condition. It is covered in detail in the operators chapter.

```python
age = 31

adult = True if age >= 18 else False

print(f'Adult: {adult}')
```

First the condition `age >= 18` is evaluated. If it is true, the value before the `if`  
keyword is returned; otherwise, the value after the `else` keyword is returned. The  
result is assigned to the `adult` variable.

## The pass statement

The `pass` statement does nothing. It is used as a placeholder where a statement is  
syntactically required but no action is needed. This is useful during development, when  
the logic of a branch has not been implemented yet.

```python
value = 5

if value < 0:
    pass
else:
    print(value)
```

The `pass` statement is a null operation; the program continues without any action. Once  
the branch is implemented, `pass` is replaced with the actual code.

## Pattern matching

*Pattern matching* is a powerful conditional construct that allows us to compare a value  
against a series of patterns and to execute code based on which pattern matches. It was  
introduced in Python 3.10 and is a much more advanced construct than the `if/elif/else`  
statements. Pattern matching is created with the `match` and `case` keywords and is  
covered in detail in a separate chapter.
