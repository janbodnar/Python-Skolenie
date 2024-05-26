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

## Required argument

An argument is made required with the `required` option.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True)

args = parser.parse_args()
print(f'Hello {args.name}')
```

## Positional arguments

The following example works with positional arguments. They are created with `add_argument`.

```python
import argparse

parser = argparse.ArgumentParser()
   
parser.add_argument('name')
parser.add_argument('age')

args = parser.parse_args()

print(f'{args.name} is {args.age} years old')
```

The example expects two positional arguments: `name` and `age`.

```
$ positional_arg.py Peter 23
Peter is 23 years old
```

## Python argparse dest

The `dest` option of the `add_argument` gives a name to the argument. If not given, it is   
inferred from the option.

```python
import argparse
import datetime

# dest gives a different name to a flag

parser = argparse.ArgumentParser()
parser.add_argument('-n', dest='now', action='store_true', help="shows now")
args = parser.parse_args()

# we can refer to the flag
# by a new name
if args.now:

    now = datetime.datetime.now()
    print(f"Now: {now}")
```

## Argument type

The `type` argument determines the argument type.

```python
import argparse
import random

# type determines the type of the argument

parser = argparse.ArgumentParser()
   
parser.add_argument('-n', type=int, required=True, 
    help="define the number of random integers")
args = parser.parse_args()

n = args.n

for i in range(n):
    print(random.randint(-100, 100))
```

## Default arg value

The `default` option specifies the default value, if the value is not given.

```python
import argparse

# required defines a mandatory argument 
# default defines a default value if not specified

parser = argparse.ArgumentParser()

parser.add_argument('-b', type=int, required=True, help="defines the base value")
parser.add_argument('-e', type=int, default=2, help="defines the exponent value")
args = parser.parse_args()

val = 1

base = args.b
exp = args.e

for i in range(exp):
    val *= base

print(val)
```

The example computes exponentiation. The exponent value is not required; if not given, the default will be 2.

```
$ power.py -b 3
9
$ power.py -b 3 -e 3
27
```

## The append action

The `append` action allows to group repeating options.
   
```python
import argparse

# append action allows to group repeating
# options

parser = argparse.ArgumentParser()
   
parser.add_argument('-n', '--name', dest='names', action='append', 
    help="provides names to greet")

args = parser.parse_args()

names = args.names

for name in names:
    print(f'Hello {name}!')
```

The example produces greeting messages to all names specified with the `n` or `name` options;
they can be repeated multipile times.

```
$ appending.py -n Peter -n Lucy --name Jane
Hello Peter!
Hello Lucy!
Hello Jane!
```


## The metavar option

The `metavar` option gives a name to the expected value in error and help outputs.

```python
import argparse

# metavar gives name to the expected value 
# in error and help outputs

parser = argparse.ArgumentParser()
   
parser.add_argument('-v', type=int, required=True, metavar='value', 
    help="computes cube for the given value")
args = parser.parse_args()

print(args)

val = args.v

print(val * val * val)
```

The example names the expected value value. The default name is V.

```
$ metavar.py -h
usage: metavar.py [-h] -v value

optional arguments:
  -h, --help  show this help message and exit
  -v value    computes cube for the given value
```
The given name is shown in the help output.














