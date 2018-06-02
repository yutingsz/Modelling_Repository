# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:41:17 2018

@author: Ting Yu Dell
"""

# Numbers
17 / 3  # int / int -> float
17 / 3.0  # int / float -> float

# The // operator is also provided for doing floor division no matter what the operands are. 
17 // 3  # int / int -> int
# The remainder can be calculated with the % operator
17 % 3.0  # int / float -> float

5 ** 2  # 5 squared

#------------------------------------------------------
# String
#------------------------------------------------------
"Isn\'t, she said."

# End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#Strings can be concatenated (glued together) with the + operator, and repeated with *:
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
word = 'Python'
word[-1]  # last character

# This makes sure that s[:i] + s[i:] is always equal to s:
word[:2] + word[2:]

#------------------------------------------------------
# Lists
#------------------------------------------------------
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

list(range(5))


#------------------------------------------------------
# Arbitrary Argument Lists
#------------------------------------------------------
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

# Unpacking Argument Lists
# The reverse situation occurs when the arguments are already in a list or tuple 
# but need to be unpacked for a function call requiring separate positional arguments. 
# For instance, the built-in range() function expects separate start and stop arguments. 
# If they are not available separately, write the function call with the *-operator 
# to unpack the arguments out of a list or tuple:

list(range(3, 6))            # normal call with separate arguments
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list

#------------------------------------------------------
# Lambda Expressions
# Small anonymous functions can be created with the lambda keyword.
#------------------------------------------------------
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

#-----------------------------------------------------------
# List
#-----------------------------------------------------------
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.append('grape')
fruits.sort()
fruits.pop()

#-----------------------------------------------------------
# List Comprehensions
#-----------------------------------------------------------
squares = []
for x in range(10):
    squares.append(x**2)
    
# Note that this creates (or overwrites) a variable named x that still exists after the loop completes. 
# We can calculate the list of squares without any side effects using:
squares = list(map(lambda x: x**2, range(10)))
# or, equivalently:
squares = [x**2 for x in range(10)]

#For example, this listcomp combines the elements of two lists if they are not equal:
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#and it’s equivalent to:
# Note how the order of the for and if statements is the same in both these snippets.

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]

list(zip(*matrix))

#-----------------------------------------------------------
# Tuples 
#-----------------------------------------------------------
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)
t = (12345, 54321, 'hello!')

# The reverse operation is also possible:
x, y, z = t

#-----------------------------------------------------------
# Sets 
#-----------------------------------------------------------
set() # Empty Set

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
'orange' in basket                 # fast membership testing

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both

# Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}

#-----------------------------------------------------------
# Dictionaries
#-----------------------------------------------------------
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
sorted(tel.keys())
['guido', 'irv', 'jack']
'guido' in tel
'jack' not in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
{x: x**2 for x in (2, 4, 6)}

# Looping Techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
    
# When looping through a sequence, the position index 
# and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
    
# To loop over two or more sequences at the same time, 
# the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
# -------------------------------------------------------
# Generator Expressions
# -------------------------------------------------------
sum(i*i for i in range(10))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product


from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

unique_words = set(word  for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

#---------------------------------------------------------
# regular expression
#---------------------------------------------------------
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

#---------------------------------------------------------
# Random 
#---------------------------------------------------------
import random
random.choice(['apple', 'pear', 'banana'])

random.sample(range(100), 10)   # sampling without replacement
random.random()    # random float
random.randrange(6)    # random integer chosen from range(6)

#---------------------------------------------------------
# Date and Time
#---------------------------------------------------------
from datetime import date
now = date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday

#---------------------------------------------------------
# Precision
#---------------------------------------------------------
format(0.1, '.17f')



#---------------------------------------------------------
# Multi-threading
#---------------------------------------------------------
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')