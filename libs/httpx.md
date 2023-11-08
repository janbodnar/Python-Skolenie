# Creating web requests 

## The httpx module

HTTPX is an HTTP client for Python 3, which provides sync and async APIs, and support for  
both HTTP/1.1 and HTTP/2. It has similar API to the popular Python requests library.  
HTTPX requires Python 3.6+.

$ pip install httpx

We install the module with the pip command.

The httpx supports asynchronous web requests. With the combination of httpx and asyncio  
modules and async and await keywords, we can generate asynchronous web requests.  
This may lead to considerable increase of efficiency in our programs.

## HTTP

The Hypertext Transfer Protocol (HTTP) is an application protocol for distributed, collaborative,  
hypermedia information systems. HTTP is the foundation of data communication for the World Wide Web.

## Status code 

```python
#!/usr/bin/python

import httpx 

r = httpx.head('http://webcode.me')
print(r.status_code)
```

## GET request 

```python
#!/usr/bin/python

import httpx 

r = httpx.get('http://webcode.me')
print(r.text)
```

## Async GET request 

```python
#!/usr/bin/python

import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get('http://test.webcode.me')
        print(r.text)

asyncio.run(main())
```

## Query params 

```python
#!/usr/bin/python

import httpx 

payload = {'name': 'John Doe', 'occupation': 'gardener'}
r = httpx.get('https://httpbin.org/get', params = payload)
print(r.text)
```

## Multiple async requests

```python
#!/usr/bin/python

import httpx
import asyncio

async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)

urls = ['http://webcode.me', 'https://httpbin.org/get',
    'https://google.com', 'https://stackoverflow.com',
    'https://github.com']

async def launch():
    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp.status_code for resp in resps]

    for status_code in data:
        print(status_code)

asyncio.run(launch())
```

## Comparing blocking & non-blocking requests 

Sync example

```python
#!/usr/bin/python

import httpx
import time

urls = ['http://webcode.me', 'https://httpbin.org/get', 
    'https://google.com', 'https://stackoverflow.com', 
    'https://github.com', 'https://mozilla.org']

start_time = time.monotonic()

for url in urls:
    r = httpx.get(url)
    print(r.status_code)

print(f'Elapsed: {time.monotonic() - start_time}')
```

Async example

```python
#!/usr/bin/python

import httpx
import asyncio
import time

async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)

urls = ['http://webcode.me', 'https://httpbin.org/get', 
    'https://google.com', 'https://stackoverflow.com', 
    'https://github.com']

async def launch():
    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp.status_code for resp in resps]
    
    for status_code in data:
        print(status_code)

start_time = time.monotonic()
asyncio.run(launch())
print(f'Elapsed: {time.monotonic() - start_time}')
```



