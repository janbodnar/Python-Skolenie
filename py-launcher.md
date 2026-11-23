# The Python Launcher on Windows

On Windows, the command `python` does not name a single program. It names  
whichever installed interpreter happens to come first in the `PATH`  
environment variable. Install a second version, and the meaning of  
`python` can change without any warning. The **Python launcher**, whose  
command is `py`, makes the choice explicit and predictable.

> **Note**: This chapter is the only place in the course where examples  
> use `py`. Everywhere else we type `python`, the recommended command on  
> all platforms. Read this chapter when you work on Windows and need to  
> choose between versions, or when `python` starts the wrong one.

The launcher began as a small `py.exe` program bundled with the Windows  
installer (PEP 397, Python 3.3). Since Python 3.14 it is part of the  
**Python install manager**, an application that also installs and updates  
Python itself (PEP 773). The standalone launcher still works, but it is  
deprecated and receives no new features.

## What the Launcher Does

When you type a command, Windows searches the directories in `PATH` from  
first to last and runs the first match. Python installers add their own  
directory to `PATH`, so the version added last often wins. That is how a  
beginner ends up running Python 3.12 while believing that 3.15 is in use.

To choose an interpreter, the launcher does not rely on `PATH`. It  
collects the Python installations registered on the system, including its  
own records and the registry entries described by PEP 514, and chooses  
among them by version. It prefers a 64-bit build for the machine's  
processor (x64 or ARM64) over a 32-bit one, and newer versions over older  
ones, so the result depends on what is installed, not on the order of  
installation.

In this chapter, a **runtime** means one installed copy of Python, with  
its own standard library and its own set of packages.

| Command | Finds the interpreter through |
| --- | --- |
| `python` | `PATH`, plus an active virtual environment |
| `py` | Registered installations and version rules |

Both commands come from the install manager, so on a current Windows  
machine either one works. Use `python` for everyday work and `py` when the  
version matters.

## Checking Which Versions You Have

Ask the `python` command for its version:

```text
C:\> python --version
Python 3.15.2
```

Then ask the launcher what it can see:

```text
C:\> py list
Tag      Name            Managed By  Version  Alias
3.15  *  Python 3.15.2   PythonCore  3.15.2   python3.15.exe, python3.exe
3.12     Python 3.12.10  PythonCore  3.12.10  python3.12.exe
```

The star marks the **default runtime**, the version that `py` launches  
when you do not ask for one. The `Tag` column contains the short names  
used to request a version. The `Alias` column lists commands that start  
this particular installation; those commands work only if the aliases  
directory was added to `PATH`. Column widths follow the longest value, so  
your table will be spaced a little differently.

If the list is empty, install a runtime:

```text
C:\> py install 3.15
```

On a brand-new machine, the first launch of `python` or `py` also installs  
the latest release automatically. Installing explicitly is easier to  
follow and prints a message when it finishes.

## Running a Script

Running a script through the launcher looks the same as running it with  
`python`:

```text
C:\> py hello.py
Hello, World!
```

Arguments after the file name go to the script, not to the launcher:

```python
# greet.py
import sys

name = sys.argv[1] if len(sys.argv) > 1 else "World"
print(f"Hello, {name}!")
```

`sys.argv` holds the command-line arguments, and `sys.argv[0]` is the  
script name, so `sys.argv[1]` is `Jane` here:

```text
C:\> py greet.py Jane
Hello, Jane!
```

Interpreter options also work, because the launcher passes everything  
except its own selector to the interpreter:

```text
C:\> py -c "print(2 + 3)"
5
C:\> py -m this
```

The second command prints the Zen of Python, exactly like  
`python -m this`.

## Choosing a Version

Pass a version selector as the first argument. The short form `-3.12`  
means "Python 3.12 from python.org":

```text
C:\> py -3.12 --version
Python 3.12.10
```

The general form `-V:TAG` selects by tag and can also match other  
distributors:

```text
C:\> py -V:3.12 greet.py Jane
Hello, Jane!
C:\> py -V:3 greet.py Jane
Hello, Jane!
```

`-V:3` means the newest installed Python 3, so it keeps working after you  
upgrade. The selector must come before every other argument. Written after  
the file name, it would be passed to the script instead.

If the requested version is not installed, `py` stops with a clear  
message:

```text
C:\> py -3.11 greet.py Jane
No runtime installed that matches 3.11. Try running "py install 3.11".
```

It does not fall back silently to another version, which is the whole  
point of using the launcher. Install and remove runtimes with  
`py install` and `py uninstall`:

```text
C:\> py install 3.11
C:\> py uninstall 3.11
```

Without `-y`, uninstall asks for confirmation. The command  
`py list --online` shows versions that are available for download but not  
installed yet.

### Changing the Default

When nothing else decides, `py` launches the default runtime: the newest  
stable Python 3 from python.org. Set the environment variable  
`PYTHON_MANAGER_DEFAULT` to choose another:

```text
C:\> set PYTHON_MANAGER_DEFAULT=3.12
C:\> py list
```

The star moves to 3.12, and `py greet.py` now uses 3.12. The `set` command  
affects only the current Command Prompt window; a new window forgets it.  
For a permanent setting, use the "Edit environment variables for your  
account" page in Windows settings, or edit the install manager's JSON  
configuration file at `%AppData%\Python\pymanager.json`.

When several rules could apply, the launcher decides in this order:

1. An explicit selector, such as `-3.12`
2. A shebang line in the script
3. An active virtual environment
4. The default runtime

## Shebang Lines

A **shebang** is a first line that starts with `#!` and names an  
interpreter. Unix uses it when a script is executed directly. The Windows  
launcher reads it when it runs a script and no version was requested.

```python
#! /usr/bin/env python3
import sys

print(sys.version_info[:3])
```

