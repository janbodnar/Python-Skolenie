#!/usr/bin/python

import requests as req

resp = req.request(method='GET', url="http://webcode.me")
print(resp.text)
