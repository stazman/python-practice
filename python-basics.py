# The return value of a method invocation that results in mutating a data structure is None

#Debugging in Python: put this code where you want to set a breakpoint for the debugging. You would put it in the same place you would put debugger in Chrome Dev Console for JS:

      # import pdb; pdb.set_trace()

      # https://codeburst.io/how-i-use-python-debugger-to-fix-code-279f11f75866#:~:text=Python%20has%20a%20built%2Din,that%20does%20the%20main%20job.&text=As%20soon%20as%20the%20interpreter,but%20with%20some%20new%20commands

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
