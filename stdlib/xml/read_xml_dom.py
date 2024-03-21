
```python
#!/usr/bin/python

from xml.dom import minidom


def parse_products(file):
    """Parses the XML file and returns a list of dictionaries containing product information."""
    products = []
    try:
        doc = minidom.parse(file)
        root = doc.documentElement  # Get the root element (<products>)

        for product_element in root.getElementsByTagName("product"):
            product = {}
            for child in product_element.childNodes:
                if child.nodeType == child.ELEMENT_NODE:  # Check for element nodes
                    tag = child.tagName
                    value = child.firstChild.nodeValue.strip()  # Get text content
                    product[tag] = value
            products.append(product)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"Error parsing XML: {e}")
    return products


# Example usage:
products = parse_products("products.xml")


print(products)

# Access product information
for product in products:
    print(f"ID: {product['id']}, Name: {product['name']}")
```
