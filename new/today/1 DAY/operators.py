a = b = c = d = e = 10

print(b)

power = 2 ** 2
print(power)

div = 11 / 2  # div with decimal
print(div)

div2 = 11 // 2  # div without decimal >> nezaokluhluje
print(div2)

###############################################################
x = 2
word = " apples"

msg = str(x) + word
print(msg)

###############################################################

x = '11'
z = '2'

print(x + z)

print(int(x) + int(z))
###############################################################
print(not 4 < 3)  ##ret true
print(not 4 > 3)  ## ret false

###############################################################
words = ['sky', 'war', 'rock']

if 'sky' in words:
    print('word sky is in the list')

if 'water' not in words:
    print('word water is not in the list')
