# Timing 

The `timeit` module provides a simple way to time small bits of Python code.  


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
