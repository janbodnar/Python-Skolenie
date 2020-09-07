#!/usr/bin/python

from pathlib import Path

def tree(directory):

    print(f'+ {directory}')

    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth

        # print(f'{spacer}+ {path.name}')

        if path.is_file():
            print(f'{spacer}f {path.name}')
        else:
            print(f'{spacer}d {path.name}')

path = Path.home() / 'Downloads'

tree(path)