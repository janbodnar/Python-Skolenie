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
