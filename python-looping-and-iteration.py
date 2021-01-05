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