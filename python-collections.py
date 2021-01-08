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

# You can use the literal or list constructor to create a list. Note the double round brackets in the constructor:

l = [1,2,3,4] # literal

l2 = list(('cat', 3, True, None, True)) # constructor

for item in l:
  print(item)

for item in l2:
  print(item)


# Accessing list items

print(l2[0])

print(l2[-1])

print(l2[0:2]) # not inclusive of item at index 2

print(l2[2:]) # inclusive of item at index 2

print(l2[:2]) # not inclusive of item at index 2


#Tuples

# A tuple is a collection which is ordered and unchangeable.

# A tuple is similar to an enum in Java or objects passed through Object.freeze() in JavaScript, which are unchangeable.

  # JavaScript ... const arr = [1,2,3,4]; Object.freeze(arr); arr.pop() will result in an error
  # Java ... enum TestEnum = { YESTERDAY, TODAY, TOMORROW };

# Since tuples are indexed, lists can have items with the same value

# Tuples are used to store multiple items in a single variable.

# Tuples are written with round brackets.

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

test_tuple_one_item = ( "happy", )
# OR
test_tuple_one_item_constructor = tuple(("happy", ))
# note double round brackets ... without them, it will turn each character in "happy" into an item

print(test_tuple_one_item)
print(test_tuple_one_item_constructor)

print(len(test_tuple_one_item))



#Sets





#Dictionaries