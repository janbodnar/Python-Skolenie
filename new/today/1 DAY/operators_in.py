## TOUPLE >> OKRUHLE ZATVORKY
## WSET >> ZLOZENE ZATVORKY {} >> NESMU BYT DUPLIKATY

# membership.py

items = ("coin", "book", "pencil", "spoon", "paper")

if "coin" in items:
    print("There is a coin in the tuple")
else:
    print("There is no coin in the tuple")

if "bowl" not in items:
    print("There is no bowl in the tuple")
else:
    print("There is a bowl in the tuple")