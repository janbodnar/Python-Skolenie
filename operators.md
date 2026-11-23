# Python Operators

An **operator** is a symbol or a keyword that performs an operation on values.  
You already know many operators from mathematics: `+` adds two numbers, `*`  
multiplies them. The values that an operator works with are called **operands**.  
In the expression `3 + 4`, the operator is `+` and the operands are `3` and `4`.

Most operators work with two operands; they are called **binary operators**. A  
few operators work with a single operand; they are called **unary operators**.  
For example, the minus sign in `-5` is a unary operator.

This chapter covers these groups of operators:

- arithmetic operators
- assignment operators
- comparison operators
- logical operators
- membership operators
- identity operators
- the conditional expression
- bitwise operators

At the end, you will learn in which order Python evaluates operators in a longer  
expression, and see a complete example that combines several kinds of operators.

## Arithmetic operators

Arithmetic operators do calculations with numbers:

| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `7 + 2` | `9` |
| `-` | Subtraction | `7 - 2` | `5` |
| `*` | Multiplication | `7 * 2` | `14` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Remainder (modulo) | `7 % 2` | `1` |
| `**` | Power | `7 ** 2` | `49` |

The first five work as in mathematics:

```python
price = 12
quantity = 3

print(price + 5)
print(price - 5)
print(price * quantity)
print(price / quantity)
print(price ** 2)
```

```text
$ python arithmetic.py
17
7
36
4.0
144
```

Notice the result of the division: `4.0`, not `4`. The `/` operator always  
returns a floating-point number, even when the division is exact.

### Division

Python has three operators related to division:

```python
print(9 / 4)
print(9 // 4)
print(9 % 4)
```

```text
$ python division.py
2.25
2
1
```

- `/` is the ordinary division. `9 / 4` is `2.25`.
- `//` is the **floor division**. It divides and then rounds the result down to  
  a whole number. `9 // 4` is `2`.
- `%` is the **remainder** operator, also called **modulo**. `9 % 4` is `1`,  
  because 4 fits into 9 twice and 1 remains.

The `//` and `%` operators are useful together. For example, they convert  
minutes to hours and minutes:

```python
minutes = 135

hours = minutes // 60
rest = minutes % 60

print(f"{minutes} minutes is {hours} h {rest} min")
```

```text
$ python minutes.py
135 minutes is 2 h 15 min
```

The `%` operator also tells you whether a number is even: an even number divided  
by 2 gives the remainder 0.

```python
print(10 % 2)
print(7 % 2)
```

```text
$ python even.py
0
1
```

With negative numbers, remember that `//` always rounds down, toward negative  
infinity, and the result of `%` has the same sign as the divisor:

```python
print(-7 // 3)
print(-7 % 3)
```

```text
$ python negative.py
-3
2
```

The exact result of `-7 / 3` is about `-2.33`. Rounded down, it is `-3`, not  
`-2`. Some other languages, such as C and Java, give different results here.

Dividing by zero is an error:

```python
total = 100
people = 0

print(total / people)
```

```text
$ python zero.py
Traceback (most recent call last):
  File "/home/user/project/zero.py", line 4, in <module>
    print(total / people)
          ~~~~~~^~~~~~~~
ZeroDivisionError: division by zero
```

### Unary plus and minus

The `-` sign before a single value is the unary minus. It changes the sign of  
the value. The unary plus, `+`, leaves the value unchanged and is rarely used.

```python
temperature = 5

print(-temperature)
print(-(-temperature))
print(+temperature)
```

```text
$ python unary.py
-5
5
5
```

### Operators with strings

Some arithmetic operators also work with strings. The `+` operator joins two  
strings together, and the `*` operator repeats a string:

```python
first_name = "John"
last_name = "Doe"

print(first_name + " " + last_name)
print("-" * 20)
print("ha" * 3)
```

```text
$ python strings.py
John Doe
--------------------
hahaha
```

A common mistake is to add a number to a string:

```python
count = 3

print(count + " apples")
```

```text
$ python apples.py
Traceback (most recent call last):
  File "/home/user/project/apples.py", line 3, in <module>
    print(count + " apples")
          ~~~~~~^~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Python does not convert the number to a string automatically. Convert it  
yourself with the `str()` function, or use an f-string:

```python
count = 3

print(str(count) + " apples")
print(f"{count} apples")
```

```text
$ python apples_fixed.py
3 apples
3 apples
```

### Matrix multiplication

The last arithmetic operator, `@`, is used for matrix multiplication. The  
built-in types do not support it; it is used with matrices from libraries such  
as NumPy, as in `m1 @ m2`.

## Assignment operators

The **assignment operator** `=` stores a value in a variable:

```python
score = 10
print(score)

