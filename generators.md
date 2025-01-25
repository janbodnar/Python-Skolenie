# Generators 

In Python, a generator is a special type of function that returns an iterator,  
which we can iterate over (one value at a time). They are used to create  
iterators in a more straightforward way. Here are the key points about  
generators:  
  
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
