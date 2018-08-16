#!/usr/bin/python3

import requests as req

resp = req.get("http://www.google.com")

print(resp.status_code)
print(resp.history)
print(resp.url)
