actors = ["Jack Nicholson", "Antony Hopkins", "Adrien Brody"]
print(type(actors))

actors2 = tuple(actors)
print(actors2)

#simple_list.py

num = [10, 0, 2, 5, 4, 6, 7]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(num[0])
print(num[2:])
print(len(num))
print(num + [8, 9])

###############################################

vals = (10, 0, 2, 5, 4, 6, 7)
sorted_vals = sorted((vals))
print(sorted_vals)

sorted_vals2 = sorted(vals, reverse=True)
print(sorted_vals2)