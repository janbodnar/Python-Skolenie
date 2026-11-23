# Introduction to Python

Python is a general-purpose, high-level programming language designed with a  
strong emphasis on **readability** and **programmer productivity**. Its clean  
syntax makes it an excellent first language, while its large ecosystem of  
libraries makes it a practical tool for professionals in almost every field.

## The Story of Python

Python was created by **Guido van Rossum** at the end of the 1980s and first  
released in **1991**. The name does not come from the snake but from the British  
comedy series *Monty Python's Flying Circus*.

Python was designed to be:

- simple and intuitive
- readable, with minimal syntactic clutter
- extensible and versatile

> 🎥 **Watch**: [The Story of Python](https://www.youtube.com/watch?v=GfH4QL4VqJ0)

### The Zen of Python

The design philosophy of Python is summarized in *The Zen of Python* (PEP 20), a  
set of 19 short principles written by Tim Peters. You can display them directly  
in Python:

```python
import this
```

A few of the best-known principles:

```text
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Readability counts.
```

Code that follows these principles and uses the language's idioms well is often  
called **Pythonic**.

### Influences

Python borrowed ideas from several older languages:

| Language | Contribution to Python |
| --- | --- |
| **ABC** | Indentation-based blocks, readability, built-in high-level types |
| **Modula-3** | Modules, exceptions, classes |
| **C** | Syntax of expressions and operators |
| **Lisp** | Functional tools such as `lambda`, `map`, and `filter` |
| **Haskell** | List comprehensions |
| **Icon** | Generators |
| **Perl** | Regular expressions, practicality in text processing |

---

## Key Characteristics of Python

Python is **open source software**, released under the permissive Python  
Software Foundation License. Its development is coordinated by the Python  
Software Foundation (PSF) and carried out by a large, global community of  
volunteers.

### Core features

1. **High-level and readable**: Python hides low-level details such as memory  
   management, so you can focus on solving the problem.
2. **Interpreted**: You run Python source code directly, without a separate  
   compilation step. Behind the scenes, CPython compiles the code to bytecode  
   and executes it in a virtual machine. This makes the edit-and-run cycle fast  
   and is ideal for experimenting.
3. **Dynamically typed**: You do not declare the types of variables. A type  
   belongs to the value (the object), not to the variable name, and it is  
   checked while the program runs.
4. **Strongly typed**: Python does not silently convert between unrelated types.  
   For example, `"5" + 3` raises an error instead of guessing what you meant.
5. **Significant indentation**: Python uses indentation instead of braces or  
   keywords to mark blocks of code. This enforces clean, consistent formatting.
6. **Multi-paradigm**: Python supports procedural programming (functions),  
   object-oriented programming (classes and inheritance), and elements of  
   functional programming (`lambda`, comprehensions, `map`, `filter`).
7. **Cross-platform**: Python runs on Windows, macOS, Linux, Raspberry Pi, and  
   many other systems. The same script usually runs unchanged on all of them.
8. **Batteries included**: The standard library contains modules for working  
   with files, text, dates, networking, databases, and much more.

### What is Python used for?

- Web development (Django, Flask, FastAPI)
- Data analysis and scientific computing (NumPy, pandas, SciPy)
- Artificial intelligence and machine learning (PyTorch, TensorFlow,  
  scikit-learn)
- Automation, scripting, and system administration
- Testing (pytest)
- Education and teaching programming
- Game development (Pygame)

> **Note**: Python has become the main language of artificial intelligence and  
> data science, largely thanks to its extensive ecosystem of libraries.

### Official resources

- **Official website**: [python.org](https://www.python.org)
- **Documentation**: [docs.python.org](https://docs.python.org/3/)
- **Package index (PyPI)**: [pypi.org](https://pypi.org)

![Python Logo](images/python.jpg)

---

## Python Implementations

Python is a language **specification** with several implementations. An  
implementation is a program that actually runs Python code.

| Implementation | Written in | Description |
| --- | --- | --- |
| **CPython** | C | The reference and by far the most widely used implementation. When people say "Python", they usually mean CPython. |
| **PyPy** | RPython | An implementation with a just-in-time (JIT) compiler, often much faster for long-running programs. |
| **MicroPython** | C | A lightweight implementation for microcontrollers and embedded systems. |
| **GraalPy** | Java | Python on the GraalVM, with access to Java libraries. |
| **IronPython** | C# | Python for .NET, with access to .NET libraries. |
| **Jython** | Java | Python on the Java Virtual Machine. Supports only Python 2.7. |

This course uses **CPython**.

---

## Popularity and Community

Python is one of the most popular programming languages in the world:

- **TIOBE Index**: Python has held the first position in recent years.
- **Stack Overflow Developer Survey**: Python is regularly among the most used  
  and most wanted languages.
- **JetBrains Developer Ecosystem Survey**: Python shows strong use in data  
  science, web development, and automation.

You can check the current results here:

- [TIOBE Index](https://www.tiobe.com/tiobe-index/)
- [Stack Overflow Developer Survey](https://survey.stackoverflow.co/)
- [JetBrains Developer Ecosystem](https://www.jetbrains.com/lp/devecosystem/)

### Notable software written in Python

- **Django** and **Flask**: web frameworks
- **Jupyter**: interactive notebooks for data analysis and teaching
- **Ansible**: IT automation and configuration management
- **NumPy** and **pandas**: numerical computing and data analysis
- **PyTorch** and **TensorFlow**: machine learning libraries
- **Mercurial**: distributed version control system

Python is also widely used as a scripting language inside other applications,  
such as Blender, GIMP, and QGIS.

---

## Learning Resources

### Books

- **Python Crash Course**, 3rd Edition, by Eric Matthes: a beginner-friendly  
  introduction with practical projects.
- **Automate the Boring Stuff with Python** by Al Sweigart: practical  
  automation tasks; [free to read online](https://automatetheboringstuff.com/).
- **Fluent Python**, 2nd Edition, by Luciano Ramalho: idiomatic Python for  
  intermediate and advanced programmers.

### Video courses

- [Python for Everyone: Zero to Hero (6 hours)](https://www.youtube.com/watch?v=JZDQKj9BOoc)
- [Python Full Course for Beginners](https://www.youtube.com/watch?v=H2EJuAcrZYU)
- [Corey Schafer's Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)

### Online platforms

- [The official Python tutorial](https://docs.python.org/3/tutorial/)
- [Python for Everybody](https://www.py4e.com/): a free course by  
  Charles Severance (University of Michigan)
- [Real Python](https://realpython.com/): tutorials and articles

---

## Writing and Running Python Scripts

### Checking the installation

Before you start, check that Python is installed. Open a terminal (a command  
prompt on Windows) and ask for the version:

```bash
$ python --version
Python 3.15.2
```

If the command is not found, download Python from  
[python.org](https://www.python.org/downloads/). On Linux, Python is usually  
installed already or available from the system package manager.

### Your first script

A Python script is a plain text file with the `.py` extension. Create a file  
named `hello.py` with this content:

```python
print("Hello, World!")
```

Run it by passing the file name to the interpreter:

```bash
$ python hello.py
Hello, World!
```

The `print()` function writes its argument to the screen. This is the whole  
program; Python needs no `main` function or other boilerplate.

### The shebang line

On Unix-like systems (Linux, macOS), a script can start with a **shebang** line.  
It tells the system which interpreter should run the file:

```python
#!/usr/bin/env python3

print("Hello, World!")
```

After you make the file executable, you can run it directly, without typing  
`python`:

```bash
$ chmod +x hello.py
$ ./hello.py
Hello, World!
```

On Windows, the shebang line is not needed, but it does no harm.

### Interactive mode

Python can also run in **interactive mode**, often called the REPL  
(read–evaluate–print loop). Start the interpreter without a file name:

```text
$ python
Python 3.15.2 (main, Oct 26 2026, 14:06:56) [Clang 23.1.3] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello")
Hello
>>> 2 + 3
5
>>> exit
```

The `>>>` prompt means that Python is waiting for your input. Each statement  
runs as soon as you press Enter, and the value of an expression, such as `2 +  
3`, is printed automatically. Interactive mode is ideal for quick experiments  
and for trying out the examples in this course. To leave it, type `exit` or  
press Ctrl+D (Ctrl+Z and Enter on Windows).

---

## Summary

| Aspect | Description |
| --- | --- |
| **Creator** | Guido van Rossum, first released in 1991 |
| **Philosophy** | Readability and simplicity (The Zen of Python) |
| **Paradigms** | Procedural, object-oriented, functional elements |
| **Typing** | Dynamic and strong |
| **Execution** | Interpreted (compiled to bytecode and run in a virtual machine) |
| **Common uses** | Web, AI and machine learning, data science, automation, scripting |
| **Implementations** | CPython (reference), PyPy, MicroPython, GraalPy, IronPython, Jython |
| **Scripts** | Plain text `.py` files, run with `python file.py` |

## Next Steps

This introduction gives you the background for the rest of the course. Continue  
with:

1. **Lexical structure**: comments, names, keywords, literals, and operators
2. **Basic data types**: numbers, strings, and booleans
3. **Control flow**: conditions and loops
4. **Functions**: defining and calling functions
5. **Data structures**: lists, tuples, dictionaries, and sets
6. **File I/O**: reading and writing files
7. **Exception handling**: dealing with errors
8. **Modules and packages**: organizing and importing code
