# The argparse module 

The `argparse` module makes it easy to write user-friendly command-line interfaces. It parses the  
defined arguments from the `sys.argv`. The module also automatically generates help and usage messages,  
and issues errors when users give the program invalid arguments.  

The argparse is a standard module; we do not need to install it. A parser is created with `ArgumentParser`  
and a new parameter is added with `add_argument`. Arguments can be optional, required, or positional.  

## Optional arguments 

The following example creates a simple argument parser. 

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

The example adds one argument having two options: a short `-o` and a long `--ouput`.   
These are optional arguments.

```python
import argparse
```

The module is imported.

```python
parser.add_argument('-o', '--output', action='store_true', 
    help="shows output")
```

An argument is added with `add_argument`. The action set to `store_true` will store the argument as `True`,   
if present. The help option gives argument help.

```python
args = parser.parse_args()
```

The arguments are parsed with parse_args. The parsed arguments are present as object attributes. In our case,   
there will be `args.output` attribute.

```python
if args.output:
    print("This is some output")
```

If the argument is present, we show some output.

```
$ optional_arg.py -o
This is some output
$ optional_arg.py --output
This is some output
```

We run the program with the `-o` and `--output`.

```
$ optional_arg.py --help
usage: optional_arg.py [-h] [-o]

optional arguments:
    -h, --help    show this help message and exit
    -o, --output  shows output
```

We can show the program help.

