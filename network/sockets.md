# Python Socket Programming – Full Tutorial  
*Last modified: May 2026*  

Socket programming gives you low‑level access to network communication. This  
tutorial teaches the fundamentals, from basic data exchange to multi‑client  
servers and secure connections. All examples are self‑contained and fully  
runnable. Understanding sockets is essential for building networked  
applications, debugging connectivity issues, or simply learning how protocols  
like HTTP work under the hood.  

## 1. Socket Basics  
A **socket** is an endpoint for sending and receiving data across a network.  
Python's `socket` module provides the standard BSD socket API, which is  
consistent across Unix, Linux, Windows, and macOS. Sockets abstract the  
complexities of network protocols, letting you focus on application logic.  

### Address families  
When creating a socket, you must choose an address family (the type of network  
addresses you will use). The most common are:  

| Family           | Meaning                          |  
||  
| `AF_INET`        | IPv4 Internet protocols          |  
| `AF_INET6`       | IPv6 Internet protocols          |  
| `AF_UNIX` / `AF_LOCAL` | Local (same machine) communication via filesystem path |  
| `AF_BLUETOOTH`   | Bluetooth communication          |  

Choosing the right address family depends on your deployment environment.  
`AF_INET` works everywhere but is limited to 32‑bit addresses. `AF_INET6`  
supports the larger IPv6 address space and is future‑proof. `AF_UNIX` is  
highly efficient for local IPC because it bypasses the network stack entirely.  

### Socket types  
The socket type determines how data is transmitted:  

| Type               | Protocol | Behaviour                                      |  
|-||  
| `SOCK_STREAM`      | TCP      | Reliable, connection‑oriented, ordered stream  |  
| `SOCK_DGRAM`       | UDP      | Datagrams, connectionless, unordered, no guarantee |  

TCP guarantees delivery and order but adds overhead for handshakes and  
acknowledgments. UDP is faster and lighter but requires your application to  
handle loss, duplication, and reordering. Choose TCP for correctness, UDP for  
speed or broadcast scenarios.  

### Creating a socket  
```python
import socket

# TCP IPv4 socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# UDP IPv4 socket
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```
Using a `with` statement automatically closes the socket when the block exits.  

The `socket()` constructor takes the address family and socket type as  
positional arguments. A third optional argument specifies the protocol number  
(usually zero to select the default). Always close sockets to free system  
resources; the context manager (`with`) ensures this happens even if an  
exception occurs. For long‑running servers, consider setting `SO_REUSEADDR` to  
avoid "address already in use" errors after restarts.  

 

## 2. Hostnames and IP Addresses  
### Get the IP address of a host  
```python
#!/usr/bin/env python3
"""get_ip.py – resolve a hostname to an IP"""
import socket

host = 'example.com'
ip = socket.gethostbyname(host)
print(f'{host} -> {ip}')
```
For more detailed address info, use `getaddrinfo` (works for IPv4/IPv6):  
```python
#!/usr/bin/env python3
"""getaddrinfo_demo.py – detailed address resolution"""
import socket

host = 'example.com'
for res in socket.getaddrinfo(host, 80, proto=socket.IPPROTO_TCP):
    family, socktype, proto, canonname, sockaddr = res
    print(f'family={family}, addr={sockaddr}')
```

`gethostbyname` is simple but IPv4‑only and may return only one address.  
`getaddrinfo` is the modern, protocol‑agnostic alternative: it returns a list  
of 5‑tuples containing family, type, protocol, canonical name, and socket  
address. This is essential for dual‑stack (IPv4/IPv6) applications. Always  
handle `socket.gaierror` when resolving hostnames, as DNS lookups can fail.  

 

## 3. UDP Sockets  
UDP sends independent messages (datagrams) with no connection, no ordering  
guarantee, and no delivery confirmation. It is ideal for broadcast, multicast,  
real‑time media, or protocols that implement their own reliability layer.  

### UDP client – Quote of the Day  
Many QOTD services listen on port 17. Send any datagram and you'll receive a  
quote.  
```python
#!/usr/bin/env python3
"""udp_qotd_client.py"""
import socket

server = ("djxmmx.net", 17)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"", server)               # trigger a response
    data, addr = s.recvfrom(1024)
    print(f"From {addr}:\n{data.decode()}")
```

The `sendto` method transmits a datagram to a specific address without  
establishing a connection. `recvfrom` returns both the data and the sender's  
address, which is useful when communicating with multiple peers. Note that UDP  
is unreliable: the request or response may be lost, so production code should  
implement retries and timeouts.  

### UDP echo server and client  
To make the example fully self‑contained, let's write both sides.  
```python
#!/usr/bin/env python3
"""udp_echo_server.py"""
import socket

HOST = '127.0.0.1'
PORT = 7000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP echo server listening on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        print(f"Received from {addr}: {data}")
        s.sendto(data, addr)            # echo back
```
```python
#!/usr/bin/env python3
"""udp_echo_client.py"""
import socket

server = ('127.0.0.1', 7000)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    msg = b'Hello UDP!'
    s.sendto(msg, server)
    data, _ = s.recvfrom(1024)
    print(f"Server replied: {data.decode()}")
```

Unlike TCP, a UDP server does not call `listen` or `accept`. It simply binds  
to a port and receives datagrams from any sender. Each `recvfrom` call returns  
the sender's address, allowing the server to reply directly. Because UDP is  
connectionless, the server can handle many clients without threads, but it  
must be careful not to block indefinitely on `recvfrom` if a client disappears.  

