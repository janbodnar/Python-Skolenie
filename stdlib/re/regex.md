# Regular expressions

*Regular expressions* are used for text searching and more advanced text manipulation.  
Regular expressions are built-in tools like grep, sed, text editors like vi, emacs,  
programming languages like Tcl, Perl, and Python.

## Python re module

In Python, the `re` module provides regular expression matching operations.  

A pattern is a regular expression that defines the text we are searching for  
or manipulating. It consists of text literals and metacharacters. The pattern is  
compiled with the compile function. Because regular expressions often include  
special characters, it is recommended to use raw strings. (Raw strings are preceded with r character.)  
This way the characters are not interpreded before they are compiled to a pattern.  

After we have compiled a pattern, we can use one of the functions to apply the pattern  
on a text string. The funcions include `match`, `search`, `find`, and `finditer`.  

## Regular expressions

The following table shows some basic regular expressions:  


- `.` -	matches any single character
- `?`	- matches the preceding element once or not at all
- `+` -	matches the preceding element once or more times
- `*`	- matches the preceding element zero or more times
- `^`	- matches the starting position within the string
- `$`	- matches the ending position within the string
- `|`	- alternation operator
- `[abc]` -	matches a or b, or c
- `[a-c]`	- range; matches a or b, or c
- `[^abc]` - negation, matches everything except a, or b, or c
- `\s` - matches white space character
- `\w` - matches a word character; equivalent to `[a-zA-Z_0-9]`

## The regex functions

We look for matches with regex functions.  


- `match`	- determines if the RE matches at the beginning of the string
- `fullmatch`	- determines if the RE matches the whole of the string
- `search` - scans through a string, looking for any location where this RE matches
- `findall`	- finds all substrings where the RE matches, and returns them as a list
- `finditer` - finds all substrings where the RE matches, and returns them as an iterator
- `split`	- splits the string by RE pattern

The `match`, `fullmatch`, and `search` functions return a match object if they are successful. 
Otherwise, they return `None`.

## The match function

The `match` function returns a match object if zero or more characters at the beginning  
of string match the regular expression pattern.

match_fun.py
#!/usr/bin/python

import re

words = ('book', 'bookworm', 'Bible', 
    'bookish','cookbook', 'bookstore', 'pocketbook')

pattern = re.compile(r'book')

for word in words:

    if re.match(pattern, word):
        print(f'The {word} matches')
In the example, we have a tuple of words. The compiled pattern will look for a 'book' string in each of the words.

pattern = re.compile(r'book')
With the compile function, we create a pattern. The regular expression is a raw string and consists of four normal characters.

for word in words:

    if re.match(pattern, word):
        print(f'The {word} matches')
We go through the tuple and call the match function. It applies the pattern on the word. The match function returns a match object if there is a match at the beginning of a string. It returns None if there is no match.

$ ./match_fun.py 
The book matches 
The bookworm matches 
The bookish matches 
The bookstore matches 
Four of the words in the tuple match the pattern. Note that the words that do not start with the 'book' term do not match. To include also these words, we use the search function.

The fullmatch function
The fullmatch function looks an exact match.

fullmatch_fun.py
#!/usr/bin/python

import re

words = ('book', 'bookworm', 'Bible', 
    'bookish','cookbook', 'bookstore', 'pocketbook')

pattern = re.compile(r'book')

for word in words:

    if re.fullmatch(pattern, word):
        print(f'The {word} matches')
In the example, we use the fullmatch function to look for the exact 'book' term.

$ ./fullmatch_fun.py 
The book matches
There is only one match.

The search function
The search function looks for the first location where the regular expression pattern produces a match.

search_fun.py
#!/usr/bin/python

import re

words = ('book', 'bookworm', 'Bible', 
    'bookish','cookbook', 'bookstore', 'pocketbook')

pattern = re.compile(r'book')

for word in words:

    if re.search(pattern, word):
        print(f'The {word} matches')   
In the example, we use the search function to look for the 'book' term.

