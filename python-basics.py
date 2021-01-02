#This is a single-line comment. Python doesn't have multi-line comments per se,
# but you can use a multi-line string (three quotation marks before and after comment)

"""
This is a comment
written in
more than just one line
"""

'''
This is a comment
written in
more than just one line
'''

x = "l"

print(x)

#Are all variables always in global scope?

#x = bool(0)
y = bool("")
z = bool(False)
#display x:
print(x)
print(y)
print(z)

#display the data type of x:
print(type(x)) 


# Casting

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(x)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

f = 5
g = float(f)

print(g)


# No random function like Math.random() in JavaScript

import random

print(random.randrange(1, 10))


# Global Variables with global keyword (different than JavaScript)

# The local_var function is invoked  

foo = "Constantinople"

def local_var():
  foo = "Istanbul"
  print(foo)

local_var()

print(foo)


def global_var():
  global foo
  foo = "Istanbul"

global_var()

print(foo)



