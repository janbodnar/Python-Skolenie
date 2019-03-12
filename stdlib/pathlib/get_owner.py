#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')

print(f'The owner of the {path.name} is {path.owner()}')