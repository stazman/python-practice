# Looping/Iteration:

# while loops

x = 0

y = 0

z = 0

# notice that 5 is skipped

while x<12:
  x+=1
  if x == 5:
    continue
  print(x)

while y<12:
  print(y)
  y+=1
  if y == 7:
    break

# With the else statement we can run a block of code once when the condition no longer is true:

while z<12:
  z+=1
  print(z)
else:
  print("z is no longer smaller than 12")



# for loops

# there's no for statement ... use for...in in Python for simple looping (but the for...in in JavaScript is specifically for iterating through objects (to expose keys))

l = ["bed", "bugs", "aren't", "so", "cute"]

for w in l:
  print(w)

# nested loop

l2 = ["bed", "bugs", "are", "so", "yucky"]

for w in l2:
   for char in w:
     if char == "b":
       continue
     elif char == "e":
       break
     elif char == "k":
       break
     print(char)

# range() Function

# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number (NONINCLUSIVE).

# parameter order ---> start, end, increment


for num in range(10):
  print(num)

for num2 in range(2, 26, 2):
  print(num2)


# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for w in l2:
  print(w)
else:
  print("There are no more words in this list")


# Note: The else block will NOT be executed if the loop is stopped by a break statement.

for w in l2:
  if (w == "yucky"): break
  print(w)
else:
  print("There are no more words in this list")

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for w in l2:
  pass

# iterating over dictionaries

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
d_items = a_dict.items()
print(d_items)

for item in a_dict.items():
 print(item[0])

for item in a_dict.items():
 print(item[1])

for item in a_dict.items():
 print(item[0][0])

 pet1 = {'name': 'Cash', 'species': 'canine', 'age': 2 }

 print(pet1.items())

pet_keys = pet1.keys()

print(pet_keys)

# keys() and values() work differently here than in JS, which doesn't call these methods on variables assigned objects but passes objects through built in Object.keys() and Object.values() methods

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value

print(total_income)


# Checking if a key exists in a dictionary:

def checkifkeyexists(i):
  if i in incomes:
    print(f'The key {i} exists in this dictionary')
    incomes[i] = "amount to be determined"
    print(incomes)
  else:
    print(f'The key {i} does not exist in this dictionary')

checkifkeyexists("banana")

checkifkeyexists("kumquat")


# looping through nested dictionaries



# iterating over sets practice ???



# iterating over tuples practice ???


# Iterators

# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Iterator vs Iterable:

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from. All these objects have a iter() method which is used to get an iterator

s = set(( "dog", "cat", "bird" ))

print(s)

s_it = iter(s)

print(next(s_it))
print(next(s_it))
print(next(s_it))

# Strings are also iterable objects, containing a sequence of characters

h = "hello"

h_it = iter(h)

print(next(h_it))
print(next(h_it))
print(next(h_it))
print(next(h_it))
print(next(h_it))

# The relationshipo between a loop and an iterator: The for loop actually creates an iterator object and executes the next() method for each loop.

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

# Challenge example: Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class AdderUpper:
  def __iter__(self):
    self.num = 0
    return self

  def __next__(self):
    x = self.num
    self.num += 1
    return x

adds = AdderUpper()

adds_it = iter(adds)

print(next(adds_it))
print(next(adds_it))
print(next(adds_it))
print(next(adds_it))
print(next(adds_it))
print(next(adds_it))
print(next(adds_it))


# To prevent the iteration from going on forever, we can use the StopIteration statement.

# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:


class AdderUpper:
  def __iter__(self):
    self.num = 0
    return self

  def __next__(self):
    if self.num <= 4:
      x = self.num
      self.num += 1
      return x
    else:
      raise StopIteration

adds = AdderUpper()

adds_it = iter(adds)

print(next(adds_it))
print(next(adds_it))
print(next(adds_it))
print(next(adds_it))
print(next(adds_it))
print(next(adds_it))
print(next(adds_it))