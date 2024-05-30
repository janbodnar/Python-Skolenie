# The os module 


## os.path

```python
import os, datetime

path = os.path.join('C://Users/Jano', 'Documents', 'words.txt')
size = os.path.getsize(path)
mtime = os.path.getmtime(path)

print('Size:', size)
print('Last modified:', datetime.datetime.fromtimestamp(mtime))
```
