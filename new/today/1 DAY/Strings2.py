###############################################################################
name = 'Peter'
age = 22
weight = 56.7

## %s >> string %d >> integer (decimal) %f >> float , %.2f >> zaokruhli na 2 des
print('%s is %d years old and he has %.2f weight'  % (name, age, weight))

print('{} is {} years old and he has {} weight'.format(name,age,weight))

print(f'{name} is {age} years old and he has {weight} weight')  ## f aby sa premenne evauovali