### UDP broadcasting  
Sending to `<broadcast>` or `255.255.255.255` delivers the datagram to all  
devices on the local network. You must enable broadcasting with `SO_BROADCAST`.  
```python
#!/usr/bin/env python3
"""broadcast_sender.py"""
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(b"Hello everyone!", ('255.255.255.255', 5000))
    print("Broadcast sent")
```
**Receiver:**  
```python
#!/usr/bin/env python3
"""broadcast_receiver.py"""
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 5000))
    while True:
        data, addr = s.recvfrom(1024)
        print(f"From {addr}: {data.decode()}")
```

Broadcasting is useful for service discovery or sending announcements to all  
hosts on a subnet. The `SO_REUSEADDR` option allows multiple receivers to bind  
to the same port, which is necessary for broadcast listeners. Be aware that  
broadcast traffic is often filtered by routers and may not cross subnet  
boundaries.  

### UDP multicast  
Multicast sends datagrams to a group of hosts (class D address  
224.0.0.0–239.255.255.255). The receiver joins the group.  
```python
#!/usr/bin/env python3
"""multicast_sender.py"""
import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # TTL: how many routers the packet can traverse
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    s.sendto(b"Multicast message", (MCAST_GRP, MCAST_PORT))
    print("Multicast sent")
```
```python
#!/usr/bin/env python3
"""multicast_receiver.py"""
import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', MCAST_PORT))
    # Tell the kernel we want to join this multicast group
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        data, addr = s.recvfrom(1024)
        print(f"From {addr}: {data.decode()}")
```

Multicast is efficient for one‑to‑many communication like live video or stock  
ticks. The sender sets `IP_MULTICAST_TTL` to control how far the packet  
travels (1 = local network, higher = through routers). Receivers join the  
group using `IP_ADD_MEMBERSHIP`; the kernel then delivers matching packets.  
Multicast requires network infrastructure support and is often disabled on  
public networks.  

 

## 4. TCP Sockets  
TCP provides a reliable, ordered byte stream. A typical flow is: server  
`bind` → `listen` → `accept` → `send`/`recv`; client `connect` → `send`/`recv`.  
TCP handles retransmission, flow control, and congestion avoidance, making it  
the default choice for most application protocols.  

### Simple time server and client  
Instead of relying on an external time server, we'll implement our own.  
```python
#!/usr/bin/env python3
"""tcp_time_server.py"""
import socket
import time

HOST = '127.0.0.1'
PORT = 8013

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Time server listening on port {PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        now = time.ctime() + "\n"
        conn.sendall(now.encode())
```
```python
#!/usr/bin/env python3
"""tcp_time_client.py"""
import socket

server = ('127.0.0.1', 8013)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server)
    data = b''
    while True:
        chunk = s.recv(1024)
        if not chunk:
            break
        data += chunk
    print(f"Server time: {data.decode().strip()}")
```

This example illustrates the classic TCP server pattern: bind, listen, accept,  
then communicate over the returned connection socket. The client connects and  
reads until the server closes the connection (indicated by `recv` returning  
empty bytes). Note that `recv` may return fewer bytes than requested; looping  
until the connection closes ensures we receive the complete message.  

### HTTP HEAD and GET requests using raw sockets  
```python
#!/usr/bin/env python3
"""http_head.py"""
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("webcode.me", 80))
    request = (
        "HEAD / HTTP/1.1\r\n"
        "Host: webcode.me\r\n"
        "Accept: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    s.sendall(request.encode())
    response = b''
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk
    print(response.decode())
```
```python
#!/usr/bin/env python3
"""http_get.py"""
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("webcode.me", 80))
    request = (
        "GET / HTTP/1.1\r\n"
        "Host: webcode.me\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    s.sendall(request.encode())

    response = b''
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

    # Separate headers and body
    header, _, body = response.partition(b"\r\n\r\n")
    print(header.decode())
    print("body )
    print(body.decode())
```

These examples show how HTTP is just text over TCP. The `Host` header is  
required by HTTP/1.1 for virtual hosting. Setting `Connection: close` tells the  
server to close the connection after the response, simplifying client logic.  
Parsing HTTP properly requires handling chunked encoding, compression, and  
other features; for production use, prefer libraries like `requests` or  
`http.client`.  

### Echo client & server (single client)  
```python
#!/usr/bin/env python3
"""echo_server_single.py"""
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Echo server listening on {PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```
```python
#!/usr/bin/env python3
"""echo_client.py"""
import socket

server = ('127.0.0.1', 65432)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server)
    messages = [b'Hello', b'World', b'quit']
    for msg in messages:
        s.sendall(msg)
        data = s.recv(1024)
        print(f"Echo: {data.decode()}")
    s.shutdown(socket.SHUT_WR)   # signal we're done sending
```

The echo protocol is a common testing tool. The server loops on `recv` until  
the client closes its write end, indicated by `recv` returning empty bytes.  
The client uses `shutdown(SHUT_WR)` to signal completion without closing the  
socket immediately, allowing it to receive any final data. This half‑close  
pattern is useful for request‑response protocols.  

 

## 5. Handling Multiple Clients  
A real server must serve many clients simultaneously. Python offers several  
approaches, each with trade‑offs in complexity, performance, and scalability.  

### Multi‑threaded echo server  
```python
#!/usr/bin/env python3
"""echo_server_threads.py"""
import socket
import threading

def handle_client(conn, addr):
    print(f"[{addr}] connected")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    print(f"[{addr}] disconnected")

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Multi-threaded echo server on port {PORT}")
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.daemon = True
        t.start()
```
*Explanation:* Each client gets its own thread, so blocking `recv` doesn't  
stall others. For production you may prefer a thread pool.  

Threading is simple but has overhead: each thread consumes memory and context  
switches add CPU cost. Use `daemon=True` so threads don't prevent program  
exit. For better resource management, consider `concurrent.futures.ThreadPoolExecutor`  
to limit concurrent threads. Also, ensure handler functions are thread‑safe if  
they share state.  

