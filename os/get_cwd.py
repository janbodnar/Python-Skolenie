#!/usr/bin/python3

import os
from pathlib import Path

cwd = os.getcwd()
print(cwd)

try:
    home = str(Path.home())
    cwd = os.chdir(home)
    cwd = os.getcwd()
    print(cwd)

except OSError:
    print("failed to change directory")      


print(os.getcwd.__doc__)
