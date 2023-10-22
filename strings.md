# Strings 


A *string* in Python is a sequence of characters. Strings are immutable; this means that once defined,  
they cannot be changed. Many Python methods, such as `replace`, `join`, or `split` modify strings.  
However, they do not modify the original string. They create a copy of a string which they modify  
and return to the caller.

## String literals

Python strings can be created with single quotes, double quotes, or triple quotes. When we use triple  
quotes, strings can span several lines without using the escape character.  

```python
#!/usr/bin/python

# string_literals.py

a = "proximity alert"
b = 'evacuation'
c = """
requiem
for
a
tower
"""

print(a)
print(b)
print(c)
```

In our example we assign three string literals to a, b, and c variables. And we print them  
to the console.

```
$ ./string_literals.py
proximity alert
evacuation

requiem
for
a
tower
Unicode in Python
```

If we want to create Unicode strings, we add a u or U character at the beginning of the text.

```python
#!/usr/bin/python

# unicode.py

text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

print(text)
```

In our example, we print Leo Tolstoy: Anna Karenina in Cyrillic.

```
$ ./unicode.py
Лев Николаевич Толстой:
Анна Каренина
```

We can use the Russian letters directly.

```python
#!/usr/bin/python

# unicode2.py

text = 'Лев Николаевич Толстой: Анна Каренина'

print(text)
```

In this example, we use non-latin characters directly in the source code.  
We have defined UTF-8 encoding with a encoding comment.  


## Using quotes

Strings in Python are delimited by single or double quote characters. What if we wanted to  
display quotes, for example in a direct speech? There are two basic ways to do this. 

```python
#!/usr/bin/python

# quotes.py

print("There are many stars.")
print("He said, \"Which one is your favourite?\"")

print('There are many stars.')
print('He said, "Which one is your favourite?"')
```

We use the `\` character to escape additional quotes. Normally the double quote character is  
used to delimit a string literal. However, when escaped, the original meaning is suppressed.  
It appears as a normal character and can be used within a string literal. The second way to  
use quotes within quotes is to mix single and double quotes.

```
$ ./quotes.py
There are many stars.
He said, "Which one is your favourite?"
There are many stars.
He said, "Which one is your favourite?"
```

## String length

The `len` method calculates the number of characters in a string. The white characters are also counted. 

```python
#!/usr/bin/python

# string_length.py

s1 = "Eagle"
s2 = "Eagle\n"
s3 = "Eagle  "

print(len(s1))
print(len(s2))
print(len(s3))
We compute the length of three strings.

s1 = "Eagle"
s2 = "Eagle\n"
s3 = "Eagle  "
```

Three strings are defined. The second string has a new line character at its end.  
The third has two additional space characters.

```python
print(len(s1))
```

We print the number of characters to the console.

```python
$ ./length.py
5
6
7
```

From the output we can see that the white spaces (new line character and space characters in our case)  
are counted, too.

## Stripping white characters

In string processing, we might often end up with a string that has white characters at the beginning  
or at the end of a string. The term white spaces (characters) refers to invisible characters  
like new line, tab, space or other control characters. We have the `strip`, `lstrip`, and `rstrip`  
methods to remove these characters.

```python
#!/usr/bin/python

# strippig.py

s = " Eagle  "

s2 = s.rstrip()
s3 = s.lstrip()
s4 = s.strip()

print('{0} {1}'.format(s, len(s)))
print('{0} {1}'.format(s2, len(s2)))
print('{0} {1}'.format(s3, len(s3)))
print('{0} {1}'.format(s4, len(s4)))
```

We apply the stripping methods on a string word which has three white spaces. One space at the start and  
two spaces at the end. Note that these methods remove any number of white spaces, not just one.  

```python
s2 = s.rstrip()
```

The rstrip method returns a string with the trailing white space characters removed.

```python
s3 = s.lstrip()
```

The `lstrip` method returns a string with the leading white space characters removed.

```python
s4 = s.strip()
```

The strip method returns a copy of the string with the leading and trailing characters removed.  

```python
print('{0} {1}'.format(s2, len(s2)))
```

The `format` method is used to dynamically build a string. The `{0}` is a control character referring  
to the first parameter of the format method. The `{1}` refers to the second parameter.  

```
$ ./stripping.py
 Eagle   8
 Eagle 6
