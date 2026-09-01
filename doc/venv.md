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
   `py -m venv myenv`  

2. **Activate the virtual environment**:  
   - On Windows: `myenv\Scripts\activate`  
   - On Unix or MacOS: `source ./myenv/bin/activate`  

3. **Deactivate the virtual environment**:  
   `deactivate`  

4. **Install packages using pip**:  
   `pip install package-name`  

5. **List installed packages**:  
   `pip list`  

6. **Remove packages**:  
   `pip uninstall package-name`  


## requirements.txt 

A `requirements.txt` file is a plain text file used in Python projects to list  
out the external libraries or packages that the project depends on. These  
libraries are not part of the Python standard library and need to be installed  
separately.  

Here are some key points about requirements.txt:  

*Function:* It specifies the exact dependencies needed for a project, ensuring  
everyone working on the project has the same environment set up. This promotes  
reproducibility and avoids compatibility issues.  

*Benefits:*  
Easy Installation: With `requirements.txt`, you can install all the required  
packages at once using the `pip install -r requirements.txt` command. This saves  
time and avoids manual installation of each package.  

*Collaboration:* When you share your project, others can easily set up their  
environment by installing the dependencies listed in the requirements.txt file.  

*Location:* The `requirements.txt` file is typically placed in the root directory  
of your Python project.  

*Format:* The file is a simple text file where each line specifies a package and  
optionally its version. There are ways to specify version constraints as well  
(e.g., installing a specific version range or the latest compatible version).  

Overall, `requirements.txt` is a best practice for managing dependencies in  
Python projects, promoting a consistent and efficient development workflow.  


Once you've installed all the necessary packages for your project using pip,   
you can generate a `requirements.txt` file that captures those dependencies  
and their versions. 

`pip freeze > requirements.txt`


The command lists all the installed Python packages and their versions in your  
current virtual environment. The `>` redirects the output of the pip freeze command.  
The `requirements.txt` file specifies the filename where the list of packages will  
be saved.  

The `pip uninstall -r requirements.txt -y` uninstalls all packages in the 
`requirements.txt` file.  









