# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:13:44 2018

@author: Ting Yu Dell
"""

#-----------------------------------------------------------
# Output
# Python has ways to convert any value to a string: 
# pass it to the repr() or str() functions.
s = 'Hello, world.'
str(s)
repr(s)

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

import math
print('The value of PI is approximately %5.3f.' % math.pi)

f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()
f.closed

# f.readline() reads a single line from the file
f.readline()
for line in f:
    print(line, end='')
    

# Saving structured data with json
import json
# view its JSON string representation with a simple line of code:
json.dumps([1, 'simple', 'list'])

# called dump(), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:
json.dump(x, f)

x = json.load(f)