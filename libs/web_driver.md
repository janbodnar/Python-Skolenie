# Web Driver 


*WebDriver* is a remote control interface that enables introspection and control of user agents (i.e., web browsers).   
It provides a platform and language-neutral wire protocol as a way for out-of-process programs to remotely instruct  
the behavior of web browsers. This specification defines a REST-like API for browser automation. WebDriver is used   
for automating web application testing to verify that they work as expected. It is designed to be a simpler and more   
concise programming interface.

The WebDriver specification defines a *REST-like API* for interacting with web browsers. This REST API uses standard   
HTTP methods (GET, POST, DELETE) to perform operations on browser sessions, elements on a webpage, and other  
browser-related resources. Each operation is associated with a specific URL endpoint, which the WebDriver client  
communicates with the WebDriver server to execute commands and retrieve results. This API enables seamless and  
standardized communication between automation scripts and web browsers, making it easier to perform tasks like  
navigating to URLs, interacting with web elements, taking screenshots, and more.

*ChromeDriver* is a standalone server that implements the WebDriver protocol for Google Chrome. It acts as a bridge   
between your test scripts written in languages like Python, Java, etc., and the Chrome browser. When you run your   
automated tests, ChromeDriver communicates with Chrome to execute the commands and actions you've specified.   
It supports various features like headless mode, mobile emulation, and more.



Download:  

`https://googlechromelabs.github.io/chrome-for-testing/#stable`

Chromedriver status implementation:  
`https://chromium.googlesource.com/chromium/src/+/master/docs/chromedriver_status.md`

Get driver status    

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

Get title using *GET	/session/{session id}/title* endpoint

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

        # Step 3: call title endpoint to get the title of the webpage
        title_resp = requests.get(
            f"{chromedriver_url}/session/{session_id}/title",
        )

        title_resp.raise_for_status()
        title_data = title_resp.json()
        title = title_data["value"]

        print(f"The title of the webpage is: {title}")

        # Step 4: Delete the session (cleanup)
        delete_session_response = requests.delete(
            f"{chromedriver_url}/session/{session_id}")
        delete_session_response.raise_for_status()

        print("Session deleted successfully.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while interacting with ChromeDriver: {e}")


if __name__ == "__main__":
    target_url = "https://example.com/"
    get_webpage_title(target_url)
```


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

## Button click

Headless example:  

```python
import requests

