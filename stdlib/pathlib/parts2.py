#!/usr/bin/env python

from pathlib import Path
import os

path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')

print(f"The stem is: {path.stem}")
print(f"The name is: {path.name}")
print(f"The suffix is: {path.suffix}")
print(f"The anchor is: {path.anchor}")

print(f"File name: {os.path.splitext(path.stem)[0]}")

print("The suffixes: ")
print(path.suffixes)