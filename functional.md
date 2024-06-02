# Functional programming


Functional programming is a programming paradigm where the primary method of  
computation is the evaluation of functions. 

Key points:

- **Pure Functions**: Ideally, functions only take inputs and produce outputs, without any  
  internal state that affects the output produced for a given input². Functions that have no  
  side effects at all are called purely functional.  

- **First-Class Functions**: In functional programming, functions are considered *first-class citizens*.  
  This means we can use them to store and manipulate data.  

- **Declarative Style**: It is a declarative type of programming style. Its main focus is on "what to solve"  
  in contrast to an imperative style where the main focus is “how to solve”³.

- **Python and Functional Programming**: Python supports functional programming but also contains features
  of other programming models. While Python is not primarily a functional language, it's good to be familiar
  with `lambda`, `map()`, `filter()`, and `reduce()` because they can help you write concise,
  high-level, parallelizable code.

In a functional program, input flows through a set of functions. Each function operates on its input and produces  
some output. This style discourages functions with side effects that modify internal state or make other changes   
that aren't visible in the function's return value.


## itertools 

```python
from itertools import product


res = list(product('ABCD', repeat=2))
print(res)
```