score = score + 5
print(score)
```

```text
$ python assignment.py
10
15
```

In mathematics, `score = score + 5` would be nonsense, because no number equals  
itself plus 5. In Python, `=` does not mean "is equal to". It means: evaluate  
the expression on the right and store the result in the variable on the left.  
The right side is `10 + 5`, so `score` becomes `15`.

The left side must be something that can hold a value, such as a variable name.  
You cannot assign to a number:

```python
3 = score
```

```text
$ python literal.py
  File "/home/user/project/literal.py", line 1
    3 = score
    ^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

You can assign one value to several variables at once:

```python
x = y = z = 0

print(x, y, z)
```

```text
$ python chained.py
0 0 0
```

### Compound assignment

Changing a variable based on its own value is so common that Python has shorter  
operators for it. `score += 5` means the same as `score = score + 5`:

```python
score = 10

score += 5
print(score)

score -= 3
print(score)

score *= 2
print(score)

score //= 5
print(score)
```

```text
$ python compound.py
15
12
24
4
```

Every binary arithmetic and bitwise operator has a compound form:

```text
+=   -=   *=   /=   //=   %=   **=   @=   &=   |=   ^=   <<=   >>=
```

The expression on the right side is always evaluated first, as a whole:

```python
price = 10
price *= 2 + 1

print(price)
```

```text
$ python compound_order.py
30
```

The result is `30`, because the statement means `price = price * (2 + 1)`, not  
`price = price * 2 + 1`.

### The assignment expression

Python 3.8 added the **assignment expression** `:=`, nicknamed the walrus  
operator because `:=` looks like the eyes and tusks of a walrus. Unlike `=`, it  
can be used inside a larger expression: it stores a value in a variable and also  
returns that value.

```python
word = "falcon"

if (n := len(word)) > 3:
    print(f"The word has {n} letters")
```

```text
$ python walrus.py
The word has 6 letters
```

The `:=` operator stores the length of the word in `n`, and the comparison then  
uses the same value. Without `:=`, you would compute the length on a separate  
line first. Beginners do not need it often; ordinary assignment is usually  
clearer.

## Comparison operators

Comparison operators compare two values. The result is always a boolean value:  
`True` or `False`.

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 5` | `False` |
| `<` | less than | `3 < 5` | `True` |
| `<=` | less than or equal to | `5 <= 5` | `True` |
| `>` | greater than | `3 > 5` | `False` |
| `>=` | greater than or equal to | `3 >= 5` | `False` |

```python
age = 17

print(age >= 18)
print(age < 18)
print(age == 17)
print(age != 17)
```

```text
$ python comparison.py
False
True
True
False
```

Comparisons are most often used in conditions, for example in an `if` statement:

```python
age = 17

if age >= 18:
    print("You can vote")
else:
    print("You are too young to vote")
```

```text
$ python comparison_if.py
You are too young to vote
```

Do not confuse `=` with `==`. A single `=` assigns, a double `==` compares.  
Using `=` in a condition is a syntax error:

```python
age = 17

if age = 18:
    print("Happy birthday!")
```

```text
$ python equals_mistake.py
  File "/home/user/project/equals_mistake.py", line 3
    if age = 18:
       ^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

### Comparing strings

Strings can be compared, too. `==` checks whether two strings are the same, and  
`<` and `>` compare them alphabetically:

```python
print("apple" == "apple")
print("apple" < "banana")
print("apple" < "Banana")
```

```text
$ python compare_strings.py
True
True
False
```

The last result may surprise you. Python compares strings character by  
character, using the number that represents each character in Unicode, its  
**code point**. The built-in `ord()` function returns this number:

```python
print(ord("a"))
print(ord("b"))
print(ord("B"))
```

```text
$ python code_points.py
97
98
66
```

All uppercase letters have smaller code points than lowercase letters, so  
`"Banana"` comes before `"apple"`. To compare strings regardless of case,  
convert both to lowercase first, for example with `"apple".lower() <  
"Banana".lower()`.

Comparing values of unrelated types, such as a string and a number, with `<` or  
`>` is an error:

```python
print("10" > 5)
```

```text
$ python compare_types.py
Traceback (most recent call last):
  File "/home/user/project/compare_types.py", line 1, in <module>
    print("10" > 5)
          ^^^^^^^^
TypeError: '>' not supported between instances of 'str' and 'int'
```

The `==` operator does not raise an error in this case; it simply returns  
`False`, because a string is never equal to a number.

