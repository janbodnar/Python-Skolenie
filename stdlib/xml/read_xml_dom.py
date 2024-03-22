#!/usr/bin/python

from xml.dom import minidom


def parse_products(fname):

    products = []
    doc = minidom.parse(fname)
    root = doc.documentElement  # Get the root element (<products>)

    for product_element in root.getElementsByTagName("product"):
        product = {}
        for child in product_element.childNodes:
            if child.nodeType == child.ELEMENT_NODE:  # Check for element nodes
                tag = child.tagName
                value = child.firstChild.nodeValue.strip()  # Get text content
                product[tag] = value

        products.append(product)
    return products


products = parse_products("products.xml")
print(products)

for product in products:
    print(product)
