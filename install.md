# Installation

- Python language
- VS Code editor & Python extension
- Windows Terminal


## Download

[www.python.org/downloads/](https://www.python.org/downloads/)

## Using winget 

winget is a modern Windowns package manager.  

```
winget install Python.Python.3.12
```

## PATH variable

The `PATH` variable in Windows is an environment variable that contains a list of  
directories where the operating system looks for executable files. When you type  
a command in the command prompt, Windows searches through the `PATH` directories to  
find the executable file to run.

Press `Windows+R`, type `sysdm.cpl`, and press `Enter` to open System Properties.  
Go to the Advanced tab and click on Environment Variables.  


To print all paths:  

```
echo %path%
```

To print all directories, each directory is on a separate line:  

```
echo %path:;=&echo(%
```

## VS Code 

VS Code, short for Visual Studio Code, is a popular source code editor that's both  
lightweight and powerful. Unlike a full-fledged Integrated Development Environment  
(IDE) like Visual Studio, VS Code focuses on being a fast and efficient tool for writing code.  

[https://code.visualstudio.com/download](https://code.visualstudio.com/download)

```
winget install Microsoft.VisualStudioCode
```