Eagle   7
Eagle 5
```

## Escape sequences

When we work with strings, we can use escape sequences. The escape sequences are special characters have  
a specific purpose, when used within a string.

```python
print("   bbb\raaa") # prints aaabbb
```

The carriage return `\r` is a control character for end of line return to beginning of line.

```python
#!/usr/bin/python

# strophe.py

print("Incompatible, it don't matter though\n'cos someone's bound to hear my cry")
print("Speak out if you do\nYou're not easy to find")
```

The new line is a control character, which begins a new line of text.

```
$ ./strophe.py
Incompatible, it don't matter though
'cos someone's bound to hear my cry
Speak out if you do
You're not easy to find
Next we examine the backspace control character.
```

```python
print("Python\b\b\booo") # prints Pytooo
```

The backspace control character `\b` moves the cursor one character back. In our case,   
we use three backspace characters to delete three letters and replace them with three o characters. 

```python
print("Towering\tinferno") # prints Towering        inferno
```

The horizontal tab puts a space between text.

```
"Johnie's dog"
'Johnie\'s dog'
```

Single and double quotes can be nested. Or in case we use only single quotes, we can use the  
backslash to escape the default meaning of a single quote. 

If we prepend an r to the string, we get a raw string. The escape sequences are not interpreted.  

```python
#!/usr/bin/python

# raw.py

print(r"Another world\n")
```

```
$ ./raw.py
Another world\n
```

We get the string with the new line character included.

## Comparing strings
Comparing strings is a common job in programming. We can compare two strings with the `==` operator.  
We can check the opposite with the non-equality `!=` operator. The operators return a boolean `True` or `False`.

```python
#!/usr/bin/python

# comparing.py

print("12" == "12")
print("17" == "9")
print("aa" == "ab")

print("abc" != "bce")
print("efg" != "efg")
```

In this code example, we compare some strings.

```python
print("12" == "12")
```

These two strings are equal, so the line returns True.

```python
print("aa" == "ab")
```

The first two characters of both strings are equal. Next the following characters are  
compared. They are different so the line returns `False`.

```python
print("abc" != "bce")
```

Since the two strings are different, the line returns `True`.

```python
$ ./comparing.py
True
False
False
True
False
```

## Accessing string elements

It is possible to access string elements in Python.

```python
#!/usr/bin/python

# string_elements.py

s = "Eagle"

print(s[0])
print(s[4])
print(s[-1])
print(s[-2])

print("****************")

print(s[0:4])
print(s[1:3])
print(s[:])
```

An index operation is used to get elements of a string.

```python
print(s[0])
print(s[4])
```

The first line prints the first character. The second line prints the fifth character. The indexes  
start from zero.  

```python
print(s[-1])
print(s[-2])
```

When the index is negative, we retrieve elements from the end of the string. In this case, we print   
the last and last but one characters.

```python
print(s[0:4])
```

Ranges of characters can be accessed too. This line prints a range of characters starting from the   
first and ending with the fourth character.  

```python
print(s[:])
```

This line prints all the characters from the string.

```
$ ./string_elements.py
E
e
e
l
****************
Eagl
ag
Eagle
```

A for loop can be used to traverse all characters of a string.

```python
#!/usr/bin/python

# traverse.py

s = "ZetCode"

for i in s:
  print(i, " ", end="")
```

The script prints all the characters of a given string to the console.

```
$ ./traverse.py
Z e t C o d e
```

## Finding substrings

The `find`, `rfind`, `index` and `rindex` methods are used to find substrings in a string. They return   
the index of the first occurrence of the substring. The find and index methods search from the  
beginning of the string. The rfind and rindex search from the end of the string.

The difference between the find and index methods is that when the substring is not found, the former 
returns -1. The latter raises `ValueError` exception.

```
find(str, beg=0, end=len(string))
rfind(str, beg=0, end=len(string))
index(str, beg=0, end=len(string))
rindex(str, beg=0, end=len(string))
```

The `str` is the substring to be searched for. The beg parameter is the starting index, by default it is 0.  
The end parameter is the ending index. It is by default equal to the length of the string.

```python
#!/usr/bin/python

# substrings.py

a = "I saw a wolf in the forest. A lone wolf."

print(a.find("wolf"))
print(a.find("wolf", 10, 20))
print(a.find("wolf", 15))

