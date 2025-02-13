# XML 

XML (Extensible Markup Language) is a text-based format that uses tags to define  
the structure of data. It's both human-readable and machine-readable, allowing for  
flexible data exchange. Think of it as a labeled document where the tags act like  
labels describing the content within.


## XML processing

1. **ElementTree**: This is a lightweight and efficient API for parsing and creating  
XML data. It provides methods to iterate over elements in the XML tree.  

2. **minidom**: minidom is a minimal implementation of the Document Object Model  
interface, with an API similar to that in other languages. It is intended for  
simple, one-time tasks.  

3. **SAX (Simple API for XML)**: SAX is a standard interface for event-driven XML  
parsing. It provides a mechanism to read data from an XML document.  

4. **DOM (Document Object Model)**: DOM is a standard tree structure, where each  
node contains one of the components from an XML structure.  

5. **xmltodict**: xmltodict is a Python module that makes working with XML feel  
like you are working with JSON. It converts XML to an OrderedDict.  

6. **BeautifulSoup**: BeautifulSoup is a Python library used for web scraping  
purposes to pull the data out of HTML and XML files. It creates a parse tree  
from page source code that can be used to extract data in a hierarchical and  
readable manner.  


## xml.etree.ElementTree (ElementTree)

* A lightweight and user-friendly API for parsing and manipulating XML data.  
* Represents the XML document as a tree structure, with elements as nodes.  
* Ideal for smaller to medium-sized XML files.  

```python
import xml.etree.ElementTree as ET

tree = ET.parse("products.xml")
root = tree.getroot()

for product in root.findall("product"):
  id = product.find("id").text
  name = product.find("name").text
  print(f"ID: {id}, Name: {name}")
```


## xml.dom.minidom (minidom)

A W3C DOM (Document Object Model) compliant parser. Provides a more comprehensive API for  
accessing and modifying XML elements and attributes. Offers functionalities like navigating  
the document tree, adding/removing nodes, and modifying attributes. 

Might be slower than `ElementTree` for large datasets.

Example:

```python
from xml.dom import minidom

doc = minidom.parse("products.xml")
root = doc.documentElement

for product in root.getElementsByTagName("product"):
  id = product.getElementsByTagName("id")[0].firstChild.nodeValue
  name = product.getElementsByTagName("name")[0].firstChild.nodeValue
  print(f"id: {id}, name: {name}")
```

Reading attributes. 

```python
#!/usr/bin/python

from xml.dom import minidom

doc = minidom.parse("products2.xml")
root = doc.documentElement

for product in root.getElementsByTagName("product"):
  pid = product.getAttribute('id')
  name = product.getElementsByTagName("name")[0].firstChild.nodeValue
  price = product.getElementsByTagName("price")[0].firstChild.nodeValue
  quantity = product.getElementsByTagName("quantity")[0].firstChild.nodeValue
  print(pid, name, price, quantity)
```


## xml.sax (SAX - Simple API for XML)

An event-based parser that processes XML data as a stream of events  
(start/end tags, character data). More memory-efficient for very large XML files as it  
doesn't need to load the entire document in memory at once. Requires writing custom  
event handlers to handle different parsing events.  

```python
from xml.sax import make_parser, ContentHandler

class ProductHandler(ContentHandler):
  def __init__(self):
    self.current_data = ""
    self.product = {}
  
  def startElement(self, name, attrs):
    self.current_data = ""
    if name == "product":
      self.product = {}
  
  def characters(self, content):
    self.current_data += content.strip()
  
  def endElement(self, name):
    if name != "product":
      self.product[name] = self.current_data
    else:
      print(f"ID: {self.product['id']}, Name: {self.product['name']}")

parser = make_parser()
parser.setContentHandler(ProductHandler())
parser.parse("products.xml")
```

```python
import xml.sax

class ProductHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.id = ""
        self.name = ""
        self.price = ""
        self.quantity = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "product":
            print(f"\nProduct ID: {attributes['id']}")

    # Call when an element ends
    def endElement(self, tag):
        if self.current_data == "name":
            print(f"Name: {self.name}")
        elif self.current_data == "price":
            print(f"Price: {self.price}")
        elif self.current_data == "quantity":
            print(f"Quantity: {self.quantity}")
        self.current_data = ""

    # Call when a character is read
    def characters(self, content):
        if self.current_data == "name":
            self.name = content
        elif self.current_data == "price":
            self.price = content
        elif self.current_data == "quantity":
            self.quantity = content

if __name__ == "__main__":
    # Create an XMLReader
    parser = xml.sax.make_parser()
    
    # Turn off namespace
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    
    # Override the default ContextHandler
    Handler = ProductHandler()
    parser.setContentHandler(Handler)
    
    # Parse the XML file
    parser.parse("products2.xml")
```


## Third-party libraries

Several powerful third-party libraries like lxml and Beautiful Soup offer extended  
functionalities for complex XML processing including:

- Support for various XML namespaces.  
- Advanced XPath and CSS selector support for element selection.  
- Validation against XML schemas.  

These libraries typically build upon the standard libraries mentioned above and  
provide a more feature-rich experience.

Choosing the right parser depends on the size and complexity of your XML data,  
performance requirements, and desired level of control over the parsing process.  
