# aiohttp — Build Async HTTP Servers in Python

`aiohttp` is a modern asynchronous HTTP framework for both **client** and **server** side. It lets  
you write high‑performance web services and applications using Python’s `async`/`await` syntax. Unlike  
the built‑in `http.server`, `aiohttp` is non‑blocking, handles thousands of concurrent connections  
effortlessly, and provides a rich set of features out of the box.

In this tutorial you’ll learn:

- Installing `aiohttp` and running a basic server
- Routing: handling different paths and methods
- Reading query parameters, forms, and JSON
- Streaming uploads and downloads
- Serving static files
- Testing your server with `xh` (a friendly HTTPie‑like tool) and load testing with `hey`
- Important security considerations


## Installation

`aiohttp` is not part of the standard library, so you need to install it first:

```bash
pip install aiohttp
```

All examples in this tutorial require Python 3.7 or newer. Verify your installation:

```bash
python -c "import aiohttp; print(aiohttp.__version__)"
```


## Your first aiohttp server

Create a file named `server.py`:

```python
from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, World!")

app = web.Application()
app.add_routes([web.get("/", hello)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

Run it:

```bash
python server.py
```

Now open `http://localhost:8000` in your browser or test with `xh`:

```bash
xh http://localhost:8000
```

You’ll see the response `Hello, World!`.

### How it works

- `web.Application()` creates the server application.
- `web.get("/", hello)` binds a GET handler to the path `/`.
- `web.run_app(app)` starts the event loop and runs the app on port 8000.

Every handler must be an `async` function that receives a `request` object and returns a `web.Response`.


## Routing multiple endpoints

You can add several routes, each with a different method or path.

```python
from aiohttp import web

async def home(request):
    return web.Response(text="Home page")

async def health(request):
    return web.json_response({"status": "ok"})

async def echo(request):
    # For any other path, return a 404
    return web.Response(text="Not found", status=404)

app = web.Application()
app.add_routes([
    web.get("/", home),
    web.get("/health", health),
    # Catch-all (should be last)
    web.get("/{tail:.*}", echo),
])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

Test them:

```bash
xh http://localhost:8000/
xh http://localhost:8000/health
xh http://localhost:8000/nonexistent    # returns 404
```

You can also use the decorator syntax, but `app.add_routes` keeps everything in  
one place and is easier to read.


## Parsing query parameters

Query parameters are available via `request.query`, which behaves like a multi‑dict.

```python
from aiohttp import web

async def greet(request):
    name = request.query.get("name", "World")
    return web.Response(text=f"Hello, {name}!")

