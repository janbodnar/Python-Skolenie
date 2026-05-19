# A Complete Guide to Python `pathlib` – Object‑Oriented File System Paths

The `pathlib` module, introduced in Python 3.4, provides an object‑oriented interface to the file  
system. Instead of juggling strings and `os.path` functions, you create `Path` objects that offer  
properties and methods for common operations – like joining paths, reading or writing files, listing directories, and more.


## Table of Contents

1. [Getting Started – Creating Path Objects](#1-getting-started--creating-path-objects)
2. [Current and Home Directories](#2-current-and-home-directories)
3. [Navigating and Changing Directories](#3-navigating-and-changing-directories)
4. [Path Properties and Components](#4-path-properties-and-components)
   - [Parts, drive, root, anchor](#parts-drive-root-anchor)
   - [Name, stem, suffix(es)](#name-stem-suffixes)
   - [Parents and parent](#parents-and-parent)
5. [Building Paths – Joining and Resolving](#5-building-paths--joining-and-resolving)
   - [The `/` operator and `joinpath()`](#the--operator-and-joinpath)
   - [Absolute vs. relative paths](#absolute-vs-relative-paths)
   - [Resolving symlinks and `resolve()`](#resolving-symlinks-and-resolve)
6. [Checking Path Type and Existence](#6-checking-path-type-and-existence)
7. [Creating and Deleting Directories](#7-creating-and-deleting-directories)
8. [Working with Files – Reading and Writing](#8-working-with-files--reading-and-writing)
   - [Text files](#text-files)
   - [Binary files](#binary-files)
   - [Low‑level file operations with `open()`](#low-level-file-operations-with-open)
9. [Copying, Moving, Renaming, and Deleting Files](#9-copying-moving-renaming-and-deleting-files)
10. [Listing Directories – `iterdir()` and `glob()`](#10-listing-directories--iterdir-and-glob)
    - [Basic listing](#basic-listing)
    - [Globbing patterns](#globbing-patterns)
    - [Recursive globbing with `rglob()`](#recursive-globbing-with-rglob)
11. [Practical Recipes](#11-practical-recipes)
    - [Printing a directory tree](#printing-a-directory-tree)
    - [Counting files by extension](#counting-files-by-extension)
    - [Merging two text files](#merging-two-text-files)
    - [Creating a dated article file](#creating-a-dated-article-file)
    - [Pretty‑printing file information](#pretty-printing-file-information)
12. [Working with Symlinks and Permissions](#12-working-with-symlinks-and-permissions)
13. [Path Comparison and Sorting](#13-path-comparison-and-sorting)
14. [`pathlib` vs. `os.path` – When to Use What](#14-pathlib-vs-ospath--when-to-use-what)
15. [Common Pitfalls and Best Practices](#15-common-pitfalls-and-best-practices)
16. [Further Reading](#16-further-reading)

---

## 1. Getting Started – Creating Path Objects

A `Path` can be created from a string, or you can use class methods to get special paths.

```python
# example_path_creation.py
from pathlib import Path

# From a string
p1 = Path("/home/user/docs/readme.txt")
p2 = Path("C:\\Users\\jano\\data.csv")   # Windows raw string or use forward slashes
p3 = Path("relative/path/to/file")

# Using class methods
cwd = Path.cwd()          # current working directory
home = Path.home()        # user's home directory

print(f"CWD: {cwd}")
print(f"Home: {home}")
```

Run it:
```bash
python example_path_creation.py
```

Output (will differ on your system):
```
CWD: /home/jano/projects/pathlib_demo
Home: /home/jano
```

On Windows you might see `WindowsPath('C:\\Users\\jano')` – the representation includes the class name, but you can use it like any string.

---

## 2. Current and Home Directories

```python
# example_cwd_home.py
from pathlib import Path

print(f"Current directory: {Path.cwd()}")
print(f"Home directory: {Path.home()}")
```

That’s it – no extra imports needed.

---

## 3. Navigating and Changing Directories

`Path` objects are immutable – methods like `chdir()` are not part of `Path` because changing the process’s working directory is a global operation. You still need `os.chdir()`. But you can easily construct new paths relative to an existing one.

```python
# example_chdir.py
from pathlib import Path
import os

original = Path.cwd()
print(f"Original: {original}")

new_dir = original / ".."   # parent directory (string-like)
os.chdir(new_dir)
print(f"After chdir: {Path.cwd()}")

# Restore (optional)
os.chdir(original)
```

Note: `Path("..")` is a valid path; using `/` we join it.

**Better:** Use `Path.parent` to get the parent directory without relying on `".."`.

---

## 4. Path Properties and Components

### Parts, drive, root, anchor

```python
# example_parts.py
from pathlib import Path

path = Path("C:/Users/jano/Documents/report.pdf")

print("Parts:", path.parts)          # ('C:\\', 'Users', 'jano', 'Documents', 'report.pdf')
print("Drive:", path.drive)          # 'C:' (Windows only; on Unix it's '')
print("Root:", path.root)            # '\\' on Windows, '/' on Unix
print("Anchor:", path.anchor)        # 'C:\\' on Windows, '/' on Unix
```

On Unix:
```python
path = Path("/home/jano/docs/report.pdf")
print(path.parts)   # ('/', 'home', 'jano', 'docs', 'report.pdf')
print(path.drive)   # ''
print(path.root)    # '/'
```

### Name, stem, suffix(es)

```python
# example_name_stem_suffix.py
from pathlib import Path

path = Path("archive.tar.gz")

print("Name:", path.name)          # 'archive.tar.gz'
print("Stem:", path.stem)          # 'archive.tar'   (name without the final suffix)
print("Suffix:", path.suffix)      # '.gz'           (last suffix)
print("Suffixes:", path.suffixes)  # ['.tar', '.gz'] (all suffixes)
```

If you need the base name without any suffix, use `path.stem.split('.')[0]` (but be careful with dots). Or use the standard library: `os.path.splitext(path.stem)[0]`.

### Parents and parent

```python
# example_parents.py
from pathlib import Path

path = Path("/home/jano/projects/tutorial/script.py")

print("Parent:", path.parent)                 # /home/jano/projects/tutorial
print("Parent of parent:", path.parent.parent) # /home/jano/projects

print("All parents:")
for parent in path.parents:                   # iterates from immediate parent upward
    print(f"  {parent}")
```

Output (Unix):
```
Parent: /home/jano/projects/tutorial
Parent of parent: /home/jano/projects
All parents:
  /home/jano/projects/tutorial
  /home/jano/projects
  /home/jano
  /home
  /
```

---

## 5. Building Paths – Joining and Resolving

### The `/` operator and `joinpath()`

```python
# example_join.py
from pathlib import Path

home = Path.home()

# Using / operator (cleanest)
docs = home / "Documents" / "work"
print(docs)

# Using joinpath() (takes multiple arguments)
pictures = home.joinpath("Pictures", "vacation", "img_001.jpg")
print(pictures)
```

Both produce the correct path separator for your operating system.

### Absolute vs. relative paths

Use `is_absolute()` to test. Convert relative to absolute with `resolve()` (which also normalizes `..` and `.`).

```python
# example_absolute.py
from pathlib import Path

rel = Path("docs/../report.txt")
abs_path = rel.resolve()   # becomes /current/working/dir/report.txt
print(f"Resolved: {abs_path}")
```

`resolve()` follows symlinks by default; use `resolve(strict=False)` to avoid errors if the path doesn’t exist.

### Relative path from one location to another

```python
# example_relative_to.py
from pathlib import Path

archive = Path("/home/jano/Downloads/wordpress-5.1.tar.gz")
home = Path.home()

rel = archive.relative_to(home)
print(rel)   # 'Downloads/wordpress-5.1.tar.gz' (on Unix)
```

If the path is not relative to the given start, `relative_to()` raises `ValueError`. You can use `os.path.relpath()` as a fallback.

---

## 6. Checking Path Type and Existence

```python
# example_check.py
from pathlib import Path

p = Path("somefile.txt")

print(p.exists())      # True if file or directory exists
print(p.is_file())     # True if it's a regular file
print(p.is_dir())      # True if it's a directory
print(p.is_symlink())  # True if it's a symbolic link
print(p.is_absolute()) # True if path is absolute
```

Also: `is_block_device()`, `is_char_device()`, `is_fifo()`, `is_socket()`.

---

## 7. Creating and Deleting Directories

```python
# example_mkdir_rmdir.py
from pathlib import Path

new_dir = Path.cwd() / "test_folder"

# Create directory
new_dir.mkdir(exist_ok=True)           # no error if exists
# new_dir.mkdir(parents=True, exist_ok=True)  # create parents as well

# Remove empty directory
new_dir.rmdir()                        # raises OSError if not empty

# To remove non‑empty directory, use shutil.rmtree()
import shutil
shutil.rmtree(new_dir, ignore_errors=True)
```

**Note:** `rmdir()` only deletes empty directories. For recursive deletion, use `shutil.rmtree()`.

---

## 8. Working with Files – Reading and Writing

### Text files

`read_text()` and `write_text()` are convenient for small to medium files.

```python
# example_read_write_text.py
from pathlib import Path

file_path = Path("hello.txt")

# Write
file_path.write_text("Hello, world!\nSecond line", encoding="utf-8")

# Read
content = file_path.read_text(encoding="utf-8")
print(content)

# Clean up
file_path.unlink()   # delete file
```

### Binary files

Use `read_bytes()` and `write_bytes()`.

```python
# example_read_bytes.py
from pathlib import Path
import binascii

img = Path("sample.jpg")
if img.exists():
    data = img.read_bytes()
    hex_preview = binascii.hexlify(data[:20])   # first 20 bytes
    print(hex_preview)
```

### Low‑level file operations with `open()`

`Path.open()` works like the built‑in `open()` but returns a file object.

```python
# example_open.py
from pathlib import Path

p = Path("data.txt")
with p.open("r") as f:
    for line in f:
        print(line.strip())
```

This is useful when you need more control (e.g., reading line by line, binary mode, or using `csv` module).

---

## 9. Copying, Moving, Renaming, and Deleting Files

`pathlib` does **not** have built‑in copy methods. Use `shutil`.

```python
# example_copy_move.py
from pathlib import Path
import shutil

src = Path("original.txt")
dst = Path("backup.txt")

# Copy
shutil.copy(src, dst)

# Move / rename
dst.rename("archive/old.txt")          # also moves across directories
# Or shutil.move(src, dst)
```

- `rename()` works for both files and directories. It can move across filesystems but may not be atomic.
- `replace(target)` is like `rename()` but overwrites the target unconditionally (on Unix it’s atomic).
- `unlink()` deletes a file (or symlink). Use `missing_ok=True` in Python 3.8+ to avoid error if file doesn’t exist.

```python
# example_delete.py
from pathlib import Path

p = Path("temporary.tmp")
p.unlink(missing_ok=True)   # no error if not there
```

---

## 10. Listing Directories – `iterdir()` and `glob()`

### Basic listing

`iterdir()` yields path objects of everything in a directory.

```python
# example_listdir.py
from pathlib import Path

for item in Path.cwd().iterdir():
    if item.is_file():
        print(f"File: {item.name}")
    elif item.is_dir():
        print(f"Dir:  {item.name}")
```

To get only files or directories, use list comprehensions:

```python
files = [p for p in Path.cwd().iterdir() if p.is_file()]
dirs  = [p for p in Path.cwd().iterdir() if p.is_dir()]
```

### Globbing patterns

`glob(pattern)` returns files matching a pattern (like `*.txt`, `data?.csv`).

```python
# example_glob.py
from pathlib import Path

for py_file in Path("src").glob("*.py"):
    print(py_file)
```

### Recursive globbing with `rglob()`

`rglob(pattern)` is equivalent to `glob("**/" + pattern)` – it searches subdirectories recursively.

```python
# example_rglob.py
from pathlib import Path

for config in Path.home().rglob("*.ini"):
    print(config)
```

**Performance warning:** Recursive glob on a large tree can be slow. Use it judiciously.

---

## 11. Practical Recipes

### Printing a directory tree

```python
# recipe_tree.py
from pathlib import Path

def print_tree(directory: Path, prefix: str = ""):
    """Print a directory tree recursively."""
    if not directory.is_dir():
        return
    items = sorted(directory.iterdir())
    for i, item in enumerate(items):
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        print(prefix + connector + item.name)
        if item.is_dir():
            extension = "    " if is_last else "│   "
            print_tree(item, prefix + extension)

if __name__ == "__main__":
    root = Path.cwd() / "my_project"
    if root.exists():
        print(root.name)
        print_tree(root)
    else:
        print(f"{root} does not exist")
```

### Counting files by extension

```python
# recipe_count_extensions.py
from pathlib import Path
from collections import Counter

def count_extensions(directory: Path):
    extensions = [p.suffix for p in directory.iterdir() if p.is_file() and p.suffix]
    return Counter(extensions)

home = Path.home()
docs = home / "Documents"
if docs.exists():
    counts = count_extensions(docs)
    for ext, count in counts.most_common():
        print(f"{ext or '(no extension)'}: {count}")
```

### Merging two text files

```python
# recipe_merge_files.py
from pathlib import Path
import sys

def merge_files(file1: Path, file2: Path):
    lines1 = file1.read_text().splitlines()
    lines2 = file2.read_text().splitlines()
    for a, b in zip(lines1, lines2):
        print(f"{a} {b}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        merge_files(Path(sys.argv[1]), Path(sys.argv[2]))
    else:
        print("Usage: python merge_files.py file1.txt file2.txt")
```

### Creating a dated article file

```python
# recipe_new_article.py
from pathlib import Path
import datetime

def create_article(title: str, base_dir: Path = Path.cwd() / "articles"):
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month).zfill(2)
    target_dir = base_dir / year / month
    target_dir.mkdir(parents=True, exist_ok=True)
    article_path = target_dir / f"{title.replace(' ', '_')}.txt"
    article_path.touch()
    return article_path

if __name__ == "__main__":
    title = input("Article title: ")
    path = create_article(title)
    print(f"Created: {path}")
```

### Pretty‑printing file information

Using `prettytable` for a nice table output.

First install: `pip install prettytable`

```python
# recipe_prettytable.py
from pathlib import Path
import datetime
from prettytable import PrettyTable

def file_table(directory: Path, pattern: str = "**/*"):
    table = PrettyTable()
    table.field_names = ["Name", "Size (bytes)", "Modified"]
    table.align["Name"] = "l"
    table.align["Size (bytes)"] = "r"
    for p in directory.glob(pattern):
        if p.is_file():
            stat = p.stat()
            modified = datetime.datetime.fromtimestamp(stat.st_mtime)
            table.add_row([p.name, stat.st_size, modified.strftime("%Y-%m-%d")])
    print(table)

if __name__ == "__main__":
    file_table(Path.cwd(), "*.py")
```

---

## 12. Working with Symlinks and Permissions

- Create a symbolic link: `path.symlink_to(target, target_is_directory=False)`
- Read the target of a symlink: `path.readlink()` (Python 3.9+)
- Change file permissions: `path.chmod(mode)` (numeric like `0o644`)
- Get owner/group: `path.owner()` and `path.group()` (may raise `KeyError` if not found)

```python
# example_symlinks.py
from pathlib import Path

link = Path("mylink")
target = Path("real_file.txt")

if not target.exists():
    target.touch()

link.symlink_to(target)
print(link.is_symlink())        # True
print(link.resolve())           # points to real_file.txt
print(link.readlink())          # real_file.txt (Python 3.9+)

# Cleanup
link.unlink()
target.unlink()
```

---

## 13. Path Comparison and Sorting

Paths can be compared with equality operators (`==`, `!=`) – they compare the string representation **after resolving the path on Windows (case‑insensitively) and keeping the case on Unix**. Ordering (`<`, `>`) works lexicographically on the string representation.

```python
# example_compare.py
from pathlib import Path

p1 = Path("/home/user/Data")
p2 = Path("/home/user/data")
print(p1 == p2)   # On Windows: True (case‑insensitive); on Unix: False

# Sorting paths
paths = [Path("z.txt"), Path("a.txt"), Path("m.txt")]
paths.sort()
print([p.name for p in paths])   # ['a.txt', 'm.txt', 'z.txt']
```

---

## 14. `pathlib` vs. `os.path` – When to Use What

| Operation                     | `pathlib` (recommended)           | `os.path` / `os` functions         |
|-------------------------------|------------------------------------|-------------------------------------|
| Join paths                    | `path / "sub"`                     | `os.path.join(path, "sub")`         |
| Get parent                    | `path.parent`                      | `os.path.dirname(path)`             |
| Get filename                  | `path.name`                        | `os.path.basename(path)`            |
| Get stem                      | `path.stem`                        | `os.path.splitext(path)[0]`         |
| Check existence               | `path.exists()`                    | `os.path.exists(path)`              |
| List directory                | `path.iterdir()`                   | `os.listdir(path)`                  |
| Recursive glob                | `path.rglob(pattern)`              | `glob.glob("**/pattern", recursive=True)` |
| Read entire file as string    | `path.read_text()`                 | `open(path).read()` (more code)     |
| Write string to file          | `path.write_text(data)`            | `open(path, "w").write(data)`       |

**Verdict:** Prefer `pathlib` for new code – it’s more readable and object‑oriented. Use `os.path` only when interacting with legacy APIs that expect strings.

---

## 15. Common Pitfalls and Best Practices

1. **Do not rely on string operations** – Use `/` or `joinpath()`.
2. **Handle `FileNotFoundError`** – Methods like `read_text()`, `resolve()`, `relative_to()` raise exceptions; catch them or check `exists()` first.
3. **Be careful with `resolve()` on broken symlinks** – It raises `FileNotFoundError` unless you set `strict=False`.
4. **`iterdir()` yields unsorted results** – Sort explicitly if order matters.
5. **`glob("**/*")` can be memory‑intensive** – Use `rglob("*")` – still traverses everything, but at least you can iterate lazily.
6. **Permissions and ownership** – `owner()` and `group()` may fail if the user ID doesn’t map to a name; wrap in try/except.
7. **Cross‑platform pitfalls** – `drive` and `root` differ; use `as_posix()` for consistent forward‑slash paths.
8. **Recursive operations on large trees** – Use `pathlib` with care; for very deep trees consider `os.scandir()`.

---

## 16. Further Reading

- [Official `pathlib` documentation](https://docs.python.org/3/library/pathlib.html)
- [PEP 428 – The pathlib module](https://peps.python.org/pep-0428/)
- [Python’s `pathlib` – a deep dive](https://realpython.com/python-pathlib/)

---

## Final Words

The `pathlib` module transforms file system operations from error‑prone string manipulation to clean, expressive,  
and cross‑platform code. Practice with the examples above, and you’ll never want to go back to `os.path` again.