$ ./search_fun.py 
The book matches 
The bookworm matches 
The bookish matches 
The cookbook matches 
The bookstore matches 
The pocketbook matches 
This time the cookbook and pocketbook words are included as well.

Dot metacharacter
The dot (.) metacharacter stands for any single character in the text.

dot_meta.py
#!/usr/bin/python

import re

words = ('seven', 'even', 'prevent', 'revenge', 'maven', 
    'eleven', 'amen', 'event')

pattern = re.compile(r'.even')

for word in words:
    if re.match(pattern, word):
        print(f'The {word} matches')
In the example, we have a tuple with eight words. We apply a pattern containing the dot metacharacter on each of the words.

pattern = re.compile(r'.even')
The dot stands for any single character in the text. The character must be present.

$ ./dot_meta.py 
The seven matches 
The revenge matches 
Two words match the pattern: seven and revenge.

Question mark meta character
The question mark (?) meta character is a quantifier that matches the previous element zero or one time.

question_mark_meta.py
#!/usr/bin/python

import re

words = ('seven', 'even','prevent', 'revenge', 'maven', 
    'eleven', 'amen', 'event')

pattern = re.compile(r'.?even')

for word in words:

    if re.match(pattern, word):
        print(f'The {word} matches')
In the example, we add a question mark after the dot character. This means that in the pattern we can have one arbitrary character or we can have no character there.

$ ./question_mark_meta.py 
The seven matches 
The even matches 
The revenge matches 
The event matches 
This time, in addition to seven and revenge, the even and event words match as well.

Anchors
Anchors match positions of characters inside a given text. When using the ^ anchor the match must occur at the beginning of the string and when using the $ anchor the match must occur at the end of the string.

anchors.py
#!/usr/bin/python

import re

sentences = ('I am looking for Jane.',
    'Jane was walking along the river.',
    'Kate and Jane are close friends.')

pattern = re.compile(r'^Jane')

for sentence in sentences:
    
    if re.search(pattern, sentence):
        print(sentence)
In the example, we have three sentences. The search pattern is ^Jane. The pattern checks if the "Jane" string is located at the beginning of the text. The Jane\. would look for "Jane" at the end of the sentence.

Exact match
An exact match can be performed with the fullmatch function or by placing the term between the anchors: ^ and $.

exact_match.py
#!/usr/bin/python

import re

words = ('book', 'bookworm', 'Bible', 
    'bookish','cookbook', 'bookstore', 'pocketbook')

pattern = re.compile(r'^book$')

for word in words:

    if re.search(pattern, word):
        print(f'The {word} matches')  
In the example, we look for an exact match for the 'book' term.

$ ./exact_match.py 
The book matches
Character classes
A character class defines a set of characters, any one of which can occur in an input string for a match to succeed.

character_class.py
#!/usr/bin/python

import re

words = ('a gray bird', 'grey hair', 'great look')

pattern = re.compile(r'gr[ea]y')

for word in words:

    if re.search(pattern, word):
        print(f'{word} matches') 
In the example, we use a character class to include both gray and grey words.

pattern = re.compile(r'gr[ea]y')
The [ea] class allows to use either 'e' or 'a' charcter in the pattern.

Named character classes
There are some predefined character classes. The \s matches a whitespace character [\t\n\t\f\v], the \d a digit [0-9], and the \w a word character [a-zA-Z0-9_].

named_character_class.py
#!/usr/bin/python

import re

text = 'We met in 2013. She must be now about 27 years old.'

pattern = re.compile(r'\d+')

found = re.findall(pattern, text)

if found:
    print(f'There are {len(found)} numbers')   
In the example, we count numbers in the text.

pattern = re.compile(r'\d+')
The \d+ pattern looks for any number of digit sets in the text.

found = re.findall(pattern, text)
With findall method, we look up all numbers in the text.

$ ./named_character_classes.py 
There are 2 numbers
Case insensitive match
By default, the matching of patterns is case sensitive. By passing the re.IGNORECASE to the compile function, we can make it case insensitive.

