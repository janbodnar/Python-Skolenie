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

## Download JPG file

```python
import requests

def download_jpg(url, filename):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Ensure the content is actually a PNG by checking the content-type
            if 'image/jpeg' in response.headers.get('content-type', ''):
                # Open a file in binary write mode
                with open(filename, 'wb') as file:
                    # Write the content to the file
                    file.write(response.content)
                print(f"JPG file successfully downloaded as {filename}")
            else:
                print("Error: The URL doesn't point to a JPG file")
        else:
            print(f"Error: Failed to download file. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: An exception occurred - {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace with your JPG URL
    url = "https://i.pinimg.com/736x/b9/07/56/b907566d35ff114a61e2636e0f4eca61.jpg"
    # Specify the output filename
    output_filename = "sid.jpg"
    
    download_jpg(url, output_filename)
```


