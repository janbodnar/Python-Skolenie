#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')

home = Path.home()

relative = path.relative_to(home)
print(relative)