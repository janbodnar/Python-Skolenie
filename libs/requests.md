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

        code = response.status_code

        if code == 200:
            print("OK - 200")
        else:
            print(f"Failed. HTTP Status Code: {code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to ChromeDriver: {e}")


if __name__ == "__main__":
    get_chrome_driver_status()
```

## Get title 

Get title using JS API

```python
import requests

def get_webpage_title(url):
    # Define the base URL for the ChromeDriver REST API
    chromedriver_url = "http://localhost:9515"

    try:
        # Step 1: Create a new session
        session_response = requests.post(f"{chromedriver_url}/session", json={
            "capabilities": {
                "alwaysMatch": {
                    "browserName": "chrome",
                    "goog:chromeOptions": {
                        "args": ["--headless"]  # Run in headless mode
                    }
                }
            }
        })
        session_response.raise_for_status()
        session_data = session_response.json()
        session_id = session_data["value"]["sessionId"]

        print(f"Session created with ID: {session_id}")

        # Step 2: Navigate to the specified URL
        navigate_response = requests.post(
            f"{chromedriver_url}/session/{session_id}/url",
            json={"url": url}
        )

        print(f"{chromedriver_url}/session/{session_id}/url")
        navigate_response.raise_for_status()

        print(f"Navigated to: {url}")

        # Step 3: Execute JavaScript to retrieve the document title
        execute_script_response = requests.post(
            f"{chromedriver_url}/session/{session_id}/execute/sync",
            json={
                "script": "return document.title",
                "args": []
            }
        )
        execute_script_response.raise_for_status()
        title_data = execute_script_response.json()
        title = title_data["value"]

        print(f"The title of the webpage is: {title}")

        # Step 4: Delete the session (cleanup)
        delete_session_response = requests.delete(f"{chromedriver_url}/session/{session_id}")
        delete_session_response.raise_for_status()

        print("Session deleted successfully.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while interacting with ChromeDriver: {e}")

if __name__ == "__main__":
    target_url = "http://example.com"
    get_webpage_title(target_url)
```


