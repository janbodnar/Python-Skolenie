# Python virtual environment

A Python **virtual environment** is an isolated environment where you can  
install Python packages without interfering with other projects or the  
system's Python interpreter. It's a way to manage dependencies on a  
per-project basis. This is particularly useful when different projects  
require different versions of the same package.  

## Advantages

Python virtual environments offer several advantages:  

1. **Dependency Management**: Each project can have its own dependencies,  
   independent of other projects.  

2. **Version Control**: Different projects can use different versions of  
   the same package without conflict.  

3. **Isolation**: Changes within a virtual environment do not affect  
   the system's Python interpreter or other projects.  

4. **Simplicity**: It's easy to create, use, and delete Python virtual  
   environments.  

## Commands

1. **Create a virtual environment**:  
   `python3 -m venv /path/to/new/virtual/environment`  

2. **Activate the virtual environment**:  
   - On Windows: `path\\to\\env\\Scripts\\activate`  
   - On Unix or MacOS: `source path/to/env/bin/activate`  

3. **Deactivate the virtual environment**:  
   `deactivate`  

4. **Install packages using pip**:  
   `pip install package-name`  

5. **List installed packages**:  
   `pip list`  

6. **Remove packages**:  
   `pip uninstall package-name`  

