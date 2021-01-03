# Conditionals:


if 5<10:
 print("Hello World!")
 print("Hello again")


def pet(result):
  if result == "cat":
    print("I have a cat")
  elif result == "dog":
    print("I have a dog")
  elif result == "bird":
    print("I have a bird")
  else:
    print("I either have no pets or I have a nontraditional pet")


pet("dog")


# short form -- all in one line if there's only one conditional statement 

if 4>3: print("The first number is larger")


# ternary operator in Python:
print("The first number is smaller") if 2>3 else print("The first number is not smaller")
# JS ---> 2>3 ? console.log("The first number is smaller") : console.log("The first number is not smaller");


if 3>2 and 2>1: print("Both first numbers are larger")

if 2>1 or 3<2: print("At least one of these two operands is true")


# nested if statements

pet = "cat"
breed = "American shorthair"


if pet == "cat":

  print("The pet is a cat.")
  if breed == "American shorthair":
    print("The breed is American shorthair.")
  else:
    print("The breed is not an American shorthair.")

else:
  print("The pet is not a cat.")


# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

if 3>2:
  pass

# if 3>2: --> causes error and program does not run


# Looping/Iteration:

# while

x = 1

y = 0

z = 0

while x<12:
  print(x)
  x+=1
  if x == 5:
    continue
  print(x)
  
while y<12:
  print(y)  
  y+=1
  if y == 7:
    break

while z<12:
  print(z)
  z+=1
else:
  print("z is no longer smaller than 12")
  

# there's no for statement ... use for...in in Python for simple looping (but the for...in in JavaScript is specifically for iterating through objects (to expose keys))

