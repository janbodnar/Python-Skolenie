# Priklady


## Show image in UI

```python
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def display_image_from_url(url):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))

    root = tk.Tk()
    root.title("Image from URL")

    tk_image = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_image)
    label.pack()

    root.mainloop()

# Replace 'YOUR_IMAGE_URL' with the actual URL of the image you want to display
display_image_from_url('https://static.wikia.nocookie.net/theiceage/images/4/4a/SIdSloth2.jpg')
```

## Show image in web app

```python

from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def display_image():
    # Replace 'YOUR_IMAGE_URL' with the actual URL of the image you want to display
    image_url = 'https://static.wikia.nocookie.net/theiceage/images/4/4a/SIdSloth2.jpg'
    response = requests.get(image_url)
    img_data = response.content

    # HTML template to display the image
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Display Image</title>
    </head>
    <body>
        <h1>Image from URL</h1>
        <img src="data:image/jpeg;base64,{{ image_data }}" alt="Image">
    </body>
    </html>
    '''

    # Convert image data to base64
    import base64
    image_data = base64.b64encode(img_data).decode('utf-8')

    return render_template_string(html_template, image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True)
```



## Filter by type

```python
vals = [1, 2, 4, 'falcon', 'war', 3.4, 2.3, True, False, None, (1, 2, 3), (3, 4)]

for val in vals:
    if type(val) == int:
        print(val)
```


```python
# calculate sum
data = "1,2,3,4,5,6,7,8,9,10"

# print data using fstring
data2 = """John,Doe,gardener
Roger,Roe,driver
Paul,Smith,teacher
"""

# read words.txt file
# print words starting with w or c
```

Riesenie: 

```python
# calculate sum
data = "1,2,3,4,5,6,7,8,9,10"

mysum = 0

fields = data.split(",")
# print(fields)

for field in fields:
    mysum += int(field)

print(mysum)


# print data using fstring
data2 = """John,Doe,gardener
Roger,Roe,driver
Paul,Smith,teacher
"""

lines = data2.splitlines()
# print(lines)

for line in lines:
    fields = line.split(",")
    print(f'{fields[0]} {fields[1]} is a {fields[2]}')


file_name = 'words.txt'

with open(file_name, 'r') as f:

    for line in f:
        if line.startswith('w') or line.startswith('c'):
            print(line.strip())
```