print(a.rfind("wolf"))
```

We have a simple sentence. We try to find the index of a substring in the sentence.

```python
print(a.find("wolf"))
```

The line finds the first occurrence of the substring 'wolf' in the sentence. It prints 8.

```python
print(a.find("wolf", 10, 20))
```

This line tries to find a 'wolf' substring. It starts from the 10th character and searches  
the next 20 characters. There is no such substring in this range and therefore the line  
prints -1, as for not found.

```python
print(a.find("wolf", 15))
```

Here we search for a substring from the 15th character until the end of the string. We find  
the second occurrence of the substring. The line prints 35.

```python
print(a.rfind("wolf"))
```

The `rfind` looks for a substring from the end. It finds the second occurrence of the 'wolf' substring.  
The line prints 35.

```
$ ./substrings.py
8
-1
35
35
```

In the second example, we use the index and `rindex` methods.

```python
#!/usr/bin/python

# substrings2.py

a = "I saw a wolf in the forest. A lone wolf."

print(a.index("wolf"))
print(a.rindex("wolf"))

try:
    print(a.rindex("fox"))
except ValueError as e:
    print("Could not find substring")
```

In the example, we search for substrings with the `index` and `rindex` methods.

```python
print(a.index("wolf"))
print(a.rindex("wolf"))
```

These lines find the first occurrence of the 'wolf' substring from the beginning and from the end.

```python
try:
    print(a.rindex("fox"))
except ValueError as e:
    print("Could not find substring")
```

When the substring is not found, the `rindex` method raises `ValueError` exception.

```python
$ ./substrings2.py
8
35
Could not find substring
```

## Basic string operations

In the next example, we do string multiplication and concatenation.

```python
#!/usr/bin/python

# add_multiply.py

print("eagle " * 5)

print("eagle " "falcon")

print("eagle " + "and " + "falcon")
```

The `*` operator repeates the string n times. In our case five times. Two string literals next to  
each other are automatically concatenated. We can also use the `+` operator to explicitly concatenate the strings.

```python
$ ./add_multiply.py
eagle eagle eagle eagle eagle
eagle falcon
eagle and falcon
```

We can use the len function to calculate the length of the string in characters.

```python
#!/usr/bin/python

# eagle.py

word = 'eagle'

print(word, "has", len(word), "characters")
```

In the example, we compute the number of characters in a string variable.  

```python
$ ./eagle.py
eagle has 5 characters
```

Some programming languages enable implicit addition of strings and numbers. In Python language,  
this is not possible. We must explicitly convert values.  

```python
#!/usr/bin/python

# string_number.py

print(int("12") + 12)
print("There are " + str(22) + " oranges.")
print(float('22.33') + 22.55)
```

We use a built-in int function to convert a string to integer. And there is also a built-in `str` 
function to convert a number to a string. And we use the float function to convert a string to  
a floating point number.

## Replacing strings

The `replace` method replaces substrings in a string with other substrings. Since strings in Python  
are immutable, a new string is built with values replaced.

```python
replace(old, new [, max])
```

By default, the replace method replaces all occurrences of a substring. The method takes a third argument  
which limits the replacements to a certain number.

```python
#!/usr/bin/python

# replacing.py

a = "I saw a wolf in the forest. A lonely wolf."

b = a.replace("wolf", "fox")
print(b)

c = a.replace("wolf", "fox", 1)
print(c)
```

We have a sentence where we replace 'wolf' with 'fox'.

```python
b = a.replace("wolf", "fox")
```

This line replaces all occurrences of the 'wolf' with 'fox'.

```python
c = a.replace("wolf", "fox", 1)
```

Here we replace only the first occurrence.

```
$ ./replacing.py
I saw a fox in the forest. A lonely fox.
I saw a fox in the forest. A lonely wolf.
```

## Splitting and joining strings

A string can be split with the split or the rsplit method. They return a list of strings which were  
cut from the string using a separator. The optional second parameter is the maximum splits allowed.  

```python
#!/usr/bin/python

# splitting.py

nums = "1,5,6,8,2,3,1,9"

k = nums.split(",")
print(k)

l = nums.split(",", 5)
print(l)

