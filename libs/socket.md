# Sockets


Socket programming is low-level. The goal of this tutorial is to introduce  
network programming including these low-level details. There are higher-level  
Python APIs such as Twisted that might be better suited.  

In programming, a socket is an endpoint of a communication between two programs  
running on a network. Sockets are used to create a connection between a client  
program and a server program.  

Python's socket module provides an interface to the Berkeley sockets API.

Note: In networking, the term socket has a different meaning. It is used for the  
combination of an IP address and a port number. Network protocols TCP/IP is a  
suite of protocols used by devices to communicate over the Internet and most  
local networks. TCP is more reliable, has extensive error checking, and requires  
more resources. It is used by services such as HTTP, SMTP, or FTP. UDP is much  
less reliable, has limited error checking, and requires less resources. It is  
used by services such as VoIP.  

The `socket.SOCK_STREAM` is used to create a socket for TCP and  
`socket.SOCK_DGRAM` for UDP.

## Address families

When we create a socket, we have to specify its address family. Then we can only  
use addresses of that type with the socket.  

- AF_UNIX, AF_LOCAL - Local communication
- AF_INET - IPv4 Internet protocols
- AF_INET6 - IPv6 Internet protocols
- AF_IPX - IPX - Novell protocols
- AF_BLUETOOTH - Wireless bluetooth protocols
- AF_PACKET - Low level packet interface

For the `AF_INET` address family, a pair (host, port) is specified. The host is  
a string representing either a hostname in Internet domain notation like  
example.com or an IPv4 address like 93.184.216.34, and port is an integer.  


## Get IP address

With `gethostbyname`, we get the IP address of the host.

```python
import socket

ip = socket.gethostbyname('example.com')
print(ip)
```

The example prints the IP address of example.com.



## UDP socket example

UDP is a communication protocol that transmits independent packets over the  
network with no guarantee of arrival and no guarantee of the order of delivery.  
One service that used UDP is the Quote of the Day (QOTD).  

```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    message = b''
    addr = ("djxmmx.net", 17)

    s.sendto(message, addr)

    data, address = s.recvfrom(1024)
    print(data.decode())
```

The example creates a client program that connects to a QOTD service.  

```python
import socket
```

We import the socket module.

```python
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
```

A datagram socket for IPv4 is created.

```python
message = b''
```

We send an empty message; the QOTD service works by sending arbitrary data to  
the socket; it simply responds with a quote. To communicate over TCP/UDP, we use  
binary strings.  

```python
addr = ("djxmmx.net", 17)
```

We provide the address and the port.

```python
s.sendto(message, addr)
```

We send data with the sendto method.

```python
data, address = s.recvfrom(1024)
```

UDP sockets use recvfrom to receive data. Its paremeter is the buffer size. The  
return value is a pair (data, address) where data is a byte string representing  
the data received and address is the address of the socket sending the data.  

```python
print(data.decode())
```

We print the decoded data to the terminal.

## TCP socket example

The are servers that provide current time. A client simply connects to the  
server with no commands, and the server responds with a current time.  

Note: Time servers come and go, so we might need to find a working server on  
https://www.ntppool.org/en/.  

```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    host = "time.nist.gov"
    port = 13

    s.connect((host, port))
    s.sendall(b'')
    print(str(s.recv(4096), 'utf-8'))
```

The example determines the current time by connecting to a time server's TCP  
socket.  

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
```

A TCP socket for IPv4 is created.

```python
host = "time.nist.gov"
port = 13
```

This is the host name and the port number of a working time server.  

```python
s.connect((host, port))
```

We connect to the remote socket with connect.

```python
s.sendall(b'')
```

The `sendall` method sends data to the socket. The socket must be connected to a   
remote socket. It continues to send data from bytes until either all data has  
been sent or an error occurs.  

```python
print(str(s.recv(4096), 'utf-8'))
```

We print the received data. The `recv` method receives up to `buffersize` bytes  
from the socket. When no data is available, it blocks until at least one byte is  
available or until the remote end is closed. When the remote end is closed and  
all data is read, it returns an empty byte string.  

## Socket HEAD request

A HEAD request is a GET request without a message body. The header of a  
request/response contains metadata, such as HTTP protocol version or content  
type.  

```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("webcode.me" , 80))
    s.sendall(b"HEAD / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\n\r\n")
    print(str(s.recv(1024), 'utf-8'))
