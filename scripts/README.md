# Scripts

## find/zip files 

```python
import pathlib
import argparse
import zipfile
import tempfile
import time


parser = argparse.ArgumentParser()
   
parser.add_argument('-p', action='store_true', help='print files')
parser.add_argument('-t', required=True, help='file type')
parser.add_argument('-d', help='search directory')
parser.add_argument('-z', action='store_true', help='archive files')
args = parser.parse_args()

p = args.p
z = args.z
file_type = args.t
search_dir = args.d

if not search_dir:
    path = pathlib.Path.home() / 'Documents'
else:
    path = pathlib.Path(search_dir)


n_of_files = 0
archive_files = []

print(f'searching for {file_type} files in {path}')

for fname in path.rglob(f'*.{file_type}'):

    if fname.is_dir():
        continue

    n_of_files += 1

    if z:
        archive_files.append(fname)

    if p:
        print(fname)


print(f'there are {n_of_files} {file_type} files in {path}')


if z:
    time_stamp = str(int(time.time()))
    temp_path = pathlib.Path(tempfile.gettempdir()) / f'archive-{file_type}-{time_stamp}.zip' 

    with zipfile.ZipFile(temp_path, 'w') as zip:

        for fname in archive_files:
            zip.write(fname)

        print(f'{temp_path} created')
```

## find large files 

The `try/except` is used within the for loop in order not to terminate the script  
when we cannot access the file.  

```python
import pathlib
import argparse


gigabyte = 1024*1024*1024

parser = argparse.ArgumentParser()
   
parser.add_argument('-p', action='store_true', help='print files')
parser.add_argument('-s', type=int, default=gigabyte,  help='file size in bytes')
parser.add_argument('-d', help='search directory')
args = parser.parse_args()

p = args.p
s = args.s 
search_dir = args.d

if not search_dir:
    path = pathlib.Path.home() / 'Documents'
else:
    path = pathlib.Path(search_dir)


print(f'searching for files larger than {s} bytes in {path}')

def should_skip(fname):

    # skip directories that we cannot access  
    excludes = ['CanonicalGroupLimited']

    for exclude in excludes:
        if exclude in fname.absolute().as_posix():
             return True 
        
    return False

def search_for_large_files():

    n_of_files = 0

    for fname in path.rglob('*'):

        if should_skip(fname):
            continue

        try: 
            if fname.is_file():

                fsize = fname.stat().st_size    

                if fsize >= s:
                    n_of_files += 1

                    if p:
                        print(fname)

        except OSError as e:
                print(e)

    return n_of_files

n_of_files = search_for_large_files()
print(f'there are {n_of_files} files larger than {s} in {path}')
```

The `stat` and `is_file` or `is_dir` methods are problematic in that they can  
throw exception if they cannot access the file. For instance, the method cannot  
follow a symlink or cannot access the due to permissions.  

```python
def should_skip(fname):

    # skip directories that we cannot access  
    excludes = ['CanonicalGroupLimited']

    for exclude in excludes:
        if exclude in fname.absolute().as_posix():
             return True 
        
    return False
```

We put the directories that we cannot access into the excludes list and do not  
process them.  