```text
C:\> py show_version.py
(3, 15, 2)
```

The path looks odd on Windows. It is there because scripts travel between  
systems: `#! /usr/bin/env python3` is the portable Unix form, and the  
launcher recognises it and substitutes its own runtime.

To pin a version, name it in the shebang:

```python
#! /usr/bin/python3.12
```

Then `py script.py` uses Python 3.12 even when the default is 3.15. The  
shebang is ignored when you pass a selector, so `py -3.15 script.py` wins  
over the first line.

## Windowed Scripts

`py` is a console program: it opens a black window for input and output.  
For a graphical user interface (GUI) application, that extra window is  
noise. The `pyw` command runs the same runtime without creating a console:

```text
C:\> pyw app.py
```

Here `app.py` stands for any graphical program that opens its own window.  
The `.pyw` extension works the same way when you double-click a file. The  
trade-off is that `print()` output and error messages have nowhere to go.  
While developing, run the script with `py` first, so that you can see the  
traceback. Switch to `pyw` only when the program works.

## pip and Virtual Environments

Install packages with `py -m pip`, not with a bare `pip`:

```text
C:\> py -m pip install requests
```

`-m pip` runs the `pip` module of the interpreter that `py` selected. A  
bare `pip` may belong to a different installation or may be missing from  
`PATH` altogether, so it is the usual source of "pip installed it, but  
Python cannot import it" confusion.

To tie packages to one project, create a virtual environment. A  
**virtual environment** is a private directory of packages that belongs  
to one project. Choose a version when you create it:

```text
C:\> py -3.12 -m venv .venv
C:\> .venv\Scripts\activate
(.venv) C:\> python --version
Python 3.12.10
```

After activation, `python` and `pip` point into `.venv`. An active  
environment also wins over the default runtime when you run `py` without a  
selector, which keeps the two commands consistent. Leave the environment  
with `deactivate`.

## The Older Launcher

From Python 3.3 to 3.13, the traditional Windows installer shipped a  
standalone `py.exe`. Its launching commands are the same ones you have  
seen: `py script.py` and `py -3.12 script.py` work in both versions. It is  
deprecated since Python 3.14, when the install manager replaced it.

For compatibility, the old listing options `py -0`, `py -0p`, and  
`py --list` still work, but `py list` is the current form.

The differences appear in configuration. The older launcher reads settings  
from `py.ini` and from environment variables such as `PY_PYTHON` and  
`PY_PYTHON3`. The install manager ignores `py.ini` and uses a JSON  
configuration file instead. If a tutorial asks you to edit `py.ini`, it is  
describing the older launcher; use `PYTHON_MANAGER_DEFAULT` or  
`py install` instead.

If both tools are present, `py` may resolve to the old launcher, which  
does not understand subcommands such as `py list` and `py install`. The  
symptom is a "can't open file" error. Uninstall "Python launcher" from the  
Installed apps page, and the install manager's `py` takes over.

## Common Problems

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| Typing `python` opens the Microsoft Store | Windows has a stub for a missing Python | Install the Python install manager, or enable the "Python (default)" alias |
| `'py' is not recognized ...` | Launcher missing, or blocked by `PATH` | Check "Manage app execution aliases"; reinstall if needed |
| `py` reports `can't open file` | Old `py.exe` takes priority | Uninstall "Python launcher" from Installed apps |
| Wrong version starts | Another install is earlier in `PATH` | Use `py -V:TAG`, or clean up `PATH` |
| `pip` is not recognized | No active environment, or aliases missing | Run `py -m pip` instead |
| `py.ini` changes have no effect | The install manager ignores it | Use `PYTHON_MANAGER_DEFAULT` |

The first error appears in full as:

```text
'py' is not recognized as an internal or external command,
operable program or batch file.
```

If the name `py` is taken by another tool, the install manager provides an  
unambiguous command with the same subcommands: `pymanager list`,  
`pymanager install 3.12`, and so on.

## Hands-On: Which Python Is Running?

Save this program as `which_python.py`:

```python
import platform
import sys

print("version:", platform.python_version())
print("executable:", sys.executable)
```

Run it with two different selectors:

```text
C:\> py -3.12 which_python.py
version: 3.12.10
executable: ...\pkgs\pythoncore-3.12-64\python.exe
C:\> py -3.15 which_python.py
version: 3.15.2
executable: ...\pkgs\pythoncore-3.15-64\python.exe
```

The paths are shortened here; your own output shows the full location. The  
first line is the version that actually ran, and the second is the file  
that ran it. When an editor, a test runner, or a build tool behaves  
differently from your terminal, this two-line script shows which  
interpreter each one picked. Use the tags that `py list` reports on your  
machine.

## Summary

| Task | Command |
| --- | --- |
| Show the current version | `python --version` |
| List installed runtimes | `py list` |
| Run a script with the default | `py script.py` |
| Run a script with a given version | `py -3.12 script.py` |
| Install another runtime | `py install 3.12` |
| Install a package | `py -m pip install requests` |
| Create a virtual environment | `py -3.12 -m venv .venv` |
| Run without a console window | `pyw app.py` |

Outside this chapter, use `python`: it is shorter, it works on every  
platform, and the install manager makes it select the right runtime. The  
launcher is the tool for the moments when you need to see or change that  
choice.

## References

- [Using Python on Windows](https://docs.python.org/3/using/windows.html)
- [PEP 773: A Python Installation Manager for Windows](https://peps.python.org/pep-0773/)
- [PEP 397: Python launcher for Windows (legacy)](https://peps.python.org/pep-0397/)
- [PEP 514: Python registration in the Windows registry](https://peps.python.org/pep-0514/)
- [Python downloads for Windows](https://www.python.org/downloads/windows/)
