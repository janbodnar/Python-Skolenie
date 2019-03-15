#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents/pyprogs')

for e in path.rglob('*.py'):
    print(e)
    
# for e in path.glob('**/*.py'):
#     print(e)    