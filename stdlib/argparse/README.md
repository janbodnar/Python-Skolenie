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

## Verbose argument 

```python
import argparse

parser = argparse.ArgumentParser()
   
parser.add_argument('-v', type=int, required=True, help="computes cube")
parser.add_argument('--verbose', action='store_true', help="gives verbose output")
args = parser.parse_args()

val = args.v
cubed = val * val * val

if args.verbose:
    print(f'{val} cubed is {cubed}')
else:
    print(cubed)
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


## The nargs argument 

The `nargs` specifies the number of command-line arguments that should be consumed.

```python
import argparse
import sys

# nargs sets the required number of argument values
# metavar gives name to argument values in error and help output

parser = argparse.ArgumentParser()
parser.add_argument('chars', type=str, nargs=2, metavar='c',
                    help='starting and ending character')

args = parser.parse_args()

try:
    v1 = ord(args.chars[0])
    v2 = ord(args.chars[1])

except TypeError as e:

    print('Error: arguments must be characters')
    parser.print_help()
    sys.exit(1)

if v1 > v2:
    print('first letter must precede the second in alphabet')
    parser.print_help()
    sys.exit(1)
```

The example shows a sequence of characters from character one to character two.   
It expects two arguments.

```
parser.add_argument('chars', type=str, nargs=2, metavar='c',
    help='starting and ending character')
```

With `nargs=2` we specify that we expect two arguments.

```
$ charseq.py e k
e f g h i j k
```

The program shows a sequence of characters from e to k.

Variable number of arguments can be set with the `*` character.

```python
import argparse

# * nargs expects 0 or more arguments

parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs='*')
args = parser.parse_args()

print(f"The sum of values is {sum(args.num)}")
```

The example computes the sum of values; we can specify variable number of  
arguments to the program.

```
$ var_args.py 1 2 3 4 5
The sum of values is 15
```

We set 1+ arguments with `nargs='+'`.

```
import argparse

# + nargs expects 1+ arguments

parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs='+')
args = parser.parse_args()

print(f"The sum of values is {sum(args.num)}")
```


## The choices option 

The choices option limits arguments to the given list.

```python
import argparse
import datetime
import time

# choices limits argument values to the 
# given list

parser = argparse.ArgumentParser()

parser.add_argument('--now', dest='format', choices=['std', 'iso', 'unix', 'tz'],
                    help="shows datetime in given format")

args = parser.parse_args()
fmt = args.format

if fmt == 'std':
    print(datetime.date.today())
elif fmt == 'iso':
    print(datetime.datetime.now().isoformat())
elif fmt == 'unix':
    print(time.time())
elif fmt == 'tz':
    print(datetime.datetime.now(datetime.timezone.utc))
```

In the example, the now option can accept the following values: `std`, `iso`, `unix`, or `tz`.

```
$ ./mytime.py --now iso
2022-08-20T09:44:22.437880
$ ./mytime.py --now unix
1660981466.8261166
```


## Head example

The following example mimics the Linux head command. It shows the n lines of a text from the   
beginning of the file.

The `words.txt` file: 

```
sky
top
forest
wood
lake
wood
```

For the example, we have this small test file.

```python
import argparse
from pathlib import Path

# head command
# working with positional arguments

parser = argparse.ArgumentParser()
   
parser.add_argument('f', type=str, help='file name')
parser.add_argument('n', type=int, help='show n lines from the top')

args = parser.parse_args()

filename = args.f

lines = Path(filename).read_text().splitlines()

for line in lines[:args.n]:
    print(line)
```

The example has two options: `f` for a file name and `-n` for the number of lines to show.

```
$ head.py words.txt 3
sky
top
forest
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

The example names the expected value value. The default name is `V`.

```
$ metavar.py -h
usage: metavar.py [-h] -v value

optional arguments:
  -h, --help  show this help message and exit
  -v value    computes cube for the given value
```

The given name is shown in the help output.


## Example

Modify this program to take the ticker name from the command line argument.  

```python
#!/usr/bin/python

import asyncio
import ccxt.async_support as ccxt

from rich import box
from rich.console import Console
from rich.table import Table
from datetime import datetime, timezone


async def tickers():

    binance = ccxt.binance()
    data = await binance.fetch_ohlcv('LTCUSDT', '1d', limit=20)
    await binance.close()

    now = f'{datetime.today()}'
    table = Table(title='Binance - LTC/USDT', box=box.ASCII,
                  caption=now, caption_justify='left')

    table.add_column('Date', justify='center', style='steel_blue')
    table.add_column('Open')
    table.add_column('High')
    table.add_column('Low')
    table.add_column('Close')
    table.add_column('Volume', justify='right', style='cadet_blue')

    for e in data:
        d = datetime.fromtimestamp(e[0]/1000.0, tz=timezone.utc)
        table.add_row(f'{d:%m/%d/%Y}', f'{e[1]:.2f}', f'{e[2]:.2f}',
                      f'{e[3]:.2f}', f'{e[4]:.2f}', f'{e[5]:.5f}')

    console = Console()
    console.print(table)

asyncio.run(tickers())
```