### Comparing floating-point numbers

Floating-point numbers are stored with limited precision, so a result of a  
calculation may differ slightly from what you expect:

```python
import math

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))
```

```text
$ python floats.py
0.30000000000000004
False
True
```

Do not compare floating-point results with `==`. Use `math.isclose()`, which  
checks whether two numbers are close enough.

### Chained comparisons

Comparisons can be chained. The expression `1 <= x <= 10` means `1 <= x and x <=  
10`, just like in mathematics:

```python
grade = 7

print(1 <= grade <= 10)
print(1 <= grade <= 5)
```

```text
$ python chained_comparison.py
True
False
```

## Logical operators

The logical operators `and`, `or`, and `not` combine boolean values. They are  
used to build more complex conditions.

```python
age = 25
has_ticket = True
is_member = False

print(age >= 18 and has_ticket)
print(has_ticket or is_member)
print(not is_member)
```

```text
$ python logical.py
True
True
True
```

- `and` gives `True` only if both operands are true.
- `or` gives `True` if at least one operand is true.
- `not` reverses the value: `True` becomes `False` and `False` becomes `True`.

The following table shows all combinations:

| `a` | `b` | `a and b` | `a or b` | `not a` |
| --- | --- | --- | --- | --- |
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |

### Short-circuit evaluation

Python evaluates `and` and `or` from left to right and stops as soon as the  
result is known. If the left operand of `and` is false, the whole expression  
must be false, so the right operand is not evaluated at all. Similarly, if the  
left operand of `or` is true, the right operand is skipped. This is called  
**short-circuit evaluation**.

It lets you protect an operation that could fail:

```python
total = 100
people = 0

if people != 0 and total / people > 20:
    print("More than 20 per person")
else:
    print("Nothing to share")
```

```text
$ python short_circuit.py
Nothing to share
```

Because `people != 0` is `False`, Python never evaluates `total / people`, so  
there is no `ZeroDivisionError`.

### Truthy and falsy values

The logical operators work with any values, not only with `True` and `False`.  
The values `False`, `None`, zero (`0`, `0.0`), and empty collections (`""`,  
`[]`, `{}`, ...) count as false; they are called **falsy**. All other values  
count as true; they are **truthy**.

`and` and `or` do not always return `True` or `False`. They return one of their  
operands: `or` returns the first truthy operand (or the last one, if none is  
truthy), and `and` returns the first falsy operand (or the last one, if all are  
truthy). `not` always returns `True` or `False`.

```python
print(0 or "default")
print(5 or "default")
print(0 and 5)
print(3 and 5)
print(not "")
```

```text
$ python operands.py
default
5
0
5
True
```

This is often used to provide a default value:

```python
name = ""

print(f"Hello, {name or 'guest'}!")
```

```text
$ python default_value.py
Hello, guest!
```

## Membership operators

The membership operators `in` and `not in` check whether a value is contained in  
a collection:

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("mango" in fruits)
print("mango" not in fruits)
```

```text
$ python membership.py
True
False
True
```

They work with strings, lists, tuples, sets, dictionaries, and other  
collections. With a string, `in` looks for a substring. With a dictionary, `in`  
checks the keys, not the values:

```python
user = {"name": "Peter", "age": 34}

print("cat" in "concatenate")
print("name" in user)
print("Peter" in user)
print(3 in (1, 2, 3))
```

```text
$ python membership_types.py
True
True
False
True
```

The membership operators are often used in conditions:

```python
allowed = ("admin", "editor")
role = "viewer"

if role not in allowed:
    print(f"Access denied for {role}")
```

```text
$ python membership_if.py
Access denied for viewer
```

## Identity operators

The identity operators `is` and `is not` check whether two names refer to the  
**same object** in memory. This is different from `==`, which checks whether two  
objects have the **same value**:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
```

```text
$ python identity.py
True
False
True
```

The lists `a` and `b` have the same contents, so `a == b` is `True`. But they  
are two separate lists, so `a is b` is `False`. The variable `c` refers to the  
same list as `a`, so `a is c` is `True`.

The most common use of `is` is to check for `None`. There is only one `None`  
object, and PEP 8 recommends comparing with it using `is` or `is not`:

```python
result = None

if result is None:
    print("No result yet")
```

```text
$ python is_none.py
No result yet
```

Do not use `is` to compare numbers or strings. Whether two equal numbers or  
strings are the same object depends on the Python implementation, so the result  
is not reliable. Python warns you about it:

```python
count = 5

print(count is 5)
```

```text
$ python is_number.py
/home/user/project/is_number.py:3: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  print(count is 5)
True
```

