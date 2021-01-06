# List of built-in methods for list()

# (https://www.w3schools.com/python/python_lists_methods.asp)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value ... like indexOf() in JS
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# Notable list methods:

# append() ... same as push() in JS

a = ["Joe", "Nan", "Laura"]

a.append("Bob")

a.append(34)

print(a)


# remove

# there's no shift to remove elements from the beginning (use remove() instead):

a.remove(a[0])

print(a)


print(a.index("Laura"))

a.remove("Laura")

print(a)

# unlike JS, you can remove items in the middle of a list





# pop()

#As an array in JS, pop() removes the last item in the array. However, Python's pop() can remove a list item at a passed-in index; JS requires a method such as slice() to remove items from the middle of an array

l1 = [1, 2, 3, 4, "five"]

print(l1.pop())

print(l1.pop(1))

print(l1)


# extend() is like JavaScript's push method, but it can only take 1 argument

l3 = [[], {}, (), 0, ""]

for item in l3:
  print(item)

l4 = ['less than zero', "more than enough"]

l5 = { 3, 2, 2} # extending a set

print(type(l5))

l3.extend(l4)

l3.extend(l5)

print(l3)
# note that only one 2 was included because sets aren't allowed to have duplicate values

l6 = ("hen", "rooster", "puppy") #extending a tuple

print(type(l6))

l3.extend(l6)

print(l3)

l7 = {"name": 'Jen', "city": "Toledo"} #extending a dictionary

print(type(l7))

l3.extend(l7)

print(l3)
# just prints the keys, not values for dictionary

l8 = [{"name": 'Jen', "city": "Toledo"}] 

l3.extend(l8)

print(l3)


# insert()

l3.insert(2, "Bob")

print(l3)


# sort()

# syntax: list.sort(reverse=True|False, key=myFunc)

ab = [5, "happy", "merry", "glad", 3]

for item in ab:
  if type(item) != type("string"):
    ab.remove(item)
    print("not a string")
  else:
    print("test")
    
print(ab)

# default sort in ascending order

ab.sort()

print(ab)


# sort in descending order

ab.sort(reverse=True)

print(ab)

# sort by "keys" representing what functions return:

# sort by length



# sort by whether or not the string in a list item includes a letter 



# sort dictionary by key values --- eg., ages





