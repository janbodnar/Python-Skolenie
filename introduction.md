# Introduction


## Python

Python is a general-purpose, dynamic, object-oriented programming language.  
The design purpose of the Python language emphasizes programmer productivity  
and code readability.  

Python was initially developed by Guido van Rossum.  

It was first released in 1991. 

Python was inspired by:

- ABC
- Haskell
- Java
- Lisp
- Icon
- Perl

Python is a high-level, general purpose, multi-platform, interpreted language.  
Python is maintained by a large group of volunteers worldwide. Python is open source software.  

Python is a minimalistic language. One of its most visible features is that it  
does not use semicolons nor brackets; Python uses indentation instead.  

Python supports several programming styles. It does not force a programmer to a specific  
paradigm. It supports procedural, object oriented, and functional programming.  


The official web site for the Python programming language is [python.org](https://python.org)

![Python](images/python.jpg)


## Basic characteristics

1. *High-Level and Readable*: Python is a high-level language designed for readability.  
2. *Interpreted*: Python runs on an interpreter system, allowing code execution as soon as  
   it's written. This makes prototyping quick and efficient.  
4. *Dynamic Typing*: You don't need to declare variable types explicitly; Python infers  
   them dynamically during runtime.  
5. *Significant Indentation*: Python uses whitespace (indentation) to define scope, such as loops,  
   functions, and classes. No curly braces are needed.
6. *Versatile Use Cases*:  
   - Web development (server-side)  
   - Software development  
   - Mathematics and scientific computing  
   - System scripting  
   - Handling big data  
7. *Cross-Platform*: Python works on various platforms (Windows, Mac, Linux, Raspberry Pi, etc.).
8. *Fewer Lines of Code*: Python allows developers to write programs with fewer lines compared  
    to some other languages.


## Python implementations

Formally, Python programming language is a specification. There are three main implementations  
of Python: CPython, IronPython, and Jython. CPython is implemented in C language. It is the  
most widely used implementation of Python. When people talk about Python language, they  
mostly mean CPython. IronPython is implemented in C#. It is part of the .NET framework.  
Similarly, Jython is an implementation of the Python language in Java. Jython  
program is translated into the Java bytecode and executed by the JVM (Java Virtual Machine).  
In this tutorial, we work with CPython.  

 
## Popularity
 
Python belongs to the most popular programming languages. Several surveys put Python to top ten  
languages. Some very popular Python projects include  
a distributed source management tool Mercurial, a Django web framework, a PyQt GUI library,  
or a package management utility called Yum.  

[Stackoverflow survey ](https://survey.stackoverflow.co/2023/#programming-scripting-and-markup-languages)  
[JetBrains survey](https://www.jetbrains.com/lp/devecosystem-2023/python/)  

## Learning materials 

Books:  
- [Python Crash Course](https://www.amazon.co.uk/Python-Crash-Course-3Rd-Matthes/dp/1718502702)

Videos:  
- [Python for Everyone: From Zero to Hero 6 Hours Complete Course](https://www.youtube.com/watch?v=JZDQKj9BOoc)
- [Python Full Course for Beginners](https://www.youtube.com/watch?v=H2EJuAcrZYU)

## Python scripts

Every script in the Unix starts with a <em>shebang</em>. The shebang is the first two  
characters in the script: <code>#!</code>. The shebang is followed by the  
path to the interpreter, which will execute our script. Shebangs do not work on Windows;  
but it it a good practice to include them even on Windows, since we might expect our 
programs to be run on Unix, too. 


```python
# simple.py

print("The Python tutorial")
```

This is our first Python script. The script will print "The Python tutorial"  
string to the console. Python scripts have `.py` extension.  


```
$ which python
/usr/bin/python
```

We can find out the path to the Python interpreter using the <code>which</code> command.  


Python scripts can be run in two ways:  

```
$ python first.py
The Python tutorial
```

<p>
Python script is given as an argument to the interpreter. 
</p>

```
$ chmod +x first.py 
$ ./first.py 
The Python tutorial
```


We use the <code>chmod</code> command to make the file executable. 
The program is launched.

## Lists 

A Python list is a fundamental data structure that allows you to store an ordered  
collection of items. Here are some key characteristics of Python lists:

- Ordered: Elements in a list have a defined sequence, and the order you add them  
  in is preserved. This means you can access elements by their position (index) in the list.  
- Mutable: You can change, add, or remove elements from a list even after it's created.  
  This makes them flexible for storing and manipulating data.  
- Heterogeneous: Lists can hold elements of different data types (e.g., integers, strings, booleans)  
  within the same list.  

You can create a Python list using square brackets `[]` and separating elements with commas.  

```python
vals = [1, 2, 3, 4, 5]
print(vals)

for val in vals:
    print(val)

words = ['sky', 'book', 'war', 'cup']
print(words)
```

The example creates a list of integers and a list of strings.  

```python
vals = [1, 2, 3, 4, 5]
print(vals)
```

We define and print a list of integers.

```python
for val in vals:
    print(val)
```

We go over the elements of a list with `for` loop.  


## Python reading input


The <code>input</code> function reads a line from input, converts it to a  
string (stripping a trailing newline), and returns that. The function takes  
an optional argument, which is written to standard output without a trailing newline,  
if present.


```python
# read_input.py

name = input("Enter your name:")
print("Hello", name)
```


The example prints a prompt and reads a name from the console. Then it prints a greeting  
to the console.


```
$ ./read_input.py 
Enter your name:Peter
Hello Peter
```

## Python command line arguments

Python programs can receive command line arguments. The <code>sys.argv</code> contains  
a list of command line arguments passed to a Python script. The <code>argv[0]</code> is   
the script name; the remaining elements are arguments passed to the script.  
 

```python
# command_line_arguments.py

import sys

print("Script name:", sys.argv[0])
print("Arguments:", end=" ")

for arg in sys.argv[1:]:
    print(arg, end=" ")

print()
```

The example prints the command line arguments passed to the script.

```python
import sys
```

We import the <code>sys</code> module, which has the <code>argv</code> variable.

```python
print("Script name:", sys.argv[0])
```


The name of the program is printed.


```python
for arg in sys.argv[1:]:
    print(arg, end=" ")
```


We go through the list of arguments stored in <code>sys.argv</code> and  
print them to the console. With the <code>end</code> option we append a new   
space to the end instead of a new line.  


```python
print()
```

At the end, a new line is printed to the console.


```
$ ./command_line_arguments.py 1 2 3
Script name: ./command_line_arguments.py
Arguments: 1 2 3 
```

## Random values 

The `raindom` module is used to work with randomness.  

```python
import random 

r1 = random.randint(0, 10)
print(r1)

r2 = random.randrange(500, 1000, 50)
print(r2)

vals = [11, 22, 33, 44, 55, 66, 77]
r3 = random.choice(vals)
print(r3)

words = ['sky', 'atom', 'war', 'cup', 'book', 'zebra', 'moon']
r4 = random.sample(words, 2)
print(r4)
```

