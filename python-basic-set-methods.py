# Built-in Set Methods

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others


# ---- Adding set items ----

petset = { "Cash", "Carter", "Lizzie", "Squeaky", "Joshua" }

print(petset.add("Porch Lizard"))

print(petset)

# Keep running this code and see how the order of the result set changes each time you run it


peopleset = { "Chris", "Susan"}

petset.update(peopleset)

print(petset)

# Keep running this code and see how the order of the result set changes each time you run it


# The object in the update() method does not have be a set, it can be any iterable object (tuples, lists, dictionaries etc). This is equivalent to list's expand() method.

nuclear_family = ["Tony", "Helen", "Phillip", "Paul", "David"]

petset.update(nuclear_family)

print(petset)


nuclear_pets = ( "Kara", "Denny", "Tiny" )

petset.update(nuclear_pets)

print(petset)


neighbor1 = { "name": "Chris Sharpe", "age": 48 }
# It only includes the keys in the set

petset.update(neighbor1)

print(petset)


# Array of dictionaries causes error:  
# neighbors = [{ "name": "Chris Sharpe", "age": 48 }, { "name": "Kelly Sharpe", "age": 44}]

# petset.update(neighbors)

# print(petset)

"""
File "/Users/christopher_distasio/python-practice/python-set-methods.py", line 65, in <module>
  petset.update(neighbors)
TypeError: unhashable type: 'dict'

"""

# ---- Removing items ----

print(petset.remove("Porch Lizard"))

print(petset)


# If the item to remove does not exist, remove() will raise an error:

# print(petset.remove("Fido"))


# discard() works the same as remove(), but it won't raise an error if the item to be removed doesn't exist

print(petset.discard("David"))

print(petset)


print(petset.discard("Mephistopheles"))

print(petset)


# You can also use the pop(), method to remove an item, but this method will remove only the last item. 

# Important! Remember that sets are unordered, so you will not know what item that gets removed.

# As with lists, the return value of the pop() method is the removed item.

print(petset.pop())

print(petset)


# clear() empties out the set but doesn't delete it

print(petset.clear())

print(petset)


# The del keyword deletes the set entirely

del petset

print(petset)