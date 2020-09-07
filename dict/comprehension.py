#!/usr/bin/python

# comprehension.py

capitals = { "Bratislava": 424207, "Vilnius": 556723, "Lisbon": 564657,
             "Riga": 713016, "Jerusalem": 780200, "Warsaw": 1711324,
             "Budapest": 1729040, "Prague": 1241664, "Helsinki": 596661,
             "Yokyo": 13189000, "Madrid": 3233527 }


capitals2 = { key:val for key, val in capitals.items() if val < 1000000 }

print(capitals2)


