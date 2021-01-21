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

class Creature:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species

cash = Creature("Cash", 2, "dog")

print(cash.name)

class Creature:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species

  def printname(self):
    print(self.name)

carter = Creature("Carter", 2, "dog")

carterprint = carter.printname()

print(carterprint)


class Creature:
  def __init__(customself, name, age, species):
    customself.name = name
    customself.age = age
    customself.species = species

  def printname(customself):
    print(customself.name)

carter = Creature("Carter", 2, "dog")

carterprint = carter.printname()

print(carterprint)


# Cannot do the same thing in JS:

# class Creature {
#   constructor(name, age){
#     this.name = name;
#     this.age = age;
#   }
# }

# // function thisTest(this){
# //   console.log(this.name);
# // }

# const cash = new Creature("Cash", 2);

# console.log(cash.name)

# modifying an object

print(carter.age)

# deleting an object

del carter

# print(carter)


# Inheritance

# Use the pass keyword when you do not want to add any other properties or methods to the class.

class Person(Creature):
  pass

chris = Person("Chris", 34, "human")

print(chris.name)

chris.printname()


# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function. The child's __init__() function overrides the inheritance of the parent's __init__() function.

class Person(Creature):
  def __init__(self, name, age, shoesize):
    self.name = name
    self.age = age
    self.shoesize = shoesize

chris = Person("Chris", 34, 10)

print(chris.shoesize)

# print(chris.species) # Shows error because species not available due to the child's overriding __init__() method


# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Person(Creature):
  def __init__(self, name, age, species):
    Creature.__init__(self, name, age, species)

susan = Person("Susan", 40, "human")

print(susan.name)

# super() does the same thing that the parent class name does here, but without the need for the parent name

class Person(Creature):
  def __init__(self, name, age, species, shoesize, wearsgloves, phonebrand):
    super().__init__(name, age, species) # note that self is not used or even allowed here
    # properties and methods specific to the child class can be added under the line with the super() keyword
    self.shoesize = shoesize
    self.wearsgloves = wearsgloves
    self.smartphonebrand = phonebrand # note that the name of the child-specific property can have a different name for the property called on self

  def sayhello(self):
    print("Hello, " + self.name)

joe = Person("Joe", 45, "human", 10, True, "LG")

print(joe.name)

print(joe.shoesize)

print(joe.wearsgloves)

joe.sayhello()

# Note: If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.