app = web.Application()
app.add_routes([web.get("/greet", greet)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

Test:

```bash
xh "http://localhost:8000/greet?name=Ada"
# => Hello, Ada!
```


## Returning JSON

Use `web.json_response()` to automatically set the correct content type and serialize Python objects.

```python
from aiohttp import web

async def items(request):
    data = [
        {"id": 1, "name": "apple"},
        {"id": 2, "name": "banana"},
    ]
    return web.json_response(data)

app = web.Application()
app.add_routes([web.get("/api/items", items)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

```bash
xh http://localhost:8000/api/items
```

---

## 6. Serving static files

`aiohttp` can serve static files from a directory with `web.static()`.

```python
from aiohttp import web
import pathlib

async def index(request):
    return web.FileResponse("./index.html")

app = web.Application()
# Serve files from the 'static' subdirectory under the /static URL prefix
app.router.add_static("/static/", path="./static", name="static")

# Or serve one specific file
app.add_routes([web.get("/", index)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

Make sure the `static` folder exists, then visit `http://localhost:8000/static/logo.png`.


##  Handling POST requests

### Reading plain text or binary body

Use `await request.text()` or `await request.read()`.

```python
from aiohttp import web

async def upload_text(request):
    body = await request.text()
    return web.Response(text=f"Received: {body}")

app = web.Application()
app.add_routes([web.post("/text", upload_text)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

Test:

```bash
echo "Hello from xh" | xh POST http://localhost:8000/text
```

### Parsing JSON

`await request.json()` automatically decodes JSON payloads.

```python
from aiohttp import web

async def create_item(request):
    data = await request.json()
    # Pretend we saved the item and returned it with an ID
    data["id"] = 123
    return web.json_response(data, status=201)

app = web.Application()
app.add_routes([web.post("/items", create_item)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

```bash
xh POST http://localhost:8000/items name=laptop price:=999.99
```

### Parsing form data

For standard HTML forms (`application/x-www-form-urlencoded` or `multipart/form-data`) use `await request.post()`.

```python
from aiohttp import web

async def handle_form(request):
    data = await request.post()
    username = data.get("username", "anonymous")
    return web.Response(text=f"Hello, {username}!")

app = web.Application()
app.add_routes([web.post("/form", handle_form)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

Test with `xh` (it sends `application/x-www-form-urlencoded` by default):

```bash
xh --form POST http://localhost:8000/form username=Ada
```

## File downloads (streaming a file)

Stream large files instead of loading them entirely into memory.

```python
from aiohttp import web
import aiofiles  # Optional, but helps with async file I/O
import os

async def download(request):
    filepath = "large_video.mp4"
    if not os.path.exists(filepath):
        return web.Response(text="File not found", status=404)

    headers = {
        "Content-Disposition": f'attachment; filename="{os.path.basename(filepath)}"'
    }
    return web.FileResponse(filepath, headers=headers)

app = web.Application()
app.add_routes([web.get("/download", download)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

`web.FileResponse` handles chunked sending efficiently without blocking the event loop. If  
you need more control, you can manually stream using `web.StreamResponse`.


## Streaming uploads (advanced)

The original example shows how to receive a stream of chunks from the client and process them  
on the fly, without buffering the entire body. This is useful for large uploads or real‑time data.

```python
from aiohttp import web

async def stream_reader(reader, handler):
    while chunk := await reader.read(4096):
        await handler(chunk)

async def handle(request):
    async def process_chunk(chunk):
        print(f"Received {len(chunk)} bytes")

    await stream_reader(request.content, process_chunk)
    return web.Response(text="Stream received")

app = web.Application()
app.add_routes([web.post("/upload", handle)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

Test with a large file:

```bash
dd if=/dev/urandom of=test.bin bs=1M count=10   # create a 10 MB file
xh --timeout 0 POST http://localhost:8000/upload < test.bin
```

You’ll see the server printing how many bytes it received per chunk. The client receives  
`Stream received` after the whole file is transferred.

**How it works:**

- `request.content` is an `aiohttp.StreamReader`.
- `reader.read(4096)` reads up to 4096 bytes at a time, returning an empty `bytes` when the stream ends.
- The coroutine `process_chunk` is called for each chunk, so you can store, transform, or forward
  the data without holding everything in memory.


## Concurrency – async all the way

Because `aiohttp` is built on `asyncio`, it handles many connections concurrently without threads.  
Let’s simulate a slow handler:

```python
from aiohttp import web
import asyncio

async def slow(request):
    await asyncio.sleep(2)          # Simulate I/O delay
    return web.Response(text="Done")

app = web.Application()
app.add_routes([web.get("/slow", slow)])

if __name__ == "__main__":
    web.run_app(app, port=8000)
```

While one request is sleeping, the server can still serve others. Test with  
`hey` (a simple load generator):

```bash
# Send 5 concurrent requests, 2 seconds apart
hey -c 5 -z 5s http://localhost:8000/slow
```

All requests will complete in ~2 seconds, showing true concurrency.

---

## 11. Testing your server with `xh` and `hey`

### `xh` – Fast and friendly HTTP client

`xh` is a modern alternative to `curl`, written in Rust. Install it via your package manager  
or download from [github.com/ducaale/xh](https://github.com/ducaale/xh).

Examples:

```bash
# GET request
xh http://localhost:8000/

# POST JSON
xh POST http://localhost:8000/items name=Pen price:=1.5

# Form submission
xh --form POST http://localhost:8000/form username=Ada

# Download a file
xh --download http://localhost:8000/download

# Stream raw body from stdin
xh POST http://localhost:8000/upload < large_file.bin
```

### `hey` – Lightweight load testing

`hey` sends a number of concurrent requests and reports statistics. Install from  
[github.com/rakyll/hey](https://github.com/rakyll/hey).

```bash
# 200 requests, 50 concurrent
hey -n 200 -c 50 http://localhost:8000/
```

Use these tools to validate your endpoints during development.

## Security considerations

`aiohttp` itself does **not** provide HTTPS. In production you must place a reverse proxy  
like Nginx or Caddy in front, or use `aiohttp`’s ASGI mode with an ASGI server that  
supports SSL (e.g., `uvicorn` with SSL certificates).

Other points:

- **CORS:** For browser‑based access, add appropriate headers. You can write a simple middleware:
  ```python
  from aiohttp import web

  @web.middleware
  async def cors_middleware(request, handler):
      response = await handler(request)
      response.headers["Access-Control-Allow-Origin"] = "*"
      return response

  app = web.Application(middlewares=[cors_middleware])
  ```
- **Input validation:** Always validate and sanitize user input (paths, query params, JSON).  
  Use libraries like `pydantic` for robust data validation.
- **File uploads:** Limit upload size either in your code or via the reverse proxy to  
  prevent resource exhaustion.
- **Authentication / Authorization:** Not built‑in; implement it yourself with middleware  
  or use an established library like `aiohttp-session` + `aiohttp-security`.

Never expose an `aiohttp` development server directly to the internet without a secure proxy in front.

## Summary

`aiohttp` brings the power of `async`/`await` to web servers, making it ideal for:

- High‑concurrency APIs and websockets
- Streaming large payloads in both directions
- Building fast, lightweight web services
- Asynchronous microservices and backends

It gives you fine‑grained control while remaining Pythonic and well‑documented.

### When to consider alternatives

- If you prefer a higher‑level framework with automatic OpenAPI docs, try **FastAPI** (built on `Starlette`, itself
  often using `aiohttp` underneath for testing).
- For traditional synchronous WSGI apps, **Flask** or **Django** are more appropriate.
- For very simple development‑only servers, the standard library’s `http.server` works without any extra dependencies.