### Using `selectors` for I/O multiplexing  
A single‑threaded alternative that scales well.  
```python
#!/usr/bin/env python3
"""echo_server_selectors.py"""
import socket
import selectors

sel = selectors.DefaultSelector()

def accept(sock):
    conn, addr = sock.accept()
    print(f"Accepted from {addr}")
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, data=b'')

def read(conn):
    data = conn.recv(1024)
    if data:
        # Echo back
        conn.sendall(data)
    else:
        print(f"Closing {conn.getpeername()}")
        sel.unregister(conn)
        conn.close()

HOST = '127.0.0.1'
PORT = 65434

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    s.setblocking(False)
    sel.register(s, selectors.EVENT_READ, data=None)
    print(f"Selector-based echo server on port {PORT}")

    while True:
        events = sel.select()
        for key, mask in events:
            if key.data is None:    # listening socket
                accept(key.fileobj)
            else:
                read(key.fileobj)
```

The `selectors` module provides a high‑level interface to `select`, `poll`, or  
`epoll`, depending on the platform. By setting sockets to non‑blocking mode  
and registering them with a selector, a single thread can manage thousands of  
connections. This pattern avoids thread overhead but requires careful state  
management, especially for partial sends. It is the foundation of many  
high‑performance servers.  

### Asyncio TCP echo server  
`asyncio` provides a higher‑level, coroutine‑based API.  
```python
#!/usr/bin/env python3
"""echo_server_asyncio.py"""
import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Accepted from {addr}")
    while True:
        data = await reader.read(1024)
        if not data:
            break
        writer.write(data)
        await writer.drain()
    print(f"Closing {addr}")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 65435)
    addr = server.sockets[0].getsockname()
    print(f"Asyncio echo server on {addr}")
    async with server:
        await server.serve_forever()

asyncio.run(main())
```

`asyncio` combines the scalability of I/O multiplexing with a more intuitive  
programming model. Coroutines suspend at `await` points, allowing other tasks  
to run. The `StreamReader`/`StreamWriter` API simplifies reading and writing.  
This approach is ideal for I/O‑bound applications with many concurrent  
connections, such as chat servers or API gateways.  

### Simple chat server  
A chat server broadcasts messages from one client to all others.  
```python
#!/usr/bin/env python3
"""chat_server.py"""
import socket
import threading

clients = []

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.sendall(message)
            except:
                clients.remove(client)

def handle_client(conn, addr):
    name = f"{addr[0]}:{addr[1]}"
    clients.append(conn)
    print(f"{name} joined. Total clients: {len(clients)}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            broadcast(f"{name}: ".encode() + data, conn)
    finally:
        clients.remove(conn)
        conn.close()
        print(f"{name} left")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 5000))
    s.listen()
    print("Chat server started on port 5000")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
```
**Chat client** (simple version):  
```python
#!/usr/bin/env python3
"""chat_client.py"""
import socket
import threading

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Disconnected from server.")
                break
            print(data.decode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 5000))
    print("Connected to chat. Type your messages:")
    recv_thread = threading.Thread(target=receive_messages, args=(s,), daemon=True)
    recv_thread.start()
    while True:
        msg = input()
        if msg.lower() == 'quit':
            break
        s.sendall(msg.encode())
```

This chat server maintains a global list of client connections and broadcasts  
each message to all others. The `broadcast` function catches send errors to  
handle disconnected clients gracefully. Note that the global `clients` list is  
accessed from multiple threads without locking; for production, use a `threading.Lock`  
or switch to `asyncio` to avoid race conditions. The client uses a separate  
thread for receiving so that input and output can happen concurrently.  

 

## 6. Socket Options and Configuration  
You can fine‑tune sockets with `setsockopt`. Common options:  

* `SO_REUSEADDR` – Allow reuse of local addresses (essential for quick server  
  restart).  
```python
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```
* `SO_KEEPALIVE` – Enable TCP keep‑alive packets.  
```python
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
```
* `TCP_NODELAY` – Disable Nagle's algorithm (small packets sent immediately).  
```python
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
```
* Timeout – set a timeout on blocking operations (seconds).  
```python
s.settimeout(5.0)       # raise socket.timeout after 5s
```
* Non‑blocking mode – `recv`/`send` return immediately, may raise  
  `BlockingIOError`.  
```python
s.setblocking(False)
```

`SO_REUSEADDR` prevents "Address already in use" errors when restarting a  
server quickly. `SO_KEEPALIVE` helps detect dead peers but may not fire for  
minutes; application‑level heartbeats are more responsive. `TCP_NODELAY`  
reduces latency for interactive protocols but can increase packet count.  
Timeouts prevent indefinite blocking; combine with retry logic for resilience.  
Non‑blocking mode is required for `select`/`poll`/`epoll`‑based servers.  

 

## 7. Handling Large Data Transfers  
`send()` may not send all data; `recv()` may not read the full message. Always  
loop until completion.  

### Reliable `sendall` (built‑in)  
```python
s.sendall(large_data)   # loops internally until all data is sent
```

### Custom `recv_all` to read exactly N bytes  
```python
def recv_all(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            raise ConnectionError("Connection closed prematurely")
        data.extend(packet)
    return bytes(data)
```

### File transfer example (client sends a file, server receives it)  
**Server:**  
```python
#!/usr/bin/env python3
"""file_receiver.py"""
import socket

HOST = '0.0.0.0'
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print("Waiting for file...")
    conn, addr = s.accept()
    with conn, open('received_file.txt', 'wb') as f:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
    print(f"File received from {addr}")
```
**Client:**  
```python
#!/usr/bin/env python3
"""file_sender.py"""
import socket

server = ('127.0.0.1', 9001)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server)
    with open('sample.txt', 'rb') as f:
        while chunk := f.read(4096):
            s.sendall(chunk)
    s.shutdown(socket.SHUT_WR)   # signal we're done
    print("File sent")
```

