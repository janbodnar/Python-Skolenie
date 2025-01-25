# Generators 



```python

# pip install memory_profiler

from memory_profiler import memory_usage

def sum_squares_generator(n):
    return sum(i**2 for i in range(n))

def sum_squares_list(n):
    return sum([i**2 for i in range(n)])

if __name__ == "__main__":
    n = 10_000_000

    # Measure memory usage of generator-based function
    gen_mem_usage = memory_usage((sum_squares_generator, (n,)), interval=0.1)

    # Measure memory usage of list-based function
    list_mem_usage = memory_usage((sum_squares_list, (n,)), interval=0.1)

    print(f"Max memory usage (generator): {max(gen_mem_usage)} MiB")
    print(f"Max memory usage (list): {max(list_mem_usage)} MiB")
```