```

In the example, we send a HEAD request to webcode.me.

```python
s.sendall(b"HEAD / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\n\r\n")
```

A head request is issued with the HEAD command followed by the resource URL and  
HTTP protocol version. Note that the `\r\n` are mandatory part of the  
communication process. The details are described in RFC 7231 document.  

HTTPS:  

```python
import socket
import ssl

# Create a socket and wrap it with SSL
context = ssl.create_default_context()
with socket.create_connection(("webcode.me", 443)) as sock:
    with context.wrap_socket(sock, server_hostname="webcode.me") as ssock:
        # Send HTTPS request
        ssock.sendall(b"HEAD / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\n\r\n")
        
        # Receive and print the response
        print(str(ssock.recv(1024), 'utf-8'))
```



## Socket GET request

The HTTP GET method requests a representation of the specified resource.  
Requests using GET should only retrieve data.  

```python
import socket
import ssl

# Create a socket and wrap it with SSL
context = ssl.create_default_context()
with socket.create_connection(("webcode.me", 443)) as sock:
    with context.wrap_socket(sock, server_hostname="webcode.me") as ssock:
        # Send HTTPS request
        ssock.sendall(b"GET / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\nConnection: close\r\n\r\n")
        
        # Receive and print the response
        while True:
            data = ssock.recv(1024)
            if not data:
                break
            print(data.decode())
```

The example reads the home page of the `webcode.me` using a GET request.  

```python
s.sendall(b"GET / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\nConnection: close\r\n\r\n")
```

For the HTTP 1.1 protocol, the connections may be persistent by default. This is  
why we send the Connection: close header.  

```python
while True:

    data = s.recv(1024)

    if not data:
        break

    print(data.decode())
```

We use a while loop to process the received data. If no error occurs, `recv`  
returns the bytes received. If the connection has been gracefully closed, the  
return value is an empty byte string. The `recv` is a blocking method that
blocks until it is done, or a timeout is reached or another exception occurs.  


## Echo client server example

An echo server sends the message from the client back. It is a classic example  
used for testing and learning.  

The `echo_server.py`:  

```python
import socket
import time

with socket.socket() as s:

    host = 'localhost'
    port = 8001

    s.bind((host, port))
    print(f'socket binded to {port}')

    s.listen()

    con, addr = s.accept()

    with con:

        while True:

            data = con.recv(1024)

            if not data:
                break

            con.sendall(data)
```

The echo server sends the client message back to the client.

```python
host = 'localhost'
port = 8001
```


The server runs on localhost on port 8001.

```python
s.bind((host, port))
```

The `bind` method establishes the communication endpoint. It binds the socket to  
the specified address. The socket must not already be bound. (The format of  
address depends on the address family.)  

```python
s.listen()
```

The `listen` method enables a server to accept connections. The server can now  
listen for connections on a socket. The listen has a backlog parameter. It  
specifies the number of unaccepted connections that the system will allow before  
refusing new connections. The parameter is optional since Python 3.5. If not  
specified, a default backlog value is chosen.  

```python
con, addr = s.accept()
```

With `accept`, the server accepts a connection. It blocks and waits for an  
incoming connection. The socket must be bound to an address and listening for  
connections. The return value is a pair (con, addr) where con is a new socket  
object usable to send and receive data on the connection, and addr is the  
address bound to the socket on the other end of the connection.  

Note that the accept creates a new socket for communication with a client, which  
is a different socket from the listening socket.  


The `echo_client.py`:  

```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    host = "localhost"
    port = 8001

    s.connect((host, port))
    s.sendall(b'hello there')
    print(str(s.recv(4096), 'utf-8'))
```

The client sends a message to the echo server.  

## Asynchronous server example

In order to improve the performance of a server, we can use the `asyncio`  
module.

The `async_server.py`: 

```python
# From threading import current_thread

import asyncio


async def handle_client(reader, writer):

    data = (await reader.read(1024))

    writer.write(data)
    writer.close()


loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(handle_client, 'localhost', 8001))
loop.run_forever()
```

We can now test the performance of the blocking and non-blocking servers.  

```
$ ab -c 50 -n 1000 http://localhost:8001/
```

For instance, we can test the performance with the Apache benchmarking tool. In  
our case, the command sends 1000 requests, 50 at a time.  
