#!/usr/bin/python


from decimal import Decimal
import xml.etree.ElementTree as ET


def load_data_from_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    products = []

    for product in root.findall('product'):

        id = product.find('id').text
        name = product.find('name').text
        price = product.find('price').text
        quantity = product.find('quantity').text

        products.append({
            'id': int(id),
            'name': name,
            'price': Decimal(price),
            'quantity': Decimal(quantity)
        })

    return products

file_name = 'products.xml'
products = load_data_from_xml(file_name)

for product in products:
    print(product)


res = 0
delta = Decimal('1.15')

for product in products:
    res += product['price'] * delta * product['quantity'] 

print(res)
