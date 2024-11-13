# Functional programming


Functional programming is a programming paradigm where the primary method of  
computation is the evaluation of functions. 

Functional programming in Python is performed with `map`, `filter`, `lamba` functions,  
list comprehensions, `itertools`, `functools` modules or `funcy` library.  


Key points:

- **Pure Functions**: Ideally, functions only take inputs and produce outputs, without any  
  internal state that affects the output produced for a given input. Functions that have no  
  side effects at all are called purely functional.  

- **First-Class Functions**: In functional programming, functions are considered *first-class citizens*.  
  This means we can use them to store and manipulate data.  

- **Declarative Style**: It is a declarative type of programming style. Its main focus is on
- "what to solve" in contrast to an imperative style where the main focus is "how to solve".  

Python supports functional programming but also contains features of other programming models.  
While Python is not primarily a functional language, it's good to be familiar with `lambda`, `map`,  
`filter`, and `reduce` because they can help you write concise, high-level, parallelizable code.   

In a functional program, input flows through a set of functions. Each function operates on its input   
and produces some output. This style discourages functions with side effects that modify internal state  
or make other changes  that aren't visible in the function's return value.    



## itertools 


### The product function 

The `product` function computes the Cartesian product of input iterables.

```python
import itertools

colors = ['red', 'green']
sizes = ['S', 'M', 'L']

for item in itertools.product(colors, sizes):
    print(item)
```

### Permutations and combinations

Permutations and combinations are two concepts in mathematics that deal with counting or   
arranging objects. *Permutations* are  used when the order of arrangement matters.   
*Combinations* are is used when the order of arrangement does not matter.   

```python
from itertools import  permutations, combinations
from itertools import combinations_with_replacement

res = permutations('ABCD', 2)

print('permutations')
for e in res:
    print(e)

res = combinations('ABCD', 2)

print('combinations')
for e in res:
    print(e)

res = combinations_with_replacement('ABCD', 2)

print('combinations with replacement')
for e in res:
    print(e)
```

## repeat function

The `repeat` function from itertools is used to repeatedly yield the same  
value. This can be useful for various purposes, such as creating constant  
sequences or filling up iterables with a specific value.  

```python
import itertools

# Create a list of 10 zeros
zeros = list(itertools.repeat(0, 10))
print(zeros)
```

```python
from itertools import repeat

word = 'falcon'

for i in repeat(word, 3):
    print(i)

res = [e for e in repeat(range(55, 86), 7)]
print(res)

res = [list(e) for e in res]
print(res)

total_sum = sum(sum(nested) for nested in res)
print("Total sum:", total_sum)
```

## chain function

```python
from itertools import chain
 
# a list of odd numbers
odd = [1, 3, 5, 7, 9]
 
# a list of even numbers
even = [2, 4, 6, 8, 10]
 
# chaining odd and even numbers
numbers = list(chain(odd, even))
 
print(numbers)
```

---

```python
from itertools import chain
 
res = list(chain('ABC', 'DEF', 'GHI', 'JKL', 'MNO'))
print(res)
```

## accumulate function

```python
from itertools import accumulate
import operator

data = [1, 2, 3, 4, 5]

res = accumulate(data, operator.mul)

for e in res:
    print(e)

res = accumulate(data, operator.add)

for e in res:
    print(e)
```

## starmap function

The `starmap` function in Python's `itertools` module is used to apply a function  
to the arguments from each tuple in an iterable. It essentially "unpacks" each tuple  
and feeds its elements as arguments to the given function.

```python
from itertools import starmap
import operator

data = [(2, 6), (8, 4), (7, 3)]

# Calculate the products
res = starmap(operator.mul, data)

# Get the sum of the products
total_sum = sum(res)

# Print the total sum
print(total_sum)
```

We have a list of coordinates representing the sides of various triangles.  
We want to apply the Pythagorean theorem to each set of coordinates to determine  
if they form a right-angled triangle.  

Here's how you can do it using `itertools.starmap`:

