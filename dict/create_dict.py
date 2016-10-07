#!/usr/bin/python3

# create_dict.py

weekend = { "Sun": "Sunday", "Mon": "Monday" }
vals = dict(one=1, two=2)

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

d = { i: object() for i in range(4) }

print (weekend)
print (vals)
print (capitals)
print (d)
