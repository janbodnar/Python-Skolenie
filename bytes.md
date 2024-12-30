# Bytes

The bytes type is an immutable sequence of bytes. The sequence consists of  
integers in the range 0 to 255. This data type is used for storing data and data  
transmission.

When we open network sockets, work with serial I/O or open binary files, we work  
with the bytes type.

Python has a mutable equivalent of the bytes type called bytearray.

The bytes string is a human-readable representation of the bytes type. It  
consists of a sequence of ASCII characters between two single, double, or  
triple quotes. The bytes string is prefixed with the b character. For printable  
ASCII characters, the corresponding character is used. For newline, tab,  
carriage return, and `\` characters, the escape sequences `\n`, `\t`, `\r`, and  
`\\` are  used. For any other values, hexadecimal escape sequences such as  
`\xc4` or `\xc5` are used.

Each single element of the bytes type is an integer. A slice of bytes returs a slice.

## Python bytes example

In the first example, we start working with the bytes type.

```python
s = 'фальконет'
print(s)
print(len(s))

e = s.encode('utf8')
print(e)
print(len(e))

v = bytes('фальконет', 'utf8')
print(v)

w = b'\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82'
print(w)

print('-------------------------')

print(e.decode('utf8'))
print(v.decode('utf8'))
print(w.decode('utf8'))
```

In the example, we define a Unicode string and transform it to a bytes type.  
Then we turn it back to a Unicode string.

```python
s = 'фальконет'
print(s)
print(len(s))
```

We define a Unicode string and print it and its size in characters.

```
e = s.encode('utf8')
print(e)
```

We encode the string into a bytes type.

```python
print(len(e))
```

We print the number of bytes in the bytes string.

```python
v = bytes('фальконет', 'utf8')
```

We can get the bytes type using the built-in bytes function.

```python
w = b'\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82'
print(w)
```

We define a bytes string.

```python
print(e.decode('utf8'))
print(v.decode('utf8'))
print(w.decode('utf8'))
```

Here we decode the three bytes into Unicode strings.

```
$ ./main.py
фальконет
9
b'\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82'
18
b'\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82'
b'\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82'
-------------------------
фальконет
фальконет
фальконет
```

## Python transmitting bytes

The data on the network is transmitted in the bytes type.

```python
import requests

url = 'http://webcode.me/small.txt'

req = requests.get(url)

print(req.content)
print(req.content.decode('utf8'))
```

We generate a GET request to a small text resource.

```python
print(req.content)
```

Printing the request content, we get a bytes string.

```python
print(req.content.decode('utf8'))
```

We turn the bytes string into a Unicode string with decode.

```
$ ./main.py 
b'small text page\n'
small text page
```

## Python bytes read binary

When we open a file in binary mode, we retrieve the data in bytes.

The `data.txt` file:

```
Dnes bol krásny deň. 
Dážď bubnoval na okenice.
We have this text file.
```

```python
with open('data.txt', 'rb') as f:

    lines = f.readlines()

    print(lines)

    for line in lines:
        print(line.decode().rstrip())
```

We read a text file in binary mode.

```python
with open('data.txt', 'rb') as f:
```

We open the text file in rb mode.

```python
lines = f.readlines()
```

We get a list of bytes strings.

```python
for line in lines:
    print(line.decode().rstrip())
```

We go over the list and print the decoded lines.

```
$ ./main.py 
[b'Dnes bol kr\xc3\xa1sny de\xc5\x88. \r\n', b'D\xc3\xa1\xc5\xbe\xc4\x8f bubnoval na okenice.']
Dnes bol krásny deň.
Dážď bubnoval na okenice.
```

## Python bytes representations

In the following example, we represent bytes in different numerical systems.

```python
from more_itertools import sliced

s = 'château'
print(s)

v = s.encode('utf8')
print(v)

h = v.hex()
print(h)

d = list(sliced(h, 2))
print(d)

i = int(h, 16)
b = bin(i)

print(i)
print(b)

print(bytes.fromhex(f'{int(b, 2):x}').decode('utf8'))
```

We turn a French word château into a bytes type. The type is then displayed  
in hexadecimal, integer, and binary values.

```python
s = 'château'
print(s)
```

We define a Unicode string.

```python
v = s.encode('utf8')
print(v)
```

The string is encoded into a bytes string.

```python
h = v.hex()
print(h)
```

We transform the bytes string into a hex string.

```python
d = list(sliced(h, 2))
print(d)
```

We turn the hex string into a list of hexadecimal values.

```python
i = int(h, 16)
```

We transform the hex string into an integer.

```python
b = bin(i)
```

The decimal integer is transformed into binary.

```python
print(bytes.fromhex(f'{int(b, 2):x}').decode('utf8'))
```

We turn the binary back into the Unicode string.

```
$ ./main.py
château
b'ch\xc3\xa2teau'
6368c3a274656175
['63', '68', 'c3', 'a2', '74', '65', '61', '75']
7163190309837693301
0b110001101101000110000111010001001110100011001010110000101110101
château
```

## Summary

```python
import binascii

data = b"Hello there!"  # Example byte data
print(data)
print(data.hex())
print(data.decode('utf-8'))

data2 = [hex(byte) for byte in data]
print(data2)

data3 = [byte for byte in data]
print(data3)


hex_output = binascii.hexlify(data, ',').decode('utf-8')
print(hex_output)


data = [0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x74, 0x68, 0x65, 0x72, 0x65, 0x21]
print(bytes(data))
# print(binascii.hexlify(bytes(data)).decode('utf-8'))

byte_string = b"Hello there!"
hex_values = [hex(byte) for byte in byte_string]
print(hex_values)
```

