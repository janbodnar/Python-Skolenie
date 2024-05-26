# The argparse module 

The `argparse` module makes it easy to write user-friendly command-line interfaces. It parses the  
defined arguments from the `sys.argv`. The module also automatically generates help and usage messages,  
and issues errors when users give the program invalid arguments.  

The argparse is a standard module; we do not need to install it. A parser is created with `ArgumentParser`  
and a new parameter is added with `add_argument`. Arguments can be optional, required, or positional.  

## Optional arguments 

```python
import argparse

# help flag provides flag help
# store_true actions stores argument as True

parser = argparse.ArgumentParser()
   
parser.add_argument('-o', '--output', action='store_true', 
    help="shows output")

args = parser.parse_args()

if args.output:
    print("This is some output")
```


