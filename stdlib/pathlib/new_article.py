#!/usr/bin/python

from pathlib import Path
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month

name = input('Enter article name:')

path1 = Path('articles') / str(year) / str(month)
path1.mkdir(parents=True, exist_ok=True)

path2 = path1 /  f'{name}.txt'

path2.touch()

print(f'Article created at: {path2}')
