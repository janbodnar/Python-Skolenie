import xml.sax


class ProductHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.products = []

    def startElement(self, tag, attributes):
        self.tag = tag

    def endElement(self, tag):
        if self.tag == "id":
            self.id = self.id.strip()
        elif self.tag == "name":
            self.name = self.name.strip()
        elif self.tag == "price":
            self.price = self.price.strip()
        elif self.tag == "quantity":
            self.quantity = self.quantity.strip()

        if tag == "product":
            self.products.append(
                {
                    "id": self.id,
                    "name": self.name,
                    "price": self.price,
                    "quantity": self.quantity,
                }
            )
        self.tag = ""

    def characters(self, content):
        if self.tag == "id":
            self.id = content
        elif self.tag == "name":
            self.name = content
        elif self.tag == "price":
            self.price = content
        elif self.tag == "quantity":
            self.quantity = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

handler = ProductHandler()
parser.setContentHandler(handler)

fname = "products.xml"
parser.parse(fname)

for p in handler.products:
    print(p)
