#Functions

def hello():
  print("Hello")

hello()

def hello(name):
  print("Hello, " + name)

hello("Frank")

#Arbitrary arguments
def hello(*people):
  print("Hello, " + people[1])

hello("Frank", "Linda")


# Nested functions

# A function which is defined inside another function is known as a nested or inner function. Nested functions are scoped inside their parent function.


def parent():
  print("I'm the parent")
  def child():
    print("I'm the child")

  child()

parent()


# This use of a nested function beldoes not work to print the message and the inner function isn't even reachable:

def parent_returning_child():
  def child2():
    print("I'm the second child")

parent_returning_child()


# This use of a nested function works because a reference to the child is returned by the parent and

def parent_returning_child():
  def child3():
    print("I'm a child that's been returned by the parent. ")

  return child3

child3 = parent_returning_child()

child3()