# Timing 

The `timeit` module provides a simple way to time small bits of Python code.  


`timeit.timeit(stmt, setup, timer, number)`

parameters:

- stmt which is the statement you want to measure; it defaults to `pass`.  
- setup which is the code that you run before running the stmt; it defaults to `pass`.   
  We generally use this to import the required modules for our code.  
- timer which is a `timeit.Timer` object; it usually has a sensible default value so we  
  don't have to worry about it.  
- the `number` which is the number of executions you’d like to run the `stmt`.  

## Simple statement

```python
import timeit

stm = "5+5"
print(timeit.timeit(stmt=stm, number=50_000_000))
```

## power

```python
import timeit

stm = "3**3"
print(timeit.timeit(stmt=stm, number=50_000_000))

stm = "pow(3, 3)"
print(timeit.timeit(stmt=stm, number=50_000_000))
```

## for vs while

```python
import timeit


mycode = ''' 
def fn(): 
    for e in range(10000): 
        print(e)
'''

mycode2 = ''' 
def fn():
    i = 0
    while i < 10000:
        print(e)
        i += 1
'''

print(timeit.timeit(stmt=mycode, number=5_000_000))
print(timeit.timeit(stmt=mycode2, number=5_000_000))
```

## Decorator

```python
import timeit


def time_it(fn):

    def wrapper(*args, **kwargs):

        t0 = timeit.default_timer()
        fn(*args, **kwargs)
        t1 = timeit.default_timer()

        print("{0:.10f} seconds".format(t1 - t0))

    return wrapper


@time_it
def fstring_fn(vals):
    print("fstring_fn:", f"{vals[0]} {vals[1]} {vals[2]} {vals[3]} {vals[4]}")


@time_it
def format_fn(vals):
    print("format_fn:", "{0} {1} {2} {3} {4}".format(*vals))


@time_it
def oldschool_fn(vals):
    print("oldschool_fn:", "%s %s %s %s %s" % vals)


data = ('sky', 'pen', 23.0, -11, True)


fstring_fn(data)
print('---------------')
format_fn(data)
print('---------------')
oldschool_fn(data)
```

## The time module 

```python
import time
import random, faker

tm1 = time.perf_counter()

vals = [random.randrange(850, 3000, 50) for e in range(500_000)]

tm2 = time.perf_counter()
print(f'Total time elapsed: {tm2-tm1:0.2f} seconds')


faker = faker.Faker()

tm1 = time.perf_counter()

vals = [faker.random_int(850, 3000, 50) for e in range(500_000)]

tm2 = time.perf_counter()
print(f'Total time elapsed: {tm2-tm1:0.2f} seconds')
```
