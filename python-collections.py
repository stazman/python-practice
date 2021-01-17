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

# Sets do not allow duplicates

# Sets are mutable. However, since they are unordered, indexing has no meaning. We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.


s = { "one", "two", 3, False, "duplicate", ()}

s2 = { "a", "b", None, 2.3, "duplicate"}


# Cannot include {} or [] in a set literal because lists and dicts aren't hashable (and will get related error if try to)

print(len(s))


# You cannot access items in a set by referring to an index or a key.


# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword:



# ---- Looping through sets ----

for i in s:
  print(i)


for i in s2:
  print(i)



# ---- Joining sets ----

# Two ways to join sets:

# union() ---> creates a new set; does not mutate the sets to be joined
# update() ---> mutates the first set by adding the items in the new set to it


newS = s.union(s2)
print(s.union(s2))
print(newS)
print(s)
print(s2)

mutatedS = s.update(s2)
print(s.update(s2))
print(mutatedS)
print(s)
print(s2)

# intersection() and intersection_update() both include the duplicates in the resulting set (returned itself with intersection() but None returned with intersection_update)
# "Only what intersects (matches) between the two sets"

# Such as with union() and update(), intersection() makes a new set but intersection_update() mutates the original set so that only the duplicate members are included in the original set:

# intersection()

# "A safe way to find the unique values in two sets to be joined"

notMutatedIntersectedSet = { "one", "two", 3, False, "duplicate", ()}
notMutatedIntersectedSet2 = { "a", "b", None, 2.3, "duplicate"}

notMutated = notMutatedIntersectedSet.intersection(notMutatedIntersectedSet2)
print(notMutated)
print(notMutatedIntersectedSet) # Shows original first set unchanged


# intersection_update()

mutatedIntersectedUpdatedSet = { "one", "two", 3, False, "duplicate", ()}
mutatedIntersectedUpdatedSet2 = { "a", "b", None, 2.3, "duplicate"}

mutated = mutatedIntersectedUpdatedSet.intersection_update(mutatedIntersectedUpdatedSet2)
print(mutated)
print(mutatedIntersectedUpdatedSet) # Shows original first set changed



# symmetric_difference(): mutates the first array to include all EXCEPT the duplicates

# "keep only what is unique between the two sets and returns this in a new set"


notMutatedUniqueItemsOnly = { "one", "two", 3, False, "duplicate", ()}

notMutatedUniqueItemsOnly_2 = { "a", "b", None, 2.3, "duplicate"}

notMutatedUnique = notMutatedUniqueItemsOnly.symmetric_difference(notMutatedUniqueItemsOnly_2)
print(notMutatedUnique)
print(notMutatedUniqueItemsOnly) # Shows original first set unchanged


# symmetric_difference_update(): mutates the first array to include all EXCEPT the duplicates

# "keep only what is unique in the two sets but just change the first set to do so, without returning a new set"

mutatedUniqueItemsOnly = { "one", "two", 3, False, "duplicate", ()}

mutatedUniqueItemsOnly_2 = { "a", "b", None, 2.3, "duplicate"}

mutatedUnique = mutatedUniqueItemsOnly.symmetric_difference_update(mutatedUniqueItemsOnly_2)
print(mutatedUnique)
print(mutatedUniqueItemsOnly) # Shows original first set changed


#Dictionaries

# As with JS objects and Java maps, dictionary items are unordered and unchangeable, and no duplicates are allowed.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(thisdict)

# Dictionaries are unordered, so you cannot refer to an item by using an index.

# However, you can access an object key's value/s thus:


john = {
  "id": 1,
  "name": "John",
  "email": "john@here.com",
  "status": "admin"
}

print(john["email"])


print(len(john))


# looping over dictionaries

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}


# using basic looping to access keys

for item in a_dict:
  print(item)

# using keys() to access keys

for item in a_dict.keys():
  print(item)


# using basic looping to access values

for item in a_dict:
  print(a_dict[item])

# using values() to access values

for item in a_dict.values():
  print(item)


# using items() ---> makes tuples

d_items = a_dict.items()
print(d_items)

for item in a_dict.items():
 print(item[0])

for item in a_dict.items():
 print(item[1])

for item in a_dict.items():
 print(item[0][0])


# copying a dictionary

# You cannot copy a dictionary simply by typing a_dict = b_dict, because b_dict will only be a reference to a_dict, and changes made in b_dict will automatically also be made in a_dict.

b_dict = {}

a_dict = b_dict

print(a_dict)

print(b_dict)


# In addition to the copy() method, you can use the built-in constructor function dict()

john2 = dict(john)

print(john2)


# All collections can be copied using their built-in constructors:

print(l2)
print(b)
print(newS)
print(thisdict)

newl2 = list(l2)
print(newl2)

new_b = tuple(b)
print(new_b)

newnewS = set(newS)
print(newnewS)

newthisdict = dict(thisdict)
print(newthisdict)


# nested dictionaries

SWfamily = {
  'familymember1': {
    'name': 'Anakin',
    'relation': 'father'
  },
  'familymember2': {
    'name': 'Luke',
    'relation': 'son'
  },
  'familymember3': {
    'name': 'Leia',
    'relation': 'daughter'
  }
}

pet1 = {
  "name": "Cash",
  "species": "dog",
  "age": 2
}

pet2 = {
  "name": "Carter",
  "species": "dog",
  "age": 2}

mypets = {
  "pet1": pet1,
  "pet2": pet2
}

print(mypets)