# memory_profiler

`memory_profiler` is a Python library used to monitor and profile the memory usage  
of a Python program. It helps developers track memory usage and identify memory leaks  
in their code by providing detailed reports on how memory is allocated and used  
throughout the execution of the program.

Key features:

- Line-by-line memory usage: It shows the memory usage of each line of a Python function,  
  helping to pinpoint areas with high memory consumption.  
- Simple integration: By using decorators like @profile, you can easily mark functions for  
  memory profiling.  
- Real-time monitoring: It can display memory usage information in real-time, providing  
  immediate insights into memory behavior.

## The @profile decorator

The `@profile` decorator is a tool from the memory_profiler library in Python used to monitor  
and measure the memory usage of a specific function. When you add the `@profile` decorator to  
a function, it tracks the memory usage of the function line by line, providing detailed insights  
into how much memory is being used before and after each line of code within that function.

```python
from memory_profiler import profile

# Define a function to monitor its memory usage
@profile
def allocate_memory(n, count):
    strings = []
    for i in range(count):
        # Create a large string
        large_string = "a" * (n * n)
        strings.append(large_string)
        print(f"String {i+1} of length {n * n} created")
    return strings

# Call the function with larger value and multiple allocations
if __name__ == "__main__":
    allocate_memory(2000, 30)
```

`py -m memory_profiler mem_prof.py`


## The memory_usage function

The `mem_usage` function from the `memory_profiler` library is used to get the current memory usage  
of a process or specific code block. It returns the memory usage in MiB (Mebibytes) and can be helpful  
for monitoring memory consumption in your program.  

```python
import pandas as pd
import numpy as np
import time
from memory_profiler import memory_usage

def pandas_example():
    # Create a large dataset
    num_rows = 10**7
    df = pd.DataFrame({
        'col1': np.random.randint(0, 100, size=num_rows),
        'col2': np.random.random(size=num_rows),
        'col3': np.random.choice(['A', 'B', 'C', 'D'], size=num_rows)
    })

    # Measure memory usage and time taken for a pandas operation
    start_time = time.time()
    mem_usage = memory_usage((df['col1'].mean, ()))
    end_time = time.time()

    print(f"Pandas Memory Usage: {max(mem_usage)} MB")
    print(f"Pandas Time Taken: {end_time - start_time} seconds")

if __name__ == '__main__':
    pandas_example()
```
