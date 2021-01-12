# Collections

# All collections are a way to store multiple values in one variable

# Collections are a way to Python has no "new" keyword to instantiate a built-in data type such as in JavaScript and Java

# Two ways of creating all collections: assigning a literal to a variable or using a constructor. Here are the constructors:

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

# All collections can have values of any data type, and they can be of different kinds within a single collection

# Note: printing the execution of adding/changing/removing an item in/to a collection returns None whereas in JavaScript it results the item/element added/changed/removed.



#Lists

# As an array in JS can, a List can contain multiple data types

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Since lists are indexed, lists can have duplicate items, with the same value

# You can use the literal or list constructor to create a list. Note the double round brackets in the constructor:

l = [1,2,3,4] # literal

l2 = list(('cat', 3, True, None, True)) # constructor

for item in l:
  print(item)

for item in l2:
  print(item)

# Lists (much like arrays in JavaScript, Java, and Ruby)
# Accessing list items

print(l2[0])

print(l2[-1])


print(l2[0:2]) # not inclusive of item at index 2 (range including starting point to the point after the colon)

print(l2[2:]) # inclusive of item at index 2 (including the first element and all elements to to the end of the list)

print(l2[:2]) # not inclusive of item at index 2 (rang including the element at index 0 to and not inclusive of the listed index number) 

# Remember: starting at number includes number; up to number doesn't

# In addition to looping through any collection that has an index (lists, sets, and tuples), you can use a for loop through the collection's items by exposing the index and referring to their index number, using the range() and len() functions to create a suitable iterable (otherwise, looping with for can't be done this way and you get an error)

for i in range(len(l2)):
  print(l2[i])

# however, indicating the range is not needed for a while loop:

i = 0
while i < len(l2):
  print(l2[i])
  i += 1

# JS Snippet https://docs.google.com/document/d/1s_3e9xqV7gjQ_78JVsM_p90uI0D9XZ63fsWlANctLAU/edit

# All collections that have an index (lists, tuples, sets) can have their elements repeated as many times shown in equationed, joined in place

mult = l2 * 3

print(mult)


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


# Accessing tuples: same as lists because tuples use an index

# Updating tuples: tuples are immutable, but they can be modified by being turned into a list and back to a tuple again

a = ("une", "deux", "trois")

b = tuple(("Tweety Pie", "Slinky", "Cash", "Carter", "Hedgie"))


aa = list(a)

aa[0] = "un"

print(aa)

aa2 = tuple(aa)

# aa2[0] = "une"

# unpacking a tuple ... breaking out a data structure into multiple variables for the structure's variables to be assigned to:

  # unpacking is an example of decomposition 

(french_1, french_2, french_3) = aa2

print(french_1)
print(french_2)
print(french_3)


# If the number of variables is less than the number of values (the elements), you can add an * to the variable name and the values will be assigned to the variable as a list:


(bird, snake, *dogs, hedgehog) = b

print(bird)
print(snake)
print(dogs)
print(hedgehog)



#Sets

# A set is a collection which is both unordered and unindexed.

# Sets are immutable and they do not allow duplicates

s = { "one", "two", 3, False, () }

print(len(s))

# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.



# ---- Looping through sets ----





# ---- Joining sets ----








#Dictionaries