# Python markitdown

The `markitdown` library is easy to use and provides a simple API for  
parsing and rendering Markdown.  
  
Markdown is a lightweight markup language with plain text formatting  
syntax. It's designed to be easy to read and write, allowing you to convert  
plain text into structured HTML. You can use it to format text, create lists,  
add links, insert images, and more.  

```
$ pip install markitdown
```

Before using the `markitdown` library, you need to install it using  
`pip`.

## Basic Usage of markitdown

The following example demonstrates how to use the `markitdown`   
library to convert Markdown text into HTML using an inline string.  


```python
import markdown

# Markdown text as an inline string
markdown_text = """
# Heading 1
## Heading 2
### Heading 3

- List item 1
- List item 2
- List item 3

**Bold text** and *italic text*.

[Visit ZetCode](https://zetcode.com)
"""

# Convert Markdown to HTML
html_output = markdown.markdown(markdown_text)
print(html_output)
```

In this program, the `markdown.markdown` function is used to  
convert the Markdown text into HTML. The resulting HTML is printed to the  
console.  

## Reading Markdown from a File

The following example demonstrates how to read Markdown from a file and convert  
it into HTML using the `markitdown` library.  


```md
# Example Markdown File

This is a sample Markdown file.

- Item 1
- Item 2
- Item 3

**Bold text** and *italic text*.
```

This is the `example2.md` file.


```python
import markdown

# Read Markdown from a file
with open("example.md", "r") as fd:
    markdown_text = fd.read()

# Convert Markdown to HTML
html_output = markdown.markdown(markdown_text)

print(html_output)

```

In this program, the Markdown content is read from a file named `example.md` and  
converted into HTML using the `markdown.markdown` function.  

## Customizing HTML Output
 
This example demonstrates how to use a custom extension to modify the generated  
HTML when converting Markdown using the `markdown` library.  


```md
# Custom Styled Heading

This is a sample Markdown file with custom styles.

- Item A
- Item B
- Item C
```

This is the `example3.md` file.


```python
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

class CustomStyleProcessor(Treeprocessor):
    def run(self, root):
        for elem in root.iter():
            if elem.tag == "h1":
                elem.set("class", "custom-heading")
            elif elem.tag == "li":
                elem.set("class", "custom-item")

class CustomStyleExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(CustomStyleProcessor(md), "custom_style", 10)

```

The `CustomStyleProcessor` is a custom Markdown tree processor that modifies the  
generated HTML before output. It iterates through the parsed Markdown elements  
and applies custom CSS classes to specific HTML tags.  


```python
import markdown
from custom_renderer import CustomStyleExtension

# Read Markdown from a file
with open("example_custom.md", "r", encoding="utf-8") as fd:
    markdown_text = fd.read()

# Convert Markdown to HTML with a custom extension
html_output = markdown.markdown(
    markdown_text,
    extensions=[CustomStyleExtension()]
)

print(html_output)
```

This program applies a custom extension that adds a CSS class to headings and  
list items, allowing for easier styling in HTML output.  

## Handling Extensions

The following example demonstrates how to use extensions with the  
`markitdown` library to add additional functionality, such as tables  
and code blocks, by reading Markdown from a file.  


```md
# Example with Extensions

| Column 1 | Column 2 |
|----------|----------|
| Row 1    | Data 1   |
| Row 2    | Data 2   |

```python
print("Hello there!")
```

```

This is the `example4.md` file.


```python
import markdown

# Read Markdown from a file
with open("example4.md", "r", encoding="utf-8") as fd:
    markdown_text = fd.read()

# Convert Markdown to HTML with correct extensions
html_output = markdown.markdown(
    markdown_text,
    extensions=["tables", "fenced_code"]
)

print(html_output)
```

In this program, the `tables` and `fenced_code` are used to enable table and  
code block rendering in the Markdown text.  

## Convertig HTML to Markdown

The convert function converts the given HTML code into markdown.  


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

    <h1>Document title</h1>

    <p>
        A simple HTML document.
    </p>

</body>
</html>
```

This is a simple HTML document, we call it `index.html`.


```python
from markitdown import MarkItDown

converter = MarkItDown()
filename = 'index.html'

# Convert HTML to Markdown
mk_content = converter.convert(filename)

print(mk_content.text_content)
```

The example transforms an HTML page into markdown, utilizing the `convert`  
function.

```

$ py main.py
# Document title

A simple HTML document.
```

The output only contains the core elements.  

In order to get the whole HTML document, we need to create it ourselves.  


```python
import argparse
import markdown

parser = argparse.ArgumentParser(description="Convert a Markdown file to HTML.")
parser.add_argument("filename", help="The name of the Markdown file to convert")

# Parse arguments
args = parser.parse_args()
mk_file = args.filename

# Read Markdown from the file provided as an argument
with open(mk_file, "r", encoding="utf-8") as fd:
    markdown_text = fd.read()

# Convert Markdown to HTML
body_content = markdown.markdown(markdown_text, tab_length=4)

# Create the full HTML structure
html_output = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    {body_content}
</body>
</html>"""

print(html_output)
```

The program reads the contents of the file name given as an CLI option, converts  
it to HTML and merges it with the whole document structure using Python fstring.  

## Using LLM

In the following example, we use a Llama vision model to get the description  
of an image. We use Groq service.  
   
```python
import os
from markitdown import MarkItDown
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

mid = MarkItDown(llm_client=client, llm_model="llama-3.2-11b-vision-preview")
result = mid.convert("character.png")
print(result.text_content)
```

The `llama-3.2-11b-vision-preview` model has multimodal (vision)  
capabilities, meaning it can handle image inputs along with text.  

```
result = mid.convert("character.png")
```

We pass the image file name to the `convert` method.  


