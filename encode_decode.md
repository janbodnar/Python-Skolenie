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
