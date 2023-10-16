# Interactive Python

Python code can be launched in two basic ways. As a script or inside an interactive interpreter.

```python
#!/usr/bin/python

# first.py

print("The Python tutorial")
```

This is an example of a small Python script. It is launched from a UNIX shell.  

```
$ ./first.py 
The Python tutorial
```


## Interactive interpreter
Another way of running Python code is the interactive Python interpreter. The Python interpreter is very  
useful for our explorations. When we quickly want to test some basic functionality of the Python language  
and we don't want to write a whole script. To get the interactive interpreter, we execute the Python  
command on our favourite shell.  

```
$ python
Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
This is the welcome message of the Python interpreter. We see the version of Python on our machine.  
In our case it is Python 3.10.12. The ">>>" is the prompt used in the Python interactive mode. To leave  
the interpreter and return back to the shell, we can type Ctrl+D or quit. Typing Ctrl+L clears  
the screen of the Python interpreter.  

Now we can query for some useful information.

```
>>> credits
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
```
If we type credits we get some information about organizations involved in Python development.
```
>>> copyright
Copyright (c) 2001-2023 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
```
The license command provides several pages regarding the license of Python.

## Getting help

The help command provides some help about Python.

```
>>> help
Type help() for interactive help, or help(object) for help about object.
>>>
```

We can use the command in two ways. Either we can get some help about a specific object or we enter a interactive help mode.
For example, if we type ```help(True)```, we get some information about bool objects.

Help on bool object:

```
class bool(int)
 |  bool(x) -> bool
 |  
 |  Returns True when the argument x is true, False otherwise.
 |  The builtins True and False are the only two instances of the class bool.
 |  The class bool is a subclass of the class int, and cannot be subclassed.
 |  
 |  Method resolution order:
 |      bool
 |      int
 |      object
 |  
 |  Methods defined here:
 |  
 |  __and__(...)
 |      x.__and__(y) <==> x&y
...
```

If the topic is larger than one page, we can scroll it using the arrows. If we want to quit  
the topic, we press the q key.

If we type help we get the interactive help mode of the interpreter.

```
>>> help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".
help>
```
To leave the help mode and return to the interpreter, we use the quit command.

The keywords command gives a list of available keywords in Python programming language.

```
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 


```

If we type any of the keywords, we get some help on it.

The modules command gives a list of available modules. Again, typing a name of the module  
will provide additional help.

Finally, we have the topics command.

```
help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES  
The topics command gives a list of topics regarding Python programming language. Here we can find some useful information.
```

## Python code
Next we have some practical examples of Python interpreter.

```
>>> 2 + 4
6
>>> 5 * 56
280
>>> 5 - 45
-40
>>>
```
 
Python interpreter can be used as a calculator. Each expression is executed right away and  
the result is shown on the screen.

```
>>> a = 3
>>> b = 4
>>> a**b
81
>>> a == b
False
>>> a < b
True
>>>
```

We can define variables and perform operations on them.
```
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 
'SystemRandom', 'TWOPI', 'WichmannHill', '_BuiltinMethodType', '_MethodType',
'__all__', '__builtins__', '__doc__', '__file__', '__name__', '_acos', 
'_ceil', '_cos', '_e', '_exp', '_hexlify', '_inst', '_log', '_pi', '_random',
'_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 
'betavariate', 'choice', 'expovariate', 'gammavariate', 'gauss', 
'getrandbits', 'getstate', 'jumpahead', 'lognormvariate', 'normalvariate',
'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed',
'setstate', 'shuffle', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>>
```

Here we imported a random module. With the dir function, we further explore the random module.

With the help of the special `__doc__` string, we can get help on a specific function.

```
>>> print(random.seed.__doc__)
Initialize internal state from hashable object.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If a is not None or an int or long, hash(a) is used instead.
>>>
```

The `locals` command shows our current local namespace.

```
>>> locals()
{'random': <module 'random' from '/usr/lib/python3.5/random.py'>, '__spec__': None, 
'__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, 
'__builtins__': <module 'builtins' (built-in)>, '__doc__': None, '__name__': '__main__'}
```

We can see the random module that we have previously imported.

```
>>> class Car:
...   pass
... 
>>> def function():
...   pass
... 
>>> for i in range(5):
...   print(i)
... 
0
1
2
3
4
>>>
```

We can define our own classes, functions, or use control flow structures. We must not forget to indent  
the code. To finish each of these blocks of code, we type Enter key twice.

```
>>> import os
>>> os.getcwd()
'/home/vronskij/programming/python'
>>> os.system('ls')
command_line_arguments.py  read_input.py
0
```

Here we import the os module and interact with the operating system.

Finally, we want to exit the interpreter. We can exit the interpreter in several ways:

- `Ctrl+D`
- `quit()`

We can also exit the interpreter programatically.
```
>>> raise SystemExit
$
```

or

```
>>> import sys
>>> sys.exit()
$
```

The interpreter is exited.

## The Zen of Python

The Zen of Python is a set of rules how to write good Python code. It reflects somehow 
the philosophy of the language.

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
The rules can be read by launching import this.
```