m = nums.rsplit(",", 3)
print(m)
```

We have a comma-delimited string. We cut the string into parts.

```python
k = nums.split(",")
```

We split the string into eight parts using a comma as a separator. The method returns  
a list of eight strings.

```python
l = nums.split(",", 5)
```

Here we split the string into six parts. There are five substrings and the remainder of the string.

```python
m = nums.rsplit(",", 3)
```

Here we split the string into four parts. This time the splitting goes from the right.

```python
$ ./splitting.py
['1', '5', '6', '8', '2', '3', '1', '9']
['1', '5', '6', '8', '2', '3,1,9']
['1,5,6,8,2', '3', '1', '9']
```

Strings can be joined with the join string. It returns a string concatenated from the strings passed  
as a parameter. The separator between elements is the string providing this method.

```python
#!/usr/bin/python

# split_join.py

nums = "1,5,6,8,2,3,1,9"

n = nums.split(",")
print(n)

m = ':'.join(n)
print(m)
```

First we split a string into a list of strings. Then we join the strings into one string with the  
elements being separated by the provided character.

```python
m = ':'.join(n)
```

The join method creates one string from a list of strings. The elements are separated by the `:` character.

```
$ ./split_join.py
['1', '5', '6', '8', '2', '3', '1', '9']
1:5:6:8:2:3:1:9
```

Another method which can be used for splitting strings is partition. It will split the string at the first  
occurrence of the separator and return a 3-tuple containing the part before the separator, the separator  
itself, and the part after the separator.

```python
#!/usr/bin/python

# partition.py

s = "1 + 2 + 3 = 6"

a = s.partition("=")

print(a)
```

We use the partition method in this example.

```python
a = s.partition("=")
```

This will cut the string into three parts. One before the `=` character, the separator, and the right side  
after the separator.

```python
$ ./partition.py
('1 + 2 + 3 ', '=', ' 6')
```

## String case

Python has four string methods to work with the case of the strings. These methods return  
a new modified string.

```python
#!/usr/bin/python

# convert_case.py

a = "ZetCode"

print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())
```

We have a string word on which we demonstrate the four methods.

```python
print(a.upper())
```

The upper method returns a copy of the string where all characters are converted to uppercase.

```python
print(a.lower())
```

Here we get a copy of the string in lowercase letters.

```python
print(a.swapcase())
```

The swapcase method swaps the case of the letters. Lowercase characters will be uppercase and vice versa.

```python
print(a.title())
```

The title method returns a copy of the string, where the first character is in uppercase and the  
remaining characters are in lowercase.

```
$ ./convert_case.py
ZETCODE
zetcode
zETcODE
Zetcode
```

## String operations

There are several useful built-in functions that can be used for working with strings.

```python
#!/usr/bin/python

# letters.py

sentence = "There are 22 apples"

alphas = 0
digits = 0
spaces = 0

for i in sentence:

   if i.isalpha():
      alphas += 1

   if i.isdigit():
      digits += 1

   if i.isspace():
      spaces += 1

print("There are", len(sentence), "characters")
print("There are", alphas, "alphabetic characters")
print("There are", digits, "digits")
print("There are", spaces, "spaces")
```

In our example, we have a string sentence. We calculate the absolute number of characters, number of  
alphabetic characters, digits and spaces in the sentence. To do this, we use the following functions:  
`len`, `isalpha`, `isdigit`, and `isspace`.

```
$ ./letters.py
There are 19 characters
There are 14 alphabetic characters
There are 2 digits
There are 3 spaces
```

In the next example, we print the results of football matches.

```python
#!/usr/bin/python

# teams1.py

print("Ajax Amsterdam" " - " "Inter Milano " "2:3")
print("Real Madridi" " - " "AC Milano " "3:3")
print("Dortmund" " - " "Sparta Praha " "2:1")
```

We already know that adjacent strings are concatenated.

```
$ ./teams1.py
Ajax Amsterdam - Inter Milano 2:3
Real Madridi - AC Milano 3:3
Dortmund - Sparta Praha 2:1
Next, we improve the look of the output.
```

```python
#!/usr/bin/python

# teams2.py

teams = {
      0: ("Ajax Amsterdam", "Inter Milano"),
      1: ("Real Madrid", "AC Milano"),
      2: ("Dortmund", "Sparta Praha")
}

results = ("2:3", "3:3", "2:1")

for i in teams:

   line = teams[i][0].ljust(16) + "-".ljust(5) + teams[i][1].ljust(16) + results[i].ljust(3)
   print(line)
