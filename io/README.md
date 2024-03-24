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

Using `Path`

```python
from pathlib import Path

fname = 'words.txt'

text = Path(fname).read_text()
print(text)
```


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
