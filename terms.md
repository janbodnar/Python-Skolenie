# Terms

## Garbage collection

Garbage collection in Python is the process of automatically reclaiming memory  
that is no longer in use by the program. This is essential for managing memory  
and preventing memory leaks, which can lead to inefficient use of resources and  
potentially crash the program.  

Python's garbage collection system helps manage memory automatically, allowing  
developers to focus on writing code without worrying too much about memory  
management.  

## Dynamic langauge

Python is dynamic, meaning its behavior is largely determined at runtime rather  
than at compile time. This includes:  

- Interpreted Language: Python is executed line-by-line at runtime by the  
  interpreter, which allows for quick testing and debugging without the need for  
  compilation.
- Dynamic Typing: Variables can change type as the program executes, without the  
  need for explicit declarations.
- Dynamic Memory Management: Automatic handling of memory allocation and garbage  
  collection, relieving developers from manual memory management.
- Dynamic Attribute Creation: Attributes can be added, modified, or deleted from  
  objects at runtime, providing flexibility and extensibility.  
- Run-time Reflection: Ability to inspect and modify the program structure at  
  runtime, such as accessing object types and attributes.


## Python Enhancement Proposals (PEPs)

Python Enhancement Proposals (PEPs) are design documents providing information  
to the Python community, or describing a new feature for Python or its processes  
or environment. PEPs are intended to be the primary mechanism for proposing  
major new features, collecting community input on an issue, and documenting the  
design decisions that have gone into Python.  

Key points:

- Proposals for Changes: PEPs propose changes to the Python language, libraries,  
  or processes. They can range from small enhancements to major new features.
- Community Involvement: PEPs are open to community review and feedback,  
  allowing Python developers to discuss and refine the proposals.
- Standardization: Accepted PEPs provide a standardized way of implementing new  
  features or changes, ensuring consistency across the Python ecosystem.
- Documentation: PEPs serve as detailed documentation of the design decisions  
  and rationale behind changes or new features in Python.

Example PEPs:

- PEP 8: Style Guide for Python Code – Provides guidelines for writing readable  
  and consistent Python code.
- PEP 20: The Zen of Python – A collection of aphorisms that capture the
  philosophy of Python.
- PEP 484: Type Hints – Introduces a standard for adding type hints to Python  
  code.

Summary: 

PEPs are essential to the evolution of Python, enabling organized and  
well-documented changes that incorporate community feedback and expertise. They  
help ensure that Python remains a robust, adaptable, and widely-used programming  
language.  


## Python Versioning System

Python uses a form of a semantic versioning system to manage and identify  
different releases of the language. The version numbers follow a structured  
format to convey information about the nature of changes in each release.  

## Version Number Format

Python version numbers are typically represented in the format: MAJOR.MINOR.MICRO

- MAJOR: Indicates significant changes that may include backward-incompatible  
changes. Major version changes introduce new language features or substantial  
changes to existing features.  

Example: Python 2.x to Python 3.x  

- MINOR: Represents smaller, backward-compatible enhancements and improvements.  
  Minor version updates may include new features, optimizations, and other  
  enhancements while maintaining backward compatibility with the previous major  
  version.  

Example: Python 3.8 to Python 3.9

MICRO: Denotes maintenance releases that include bug fixes and minor  
improvements. These updates focus on addressing issues without introducing new  
features or changes that might affect backward compatibility.  

Example: Python 3.9.1 to Python 3.9.2

## Example

Python 3.9.2:

- MAJOR: 3 (Introduces new language features)
- MINOR: 9 (Backward-compatible improvements)
- MICRO: 2 (Bug fixes and minor improvements)

This structured versioning system helps developers understand the nature and  
scope of changes in each release, enabling better planning for upgrades and  
compatibility considerations.  