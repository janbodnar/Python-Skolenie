# The pip manager

`pip`, also known as the Python Package Index, serves as a package manager that simplifies  
the process of installing, uninstalling, and managing Python packages. It is included by default  
with Python installations and facilitates the installation of packages from the PyPI repository or  
other sources. Additionally, pip offers the capability to generate a `requirements.txt` file that captures  
the list of installed packages, enabling the replication of the same environment  
on a different system. 

To install the packages specified in a `requirements.txt` file, the command `pip install -r requirements.txt`  
should be executed in the command line interface. Utilizing pip enhances the ease of managing Python projects   
and their associated dependencies.

The `pip` is located in the `Scripts` directory of the Python standard installation such as:  
`C:\Users\Jano\AppData\Local\Programs\Python\Python312\Scripts\`  
The `Scripts` directory directory contains various utility scripts that are part of Python's standard library  
or are installed with Python packages.



The currently used Python installation location can be found with `sys.executable`.  

## Upgrade pip 

`python -m pip install --upgrade pip`

## List packages 

`pip list` - list installed packages in the tabular format
`pip list -o` - list outdated packages
`pip list -u` - list up-to-date packages

## Check version of package

`pip show numpy`

## Upgrade package 

`pip install -U flask`

## Remove package

`pip uninstall flask`

## Freeze packages 

`pip freeze > requirements.txt` - provides a list of currently installed packages and their versions  
`pip install -r requirements.txt` - installs libraries in the file along with their dependencies 

