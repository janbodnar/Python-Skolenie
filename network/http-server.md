# http.server — Build Simple HTTP Servers in Python

The `http.server` module is a built‑in Python library that lets you create HTTP
servers for development, testing, and small internal tools. It is lightweight,
requires no external dependencies, and comes with everything you need to serve
static files or build tiny custom APIs.

In this tutorial you'll learn:

- How to start a static file server in one line
- The architecture of the module (servers and handlers)
- Building custom endpoints that handle GET, POST, and other methods
- Parsing query parameters and serving JSON
- Handling file downloads, uploads, and large streaming responses
- Adding concurrency with threading
- Important security rules for safe development use

---

## 1. A tiny HTTP primer

HTTP (Hypertext Transfer Protocol) is a **request–response** protocol:

1. A client (browser, `curl`, another program) opens a TCP connection to a
   server.
2. The client sends a request containing a **method** (like `GET` or `POST`), a
   **path** (like `/users/42`), optional **headers**, and an optional **body**.
3. The server replies with a **status code** (e.g. `200 OK`), **response
   headers**, and an optional **body**.

The `http.server` module lets you catch those requests in Python and craft the
response yourself.

---

## 2. Quick‑start: serve a directory of files

Python ships with a ready‑made file server. Open a terminal:

```bash
python -m http.server 8000
```

Now open `http://localhost:8000` in your browser. You'll see a directory
listing and can browse files.  
By default the server binds to all interfaces (`0.0.0.0`). To bind only to
localhost, use:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

The command‑line server is perfect for sharing files on a local network or
doing quick front‑end work.

---

## 3. Core classes

The module is built around two main concepts:

- **`http.server.HTTPServer`**  
  A basic HTTP server that listens on a TCP socket and hands incoming
  connections to a *request handler*.

- **`http.server.BaseHTTPRequestHandler`**  
  The base class for handling HTTP requests. You subclass it and override one
  or more `do_<METHOD>` methods.

There is also a ready‑made subclass:

- **`http.server.SimpleHTTPRequestHandler`**  
  Serves files from the current directory (or another directory passed to the
  constructor). The command‑line server uses it internally.

### Inside a request handler

When a request arrives, Python creates an instance of your handler class and
gives you these attributes:

| Attribute     | Description                                                    |
|---------------|----------------------------------------------------------------|
| `self.command`| The request method as a string: `'GET'`, `'POST'`, …           |
| `self.path`   | The request path, including any query string: `/search?q=py`   |
| `self.headers`| An `http.client.HTTPMessage` dictionary of request headers     |
| `self.rfile`  | An input stream from which you can **read** the request body   |
| `self.wfile`  | An output stream to which you **write** the response body      |

Those two streams behave like binary files (`read()` / `write()`).

---

## 4. Building custom handlers

### 4.1 The simplest GET handler

Override `do_GET` and write a response using these steps:

1. Call `self.send_response(status_code)`
2. (optional) Set headers with `self.send_header(key, value)`
3. Call `self.end_headers()`
4. Write the body to `self.wfile`

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

> **Note:** The body **must** be bytes. Use `.encode()` if you have a string.

### 4.2 Routing: different paths, different answers

You can branch on `self.path` to create several endpoints:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"<h1>Home</h1>")
        elif self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

### 4.3 Parsing query parameters

The path may contain a query string after `?`. Use `urllib.parse`:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/greet":
            params = parse_qs(parsed.query)
            name = params.get("name", ["World"])[0]
            body = f"Hello, {name}!".encode()

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

Calling `http://localhost:8000/greet?name=Ada` will return `Hello, Ada!`.

### 4.4 Returning JSON

Return structured data by serialising objects with `json.dumps`:

```python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/items":
            data = [
                {"id": 1, "name": "apple"},
                {"id": 2, "name": "banana"},
            ]
            body = json.dumps(data).encode()   # convert to bytes

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

Remember to set `Content-Type` to `application/json` so clients know how to
interpret the response.

### 4.5 Serving a file download (CSV example)

Let's improve the original snippet with proper error handling and security.

```python
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

CSV_PATH = "data.csv"

class DownloadHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/download":
            self.send_response(404)
            self.end_headers()
            return

        # Protect against path traversal (../../etc/passwd)
        safe_path = os.path.abspath(CSV_PATH)
        if not safe_path.startswith(os.getcwd()):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Forbidden")
            return

        try:
            with open(safe_path, "rb") as f:
                data = f.read()
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/csv")
        self.send_header("Content-Disposition", "attachment; filename=data.csv")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

HTTPServer(("0.0.0.0", 8000), DownloadHandler).serve_forever()
```

Key improvements:

- We **check that the resolved path is inside the intended directory** to
  prevent directory traversal attacks.
- We handle missing files with a 404.
- We set `Content-Length` — good practice for downloads.

### 4.6 Handling POST requests

Read the request body from `self.rfile`. You must use the `Content-Length`
header to know how many bytes to read:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        # Do something with the body (echo it back in this case)
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"You sent: " + body)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Send a POST request to see the echo.")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

**Parsing form data** (application/x-www-form-urlencoded):

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        cl = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(cl).decode()
        data = parse_qs(raw)  # returns a dict of lists
        name = data.get("username", ["anonymous"])[0]

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(f"Hello, {name}".encode())

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Submit a form with username field.")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

**Receiving JSON:**

```python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        raw = self.rfile.read(content_length)
        payload = json.loads(raw)                # a Python dict

        response = {"received": payload}
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Send a JSON payload via POST.")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

### 4.7 Other HTTP methods (PUT, DELETE, PATCH)

