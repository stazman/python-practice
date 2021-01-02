# Booleans

print("\n")

# Truthy and falsy values

print("Truthy values: \n")
print(bool(True))

print("\n")

# Falsey values:


print("Falsey values: \n")

# Primitives
print("\n")

print("Falsey primitives: \n")


print(bool(False))
print(bool(0))
print(bool(""))
print(bool(None))


# Different than JavaScript which as them as true

print(bool(()))
print(bool([]))
print(bool({}))

empty_list = list()
empty_set = set()
empty_tuple = tuple()
empty_dict = dict()

print(bool(empty_list))
print(bool(empty_set))
print(bool(empty_tuple))
print(bool(empty_dict))

"""
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""

# Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x, str))


print("\n")