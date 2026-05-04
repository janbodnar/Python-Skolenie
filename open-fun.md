# The open function

In Python, the `open` function is the primary way to interact with files on the  
filesystem. It returns a **file object** that provides methods for reading,  
writing, and navigating file content. File I/O is fundamental for data  
persistence, logging, configuration, and many other programming tasks.  

The `open` function works with both text and binary data, supports a variety of  
access modes, and can handle encodings, buffering, and error strategies. Used  
together with the context manager (`with` statement), it ensures that files are  
properly closed after use.

## Opening a file

The simplest use of `open` requires a file path and a mode. The default mode is  
`'r'` (read, text mode).

```python
#!/usr/bin/python

# simplest_open.py

f = open('example.txt', 'r')
content = f.read()
f.close()

print(content)
```

It is good practice to always close a file when you are finished with it,  
otherwise operating system resources may be leaked.

## File modes

The mode string controls how the file is opened. Common modes are:

| Mode | Meaning                  |
|------|--------------------------|
| `'r'`  | read (default)          |
| `'w'`  | write (overwrites)      |
| `'a'`  | append                  |
| `'x'`  | exclusive creation      |
| `'r+'` | read and write          |
| `'w+'` | write and read (overwrites) |
| `'a+'` | append and read         |

A `'b'` suffix (e.g. `'rb'`, `'wb'`) opens the file in binary mode. A `'t'`  
suffix forces text mode (the default).

```python
#!/usr/bin/python

# modes.py

# Write a new file (overwrites if exists)
with open('data.txt', 'w') as f:
    f.write('First line\n')

# Append to the file
with open('data.txt', 'a') as f:
    f.write('Second line\n')

# Exclusive creation – fails if file already exists
try:
    with open('unique.txt', 'x') as f:
        f.write('Created!\n')
except FileExistsError:
    print('unique.txt already exists')
```

## Text and binary mode

Text mode (`'t'`) decodes bytes to strings using a character encoding and  
converts platform‑specific line endings to `'\n'` on reading and back on  
writing. Binary mode (`'b'`) reads and writes raw bytes without any  
translation – useful for non‑text files like images or compressed data.

```python
#!/usr/bin/python

# binary_read.py

with open('data.bin', 'wb') as f:
    f.write(b'\x00\xFF\x00\xFF')

with open('data.bin', 'rb') as f:
    raw = f.read()
    print(raw)          # b'\x00\xff\x00\xff'
```

## The encoding argument

When reading or writing text, you should explicitly specify the encoding to  
avoid platform‑dependent behaviour. The default encoding is usually UTF‑8,  
but it can differ. The `encoding` parameter sets the desired character set.

```python
#!/usr/bin/python

# encoding.py

text = 'Café – résumé'

# Write with explicit encoding
with open('cafe.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# Read back with the same encoding
with open('cafe.txt', 'r', encoding='utf-8') as f:
    restored = f.read()
    print(restored)     # Café – résumé
```

If the file contains characters that cannot be encoded with the given encoding,  
a `UnicodeEncodeError` will be raised. The `errors` parameter can be used to  
control this behaviour (e.g., `'ignore'`, `'replace'`, `'xmlcharrefreplace'`).

## Context manager

Using `open` directly requires remembering to call `.close()`. The recommended  
approach is to use the `with` statement, which acts as a context manager and  
automatically closes the file at the end of the block, even if exceptions occur.

```python
#!/usr/bin/python

# context_manager.py

# Preferred way
with open('numbers.txt', 'r') as f:
    content = f.read()
    print(content)
# File is automatically closed here
```

This is more concise, safe, and idiomatic.

## Reading the entire file

The `.read()` method reads the whole file content and returns it as a single  
string (or bytes if in binary mode).

```python
#!/usr/bin/python

# read_all.py

with open('poem.txt', 'r') as f:
    whole_text = f.read()
    print(repr(whole_text))
```

For large files, reading everything at once may consume a lot of memory. In such  
cases, iterate over the file line by line.

## Reading line by line

A file object is iterable and yields each line in turn. You can also use  
`.readline()` to read one line at a time or `.readlines()` to get a list of all  
lines.

```python
#!/usr/bin/python

# read_lines.py

with open('quotes.txt', 'r') as f:
    for line in f:
        print(line.rstrip('\n'))

# Or with readlines()
with open('quotes.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
```

The iteration approach is memory efficient because only one line is held in  
memory at a time.

## Writing to a file