The program still runs, but the `SyntaxWarning` tells you that you probably  
meant `==`.

## The conditional expression

The **conditional expression**, sometimes called the ternary operator, chooses  
one of two values based on a condition:

```text
value_if_true if condition else value_if_false
```

Python evaluates the condition first. If it is true, the result is the value  
before `if`; otherwise, the result is the value after `else`.

```python
age = 15

status = "adult" if age >= 18 else "minor"

print(f"Status: {status}")
```

```text
$ python conditional.py
Status: minor
```

The same code with an `if` statement takes four lines:

```python
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

The conditional expression is good for short, simple choices. When the condition  
or the values get long, the `if` statement is easier to read.

A common beginner pattern is `True if condition else False`. It is unnecessary,  
because the condition itself is already `True` or `False`: write `is_adult = age  
>= 18` instead.

## Bitwise operators

Computers store integers as binary numbers, made of bits with the values 0 and  
1. Bitwise operators work with the individual bits of integers. You will not  
need them often, but you will meet them in low-level code, in network  
programming, and when working with flags.

| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| `&` | bitwise and | `6 & 3` | `2` |
| `\|` | bitwise or | `6 \| 3` | `7` |
| `^` | bitwise exclusive or | `6 ^ 3` | `5` |
| `~` | bitwise negation | `~6` | `-7` |
| `<<` | left shift | `6 << 1` | `12` |
| `>>` | right shift | `6 >> 1` | `3` |

The built-in `bin()` function shows the binary form of an integer, which helps  
to understand what the operators do. The `0b` prefix marks a binary number:

```python
a = 6    # 110 in binary
b = 3    # 011 in binary

print(bin(a & b))
print(bin(a | b))
print(bin(a ^ b))
```

```text
$ python bitwise.py
0b10
0b111
0b101
```

The operators compare the numbers bit by bit:

```text
    110         110         110
  & 011       | 011       ^ 011
  = 010       = 111       = 101
```

- `&` sets a bit to 1 only if the bit is 1 in both numbers.
- `|` sets a bit to 1 if the bit is 1 in at least one of the numbers.
- `^` sets a bit to 1 if the bit is 1 in exactly one of the numbers.

The shift operators move all bits to the left or to the right. Shifting left by  
`n` bits multiplies the number by 2<sup>n</sup>; shifting right by `n` bits  
divides it by 2<sup>n</sup> and rounds down:

```python
print(6 << 1)
print(6 << 3)
print(6 >> 1)
print(bin(6), bin(6 << 1), bin(6 >> 1))
```

```text
$ python shift.py
12
48
3
0b110 0b1100 0b11
```

The `~` operator inverts all bits. Because of the way Python represents negative  
integers, `~x` always equals `-x - 1`, so `~6` is `-7`.

### Flags

A practical use of bitwise operators is storing several yes-or-no settings,  
called **flags**, in a single number. Each flag uses one bit. File permissions  
on Linux work this way: reading is `4` (binary `100`), writing is `2` (`010`),  
and executing is `1` (`001`).

```python
READ = 4
WRITE = 2
EXECUTE = 1

permissions = READ | WRITE

print(permissions)
print(bool(permissions & READ))
print(bool(permissions & EXECUTE))

permissions |= EXECUTE
print(permissions)
```

```text
$ python flags.py
6
True
False
7
```

The `|` operator combines flags, and the `&` operator tests whether a flag is  
set. The value `7` means that all three permissions are set; this is the `7`  
that you see in commands such as `chmod 755`.

## Operator precedence

When an expression contains several operators, Python must decide which one to  
evaluate first. Is `3 + 5 * 5` equal to 28 or 40? As in mathematics,  
multiplication goes before addition, so the result is 28. The rules that decide  
the order are called **operator precedence**. Parentheses change the order,  
because the expression inside them is evaluated first:

```python
print(3 + 5 * 5)
print((3 + 5) * 5)
print(2 ** 3 * 5)
```

```text
$ python precedence.py
28
40
40
```

The following table lists the operators from the highest precedence (evaluated  
first) to the lowest. Operators in the same row have the same precedence.

| Operators | Description |
| --- | --- |
| `(...)` | Parentheses |
| `x[i]`, `x(...)`, `x.attr` | Indexing, calls, attribute access |
| `**` | Power |
| `+x`, `-x`, `~x` | Unary plus, minus, bitwise negation |
| `*`, `@`, `/`, `//`, `%` | Multiplication, division, remainder |
| `+`, `-` | Addition, subtraction |
| `<<`, `>>` | Shifts |
| `&` | Bitwise and |
| `^` | Bitwise exclusive or |
| `\|` | Bitwise or |
| `==`, `!=`, `<`, `<=`, `>`, `>=`, `in`, `not in`, `is`, `is not` | Comparisons, membership, identity |
| `not` | Logical not |
| `and` | Logical and |
| `or` | Logical or |
| `... if ... else ...` | Conditional expression |
| `:=` | Assignment expression |

