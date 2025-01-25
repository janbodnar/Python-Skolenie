# Generators 

A generator is a special type of iterator that produces values on-the-fly instead of storing  
them all in memory. Unlike regular functions that return a single value and exit, generators  
use the `yield` keyword to pause execution and resume later, retaining their state between  
iterations. This *lazy evaluation* makes them ideal for:

- Processing large or infinite datasets.
- Reducing memory overhead.
- Building data pipelines.

Key points about generators:  
  
1. **Yield Keyword**: Instead of returning a single value, a generator can yield  
   a series of values, pausing after each one and resuming from the same state  
   when the next value is requested. This is achieved using the `yield` keyword.  
  
2. **Memory Efficiency**: Generators are more memory-efficient compared to  
   regular functions that return a list. This is because generators generate  
   values one at a time and do not store the entire sequence in memory.  
  
3. **Lazy Evaluation**: Generators perform lazy evaluation. This means that  
   values are generated only when they are needed, reducing memory consumption  
   and allowing for efficient use of resources.  
  
4. **State Retention**: Generators retain their state between iterations. Each  
   time the generator's `__next__()` method is called (either implicitly via a  
   loop or explicitly), it resumes execution from where it left off and  
   continues until it encounters another `yield` statement or the function  
   completes.

## Syntax 

Generators can be defined in two ways:

- Generator Functions: Use yield instead of return.
- Generator Expressions: Similar to list comprehensions but with `()`.


   
  
Here's a simple example of a generator function:  
  
```python  
def count_up_to(max):  
    count = 1  
    while count <= max:  
        yield count  
        count += 1  
  
# Usage  
counter = count_up_to(5)  
for number in counter:  
    print(number)  # Outputs: 1, 2, 3, 4, 5  
```  
  
In this example, `count_up_to` is a generator function that yields numbers from  
1 up to a specified maximum. The `for` loop iterates over the generator,  
printing each number one at a time.  
  
Generators are handy for working with large datasets or streams of data where  
generating and storing the entire sequence at once would be impractical.  

  
## When to Use Generators

- Processing large datasets (files, streams).  
- Working with infinite sequences (e.g., Fibonacci numbers).  
- Memory-constrained environments (e.g., IoT devices).  


## Example 

The script measures and prints the maximum memory usage of both  
the generator-based and list-based functions, allowing you to compare  
their memory efficiency.

```python
# pip install memory_profiler

from memory_profiler import memory_usage

def sum_squares_generator(n):
    return sum(i**2 for i in range(n))

def sum_squares_list(n):
    return sum([i**2 for i in range(n)])


n = 10_000_000

# Measure memory usage of generator-based function
gen_mem_usage = memory_usage((sum_squares_generator, (n,)), interval=0.1)

# Measure memory usage of list-based function
list_mem_usage = memory_usage((sum_squares_list, (n,)), interval=0.1)

print(f"Max memory usage (generator): {max(gen_mem_usage)} MiB")
print(f"Max memory usage (list): {max(list_mem_usage)} MiB")
```

## Chaining of operations

Generators can be combined for efficient data transformations.  

```python
from memory_profiler import memory_usage

def generator_chain(n):
    numbers = (i for i in range(n) if i % 2 == 0)
    squares = (i**2 for i in numbers)
    return sum(squares)

def list_chain(n):
    numbers = [i for i in range(n) if i % 2 == 0]
    squares = [i**2 for i in numbers]
    return sum(squares)

if __name__ == "__main__":
    n = 10_000_000

    gen_mem_usage = memory_usage((generator_chain, (n,)), interval=0.1)
    list_mem_usage = memory_usage((list_chain, (n,)), interval=0.1)

    print(f"Max memory usage (generator): {max(gen_mem_usage)} MiB")
    print(f"Max memory usage (list): {max(list_mem_usage)} MiB")
```

1. **Memory Efficiency**:   
    - **Generators**: Generators are more memory-efficient as they generate  
      items on-the-fly and do not store the entire list in memory. This is  
      particularly useful when dealing with large datasets.  
    - **Lists**: Lists store all elements in memory, which can lead to high  
      memory usage and potential memory errors for large datasets.  
  
2. **Performance**:  
    - **Generators**: Generators have a slight overhead due to yielding values  
      one at a time, but the difference is usually negligible compared to the  
      memory benefits.  
    - **Lists**: List comprehensions can be faster for smaller datasets because  
      they avoid the generator overhead, but they are impractical for large  
      datasets due to memory constraints.  

## Reading large files

When working with large files, loading the entire file into memory can be inefficient  
and impractical. Instead, you can use a generator to read the file line-by-line:  

```python
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Usage
file_path = 'large_file.txt'
for line in read_large_file(file_path):
    process(line)  # Replace with your processing logic
```
