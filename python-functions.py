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





