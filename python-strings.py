#Strings
#https://www.w3schools.com/python/python_ref_string.asp


#looping through strings

for x in 'hello':
  print(x)


happy = "happy"

print(len(happy))

# there's no for statement ... use for...in in Python for simple looping (but the for...in in JavaScript is specifically for iterating through objects (to expose keys))

for aa in happy:
  print(aa)

print("app" in happy)



# This functionality works like the JavaScript includes() method for both arrays and strings

if "app" in happy:
  print("String present")

print("app" not in happy)

if "epp" not in happy:
  print("String not present")


#slice string

bb = 'hello'
print(bb[2:5])
print(bb[:3])
print(bb[1:])
print(bb[-4:])
print(bb[-4: -1])


#format() method

#use of placeholders (not really interpolation)
#the string format method has a lot of types (operators):
#https://www.w3schools.com/python/ref_string_format.asp

txt = "For only {price} dollars!"
print(txt.format(price = 49))

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

# Practice format() ???



# Literal string interpolation through f-strings
# Python 3.6 added new string interpolation method called literal string interpolation and introduced a new literal prefix f. This new way of formatting strings is powerful and easy to use. It provides access to embedded Python expressions inside string constants.

f = bool(True)

s = f"This is a {f} example of literal string interpolation though the f-string in Python"

print(s)


a = f'You can also use literal string interpolation through the f-string to show arithmetic operations: {4*2}'

print(a)

pb = "Jif peanut butter is the best, bar "
n = None

v = f'In fact, you can use f-strings to use interpolation with any variable/s: {pb}{n}'

print(v)

# Note: In the above example, {pb, n} would create a tuple



# split()

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# concatenation

# Concatenating strings with other data types is illegal without casting in Python but not in JavaScript

a = "His name is Dave and his age is " + str(34)
print(a)

a_no_cast = "His name is Dave and his age is " + 34

"""
const a = "My age is " + 34;

console.log(a);
"""

while x<12:
  # print(x)
  x+=1
  if x == 5:
    continue
  print(x)
  # if x == 11:
  #   break
