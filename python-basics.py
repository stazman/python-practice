if 5<10:
 print("Hello World!")
 print("Hello again")

x = "hello"
y = "world"

x = "Goodbye"

print(x)
print(y)


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

import random

print(random.randrange(1, 10))