```python
from itertools import starmap

# List of coordinates representing sides of triangles
coordinates = [(2, 3, 4), (3, 4, 5), (6, 8, 10), (1, 5, 7), (7, 4, 10)]

# Apply Pythagorean theorem to each set of coordinates
right_triangles = list(starmap(lambda x, y, z: True if ((x * x) + (y * y)) == (z * z) else False, coordinates))

print("Tuples which form right-angled triangle:", right_triangles)

# Print the coordinates that form right-angled triangles
print("The right triangle coordinates are:", [coord for coord, is_right in zip(coordinates, right_triangles) if is_right])
```

In this example, `starmap` applies the lambda function to each tuple in the `coordinates` list.  
The lambda function takes three arguments, `x`, `y`, and `z`, representing the sides of a triangle,  
and returns `True` if the sides form a right-angled triangle (according to the Pythagorean theorem),  
and `False` otherwise¹.

## splitter function

Functional way of splitting data.  

```python
def splitter(data, pred):
    yes, no = [], []
    for d in data:
        (yes if pred(d) else no).append(d)
    return [yes, no]


def has3chars(e: str):
    return len(e) == 3


def starts_w(e: str):
    return e.startswith('w')


vals = ['sky', 'top', 'small', 'warm', 'cup', 'notice', 'war', 'horse']

yes, no = splitter(vals, has3chars)
print(yes)
print(no)

yes, no = splitter(vals, starts_w)
print(yes)
print(no)
```

## groupby function

The `groupby` function requires sorting of data.    

Splitting users into groups by occupation.  

```python
from itertools import groupby

users = [
    {'first_name': 'John', 'last_name': 'Doe', 'occupation': 'gardener'},
    {'first_name': 'Roger', 'last_name': 'Roe', 'occupation': 'driver'},
    {'first_name': 'Adam', 'last_name': 'Novak', 'occupation': 'teacher'},
    {'first_name': 'Paul', 'last_name': 'Novak', 'occupation': 'programmer'},
    {'first_name': 'Roman', 'last_name': 'Meszaros', 'occupation': 'programmer'},
    {'first_name': 'Tomas', 'last_name': 'Bruzik', 'occupation': 'driver'},
]

users.sort(key=lambda user: user['occupation'])

for key, group in groupby(users, key=lambda user: user['occupation']):

    print(f'{key}s:')
    print(list(group))
```

## Custom groupby function

```python

def group_by(seq, f):

    groups = {}

    for e in seq:
        
        res = f(e)

        if res in groups:
            groups[res].append(e)
        else:
            groups[res] = [e]

    return groups



vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = group_by(vals, lambda e: e % 2 == 0)
print(res)

words = ['sky', 'top', 'small', 'warm', 'cup', 'notice', 'war', 'horse']

res = group_by(words, len)
print(res)
```

```python
from collections import namedtuple


def group_by(seq, f):

    groups = {}

    for e in seq:

        res = f(e)

        if res in groups:
            groups[res].append(e)
        else:
            groups[res] = [e]

    return groups


User = namedtuple('User', 'fname lname occupation')

users = [
    User('John', 'Doe', 'gardener'),
    User('Roger', 'Roe', 'driver'),
    User('Adam', 'Novak', 'teacher'),
    User('Paul', 'Novak', 'programmer'),
    User('Roman', 'Meszaros', 'programmer'),
    User('Tomas', 'Bruzik', 'driver')
]

res = group_by(users, lambda user: user.occupation)

for k in res.keys():
    print(k, res[k])
```


## Splitting data   

Splitting data by predicate function.  

```python
import itertools as it

def pred(e):

    return e % 2

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s_vals = sorted(vals, key=pred)

res = [tuple(v) for _, v in it.groupby(s_vals, key=pred)]

print(res)
```

## partition function 

The `more_itertools` has a function for this called `partition`.  
It is a third-party library.  

```python
from more_itertools import partition

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

yes, no = partition(lambda e: e %2, vals)
print(list(yes), list(no))
```

