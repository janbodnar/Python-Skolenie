import xml.etree.ElementTree as ET
#!/usr/bin/python

import xml.dom.minidom

# Define a dictionary of products
products = {
    '1': {'name': 'Product1', 'price': 100, 'quantity': 50},
    '2': {'name': 'Product2', 'price': 200, 'quantity': 30},
    '3': {'name': 'Product3', 'price': 150, 'quantity': 20},
}

# Create the root element
root = ET.Element('products')

# Iterate over the products and add them to the XML
for id, info in products.items():
    product = ET.SubElement(root, 'product', id=id)
    for key, val in info.items():
        ET.SubElement(product, key).text = str(val)

# Create a string representation of the XML
xml_str = ET.tostring(root, 'utf-8')

# Parse the string to a DOM object
dom = xml.dom.minidom.parseString(xml_str)

# Prettify the DOM object
pretty_xml_str = dom.toprettyxml(indent="  ")

# Write the pretty XML to a file
with open('products2.xml', 'w') as f:
    f.write(pretty_xml_str)
