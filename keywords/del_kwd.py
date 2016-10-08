#!/usr/bin/python

# del_kwd.py

class Rock:
    
    def __init__(self):
        
        self.weight = 4.5
        self.col = "gray"
        
    def __str__(self):
        
        attr = []
        
        for key, value in self.__dict__.iteritems():
            attr.append((key, value))
            
        return str(attr)    
        
rock = Rock()
print rock

del rock.col
print rock

a = [1, 2, 3, 4]

print a
del a[:2]
print a
