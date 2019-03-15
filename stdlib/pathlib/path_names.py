#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')

print(path)
print(path.as_uri())
print(path.as_posix())