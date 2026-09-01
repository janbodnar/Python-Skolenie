# Loops

A *loop* is a sequence of instructions that is continually repeated until a certain  
condition is reached. For instance, we have a collection of items and we create a loop  
to go through all the elements of the collection. Loops in Python can be created with  
the `for` or `while` statements.

The `while` statement repeats a block as long as its condition holds true, while the  
`for` statement iterates over the items of a collection. The Python `for` loop has a  
rich syntax and is covered in detail in a separate chapter.

## The while statement

The `while` keyword is used to create a cycle. The statements inside the while  
loop are executed until the expression evaluates to `False`.  

```python
i = 0

msg = 'an old falcon'

while i <= 8:
    print(msg)
    i += 1
```

The example prints the string `an old falcon` 9 times. The variable `i` is used as a  
counter. It is initialized to zero.



```python
# while_kwd.py

numbers = [22, 34, 12, 32, 4]
mysum = 0

i = len(numbers)

while i != 0:

    i -= 1
    mysum = mysum + numbers[i]

print('The sum is:', mysum)
```

We want to calculate the sum of all values in the numbers list. We utilize the while  
loop. We determine the length of the list. The while loop is executed over and over  
again, until `i` is equal to zero. In the body of the loop, we decrement the counter  
and calculate the sum of the values.

```
$ ./while_kwd.py
The sum is: 104
```

## The infinite loop

If the condition of a while loop never becomes false, we have an infinite loop. Infinite  
loops are often combined with the `break` statement, which terminates the loop when a  
certain condition is met.

```python
while True:
    answer = input('Enter your name: ')
    if answer:
        break
```

The loop asks for input endlessly until the user enters a non-empty string.

## The break statement

The `break` keyword is used to interrupt the cycle if needed.

```python
# break_kwd.py

import random

while True:

    val = random.randint(1, 30)
    print(val, end=' ')

    if val == 22:
        break

print()
```

In our example, we print random integer numbers. If the number equals 22, the cycle is  
interrupted with the `break` keyword. The `while True` creates an endless cycle. The  
`break` is used to jump out of this endless cycle.

## The continue statement

The `continue` statement is used to interrupt the current cycle without jumping out of  
the whole cycle. It initiates a new cycle.

```python
# continue_kwd.py

num = 0

while num < 1000:

    num = num + 1

    if num % 2 == 0:
        continue

    print(num, end=' ')

print()
```

In the example we print all numbers smaller than 1000 that cannot be divided by number 2  
without a remainder. When `num` is even, the `continue` statement skips the `print` call  
and the loop starts a new cycle.

## The loop else clause

Both `for` and `while` loops can have an `else` clause. The `else` block is executed when  
the loop finishes normally — that is, when the condition of a while loop becomes false or  
when a for loop exhausts its iterable. If the loop is terminated by a `break` statement,  
the `else` block is skipped.

```python
# loop_else.py

nums = [1, 3, 5, 7, 9]
key = 5

i = 0

while i < len(nums):

    if nums[i] == key:
        print('Found', key)
        break

    i += 1
else:
    print('Not found')
```

We look for a `key` value in the list. If the value is found, the loop is interrupted  
with `break` and the `else` block is skipped. If the value is not present, the loop ends  
naturally and the `else` block reports that the value was not found.

## The for statement

The `for/in` keywords are used to iterate over items of a collection in the order in  
which they appear in the container.

```python
# for_kwd.py

lyrics = """
Are you really here or am I dreaming
I can't tell dreams from truth
for it's been so long since I have seen you
I can hardly remember your face anymore
"""

for i in lyrics:

    print(i, end=' ')
```

In the example, we have a lyrics variable having a strophe of a song. We iterate over the  
text and print the text character by character. The `end` parameter of the `print`  
statement prevents printing each character on a new line.

The `for` statement has a rich syntax — including the `range`, `enumerate`, and `zip`  
functions — and it is covered in detail in a separate chapter.

## The range function

The `range` function is often used with the for loop to repeat a block a fixed number of  
times.

```python
for i in range(1, 6):
    print(i)
```

The code prints numbers 1 to 5. The `range` function generates a sequence of numbers and  
the for loop iterates over it. More examples are provided in the for loop chapter.

## Nested loops

A loop can be placed inside another loop. The inner loop is fully executed for each  
iteration of the outer loop.

```python
# nested.py

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

The inner loop goes through all its iterations before the outer loop moves to the next  
value. Nested loops are commonly used to process two-dimensional data, such as matrices  
or tables.

## Loop control summary

| Keyword      | Meaning                                                                  |
| ------------ | ------------------------------------------------------------------------ |
| `break`      | terminates the whole loop immediately                                     |
| `continue`   | skips the rest of the current iteration and starts a new one              |
| `else`       | executed when the loop finishes without hitting `break`                   |
| `pass`       | a null operation; does nothing, can stand in for not-yet-written loop body |