For large transfers, consider adding a protocol layer: send the file size  
first, then the content, so the receiver knows when to stop. You might also  
add checksums for integrity verification. The `shutdown` call ensures the  
server sees EOF and closes its read end cleanly. For very large files,  
implement progress reporting or chunked acknowledgments.  

 

## 8. Unix Domain Sockets  
For inter‑process communication on the same machine, use `AF_UNIX` with a  
filesystem path.  
```python
#!/usr/bin/env python3
"""unix_echo_server.py"""
import socket
import os

SOCKET_PATH = '/tmp/echo_unix.sock'

if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.bind(SOCKET_PATH)
    s.listen()
    print(f"Unix socket server at {SOCKET_PATH}")
    conn, _ = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```
```python
#!/usr/bin/env python3
"""unix_echo_client.py"""
import socket

SOCKET_PATH = '/tmp/echo_unix.sock'

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.connect(SOCKET_PATH)
    s.sendall(b'Hello via Unix socket!')
    data = s.recv(1024)
    print(f"Reply: {data.decode()}")
```

Unix domain sockets avoid network overhead and support file‑descriptor  
passing, making them ideal for local IPC. They are addressed by filesystem  
paths, so permissions control access. Always clean up stale socket files on  
startup. For abstract sockets (Linux‑specific, not filesystem‑visible), prefix  
the path with a null byte.  

 

## 9. Secure Sockets with SSL/TLS  
Python's `ssl` module wraps a socket to provide encryption. Use  
`ssl.create_default_context()` for a secure context.  

**SSL echo server:**  
```python
#!/usr/bin/env python3
"""ssl_echo_server.py"""
import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"SSL echo server on port {PORT}")

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    with context.wrap_socket(s, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(f"Secure connection from {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
```
*Generate a self‑signed certificate for testing:*  
```bash
openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
```

**SSL client:**  
```python
#!/usr/bin/env python3
"""ssl_echo_client.py"""
import socket
import ssl

server = ('127.0.0.1', 8443)

context = ssl.create_default_context()
# For self‑signed certificates disable hostname check and verification
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection(server) as sock:
    with context.wrap_socket(sock, server_hostname='localhost') as ssock:
        ssock.sendall(b'Secure hello!')
        data = ssock.recv(1024)
        print(f"Secure reply: {data.decode()}")
```

TLS provides confidentiality, integrity, and authentication. Always verify  
certificates in production (`CERT_REQUIRED`) and check hostnames. The  
`wrap_socket` method upgrades a plain socket to TLS; for servers, set  
`server_side=True`. Use `create_default_context` to get secure defaults  
(including protocol version and cipher selection). Never disable verification  
outside of testing.  

 

## 10. Error Handling and Robustness  
Network programming is prone to timeouts, refused connections, and abrupt  
disconnects. Always handle exceptions.  

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.settimeout(2)
    s.connect(('10.255.255.1', 80))
except socket.timeout:
    print("Connection timed out")
except ConnectionRefusedError:
    print("Server refused connection")
except OSError as e:
    print(f"Socket error: {e}")
finally:
    s.close()
```

Be mindful of partial closes. Use `shutdown(socket.SHUT_RDWR)` to gracefully  
close one or both ends, then `close()`.  

Network errors are transient; implement exponential backoff for retries.  
Log errors with context (peer address, operation) for debugging. Use  
`socket.error` (alias of `OSError`) as a catch‑all for socket‑specific issues.  
Always close sockets in `finally` blocks or use context managers to prevent  
resource leaks.  

 

## 11. Practical Utilities  
### TCP port scanner  
```python
#!/usr/bin/env python3
"""simple_port_scanner.py"""
import socket

target = '127.0.0.1'
ports_to_scan = [22, 80, 443, 8000, 65432]

for port in ports_to_scan:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
```
`connect_ex()` returns an error code instead of raising an exception – perfect  
for scanning.  

### Minimal HTTP server  
Return a simple HTML page over raw TCP.  
```python
#!/usr/bin/env python3
"""simple_http_server.py"""
import socket

HOST, PORT = '127.0.0.1', 8080

response_body = "<html><body><h1>It works!</h1></body></html>"
response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    f"Content-Length: {len(response_body)}\r\n"
    "Connection: close\r\n"
    "\r\n"
    f"{response_body}"
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Serving HTTP on port {PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024)
            print(f"Request from {addr}: {request.splitlines()[0]}")
            conn.sendall(response.encode())
```

These utilities demonstrate how sockets underpin common network tools. The  
port scanner uses `connect_ex` to avoid exception overhead. The HTTP server  
shows the minimal protocol handshake; real servers must handle methods,  
headers, and persistent connections.  



### Simple HTTP Proxy Server  

A proxy forwards HTTP requests from clients to upstream servers, useful for  
caching, filtering, or logging.  

```python
#!/usr/bin/env python3
"""simple_http_proxy.py"""
import socket
import threading

UPSTREAM = ('webcode.me', 80)
PROXY_PORT = 8888

def forward(source, destination):
    """Forward data from source to destination socket."""
    try:
        while True:
            data = source.recv(4096)
            if not data:
                break
            destination.sendall(data)
    finally:
        source.close()
        destination.close()