case_insensitive.py
#!/usr/bin/python

import re

words = ('dog', 'Dog', 'DOG', 'Doggy')

pattern = re.compile(r'dog', re.IGNORECASE)

for word in words:
    if re.match(pattern, word):
        print(f'{word} matches')
In the example, we apply the pattern on words regardless of the case.

$ ./case_insensitive.py 
dog matches
Dog matches
DOG matches
Doggy matches
All four words match the pattern.

Alternations
The alternation operator | creates a regular expression with several choices.

alternations.py
#!/usr/bin/python

import re

words = ("Jane", "Thomas", "Robert",
    "Lucy", "Beky", "John", "Peter", "Andy")

pattern = re.compile(r'Jane|Beky|Robert')

for word in words:
    
    if re.match(pattern, word):
        print(word)
We have eight names in the list.

pattern = re.compile(r'Jane|Beky|Robert')
This regular expression looks for "Jane", "Beky", or "Robert" strings.

The finditer function
The finditer function returns an iterator yielding match objects over all non-overlapping matches for the pattern in a string.

finditer_fun.py
#!/usr/bin/python

import re

text = 'I saw a fox in the wood. The fox had red fur.'

pattern = re.compile(r'fox')

found = re.finditer(pattern, text)

for item in found:

    s = item.start()
    e = item.end()
    print(f'Found {text[s:e]} at {s}:{e}')
In the example, we search for the 'fox' term in the text. We go over the iterator of the found matches and print them with their indexes.

s = item.start()
e = item.end()
The start and end functions return the starting and ending index, respectively.

$ ./finditer_fun.py 
Found fox at 8:11
Found fox at 29:32
Capturing groups
Capturing groups is a way to treat multiple characters as a single unit. They are created by placing characters inside a set of round brackets. For instance, (book) is a single group containing 'b', 'o', 'o', 'k', characters.

The capturing groups technique allows us to find out those parts of a string that match the regular pattern.

capturing_groups.py
#!/usr/bin/python

import re

content = '''<p>The <code>Pattern</code> is a compiled
representation of a regular expression.</p>'''

pattern = re.compile(r'(</?[a-z]*>)')

found = re.findall(pattern, content)

for tag in found:
    print(tag)
The code example prints all HTML tags from the supplied string by capturing a group of characters.

found = re.findall(pattern, content)
In order to find all tags, we use the findall method.

$ ./capturing_groups.py 
<p>
<code>
</code>
</p>
We have found four HTML tags.

Python regex email example
In the following example, we create a regex pattern for checking email addresses.

emails.py
#!/usr/bin/python

import re

emails = ("luke@gmail.com", "andy@yahoocom", 
    "34234sdfa#2345", "f344@gmail.com")

pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')

for email in emails:

    if re.match(pattern, email):
        print(f'{email} matches')
    else:
        print(f'{email} does not match')
This example provides one possible solution.

pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')    
The first ^ and the last $ characters provide an exact pattern match. No characters before and after the pattern are allowed. The email is divided into five parts. The first part is the local part. This is usually a name of a company, individual, or a nickname. The [a-zA-Z0-9._-]+ lists all possible characters, we can use in the local part. They can be used one or more times.

The second part consists of the literal @ character. The third part is the domain part. It is usually the domain name of the email provider such as Yahoo, or Gmail. The [a-zA-Z0-9-]+ is a character class providing all characters that can be used in the domain name. The + quantifier allows to use of one or more of these characters.

The fourth part is the dot character. It is preceded by the escape character (\) to get a literal dot.

The final part is the top level domain: [a-zA-Z.]{2,18}. Top level domains can have from 2 to 18 characters, such as sk, net, info, travel, cleaning, travelinsurance. The maximum length can be 63 characters, but most domain are shorter than 18 characters today. There is also a dot character. This is because some top level domains have two parts; for instance co.uk.

$ ./emails.py 
luke@gmail.com matches
andy@yahoocom does not match
34234sdfa#2345 does not match
f344@gmail.com matches
