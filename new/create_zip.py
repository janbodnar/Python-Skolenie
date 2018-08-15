#!/usr/bin/python3

import zipfile

with zipfile.ZipFile('myfile.zip', mode='w') as zf:
    
    zf.write('press.txt')
    zf.write('todo.txt')

print('Archive created')
