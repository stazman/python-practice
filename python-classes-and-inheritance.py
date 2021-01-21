# Classes

# There is no new keyword such as in Java and JavaScript

class FirstClass:
  age = 0

frank = FirstClass()

frank.age = 22

print(frank.age)


# __init__() is an example of a built-in function; similar to a constructor method in Java and Javascript.

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# self is like self in Ruby, and this in Java and JavaScript

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class. This is not like this in Java or JavaScript

class Pet:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species

cash = Pet("Cash", 2, "dog")

print(cash.name)

class Pet:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species

  def printname(self):
    print(self.name)

carter = Pet("Carter", 2, "dog")

carterprint = carter.printname()

print(carterprint)


class Pet:
  def __init__(customself, name, age, species):
    customself.name = name
    customself.age = age
    customself.species = species

  def printname(customself):
    print(customself.name)

carter = Pet("Carter", 2, "dog")

carterprint = carter.printname()

print(carterprint)

# modifying an object

print(carter.age)

# deleting an object

del carter

print(carter)