def click_button_on_page(url):
    # Define the base URL for the ChromeDriver REST API
    chromedriver_url = "http://localhost:9515"

    try:
        # Step 1: Create a new session
        session_response = requests.post(f"{chromedriver_url}/session", json={
            "capabilities": {
                "alwaysMatch": {
                    "browserName": "chrome",
                    "goog:chromeOptions": {
                        "args": ["--headless"]  # Run in headless mode (optional)
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
        navigate_response.raise_for_status()

        print(f"Navigated to: {url}")

        # Step 3: Find the button element by its tag name
        find_element_response = requests.post(
            f"{chromedriver_url}/session/{session_id}/element",
            json={"using": "tag name", "value": "button"}
        )
        find_element_response.raise_for_status()
        element_data = find_element_response.json()
        value = element_data['value']
        print('value', value)
        element = list(element_data['value'].keys())[0]
        print('element', element)

        element_id = value[element]
        print('element_id', element_id)
        # button_element_id = element_data["value"]["element-6066-11e4-a52e-4f735466cecf"]
        button_element_id = element_data["value"]["element-6066-11e4-a52e-4f735466cecf"]

        print(f"Button element found with ID: {button_element_id}")
        print(find_element_response.json())

        # Step 4: Click the button
        click_response = requests.post(
            f"{chromedriver_url}/session/{session_id}/element/{button_element_id}/click",
            json={}
        )
        click_response.raise_for_status()

        print("Button clicked successfully.")

        # Step 5: Retrieve the output content from the div with id="output"
        execute_script_response = requests.post(
            f"{chromedriver_url}/session/{session_id}/execute/sync",
            json={
                "script": 'return document.getElementById("output").innerText',
                "args": []
            }
        )
        execute_script_response.raise_for_status()
        output_data = execute_script_response.json()
        output_content = output_data["value"]

        print(f"Output content after clicking the button: {output_content}")

        # Step 6: Delete the session (cleanup)
        delete_session_response = requests.delete(f"{chromedriver_url}/session/{session_id}")
        delete_session_response.raise_for_status()

        print("Session deleted successfully.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while interacting with ChromeDriver: {e}")

if __name__ == "__main__":
    target_url = "https://webcode.me/click.html"  # Replace with the actual URL of your HTML page
    click_button_on_page(target_url)
```


UI example:  

```python
import requests
import time


def click_button_on_page(url):
    # Define the base URL for the ChromeDriver REST API
    chromedriver_url = "http://localhost:9515"

    try:
        # Step 1: Create a new session
        session_response = requests.post(f"{chromedriver_url}/session", json={
            "capabilities": {
                "alwaysMatch": {
                    "browserName": "chrome",
                    "goog:chromeOptions": {
                        # Open DevTools for debugging
                        "args": ["--auto-open-devtools-for-tabs"],
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
        navigate_response.raise_for_status()

        print(f"Navigated to: {url}")

        # Step 3: Find the button element by its tag name
        find_element_response = requests.post(
            f"{chromedriver_url}/session/{session_id}/element",
            json={"using": "tag name", "value": "button"}
        )
        find_element_response.raise_for_status()
        element_data = find_element_response.json()
        button_element_id = element_data["value"]["element-6066-11e4-a52e-4f735466cecf"]

        print(f"Button element found with ID: {button_element_id}")

        time.sleep(5)

        # Step 4: Click the button
        click_response = requests.post(
            f"{chromedriver_url}/session/{session_id}/element/{button_element_id}/click",
            json={}
        )
        print(click_response.json())
        click_response.raise_for_status()

        print("Button clicked successfully.")

        # Step 5: Retrieve the output content from the div with id="output"
        execute_script_response = requests.post(
            f"{chromedriver_url}/session/{session_id}/execute/sync",
            json={
                "script": 'return document.getElementById("output").innerText',
                "args": []
            }
        )
        execute_script_response.raise_for_status()
        output_data = execute_script_response.json()
        output_content = output_data["value"]

        print(f"Output content after clicking the button: {output_content}")

        time.sleep(5)

        # Step 6: Delete the session (cleanup)
        delete_session_response = requests.delete(
            f"{chromedriver_url}/session/{session_id}")
        delete_session_response.raise_for_status()

        print("Session deleted successfully.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while interacting with ChromeDriver: {e}")


if __name__ == "__main__":
    # Replace with the actual URL of your HTML page
    target_url = "https://webcode.me/click.html"
    click_button_on_page(target_url)
```

## Get Screenshot 

```python
import requests
import base64

def get_webpage_screenshot(url):
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
        navigate_response.raise_for_status()

        print(f"Navigated to: {url}")

        # Step 3: Take a screenshot of the webpage
        screenshot_response = requests.get(
            f"{chromedriver_url}/session/{session_id}/screenshot"
        )
        screenshot_response.raise_for_status()
        screenshot_data = screenshot_response.json()
        screenshot_base64 = screenshot_data["value"]

        # Convert the base64 screenshot to an image file
        with open("screenshot.png", "wb") as f:
            f.write(base64.b64decode(screenshot_base64))

        print("Screenshot saved as screenshot.png")

        # Step 4: Delete the session (cleanup)
        delete_session_response = requests.delete(
            f"{chromedriver_url}/session/{session_id}")
        delete_session_response.raise_for_status()

        print("Session deleted successfully.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while interacting with ChromeDriver: {e}")


if __name__ == "__main__":
    target_url = "https://example.com/"
    get_webpage_screenshot(target_url)
```
