# Introduction

This is an introduction to the Python programming language.  


## Python

Python is a general-purpose, dynamic, object-oriented programming language.  
The design purpose of the Python language emphasizes programmer productivity  
and code readability. Python was initially developed by Guido van Rossum.  
It was first released in 1991. Python was inspired by ABC, Haskell, Java, Lisp, Icon,  
and Perl  programming languages. Python is a high-level, general purpose,  
multi-platform, interpreted language. Python is maintained by a large group  
of volunteers worldwide. Python is open source software.  

Python is a minimalistic language. One of its most visible features is that it  
does not use semicolons nor brackets; Python uses indentation instead.  

Python supports several programming styles. It does not force a programmer to a specific  
paradigm. It supports procedural, object oriented, and functional programming.  


The official web site for the Python programming language is [python.org](https://python.org")


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


## Python scripts

Every script in the Unix starts with a <em>shebang</em>. The shebang is the first two  
characters in the script: <code>#!</code>. The shebang is followed by the  
path to the interpreter, which will execute our script. Shebangs do not work on Windows;  
but it it a good practice to include them even on Windows, since we might expect our 
programs to be run on Unix, too. 


```python
#!/usr/bin/python

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

<pre class="compact">
$ python first.py
The Python tutorial
</pre>

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



## Python reading input


The <code>input</code> function reads a line from input, converts it to a  
string (stripping a trailing newline), and returns that. The function takes  
an optional argument, which is written to standard output without a trailing newline,  
if present.


```python
#!/usr/bin/python

# read_input.py

name = input("Enter your name:")
print("Hello", name)
```


The example prints a prompt and reads a name from the console. Then it prints a greeting  
to the console.


```python
$ ./read_input.py 
Enter your name:Peter
Hello Peter
```

## Python command line arguments

Python programs can receive command line arguments. The <code>sys.argv</code> contains  
a list of command line arguments passed to a Python script. The <code>argv[0]</code> is   
the script name; the remaining elements are arguments passed to the script.  
 

```python
#!/usr/bin/python

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