```

The `ljust` method returns a left justified string, the rjust method returns a right justified  
string. If the string is smaller than the width that we provided, it is filled with spaces. 

```
$ ./teams2.py
Ajax Amsterdam  -    Inter Milano    2:3
Real Madrid     -    AC Milano       3:3
Dortmund        -    Sparta Praha    2:1
```

Now the output looks better.

## String formatting

String formatting is dynamic putting of various values into a string. String formatting can be  
achieved with the `%` operator or the format method.

```python
#!/usr/bin/python

# oranges.py

print('There are %d oranges in the basket' % 32)
print('There are {0} oranges in the basket'.format(32))
```

In the code example, we dynamically build a string. We put a number in a sentence.

```python
print('There are %d oranges in the basket' % 32)
```

We use the `%d` formatting specifier. The d character means that we are expecting an integer.  
After the string, we put a modulo operator and an argument. In this case we have an integer value.

```python
print('There are {0} oranges in the basket'.format(32))
```

The same task is achieved with the format method. This time the formatting specifier is `{0}`.

```
$ ./oranges.py
There are 32 oranges in the basket
There are 32 oranges in the basket
```

The next example shows how to add more values into a string.

```python
#!/usr/bin/python

# fruits.py

print('There are %d oranges and %d apples in the basket' % (12, 23))
print('There are {0} oranges and {1} apples in the basket'.format(12, 23))
```

In both lines, we add two format specifiers.

```
$ ./fruits.py
There are 12 oranges and 23 apples in the basket
There are 12 oranges and 23 apples in the basket
```

In the next example, we build a string with a float and a string value.

```python
#!/usr/bin/python

# height.py

print('Height: %f %s' % (172.3, 'cm'))
print('Height: {0:f} {1:s}'.format(172.3, 'cm'))
```

We print the height of a person.

```python
print('Height: %f %s' % (172.3, 'cm'))
```

The formatting specifier for a float value is %f and for a string `%s`.

```python
print('Height: {0:f} {1:s}'.format(172.3, 'cm'))
```

With the format method, we add f and s characters to the specifier.

```python
$ ./height.py
Height: 172.300000 cm
Height: 172.300000 cm
```

We might not like the fact that the number in the previous example has 6 decimal places  
by default. We can control the number of the decimal places in the formatting specifier.

```python
#!/usr/bin/python

# height2.py

print('Height: %.2f %s' % (172.3, 'cm'))
print('Height: {0:.2f} {1:s}'.format(172.3, 'cm'))
```

The decimal point followed by an integer controls the number of decimal places.  
In our case, the number will have two decimal places.

```python
$ ./height2.py
Height: 172.30 cm
Height: 172.30 cm
```

The following example shows other formatting options.

```python
#!/usr/bin/python

# various.py

# hexadecimal
print("%x" % 300)
print("%#x" % 300)

# octal
print("%o" % 300)

# scientific
print("%e" % 300000)
```

The first two formats work with hexadecimal numbers. The x character will format the number in  
hexadecimal notation. The `#` character adda `0x` to the hexadecimal number. The `o` character shows the number 
in octal format. The `e` character will show the number in scientific format.

```python
$ ./various.py
12c
0x12c
454
3.000000e+05
```

The format method also supports the binary format.

```python
#!/usr/bin/python

# various2.py

# hexadecimal
print("{:x}".format(300))
print("{:#x}".format(300))

# binary
print("{:b}".format(300))

# octal
print("{:o}".format(300))

# scientific
print("{:e}".format(300000))
```

The example prints numbers in hexadecimal, binary, octal, and scientific formats.

The next example prints three columns of numbers.

```python
#!/usr/bin/python

# columns1.py

for x in range(1, 11):
    print('%d %d %d' % (x, x*x, x*x*x))
```

The numbers are left justified and the output is not optimal.

```
$ ./columns1.py
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
```

To correct this, we use the width specifier. The width specifier defines the minimal width  
of the object. If the object is smaller than the width, it is filled with spaces.

```python
#!/usr/bin/python

# columns2.py

for x in range(1, 11):
    print('%2d %3d %4d' % (x, x*x, x*x*x))
```

Now the output looks OK. Value 2 makes the first column to be 2 charactes wide.

```
$ ./columns2.py
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Now we have the improved formatting with the format method.

```python
#!/usr/bin/python

# columns3.py

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
```