def handle_client(client_sock, client_addr):
    print(f"Proxy request from {client_addr}")
    upstream = socket.create_connection(UPSTREAM)
    # Start two threads: client->upstream and upstream->client
    t1 = threading.Thread(target=forward, args=(client_sock, upstream))
    t2 = threading.Thread(target=forward, args=(upstream, client_sock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy:
    proxy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    proxy.bind(('127.0.0.1', PROXY_PORT))
    proxy.listen(5)
    print(f"HTTP proxy listening on port {PROXY_PORT}")
    while True:
        client, addr = proxy.accept()
        threading.Thread(target=handle_client, args=(client, addr), daemon=True).start()
```

This proxy creates two forwarding threads per connection, enabling full‑duplex  
communication. For production, add request parsing to support multiple  
requests per connection (HTTP keep‑alive) and implement timeouts to prevent  
resource exhaustion. You could also add logging, caching, or header  
modification.  

### Heartbeat Monitoring Client  

A client that sends periodic heartbeats to detect server liveness.  

```python
#!/usr/bin/env python3
"""heartbeat_client.py"""
import socket
import time
import threading

SERVER = ('127.0.0.1', 9999)
HEARTBEAT_INTERVAL = 5  # seconds

def heartbeat_loop(sock):
    while True:
        try:
            sock.sendall(b'PING\n')
            response = sock.recv(16)
            if response.strip() != b'PONG':
                print("Invalid heartbeat response")
                break
            print(f"Heartbeat OK at {time.ctime()}")
            time.sleep(HEARTBEAT_INTERVAL)
        except (socket.timeout, ConnectionError) as e:
            print(f"Heartbeat failed: {e}")
            break

with socket.create_connection(SERVER, timeout=10) as s:
    s.settimeout(10)
    print(f"Connected to {SERVER}, starting heartbeat monitor")
    heartbeat_loop(s)
    print("Monitoring stopped")
```

Heartbeats help detect silent failures (e.g., network partitions). The client  
sends `PING` and expects `PONG`; any deviation triggers reconnection logic.  
For robustness, implement exponential backoff on failure and limit retry  
attempts. Servers should respond to heartbeats without blocking other  
operations.  

### Simple RPC over Sockets  

Remote Procedure Call lets you invoke functions on a remote server.  
```python
#!/usr/bin/env python3
"""simple_rpc.py"""
import socket
import json
import threading

# Server side
def rpc_server(host, port):
    def add(a, b): return a + b
    def multiply(a, b): return a * b
    functions = {'add': add, 'multiply': multiply}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"RPC server on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                request = conn.recv(4096).decode()
                req = json.loads(request)
                func_name = req['func']
                args = req['args']
                result = functions[func_name](*args)
                response = json.dumps({'result': result}).encode()
                conn.sendall(response)

# Client side
def rpc_call(host, port, func_name, *args):
    with socket.create_connection((host, port)) as s:
        request = json.dumps({'func': func_name, 'args': args}).encode()
        s.sendall(request)
        response = s.recv(4096).decode()
        return json.loads(response)['result']

# Example usage (run server in one terminal, client in another):
# Server: rpc_server('127.0.0.1', 12345)
# Client: rpc_call('127.0.0.1', 12345, 'add', 3, 4)  # returns 7
```

This minimal RPC uses JSON for serialization and a simple request/response  
pattern. For production, add authentication, error handling, timeouts, and  
support for asynchronous calls. Consider using established RPC frameworks like  
gRPC or Apache Thrift for complex applications.  

###  Service Discovery via UDP Broadcast  
Services announce themselves on the local network; clients discover them.  

```python
#!/usr/bin/env python3
"""service_discovery.py"""
import socket
import json
import threading
import time

SERVICE_NAME = "my_app"
SERVICE_PORT = 5000
DISCOVERY_PORT = 5001
BROADCAST_ADDR = ('255.255.255.255', DISCOVERY_PORT)

def service_announcer():
    """Server side: periodically broadcast service availability."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        announcement = json.dumps({
            'name': SERVICE_NAME,
            'host': socket.gethostbyname(socket.gethostname()),
            'port': SERVICE_PORT
        }).encode()
        while True:
            s.sendto(announcement, BROADCAST_ADDR)
            print(f"Announced {SERVICE_NAME}")
            time.sleep(10)

def service_discoverer(timeout=5):
    """Client side: listen for announcements and return first match."""
    services = []
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', DISCOVERY_PORT))
        s.settimeout(timeout)
        try:
            while True:
                data, addr = s.recvfrom(1024)
                info = json.loads(data.decode())
                if info['name'] == SERVICE_NAME:
                    services.append(info)
                    print(f"Discovered: {info}")
        except socket.timeout:
            pass
    return services

# Run announcer in a thread: threading.Thread(target=service_announcer, daemon=True).start()
# Then call service_discoverer() from client code
```

Service discovery enables dynamic configuration in distributed systems. The  
announcer broadcasts its address; discoverers listen and collect responses.  
Add TTL fields to announcements so stale entries expire, and implement  
deduplication to handle multiple announcements from the same service. For  
larger systems, consider DNS‑SD or Consul.  

## Final Thoughts  

Socket programming is a foundational skill for network developers. While  
high‑level frameworks abstract away many details, understanding the underlying  
mechanisms helps you debug issues, optimize performance, and design robust  
protocols. Start with simple examples, then gradually incorporate concurrency,  
security, and error handling. Always test with real network conditions:  
latency, packet loss, and partial failures reveal bugs that localhost testing  
misses.  

Remember: security first. Validate all input, use TLS for sensitive data, and  
never trust client‑provided paths or headers. With these principles and the  
examples in this tutorial, you are ready to build reliable networked  
applications in Python.  

# Python Socket Programming – Supplementary Examples

These five examples cover patterns **not demonstrated** in the main tutorial.
Each is self-contained, fully runnable, and addresses a real-world problem.


## 1. Length-Prefixed Message Framing

### The problem the tutorial skipped

The tutorial's echo server and client work fine for short messages, but TCP is a
**byte stream**, not a message protocol. If you call `sendall(b"Hello")` followed
by `sendall(b"World")`, the receiver might get `b"HelloWorld"` in one `recv`, or
`b"Hel"` and `b"loWorld"` across two — there are no boundaries.

The standard fix is a **length prefix**: send a fixed-size header containing the
payload length, then the payload. The receiver reads the header first, learns
exactly how many bytes to expect, then reads that many.

### Shared framing helpers

```python
# framing.py  –  import this in both server and client
import struct

HEADER_FORMAT = '>I'          # big-endian unsigned 32-bit int
HEADER_SIZE   = struct.calcsize(HEADER_FORMAT)   # 4 bytes

def send_msg(sock, data: bytes) -> None:
    """Prefix data with a 4-byte length header and send atomically."""
    header = struct.pack(HEADER_FORMAT, len(data))
    sock.sendall(header + data)

def recv_msg(sock) -> bytes:
    """Read a length-prefixed message; raise ConnectionError on EOF."""
    raw_len = _recv_exactly(sock, HEADER_SIZE)
    msg_len = struct.unpack(HEADER_FORMAT, raw_len)[0]
    return _recv_exactly(sock, msg_len)

def _recv_exactly(sock, n: int) -> bytes:
    """Read exactly n bytes from sock, looping as needed."""
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("Connection closed before full message received")
        buf.extend(chunk)
    return bytes(buf)
```

### Framing server

```python
#!/usr/bin/env python3
# framing_server.py
import socket
from framing import recv_msg, send_msg

HOST, PORT = '127.0.0.1', 7100

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen()
    print(f"Framing server on {PORT}")

    conn, addr = srv.accept()
    with conn:
        print(f"Client connected: {addr}")
        while True:
            try:
                msg = recv_msg(conn)
            except ConnectionError:
                break
            print(f"Received ({len(msg)} bytes): {msg.decode()}")
            send_msg(conn, b"ACK: " + msg)   # echo with prefix

    print("Client disconnected")
```

### Framing client

```python
#!/usr/bin/env python3
# framing_client.py
import socket
from framing import recv_msg, send_msg

server = ('127.0.0.1', 7100)
messages = [b"Short", b"A" * 500, b"Last message"]   # mix of sizes

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server)
    for msg in messages:
        send_msg(s, msg)
        reply = recv_msg(s)
        print(f"Server replied: {reply.decode()}")
```

**Why this matters:** Without framing, every protocol you build on top of TCP is
broken for large or bursty messages. The 4-byte `'>I'` header supports payloads
up to ~4 GB. For smaller messages, `'>H'` (2 bytes, up to 65 535 bytes) reduces
overhead. The `_recv_exactly` helper is the same pattern as the tutorial's
`recv_all`, but used to read the header *and* the body — two separate calls with
two known sizes.


## 2. IPv6 Dual-Stack Server

### The problem the tutorial skipped

The tutorial's address-family table lists `AF_INET6` but every example uses
`AF_INET`. Modern deployments increasingly need IPv6, and on Linux/macOS a
single IPv6 socket can accept both IPv4 and IPv6 clients via *dual-stack* mode.

The key option is `IPV6_V6ONLY`. When set to `0`, an `AF_INET6` socket also
accepts IPv4 connections; IPv4 client addresses arrive mapped as
`::ffff:192.168.1.1`. When set to `1` (the default on some systems), only IPv6
clients are accepted.

### Dual-stack echo server

```python
#!/usr/bin/env python3
# ipv6_echo_server.py
import socket

HOST = '::'    # listen on all IPv6 interfaces (and IPv4 via mapping)
PORT = 7200

with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as srv:
    srv.setsockopt(socket.SOL_SOCKET,   socket.SO_REUSEADDR, 1)
    # Allow both IPv4 and IPv6 clients on the same socket:
    srv.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY,  0)

    srv.bind((HOST, PORT, 0, 0))   # (host, port, flowinfo, scope_id)
    srv.listen()
    print(f"Dual-stack server on port {PORT} – accepts IPv4 and IPv6")

    while True:
        conn, addr = srv.accept()
        # addr is a 4-tuple for IPv6: (host, port, flowinfo, scope_id)
        print(f"Connection from: {addr[0]}  port {addr[1]}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
```

### IPv4 client connecting to the dual-stack server

```python
#!/usr/bin/env python3
# ipv4_client_to_v6_server.py
import socket

# Connect using IPv4 – the dual-stack server accepts this transparently
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 7200))
    s.sendall(b'Hello from IPv4!')
    print(s.recv(1024).decode())
```

### Pure IPv6 client

```python
#!/usr/bin/env python3
# ipv6_client.py
import socket

# getaddrinfo handles IPv6 address formatting correctly
for res in socket.getaddrinfo('::1', 7200, socket.AF_INET6,
                               socket.SOCK_STREAM):
    af, stype, proto, _, addr = res
    with socket.socket(af, stype, proto) as s:
        s.connect(addr)
        s.sendall(b'Hello from IPv6!')
        print(s.recv(1024).decode())
    break
```

**Why this matters:** A pure `AF_INET` server is blind to IPv6 clients. A pure
`AF_INET6` server with `IPV6_V6ONLY=1` is blind to IPv4 clients. Setting
`IPV6_V6ONLY=0` gives you one listening socket that handles both, which
simplifies deployment. Note that Windows disables dual-stack by default at the
OS level; check your platform's documentation when portability matters.


## `socketpair()` for Subprocess IPC

### The problem the tutorial skipped

The tutorial covers Unix domain sockets for local IPC, but they require a
filesystem path and two separate `bind`/`connect` calls. For **parent–child
process communication**, Python's `socket.socketpair()` creates a connected pair
of sockets in one call — no path, no bind, no accept. It is the socket
equivalent of `os.pipe()` but fully bidirectional.

```python
#!/usr/bin/env python3
# socketpair_ipc.py
import os
import socket

def child_process(sock):
    """Child: receive a task, do work, send result."""
    with sock:
        raw = sock.recv(256)
        numbers = list(map(int, raw.decode().split(',')))
        total = sum(numbers)
        sock.sendall(f"sum={total}".encode())
        print(f"[child pid={os.getpid()}] computed sum={total}")

def parent_process(sock, child_pid):
    """Parent: send a task, wait for result."""
    with sock:
        task = ','.join(str(n) for n in range(1, 11))   # "1,2,...,10"
        print(f"[parent pid={os.getpid()}] sending task: {task}")
        sock.sendall(task.encode())

        # Signal no more data so child's recv returns EOF after the reply
        sock.shutdown(socket.SHUT_WR)

        result = sock.recv(256).decode()
        print(f"[parent] result from child: {result}")

    os.waitpid(child_pid, 0)   # reap the child
    print("[parent] child finished")

# Create the connected pair BEFORE forking so both sides exist
parent_sock, child_sock = socket.socketpair(socket.AF_UNIX,
                                             socket.SOCK_STREAM)

pid = os.fork()        # Unix/macOS only; see note below for Windows

if pid == 0:           # child     parent_sock.close()          # child doesn't use the parent's end
    child_process(child_sock)
    os._exit(0)
else:                  # parent     child_sock.close()           # parent doesn't use the child's end
    parent_process(parent_sock, pid)
```

**Windows note:** `os.fork()` is unavailable on Windows. Use
`multiprocessing.Process` with `multiprocessing.reduction.ForkingPickler` to
pass a socket to a child process, or use `subprocess` with a socket inherited
via `handle_inheritance`.

**Why this matters:** `socketpair()` gives you a bidirectional channel between
related processes with zero setup overhead. It's useful for worker pools where
the parent dispatches tasks and collects results, or for test harnesses that need
a controlled, in-process "network" without binding to any port. Because both ends
are already connected, you can use `shutdown(SHUT_WR)` on either side to signal
EOF without closing the socket.


## Struct-Based Binary Protocol

### The problem the tutorial skipped

The RPC example in section 13.3 uses JSON — human-readable but verbose. Many
real protocols (DNS, MQTT, game engines, financial feeds) use compact **binary
wire formats** with fixed-size headers. Python's `struct` module lets you pack
and unpack integers, floats, and fixed-length strings directly into bytes with no
parsing overhead.

This example defines a minimal sensor-telemetry protocol:

```
Offset  Size  Type      Field
   -  -
0       1     uint8     version  (must be 1)
1       1     uint8     sensor_id
2       4     float32   temperature  (Celsius)
6       4     float32   humidity     (percent)
10      2     uint16    sequence_number
12      4     uint32    unix_timestamp
```

Total: **16 bytes per message**, compared to ~80 bytes for equivalent JSON.

### Shared protocol definition

```python
# telemetry_proto.py
import struct
import time

# Big-endian: version(B) sensor_id(B) temp(f) humidity(f) seq(H) ts(I)
WIRE_FORMAT = '>BBffHI'
MSG_SIZE    = struct.calcsize(WIRE_FORMAT)   # 16 bytes
PROTOCOL_VERSION = 1

def encode(sensor_id: int, temperature: float,
           humidity: float, seq: int) -> bytes:
    return struct.pack(
        WIRE_FORMAT,
        PROTOCOL_VERSION,
        sensor_id,
        temperature,
        humidity,
        seq,
        int(time.time()),
    )

def decode(raw: bytes) -> dict:
    if len(raw) != MSG_SIZE:
        raise ValueError(f"Expected {MSG_SIZE} bytes, got {len(raw)}")
    ver, sensor_id, temp, humidity, seq, ts = struct.unpack(WIRE_FORMAT, raw)
    if ver != PROTOCOL_VERSION:
        raise ValueError(f"Unknown protocol version {ver}")
    return {
        'sensor_id':   sensor_id,
        'temperature': round(temp, 2),
        'humidity':    round(humidity, 2),
        'sequence':    seq,
        'timestamp':   ts,
    }
```

### Telemetry server (collects readings)

```python
#!/usr/bin/env python3
# telemetry_server.py
import socket
from telemetry_proto import decode, MSG_SIZE

HOST, PORT = '127.0.0.1', 7300

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen()
    print(f"Telemetry server on {PORT}, expecting {MSG_SIZE}-byte messages")

    conn, addr = srv.accept()
    with conn:
        buf = bytearray()
        while True:
            chunk = conn.recv(64)
            if not chunk:
                break
            buf.extend(chunk)
            # Process every complete message that has arrived
            while len(buf) >= MSG_SIZE:
                reading = decode(bytes(buf[:MSG_SIZE]))
                del buf[:MSG_SIZE]
                print(f"  sensor={reading['sensor_id']:02d}  "
                      f"temp={reading['temperature']:6.2f}°C  "
                      f"humidity={reading['humidity']:5.1f}%  "
                      f"seq={reading['sequence']}")
```

### Telemetry client (sends readings)

```python
#!/usr/bin/env python3
# telemetry_client.py
import socket
import time
import random
from telemetry_proto import encode

server = ('127.0.0.1', 7300)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server)
    for seq in range(10):
        temp     = 20.0 + random.uniform(-5, 15)
        humidity = 50.0 + random.uniform(-20, 20)
        msg = encode(sensor_id=3, temperature=temp,
                     humidity=humidity, seq=seq)
        s.sendall(msg)
        print(f"Sent seq={seq}  temp={temp:.2f}  humidity={humidity:.2f}")
        time.sleep(0.2)

print("Done")
```

**Why this matters:** Binary protocols are orders of magnitude smaller and faster  
to parse than text-based ones. The key subtleties are: (1) always specify  
endianness (`>` for big-endian / network byte order, `<` for little-endian) so  
client and server agree regardless of CPU architecture; (2) the server buffers  
incoming bytes and slices out complete messages — this is the binary analogue of  
the length-prefix framing in Example 1, but the message size is fixed rather  
than dynamic; (3) `struct.calcsize` is the single source of truth for message  
size — never hardcode it.  


##  Raw ICMP Ping

### The problem the tutorial skipped

Everything in the main tutorial sits at the TCP or UDP layer (layer 4). Raw
sockets (`SOCK_RAW`) let you drop down to **layer 3** and craft packets
directly, including the ICMP protocol used by the `ping` utility.

> **Note:** Raw sockets require elevated privileges. On Linux run with `sudo`,
> or grant the capability: `sudo setcap cap_net_raw+ep python3`. On macOS, run
> with `sudo`. On Windows, raw sockets are restricted to administrators.

```python
#!/usr/bin/env python3
# raw_ping.py  –  requires root / administrator privileges
"""
Sends one ICMP Echo Request to a host and reports the round-trip time.
Implements RFC 792 manually using struct to build the ICMP header.
"""
import socket
import struct
import time
import os

# ICMP type codes
ICMP_ECHO_REQUEST = 8
ICMP_ECHO_REPLY   = 0

def checksum(data: bytes) -> int:
    """Standard Internet checksum (RFC 1071)."""
    if len(data) % 2:
        data += b'\x00'
    total = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        total += word
    total = (total >> 16) + (total & 0xFFFF)
    total += total >> 16
    return ~total & 0xFFFF

def build_icmp_packet(pid: int, seq: int) -> bytes:
    """Build an ICMP Echo Request packet."""
    # Header with checksum=0 first
    header = struct.pack('>BBHHH', ICMP_ECHO_REQUEST, 0, 0, pid, seq)
    payload = b'PythonRawPing!' + bytes(range(32 - 14))
    csum = checksum(header + payload)
    # Re-pack with the real checksum
    header = struct.pack('>BBHHH', ICMP_ECHO_REQUEST, 0, csum, pid, seq)
    return header + payload

def ping(host: str, timeout: float = 2.0) -> float | None:
    """
    Send one ICMP Echo Request; return round-trip time in ms, or None on timeout.
    """
    pid = os.getpid() & 0xFFFF
    seq = 1

    with socket.socket(socket.AF_INET, socket.SOCK_RAW,
                       socket.IPPROTO_ICMP) as s:
        s.settimeout(timeout)

        dest_ip = socket.gethostbyname(host)
        packet  = build_icmp_packet(pid, seq)

        t_send = time.perf_counter()
        s.sendto(packet, (dest_ip, 0))   # port is ignored for ICMP

        try:
            raw_reply, addr = s.recvfrom(1024)
        except socket.timeout:
            return None

        t_recv = time.perf_counter()

        # The raw reply includes the 20-byte IP header; skip it
        ip_header_len = (raw_reply[0] & 0x0F) * 4
        icmp_data     = raw_reply[ip_header_len:]

        icmp_type, icmp_code, _, rep_pid, rep_seq = struct.unpack(
            '>BBHHH', icmp_data[:8]
        )

        if icmp_type == ICMP_ECHO_REPLY and rep_pid == pid and rep_seq == seq:
            return (t_recv - t_send) * 1000   # ms

    return None

if __name__ == '__main__':
    target = '8.8.8.8'
    rtt = ping(target)
    if rtt is not None:
        print(f"Reply from {target}: time={rtt:.2f} ms")
    else:
        print(f"No reply from {target} (timeout)")
```

**How it works, step by step:**

1. **`SOCK_RAW` + `IPPROTO_ICMP`** — tells the kernel to hand you raw ICMP
   packets. You are responsible for constructing the ICMP header; the kernel
   still prepends the IP header on transmit and strips it on receive (mostly —
   `recvfrom` returns the full IP packet, so we skip the first 20 bytes).

2. **Checksum** — ICMP requires a 16-bit one's-complement checksum of the
   entire ICMP message. We pack the header with `checksum=0`, compute the
   checksum over the full packet, then re-pack with the real value.

3. **Process ID in the identifier field** — using `os.getpid() & 0xFFFF`
   prevents collisions when multiple ping processes run simultaneously, since
   each kernel-delivered ICMP reply is delivered to *all* raw sockets of the
   right type.

4. **IP header parsing** — the IP header length lives in the low nibble of the
   first byte (in 32-bit words). Multiplying by 4 gives the byte offset to the
   start of the ICMP message.

**Why this matters:** Raw sockets expose the layer beneath TCP/UDP. Beyond ping,
the same technique underlies traceroute (UDP packets with low TTL + listening for
ICMP Time Exceeded replies), custom protocol implementations, and network
security tools. Understanding how to manually build and parse headers demystifies
every protocol you use every day.


## Summary of Patterns

| # | Pattern | Key concept |
||
| 1 | Length-prefixed framing | Impose message boundaries on a TCP byte stream |
| 2 | IPv6 dual-stack server | One socket accepts both IPv4 and IPv6 clients |
| 3 | `socketpair()` IPC | Pre-connected socket pair for parent↔child communication |
| 4 | Struct binary protocol | Compact, fast, endian-safe wire formats with `struct` |
| 5 | Raw ICMP ping | Layer-3 access; manual packet construction and checksum |

## 12. Conclusion  

This tutorial covered the fundamentals of Python socket programming: creating  
TCP/UDP sockets, building clients and servers, handling multiple connections,  
using advanced features (broadcast, multicast, SSL), and writing robust  
network code. Sockets give you precise control over network communication. For  
many applications, higher‑level libraries (e.g., `http.server`, `requests`,  
`Twisted`, `asyncio` streams) are more convenient, but understanding the  
low‑level layer will make you a better network developer.  

All examples above are self‑contained and ready to run. Experiment, modify  
them, and build your own networked applications. Remember to test thoroughly,  
handle errors gracefully, and never expose development servers to untrusted  
networks.  



