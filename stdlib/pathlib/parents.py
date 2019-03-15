#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents')

print(f"The parent directory of {path} is {path.parent}")
print(f"The parent of the parent of {path} is {path.parent.parent}")

print(f"All the parents of {path.parent}: ")

print(list(path.parents))