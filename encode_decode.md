# Encoding & decoding of data 

Encoding and decoding data in Python deal with converting between text data and a format  
suitable for storage or transmission. 

## Encoding

Represents text data (strings) as a sequence of bytes. Computers understand information as  
binary (0s and 1s). Encoding translates characters in our text (letters, symbols, etc.)  
into a specific byte representation.


Common encoding schemes include:

- UTF-8: Widely used for representing text in various languages due to its ability to handle
  a vast character set.
- ASCII: Older encoding limited to basic English characters (letters, numbers, and some symbols).  

Why encode?  

*Network transmission:* Many network protocols require data to be in byte format for efficient transfer.  
*File storage:* Files on disk might use specific encodings depending on the file format.  

## Decoding

The opposite of encoding. It takes a sequence of bytes and converts them back into a human-readable   
string format. Decoding requires knowing the encoding scheme used during the initial conversion.   

Python strings have built-in methods for encoding and decoding:  

- `encode(encoding='utf-8')` - converts the string to bytes using the specified encoding (defaults to UTF-8).  
- `decode(encoding='utf-8')` - converts bytes back to a string using the specified encoding.

```python
str.encode(encoding='utf-8', errors='strict')
```

The `str.encode` function encodes the string value to the bytes type. The encoding defaults to `utf-8`.

```python
bytes.decode(encoding='utf-8', errors='strict')
```

The `bytes.decode` function decodes the bytes type to the string type. The `bytes` type is an immutable  
sequence of bytes. The sequence consists of integers in the range 0 to 255. This data type is used for storing  
data and data transmission.

We work with the bytes type when we open network sockets, work with serial I/O or open binary files.  
Python has multiple standard encodings, including `utf_8`, `utf_16`, `ascii`, `latin-1`, `iso8859_2`, or `cp1252`.  
An encoding may have multiple aliases; for instance, utf_8 has utf8 and utf-8 aliases.

## Example

In the first example, we encode a message containing emoji characters.

```python
#!/usr/bin/python

text = "one 🐘 and three 🐋"
print(text)
print(len(text))

e = text.encode('utf8')
print(e)
print(len(e))

e = text.encode('utf16')
print(e)
print(len(e))
```

The program defines a message and encodes it into bytes type using `utf8` and `utf16` encodings.

```python
text = "one 🐘 and three 🐋"
```

We define a Unicode string with two emoji characters.

```python
print(text)
print(len(text))
```

We print the text and the number of characters.

```
e = text.encode('utf8')
print(e)
print(len(e))
```

We encode the string into a bytes type using the utf8 encoding and print the bytes.  
We count the number of bytes in this encoding type.

```
e = text.encode('utf16')
print(e)
print(len(e))
```

We do the same for the `utf16` encoding.

```python
$ ./main.py 
one 🐘 and three 🐋
17
b'one \xf0\x9f\x90\x98 and three \xf0\x9f\x90\x8b'
23
b'\xff\xfeo\x00n\x00e\x00 \x00=\xd8\x18\xdc ... \x00=\xd8\x0b\xdc'
40
```

## The decode example

In the following example, we read a file in binary mode. Later we decode the data into  
`utf8` string.


```
one 🐘 and three 🐋
```

We have this `data.txt` file.

```python
#!/usr/bin/python

fname = 'data.txt'

with open(fname, mode='rb') as f:
    contents = f.read()

    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))
```

We open the file in rb mode and read its contents.

```python
contents = f.read()
```

Since it is a small file, we read the whole file into a variable with read.

```python
print(type(contents))
```

We print the type of the data.

```python
print(contents)
print(contents.decode('utf8'))
```

We print the contents and then we print the decoded contents to the terminal.

```
$ ./main.py 
<class 'bytes'>
b'one \xf0\x9f\x90\x98 and three \xf0\x9f\x90\x8b'
one 🐘 and three 🐋
```

## Transmitting bytes

The data on the network is transmitted in the `bytes` type.

```python
#!/usr/bin/python

import requests

url = 'http://webcode.me/small.txt'

resp = requests.get(url)
print(resp.content)
print(resp.content.decode('utf8'))
print(resp.text)
```

We generate a GET request to a small text resource.

```python
url = 'http://webcode.me/small.txt'
```

We define the URL.

```python
resp = requests.get(url)
```

We generate a GET request to the given URL.

```python
print(req.content)
```

Printing the request content, we get a bytes string.

```python
print(resp.content.decode('utf8'))
```

We turn the `bytes` string into a Unicode string with decode.

```python
print(resp.text)
```

The `requests` library also contains the text member function which does the decoding.

```
$ ./main.py 
b'small text page\n'
small text page
```




  