A few consequences of this table:

- Comparisons are evaluated before the logical operators, so `age >= 18 and  
  has_ticket` needs no parentheses.
- `not` is evaluated before `and`, which is evaluated before `or`.
- The power operator `**` binds more tightly than the unary minus on its left,  
  so `-2 ** 2` means `-(2 ** 2)`.

```python
print(-2 ** 2)
print((-2) ** 2)
print(not True or True)
print(not (True or True))
```

```text
$ python precedence_logic.py
-4
4
True
False
```

The precedence of `and` and `or` matters in real programs. Suppose that students  
and seniors get a discount, but only if they show a discount card:

```python
is_student = True
is_senior = False
has_card = False

wrong = is_student or is_senior and has_card
right = (is_student or is_senior) and has_card

print(wrong)
print(right)
```

```text
$ python discount.py
True
False
```

The student has no card, so there should be no discount. Because `and` has a  
higher precedence than `or`, Python reads the first expression as `is_student or  
(is_senior and has_card)`, and the result is wrong. The parentheses in the  
second expression fix it. When an expression mixes `and` and `or`, use  
parentheses to make your intention clear.

### Associativity

When operators have the same precedence, **associativity** decides the order.  
Most operators are evaluated from left to right:

```python
print(100 - 10 - 5)
print(9 / 3 * 3)
print(2 ** 3 ** 2)
```

```text
$ python associativity.py
85
9.0
512
```

`100 - 10 - 5` means `(100 - 10) - 5`, which is 85, and `9 / 3 * 3` means `(9 /  
3) * 3`, which is 9.0. The power operator is the exception: it is evaluated from  
right to left, so `2 ** 3 ** 2` means `2 ** (3 ** 2)`, which is 2<sup>9</sup> =  
512.

Comparisons are a special case: as you saw in the section on chained  
comparisons, `a < b < c` means `a < b and b < c`, not `(a < b) < c`.

## A complete example

The following program calculates the total price of a shopping cart. It uses  
arithmetic, compound assignment, membership, comparison, and logical operators,  
and the conditional expression.

```python
cart = [
    ("apples", 0.45, 6),
    ("bread", 1.99, 1),
    ("cheese", 4.50, 2),
    ("milk", 1.15, 2),
]
discounted = ("bread", "cheese")
is_member = False

total = 0

for name, price, quantity in cart:
    cost = price * quantity
    if name in discounted:
        cost *= 0.9
    total += cost
    print(f"{name:<8}{quantity:>3} x {price:>5.2f} = {cost:>6.2f}")

free_delivery = total >= 15 or is_member
delivery = 0 if free_delivery else 2.50
total += delivery

print(f"Delivery: {delivery:.2f}")
print(f"Total: {total:.2f}")
```

```text
$ python checkout.py
apples    6 x  0.45 =   2.70
bread     1 x  1.99 =   1.79
cheese    2 x  4.50 =   8.10
milk      2 x  1.15 =   2.30
Delivery: 2.50
Total: 17.39
```

- `price * quantity` computes the cost of one line of the cart.
- `name in discounted` checks whether the product has a 10% discount, and `cost  
  *= 0.9` applies it.
- `total += cost` adds the cost to the running total.
- `total >= 15 or is_member` decides whether delivery is free: either the order  
  is large enough, or the customer is a member.
- The conditional expression chooses the delivery price.

## Summary

| Group | Operators |
| --- | --- |
| Arithmetic | `+` `-` `*` `/` `//` `%` `**` `@` |
| Unary | `+x` `-x` `~x` |
| Assignment | `=` `+=` `-=` `*=` `/=` ... `:=` |
| Comparison | `==` `!=` `<` `<=` `>` `>=` |
| Logical | `and` `or` `not` |
| Membership | `in` `not in` |
| Identity | `is` `is not` |
| Conditional expression | `x if condition else y` |
| Bitwise | `&` `\|` `^` `~` `<<` `>>` |

## References

- [Python Language Reference: Expressions](https://docs.python.org/3/reference/expressions.html)
- [Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [Python Tutorial: Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
- [PEP 572: Assignment Expressions](https://peps.python.org/pep-0572/)
