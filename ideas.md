# Ideas

## List of objects

Generate a CSV file with faker.  

```python

import csv, random
from faker import Faker 

faker = Faker()
file_name = 'users.csv'

jobs = ['teacher', 'writer', 'programmer', 'shopkeeper', 'driver', 'gardener']

with open(file_name, 'w') as f:

    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('first_name', 'last_name', 'country', 'date_of_birth', 'job'))

    for _ in range(30):
        fname = faker.first_name()
        lname = faker.last_name()
        job = random.sample(jobs, 1)[0]
        # job = faker.job()
        dob = faker.date_of_birth()
        country = faker.country()

        writer.writerow((fname, lname, country, dob, job))

```

List of objects created with dataclass or namedtuple.  

```python
import csv
from dataclasses import dataclass
from collections import namedtuple

# @dataclass
# class User:
#     first_name: str
#     last_name: str
#     counry: str
#     date_of_birth: str
#     job: str

User = namedtuple('User', 'first_name last_name country date_of_birth job')

users = []
file_name = 'users.csv'

with open(file_name, 'r') as f:

    reader = csv.reader(f)
    next(reader) # skips header

    for row in reader:
        users.append(User(*row))
 
for user in users[:11]:
    print(user)
```

List of objects as dictionaries. 

```python
import csv

users = []
file_name = 'users.csv'

with open(file_name, 'r') as f:

    reader = csv.DictReader(f)
    
    i = 1
    for row in reader:
        user = {}
        user['id'] = i
        user.update(row)
        users.append(user)
        i += 1
 
for user in users[:11]:
    print(user)

# print(users)
```

Sort by age 

```python
import csv
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta

User = namedtuple('User', 'first_name last_name country date_of_birth job')

users = []
file_name = 'users.csv'

def calculate_age(dob_str):
    # dob = datetime.strptime(dob_str, "%Y-%m-%d")
    dob = datetime.fromisoformat(dob_str)
    today = datetime.today()
    
    age = relativedelta(today, dob)
    
    return age.years

with open(file_name, 'r') as f:

    reader = csv.reader(f)
    next(reader) # skips header

    for row in reader:
        users.append(User(*row))
 

sorted_users = sorted(users, key=lambda u: calculate_age(u.date_of_birth), 
                      reverse=True)
# sorted_users = sorted(users, key=lambda u: u.date_of_birth)

for user in sorted_users:
    print(user)
```

## Ordered words

An ordered word is a word in which the letters appear in alphabetic order.  

Solution I

```python
import urllib.request

url = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'

words = urllib.request.urlopen(url).read().decode("utf-8").split()

ordered = [word for word in words if word==''.join(sorted(word))]
maxlen = len(max(ordered, key=len))

maxorderedwords = [word for word in ordered if len(word) == maxlen]
print(' '.join(maxorderedwords))
```

Solution II

```python
import urllib.request

mx, url = 0, 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'

for word in urllib.request.urlopen(url).read().decode("utf-8").split():
    lenword = len(word)
    if lenword >= mx and word==''.join(sorted(word)):
        if lenword > mx:
            words, mx = [], lenword
        words.append(word)
print(' '.join(words))
```

Solution III

```python
'''The longest ordered words in a list'''

from functools import reduce
from operator import le
import urllib.request


# longestOrds :: [String] -> [String]
def longestOrds(ws):
    '''The longest ordered words in a given list.
    '''
    return reduce(triage, ws, (0, []))[1]


# triage :: (Int, [String]) -> String -> (Int, [String])
def triage(nxs, w):
    '''The maximum length seen for an ordered word,
       and the ordered words of this length seen so far.
    '''
    n, xs = nxs
    lng = len(w)
    return (
        (lng, ([w] if n != lng else xs + [w])) if (
            ordered(w)
        ) else nxs
    ) if lng >= n else nxs


# ordered :: String -> Bool
def ordered(w):
    '''True if the word w is ordered.'''
    return all(map(le, w, w[1:]))


# ------------------------- TEST -------------------------
if __name__ == '__main__':
    print(
        '\n'.join(longestOrds(
            urllib.request.urlopen(
                'http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'
            ).read().decode("utf-8").split()
        ))
    )
```

## Anagrams


Solution I

```python
import urllib.request
from collections import defaultdict
words = urllib.request.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
anagram = defaultdict(list) # map sorted chars to anagrams
for word in words:
    anagram[tuple(sorted(word))].append( word )

	
count = max(len(ana) for ana in anagram.values())
for ana in anagram.values():
	if len(ana) >= count:
		print ([x.decode() for x in ana])
```


Solution II


```python
#!/usr/bin/python

import urllib, itertools
words = urllib.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
anagrams = [list(g) for k,g in itertools.groupby(sorted(words, key=sorted), key=sorted)]

count = max(len(ana) for ana in anagrams)
for ana in anagrams:
    if len(ana) >= count:
        print ana
```

Solution III

```python
'''Largest anagram groups found in list of words.'''

from os.path import expanduser
from itertools import groupby
from operator import eq


# main :: IO ()
def main():
    '''Largest anagram groups in local unixdict.txt'''

    print(unlines(
        largestAnagramGroups(
            lines(readFile('unixdict.txt'))
        )
    ))


# largestAnagramGroups :: [String] -> [[String]]
def largestAnagramGroups(ws):
    '''A list of the anagram groups of
       of the largest size found in a
       given list of words.
    '''

    # wordChars :: String -> (String, String)
    def wordChars(w):
        '''A word paired with its
           AZ sorted characters
        '''
        return (''.join(sorted(w)), w)

    groups = list(map(
        compose(list)(snd),
        groupby(
            sorted(
                map(wordChars, ws),
                key=fst
            ),
            key=fst
        )
    ))

    intMax = max(map(len, groups))
    return list(map(
        compose(unwords)(curry(map)(snd)),
        filter(compose(curry(eq)(intMax))(len), groups)
    ))


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    return lambda a: lambda b: f(a, b)


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# lines :: String -> [String]
def lines(s):
    '''A list of strings,
       (containing no newline characters)
       derived from a single new-line delimited string.'''
    return s.splitlines()


# from os.path import expanduser
# readFile :: FilePath -> IO String
def readFile(fp):
    '''The contents of any file at the path
       derived by expanding any ~ in fp.'''
    with open(expanduser(fp), 'r', encoding='utf-8') as f:
        return f.read()


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# unwords :: [String] -> String
def unwords(xs):
    '''A space-separated string derived from
       a list of words.'''
    return ' '.join(xs)


# MAIN ---
if __name__ == '__main__':
    main()
```




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
