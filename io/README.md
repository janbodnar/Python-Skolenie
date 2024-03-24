# Input & output

## Small files

The `read` method

```python
with open('words.txt', 'r') as f:
    data = f.read()

    print(data)
```

The `readlines` method

```python
with open('words.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        print(line)
```

## The pathlib

```python
from pathlib import Path

fname = 'words.txt'

with Path(fname).open() as f:
    
    text = f.read()
    print(text)
```


```python
from pathlib import Path

fname = 'words.txt'

text = Path(fname).read_text()
print(text)
```

## File modes

| Mode | Description |
| --- | --- |
| `rw` | open for reading (default), open for writing, truncating the file first |
| `rx` | open for reading (default), open for exclusive creation, failing if the file already exists |
| `ra` | open for reading (default), open for writing, appending to the end of the file if it exists |
| `rb` | open for reading (default), binary mode |
| `rt` | open for reading (default), text mode (default) |
| `r+` | open for reading (default), open for updating (reading and writing) |
| `wx` | open for writing, truncating the file first, open for exclusive creation, failing if the file already exists |
| `wa` | open for writing, truncating the file first, open for writing, appending to the end of the file if it exists |
| `wb` | open for writing, truncating the file first, binary mode |
| `wt` | open for writing, truncating the file first, text mode (default) |
| `w+` | open for writing, truncating the file first, open for updating (reading and writing) |
| `xa` | open for exclusive creation, failing if the file already exists, open for writing, appending to the end of the file if it exists |
| `xb` | open for exclusive creation, failing if the file already exists, binary mode |
| `xt` | open for exclusive creation, failing if the file already exists, text mode (default) |
| `x+` | open for exclusive creation, failing if the file already exists, open for updating (reading and writing) |
| `ab` | open for writing, appending to the end of the file if it exists, binary mode |
| `at` | open for writing, appending to the end of the file if it exists, text mode (default) |
| `a+` | open for writing, appending to the end of the file if it exists, open for updating (reading and writing) |
| `bt` | binary mode, text mode (default) |
| `b+` | binary mode, open for updating (reading and writing) |
| `t+` | text mode (default), open for updating (reading and writing) |




## Large files

```python
with open("large_file.txt", "r") as f:
  for line in f:
    # Process each line here
    pass
```


```python
chunk_size = 1024  # Adjust chunk size as needed
with open("large_file.txt", "r") as f:
  while True:
    chunk = f.read(chunk_size)
    if not chunk:
      break
    # Process the chunk here
```

```python
from pathlib import Path

chunk_size = 4096  # Adjust chunk size for binary data

large_file = Path("large_file.binary")

with large_file.open("rb") as f:
  while True:
    chunk = f.read_bytes(chunk_size)
    if not chunk:
      break
    # Process the chunk here
```

```python
from pathlib import Path

large_file = Path("large_file.txt")

with large_file.open("r") as f:
  for line in f:
    # Process each line here
    pass
```

```python
from pathlib import Path

chunk_size = 1024

large_file = Path("large_file.txt")

with large_file.open("r") as f:
  while True:
    chunk = f.read(chunk_size)
    if not chunk:
      break
    # Process the chunk here
```
