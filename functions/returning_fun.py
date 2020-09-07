#!/usr/bin/python

# Python allows to return nested functions

def do_output(shape):

    def rectangle():

        return '''
*********
*********'''

    def triangle():

        return '''
  *
 ***
*****'''

    if shape == 'rectangle':
        return rectangle

    if shape == 'triangle':
        return triangle


f = do_output('triangle')
print(f())

print()

f = do_output('rectangle')
print(f())
