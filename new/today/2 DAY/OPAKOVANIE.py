
# 1 print first, fourth, last, last but one character
msg = 'and old falcon in the sky'
print(msg[0])
print(msg[3])
print(msg[-1])
print(msg[-2])


# 2 print first, second, last, last but one word
msg2 = 'and old falcon in the sky'
mywords = msg2.split(' ') #ak nedam parameter default je medzera
#print(mywords)
print(mywords[0])
print(mywords[1])
print(mywords[-1])
print(mywords[-2])


# create message John Doe is a gardener
# and lives in New York
name = "John Doe"
occupation = "gardener"
city = 'New York'

print(f'{name} is a {occupation} and lives in {city}')
print(name , "is a ", occupation )


# calculate the sum of positive values
vals = [1, 0, -3, 4, 5, -6, -7, 3, -1]
my_sum = 0

for i in vals:
    if i > 0:
        my_sum = my_sum + i
print(my_sum)


# print words that start with w or c
words = ['sky', 'cup', 'water', 'warm', 'spy', 'cloud', 'necessity']

for i  in words:
    if i.startswith('w') or i.startswith('c'):
        print(i, end= " ")
