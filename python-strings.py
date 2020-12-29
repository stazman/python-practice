#Strings
#https://www.w3schools.com/python/python_ref_string.asp

happy = "happy"

print(len(happy))
  
for aa in happy:
  print(aa)

print("app" in happy)

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



#looping through strings

for x in 'hello':
  print(x)


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

# split()

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# concatenation

# Concatenating strings with other data types is illegal in Python but not in JavaScript
a = "His name is Dave and his age is" + 34
print(a)

""" 
const a = "My age is " + 34;

console.log(a); 
"""

