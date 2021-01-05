# Collections

# Python has no "new" keyword to instantiate a built-in data type

a = list()
b = tuple()
c = range(6)
d = set()
e = dict()

print(a)
print(b)
print(c)
print(d)
print(e)

"""
[]
()
range(0, 6)
set()
{}
"""

#Lists

# As an array in JS can, a List can contain multiple data types

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Since lists are indexed, lists can have items with the same value

# You can use the literal or list constructor to create a list. Note the double round brackets in hte constructor:

l = [1,2,3,4]

l2 = list(('cat', 3, True, None, True))

for item in l:
  print(item)

for item in l2:
  print(item)


# Accessing list items

print(l2[0])

print(l2[-1])

print(l2[0:2]) # not inclusive of 2

print(l2[2:]) # not inclusive of 2

print(l2[:2]) # not inclusive of 2


#Tuples

# A tuple is similar to an enum in Java. It is unchangeable.



#Sets



#Dictionaries