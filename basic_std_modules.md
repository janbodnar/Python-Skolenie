# Basic standard modules 

Demonstrating some basic standard modules

## secrets 

```python
#!/usr/bin/python


import string
import secrets

chars = string.ascii_letters + string.digits + string.punctuation
passwd = "".join(secrets.choice(chars) for i in range(8))

print(passwd)
```

```python
#!/usr/bin/python


import secrets

with open("unix-words.txt") as f:
    words = [word.strip() for word in f]
    password = " ".join(secrets.choice(words) for i in range(4))
    print(password)
```

## zipfile 

Create a ZIP file.  

```python
#!/usr/bin/python

import os
import zipfile


def create_zip(zip_filename, directory):
    """
    Creates a ZIP archive from the contents of a directory.

    Args:
        zip_filename (str): The name of the ZIP file to create.
        directory (str): The directory path to compress.
    """
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(directory):
            for filename in files:
                # Create relative path within the ZIP
                archive_path = os.path.join(root[len(directory)+1:], filename)
                # Add file to the ZIP archive
                zip_file.write(os.path.join(root, filename), archive_path)


# Example usage:
zip_filename = "my_archive.zip"
current_dir = os.getcwd()  # Get current working directory
create_zip(zip_filename, current_dir)
print(f"Created ZIP archive: {zip_filename}")
```

List contents of a ZIP file.  

```python
import zipfile

def open_zip(zip_filename):
  """
  Opens a ZIP archive and lists its contents.

  Args:
      zip_filename (str): The name of the ZIP file to open.
  """
  try:
    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
      print(f"Contents of ZIP archive: {zip_filename}")
      # Get list of filenames in the archive
      filenames = zip_file.namelist()
      for filename in filenames:
        print(f"- {filename}")
  except FileNotFoundError:
    print(f"Error: ZIP file '{zip_filename}' not found.")
  except Exception as e:
    print(f"Error opening ZIP archive: {e}")

# Example usage
zip_filename = "my_archive.zip"
open_zip(zip_filename)
```



