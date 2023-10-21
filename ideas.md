# Ideas

## Roman numbers

Solution I

```python
anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M CM D CD C XC L XL X IX V IV I".split()

def to_roman(x):
    ret = []
    for a,r in zip(anums, rnums):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)
        
if __name__ == "__main__":
    test = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,40,
            50,60,69,70,80,90,99,100,200,300,400,500,600,666,700,800,900,
            1000,1009,1444,1666,1945,1997,1999,2000,2008,2010,2011,2500,
            3000,3999)
    
    for val in test:
        print '%d - %s'%(val, to_roman(val))
```

Solution II

```python
'''Encoding Roman Numerals'''

from functools import reduce
from itertools import chain


# romanFromInt ::  Int -> String
def romanFromInt(n):
    '''A string of Roman numerals encoding an integer.'''
    def go(a, ms):
        m, s = ms
        q, r = divmod(a, m)
        return (r, s * q)

    return concat(snd(mapAccumL(go)(n)(
        zip([
            1000, 900, 500, 400, 100, 90, 50,
            40, 10, 9, 5, 4, 1
        ], [
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L',
            'XL', 'X', 'IX', 'V', 'IV', 'I'
        ])
    )))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Sample of years'''
    for s in [
            romanFromInt(x) for x in [
                1666, 1990, 2008, 2016, 2018, 2020
            ]
    ]:
        print(s)


# ------------------ GENERIC FUNCTIONS -------------------

# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xxs):
    '''The concatenation of all the elements in a list.'''
    xs = list(chain.from_iterable(xxs))
    unit = '' if isinstance(xs, str) else []
    return unit if not xs else (
        ''.join(xs) if isinstance(xs[0], str) else xs
    )


# mapAccumL :: (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
def mapAccumL(f):
    '''A tuple of an accumulation and a list derived by a
       combined map and fold,
       with accumulation from left to right.'''
    def go(a, x):
        tpl = f(a[0], x)
        return (tpl[0], a[1] + [tpl[1]])
    return lambda acc: lambda xs: (
        reduce(go, xs, (acc, []))
    )


# snd :: (a, b) -> b
def snd(tpl):
    '''Second component of a tuple.'''
    return tpl[1]


# MAIN ---
if __name__ == '__main__':
    main()
```
