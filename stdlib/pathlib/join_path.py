#!/usr/bin/python

from pathlib import Path

path = Path.home()

docs = path / 'Documents'
pictures = path / 'Pictures'

print(docs)
print(pictures)