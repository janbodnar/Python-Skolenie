#!/usr/bin/python

from pathlib import Path
import datetime

path = Path('C:/Users/Jano/Documents/java/doc.txt')

created = datetime.datetime.fromtimestamp(path.stat().st_ctime)
modified = datetime.datetime.fromtimestamp(path.stat().st_mtime)
accessed = datetime.datetime.fromtimestamp(path.stat().st_atime)

print(f"Created: {created:%Y-%m-%d}")
print(f"Last modified: {modified:%Y-%m-%d}")
print(f"Last accessed: {accessed:%Y-%m-%d}")


