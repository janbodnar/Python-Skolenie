word = 'lake'
word2 = word.upper()

print(word, word2)

###########################################

word3 = '1,2,3,4,5'

fields = word3.split(',')

vals = list(map(int, fields))  ##zbavim sa uvodzoviek

print(fields)
print(word3)
print(vals)

###############################################################################
name = 'Peter'
age = 22
weight = 56.7

## %s >> string %d >> integer (decimal) %f >> float , %.2f >> zaokruhli na 2 des
print('%s is %d years old and he has %.2f weight'  % (name, age, weight))

print('{} is {} years old and he has {} weight'.format(name,age,weight))

print(f'{name} is {age} years old and he has {weight} weight')  ## f aby sa premenne evauovali