The pattern is identical — override the corresponding `do_` method:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"PUT received")

    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"DELETE received")

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Try PUT or DELETE methods.")

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

---

## 5. Advanced topics

### 5.1 Directory browsing

`SimpleHTTPRequestHandler` automatically creates an HTML directory listing for
paths that end with `/`. You can customise the directory from which files are
served:

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir("/path/to/serve")
HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler).serve_forever()
```

If you need a programmatic directory listing in your own handler, you can
build one by listing files with `os.listdir` and returning an HTML page.

### 5.2 Streaming large files

Reading a huge file into memory with `.read()` can exhaust RAM. Instead, read
and write in chunks:

```python
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/bigfile":
            filepath = "large_video.mp4"
            try:
                with open(filepath, "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/octet-stream")
                    self.send_header("Content-Length", str(os.path.getsize(filepath)))
                    self.end_headers()
                    while chunk := f.read(64 * 1024):   # 64 KB chunks
                        self.wfile.write(chunk)
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"File not found")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Only /bigfile is available.")

server = HTTPServer(("0.0.0.0", 8000), MyHandler)
server.serve_forever()
```

Because the response is written incrementally, the server remains responsive
even when many clients are downloading large files.

### 5.3 Handling multipart file uploads

Multipart form data (`<form enctype="multipart/form-data">`) is more complex
because the body contains multiple parts separated by a boundary string. The
standard library offers tools to parse it.

Using the `email` module (safe, modern, always available):

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
from email.parser import BytesParser
from email.policy import default

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_type = self.headers.get("Content-Type", "")
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        # Parse the full MIME email-like message
        msg = BytesParser(policy=default).parsebytes(
            b"Content-Type: " + content_type.encode() + b"\n\n" + body
        )

        saved_files = []
        for part in msg.iter_parts():
            if part.get_content_disposition() == "inline":
                continue
            filename = part.get_filename()
            if filename:
                with open(filename, "wb") as f:
                    f.write(part.get_payload(decode=True))
                saved_files.append(filename)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Uploaded: {', '.join(saved_files)}".encode())

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="myfile">
                <input type="submit">
            </form>
        """)

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

> The old `cgi.FieldStorage` approach is deprecated in Python 3.11 and will be
> removed; stick with the `email` module for new code.

### 5.4 Concurrency – handle multiple requests at once

By default the server handles one request at a time. For development that is
often fine, but if you need to handle several slow clients simultaneously you
can add threading.

The simplest way is to use the built‑in `ThreadingHTTPServer` (Python ≥ 3.7):

```python
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import time

class SlowHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(2)   # simulate slow operation
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Done")

server = ThreadingHTTPServer(("127.0.0.1", 8000), SlowHandler)
server.serve_forever()
```

For older Python versions you can mix in `socketserver.ThreadingMixIn`
manually:

```python
from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle each request in a separate thread."""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Threaded server works!")

server = ThreadedHTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

> Note: Because of the GIL, threading won't speed up CPU‑bound handlers. It
> helps when requests spend time waiting on I/O (disk, network, sleep).

### 5.5 Customising logging

Every request is logged to `stderr` by default. You can customise or silence
the output by overriding `log_message`:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        # Write to a log file instead of stderr
        with open("server.log", "a") as f:
            f.write("%s - - [%s] %s\n" %
                    (self.client_address[0],
                     self.log_date_time_string(),
                     format % args))

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

To **silence** logging completely:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Silent server")

    def log_message(self, format, *args):
        return          # do nothing

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
server.serve_forever()
```

### 5.6 Security – a word of caution

The built‑in server is **not** designed for the public internet:

- **No HTTPS** – all traffic is plain text.
- **No authentication** – anyone can hit your endpoints.
- **No rate limiting** – trivial to overwhelm.
- **Potential path traversal** – always sanitize paths if you serve files
  manually (use `os.path.abspath` and verify the prefix).
- **Cross‑origin requests (CORS)** – for development you may need to add a
  header like `Access-Control-Allow-Origin: *`. This can be done in a custom
  handler, but remember: it's a development convenience, not a security
  feature.

**Never expose the built‑in server directly to the internet or an untrusted
network.** For production, use a proper server (Nginx, Apache) in front, or an
ASGI/WSGI application server like Gunicorn or Uvicorn.

---

## 6. Summary

The `http.server` module is a fantastic Swiss‑army knife for:

- Serving a local directory of static files instantly
- Prototyping a simple REST API with a few endpoints
- Testing HTTP clients (your own scripts, `curl`, a mobile app)
- Demonstrating how HTTP works in a classroom or workshop
- Quick file sharing on a local network
- Building small, single‑purpose internal tools

It requires **zero configuration** and is available anywhere Python is
installed. With just a few lines of code you can go from a blank file to a
working server.

### When to reach for something else

Once you need URL routing with variables (like `/users/<id>`), middleware,
authentication, or scalable performance, switch to a lightweight web framework
such as **Flask**, **FastAPI**, or **bottle**. These frameworks give you a
richer toolbox while still keeping the development experience simple.

---

## 7. What we've covered

- Starting the command‑line file server
- Understanding `HTTPServer` and `BaseHTTPRequestHandler`
- Building custom `do_GET`, `do_POST` and other method handlers
- Path‑based routing, query string parsing, JSON APIs
- Serving file downloads with security in mind
- Handling form data and JSON uploads
- Streaming large files without blowing up memory
- Parsing multipart file uploads with the `email` module
- Adding concurrency with `ThreadingHTTPServer`
- Customising logging and nailing down security basics

Use this knowledge to build quick, local tools or to understand how web
servers work under the hood – and then take the next step with a full‑featured
framework when you're ready.
