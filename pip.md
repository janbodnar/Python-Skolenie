# The pip manager

`pip`, also known as the Python Package Index, serves as a package manager that simplifies the process of installing,  
uninstalling, and managing Python packages. It is included by default with Python installations and facilitates the  
installation of packages from the PyPI repository or other sources. Additionally, pip offers the capability to generate  
a `requirements.txt` file that captures the list of installed packages, enabling the replication of the same environment  
on a different system. 

To install the packages specified in a `requirements.txt` file, the command `pip install -r requirements.txt` should be executed  
in the command line interface. Utilizing pip enhances the ease of managing Python projects and their associated dependencies.

## Upgrade pip 

`python -m pip install --upgrade pip`

## List packages 

`pip list`

## Check version of package

`pip show numpy`
