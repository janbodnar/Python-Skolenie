# Functional programming


Functional programming is a programming paradigm where the primary method of  
computation is the evaluation of functions. 

Key points:

- **Pure Functions**: Ideally, functions only take inputs and produce outputs, without any  
  internal state that affects the output produced for a given input. Functions that have no  
  side effects at all are called purely functional.  

- **First-Class Functions**: In functional programming, functions are considered *first-class citizens*.  
  This means we can use them to store and manipulate data.  

- **Declarative Style**: It is a declarative type of programming style. Its main focus is on "what to solve"  
  in contrast to an imperative style where the main focus is "how to solve".

Python supports functional programming but also contains features of other programming models. While Python  
is not primarily a functional language, it's good to be familiar with `lambda`, `map`, `filter`, and `reduce`   
because they can help you write concise, high-level, parallelizable code.  

In a functional program, input flows through a set of functions. Each function operates on its input and produces   
some output. This style discourages functions with side effects that modify internal state or make other changes   
that aren't visible in the function's return value.  


## itertools 

```python
from itertools import product


res = list(product('ABCD', repeat=2))
print(res)
```

### Permutations and combinations

Permutations and combinations are two concepts in mathematics that deal with counting or arranging objects.  
*Permutations* are  used when the order of arrangement matters. *Combinations* are is used when the order  
of arrangement does not matter.  

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