The `.write()` method writes a string (or bytes) to the file. Use `'w'` to  
overwrite or `'a'` to append. You can write multiple lines with `.writelines()`.

```python
#!/usr/bin/python

# write_file.py

data = ['apple', 'banana', 'cherry']

with open('fruits.txt', 'w') as f:
    for item in data:
        f.write(item + '\n')
```

Note that `.write()` does not automatically add newline characters – you must  
supply them if needed.

## Appending to a file

Opening with `'a'` preserves the existing content and adds new data at the end.

```python
#!/usr/bin/python

# append_file.py

with open('log.txt', 'a') as f:
    f.write('New log entry\n')
```

If the file does not exist, it is created. The file pointer is positioned at the  
end of the file, so subsequent reads (if `'a+'` is used) need repositioning.

## Using read with a size

An optional integer argument to `.read()` limits the number of characters (or  
bytes) read at once.

```python
#!/usr/bin/python

# read_chunk.py

with open('big_file.bin', 'rb') as f:
    while chunk := f.read(4096):
        # process the 4 KiB chunk
        print(len(chunk))
```

This is essential for efficiently processing very large files.

## Seeking and telling position

The `.seek(offset, whence)` method moves the file pointer to a new position.  
`whence` can be `0` (start of file), `1` (current position), or `2` (end of  
file). The `.tell()` method returns the current byte offset.

In text mode, only seeks relative to the beginning are allowed (except when  
using zero offset). Binary mode supports all seek options.

```python
#!/usr/bin/python

# seek.py

with open('data.bin', 'rb') as f:
    print(f.tell())          # 0
    f.seek(5)
    print(f.tell())          # 5
    f.seek(-2, 1)            # move back 2 bytes from current position
    print(f.tell())          # 3
    f.seek(0, 2)             # move to end
    print(f.tell())          # file size in bytes
```

## Error handling

When a file cannot be opened, Python raises an `OSError` subclass such as  
`FileNotFoundError`, `PermissionError`, or `IsADirectoryError`. It is wise to  
handle these exceptions gracefully.

```python
#!/usr/bin/python

# error_handling.py

try:
    with open('missing.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to open this file.")
except OSError as e:
    print(f"An OS error occurred: {e}")
```

The `with` statement itself still closes the file properly even if an exception  
occurs inside the block.

## The newline parameter

When writing in text mode, the `newline` parameter controls how universal  
newline translation works. It defaults to `None`, which converts `'\n'` to the  
system’s default line separator on output and translates any platform line  
ending to `'\n'` on input. You can set it to `''` to disable translation  
(useful when working with CSV files).

```python
#!/usr/bin/python

# newline.py
import csv

with open('report.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
```

This ensures the CSV module controls line endings completely.

## Buffering

The `buffering` parameter sets the buffering policy. `-1` uses the default  
buffering (typically line buffering for interactive text files, and a fixed  
buffer size for others). `0` switches buffering off (only for binary mode), `1`  
selects line buffering (text mode only), and an integer >1 specifies a buffer  
size in bytes.

```python
#!/usr/bin/python

# buffering.py

# Unbuffered binary write
with open('unbuffered.bin', 'wb', buffering=0) as f:
    f.write(b'\x01\x02')
    # data is written immediately
```

For most uses, the default buffering is appropriate.

## Using pathlib

The `pathlib` module provides an object‑oriented approach to file paths. Its  
`Path.open()` method works exactly like the built‑in `open` function but is  
often more convenient when you manipulate paths.

```python
#!/usr/bin/python

# pathlib_open.py
from pathlib import Path

data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

file_path = data_dir / 'notes.txt'

with file_path.open('w', encoding='utf-8') as f:
    f.write('Remember the milk\n')

with file_path.open('r', encoding='utf-8') as f:
    print(f.read())
```

The `Path.open()` method delegates directly to the built‑in `open`.

## A practical example: processing a log file

The following script shows a real‑world use that combines several concepts:  
reading line by line, filtering, and writing results to a new file.

```python
#!/usr/bin/python

# filter_errors.py

input_path = 'app.log'
output_path = 'errors_only.log'

try:
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:

        for line in infile:
            if 'ERROR' in line:
                outfile.write(line)

    print(f"Filtered errors written to {output_path}")
except FileNotFoundError:
    print(f"Cannot find {input_path}")
except OSError as e:
    print(f"File error: {e}")
```

This example opens two files simultaneously – one for reading and one for  
writing – using the context manager to ensure both are properly closed.
