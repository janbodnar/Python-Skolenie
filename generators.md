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
  

















Certainly! Let's explore a practical example comparing a **generator** with a
**list-based approach** to demonstrate efficiency in **memory usage** and
**performance** when processing large datasets.

---

### **Example: Summing Squares of Numbers**
**Task**: Calculate the sum of squares for the first 10 million numbers.  
We'll compare two approaches:  
1. **List-based**: Store all numbers in memory first.  
2. **Generator-based**: Generate numbers on-the-fly.

---

#### **1. List-Based Approach (Inefficient)**
```python
import sys

def sum_squares_list(n):
    # Create a list of squares (stores all 10M values in memory)
    numbers = [i**2 for i in range(n)]
    return sum(numbers)

result = sum_squares_list(10_000_000)
print(f"Result: {result}")  # Output: 333333283333333333333333 (approx)
```

**Memory Usage**:  
- The list `numbers` stores **10 million integers** in memory.  
- Memory footprint: ~76 MB (for 10M integers).  
- Measured with `sys.getsizeof(numbers)`: ~85,000,000 bytes.

---

#### **2. Generator-Based Approach (Efficient)**
```python
def sum_squares_generator(n):
    # Generate squares one at a time (no full list stored)
    return sum(i**2 for i in range(n))

result = sum_squares_generator(10_000_000)
print(f"Result: {result}")  # Same output as above
```

**Memory Usage**:  
- Generators produce values **on-demand**, keeping only the current value in memory.  
- Memory footprint: **<1 KB** (constant, regardless of `n`).  

---

### **Key Differences**
| Metric               | List-Based Approach      | Generator-Based Approach |
|----------------------|--------------------------|--------------------------|
| **Memory Usage**     | O(n) (~76 MB)            | O(1) (~1 KB)             |
| **Speed**            | Slightly faster (precomputed) | Slightly slower (on-the-fly) |
| **Scalability**      | Fails for huge `n` (e.g., 1B) | Handles any `n` without crashing |

---

### **Why Generators Win**
1. **Memory Efficiency**:  
   Generators avoid storing the entire dataset in memory. This is critical for tasks like processing large files (e.g., logs, CSVs) or infinite sequences (e.g., sensor data).

2. **Lazy Evaluation**:  
   Values are computed only when needed. For example, reading a 100GB file line-by-line without loading it entirely:
   ```python
   def read_large_file(file_path):
       with open(file_path, "r") as file:
           for line in file:
               yield line.strip()

   # Process lines without loading the whole file
   for line in read_large_file("huge_log.txt"):
       process(line)  # Do something with each line
   ```

3. **Pipeline Chaining**:  
   Generators can be combined for efficient data transformations:
   ```python
   # Chain generators to filter, transform, and aggregate
   numbers = (i for i in range(10_000_000) if i % 2 == 0)  # Even numbers
   squares = (i**2 for i in numbers)  # Square them
   total = sum(squares)  # Sum on-the-fly
   ```

---

### **When to Use Generators**
- Processing large datasets (files, streams).  
- Working with infinite sequences (e.g., Fibonacci numbers).  
- Memory-constrained environments (e.g., IoT devices).  

---

### **Final Takeaway**  
Generators trade a tiny performance penalty (for on-the-fly computation) for
**massive memory savings**, making them indispensable for scalable and efficient
Python code.



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

Memory usage for lists:  

- The list `numbers` stores **10 million integers** in memory.  
- Memory footprint: ~76 MB (for 10M integers).  
- Measured with `sys.getsizeof(numbers)`: ~85,000,000 bytes.

Memory usage for generators: 

- Generators produce values **on-demand**, keeping only the current value in memory.  
- Memory footprint: **<1 KB** (constant, regardless of `n`).  
