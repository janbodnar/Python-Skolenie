# Python for loop

A *loop* is a sequence of instructions that is continually repeated until  
a certain condition is reached. For instance, we have a collection of items  
and we create a loop to go through all elements of the collection.  
Loops in Python can be created with `for` or `while` statements.  

## The for statement

Python for statement iterates over the items of any sequence (such as a list or a string), in the order  
that they appear in the sequence.

```python
for var in sequence:
   do_statement(s)
```

The above is the general syntax of the Python for statement.

## Loop with string

The following example uses Python for statement to go through a string.

```python
#!/usr/bin/python

word = "cloud"

for e in word:
    
    print(e)
```

We have a string defined. With the for loop, we print the letters of the word   
one by one to the terminal.

```
$ ./for_loop_string.py 
c
l
o
u
d
```

## Syntax sugar

The `for` loop is a syntax sugar for the following `while` loop:

```python
vals = [1, 2, 3, 4, 5, 6]


it = iter(vals)

while True:
    try:
        e = next(it)
    except StopIteration:
        break
    else:
        print(e)
```

The code is equivalent to:

```python
for e in vals:
  print(e)
```


## Loop & else

The for loop has an optional else statement which is executed when the looping has finished.  

```python
#!/usr/bin/python

words = ["cup", "star", "monkey", "bottle", "paper", "door"]

for word in words:
    
    print(word)
else:

    print("Finished looping")
```

We go over the list of words with a for loop. When the iteration is over, we print the *Finished looping*  
message which is located in the body following the else keyword.

```
$ ./for_loop_else.py 
cup
star
monkey
bottle
paper
door
Finished looping
```

## Loop with range

Python range function generates a sequence of numbers. 

```python
range(n)
```

The function generates numbers 0...n-1.

```python
range(start, stop, [step])
```

The function generates a sequence of numbers; it begins with start and ends with stop, which is not  
included in the sequence. The step is the increment and defaults to 1 if not provided.

With the help of the `range` function, we can repeat a code block n times.

```python
#!/usr/bin/python

for i in range(1, 6):
    
    print(f"Statement executed {i}")
```

The code example executes the code block five times.

```
$ ./repeating_statement.py 
Statement executed 1
Statement executed 2
Statement executed 3
Statement executed 4
Statement executed 5
```

In the next example we generate two sequences of integers with for loop.

```python
#!/usr/bin/python

for n in range(1, 11):
    print(n, end=' ')
    
print()

for n in range(0, 11, 2):
    
    print(n, end=' ')    
    
print()
```
  
The example prints two sequences of integers: 1, 2, ...10 and 0, 2, ...10.

```
$ ./for_loop_range.py 
1 2 3 4 5 6 7 8 9 10 
0 2 4 6 8 10
```
 
## Loop over a tuple and list

With Python for loop, we can easily traverse Python tuples and lists.

```python
#!/usr/bin/python

nums = (1, 2, 3, 4, 5, 6)   
words = ["cup", "star", "monkey", "bottle"]

for n in nums:
    
    print(n, end=' ')

print()

for word in words:
    
    print(word, end=' ')
    
print()
```

The code example prints the elements of a tuple and a list.

```
$ ./for_loop_tuple_list.py 
1 2 3 4 5 6 
cup star monkey bottle 
```

## Loop with index

Sometimes we need to get the index of the element as well; for this we can use the `enumerate` function.

```python
#!/usr/bin/python

words = ("cup", "star", "monkey", "bottle", "paper", "door")

for idx, word in enumerate(words):
    
    print(f"{idx}: {word}")
```

With the help of the enumerate function, we print the element of the list with its index.

```
$ ./for_loop_index.py 
0: cup
1: star
2: monkey
3: bottle
4: paper
5: door
```

## Loop over a dictionary

In the following example, we loop over a Python dictionary.

```python
#!/usr/bin/python

data = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary", "ru": "Russia" }    

for k, v in data.items():
    
    print(f"{k} is an abbreviation for {v}")
```

The code example prints the keys and the values of the Python dictionary.

```
$ ./for_loop_dictionary.py 
sk is an abbreviation for Slovakia
ru is an abbreviation for Russia
hu is an abbreviation for Hungary
de is an abbreviation for Germany
```

## Nested for loop

It is possible to nest a for loop into another loop.

```python
#!/usr/bin/python

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in nums:
    
    for e in i:
        
        print(e, end=' ')
    
    print()
```

We have a two-dimensional list of integers. We loop over the elements with two for loops.

```
$ ./for_loop_nested.py 
1 2 3 
4 5 6 
7 8 9
```

## Loop with zip

The `zip` function creates an iterator from the given iterables.

```python
#!/usr/bin/python

words1 = ["cup", "bottle", "table", "rock", "apple"]
words2 = ["trousers", "nail", "head", "water", "pen"]

for w1, w2 in zip(words1, words2):
    
    print(w1, w2)
```

In the example, we iterate over two lists in one for loop.

```
$ ./for_loop_zip.py 
cup trousers
bottle nail
table head
rock water
apple pen
```

## Looping custom iterables

In the next example we loop over a custom iterable.

```python
#!/usr/bin/python

import random

def myrandom(x):
    
    i = 0
    
    while i < x:
        
        r = random.randint(0, 100)
        
        yield r
        
        i = i + 1

for r in myrandom(5):
    
    print(r)
```

The code example creates a generator function that yields random integers. With the for loop  
we generate five random integers.

```
$ ./for_loop_custom_iterable.py 
14
43
53
44
70
```


## Loop with break

The break statement terminates the for loop.

```python
#!/usr/bin/python

import random
import itertools 

for i in itertools.count():
    
   val = random.randint(1, 30)
   print(val)

   if val == 22:
      break
```

In the example, we create an endless for loop. We generate and print random numbers from 1...29.  
If the generated number equals to 22, the for loop is ended with the `break` keyword.

```
$ ./for_loop_break.py 
7
27
2
27
7
9
3
25
15
22
```

## Loop with continue

The `continue` keyword is used to interrupt the current cycle, without jumping out of the  
whole loop. It initiates a new cycle.

```python
#!/usr/bin/python

num = 0

for num in range(1000):
       
   if num % 2 == 0:
      continue
      
   print(num, end=' ')
   
print()
```
We print all numbers smaller than 1000 that cannot be divided by number 2 without a remainder.

## Declarative iteration

The following Java code uses a declarative loop using `forEach`. 

```java
import java.util.List;

void main() {

    var vals = List.of("sky", "blue", "nice");

    vals.forEach(e -> System.out.println(e));
}
```

There are equivalent of Java's `forEach` loop in Python, but they are awkward.  

```python
vals = [1, 2, 3, 4, 5]

mv = map(lambda e: print(e), vals)

for _ in mv:
    pass

[print(e) for e in vals]

list(map(lambda e: print(e), vals))
```

