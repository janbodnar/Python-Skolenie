# Requests

The Python `requests` library is a popular and easy-to-use library for making HTTP requests in Python.  
It allows you to send HTTP/1.1 requests, with methods such as `GET`, `POST`, `PUT`, `DELETE`, and more.  

Features:  

- **Simplicity**: The `requests` library simplifies making HTTP requests and handling responses.  
  It's designed to be user-friendly and intuitive.  
- **Features**: It provides support for features like keeping connections open, managing sessions,  
  handling cookies, and managing request headers.  
- **Error Handling**: `requests` helps manage exceptions and errors, making it easier to debug and  
  handle different HTTP response statuses.  
- **API**: It offers a straightforward API to work with JSON, XML, and other formats returned   
  by web servers.

## Status 

```python
import requests as req

resp = req.get("https://webcode.me")

print(resp.status_code)
print(resp.history)
print(resp.url)
```

## Headers 

```python
import requests 

resp = requests.head("https://webcode.me")

print("Server: " + resp.headers['server'])
print("Last modified: " + resp.headers['last-modified'])
print("Content type: " + resp.headers['content-type'])
```

## Retrieve page

```python
import requests 

url = 'https://webcode.me/'
resp = requests.get(url)

# print(resp.content.decode('utf-8'))
print(resp.text)
```


## Retrieve JSON data

```python
import requests 

resp = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = resp.json()

print(posts)

for post in posts:
    print(f"Id: {post['id']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
```

## Driver status

Download:  

`https://googlechromelabs.github.io/chrome-for-testing/#stable`


Chromedriver status implementation:  
`https://chromium.googlesource.com/chromium/src/+/master/docs/chromedriver_status.md`

```python
import requests


def get_chrome_driver_status():
    url = "http://localhost:9515/status"

    try:
        # Send a GET request to the ChromeDriver status endpoint
        response = requests.get(url)
        print(response)

        if response.status_code == 200:
            print("OK - 200")
        else:
            print(f"Failed to retrieve status. HTTP Status Code: {
                  response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to ChromeDriver: {e}")


if __name__ == "__main__":
    get_chrome_driver_status()
```




