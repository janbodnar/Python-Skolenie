#!/usr/bin/env python

from pathlib import Path

path = Path.home()

docs = path / 'Documents'
pictures = path / 'Pictures'

print(docs)
print(pictures)