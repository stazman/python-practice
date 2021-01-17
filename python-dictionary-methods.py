# Dictionary Methods


# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
     # del keyword also works with dictionaries
# setdefault()	Returns the value of the specified key. If the key does not exist, it inserts the key with the specified value
     # when used with a loop or iteration, setdefault() can return the values of all objects in an array based on a given key
# update()  Updates the dictionary with the specified key-value pairs
# values()  Returns a list of all the values in the dictionary


employeeinfo = [
  { "id": 1,
    "name": "John",
    "email": "john@here.com",
    "status": "admin"
  },
  { "id": 2,
    "name": "Fred",
    "email": "fred@here.com",
    "status": "employee"
  },
  { "id": 3,
    "name": "Sal",
    "email": "sal@here.com",
    "status": "manager"
  },
]

john = {
  "id": 1,
  "name": "John",
  "email": "john@here.com",
  "status": "admin"
}

print(john)


# fromkeys(); like Object.assign() in JS except all values must be the same; prints out object with keys and given values

keys = ("key1", "key2", "key3")
val = "This is a value."

# use dict but not as a constructor:

fkeys = dict.fromkeys(keys, val)

print(fkeys)


# With no explicit values (prints out None for each value):

fkeys = dict.fromkeys(keys)

print(fkeys)


# keys() and values() work differently here than in JS, which doesn't call these methods on variables assigned objects but passes objects through built in Object.keys() and Object.values() methods

pet1 = {'name': 'Cash', 'species': 'canine', 'age': 2 }

print(pet1.items())

pet_keys = pet1.keys()

print(pet_keys)


incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value

print(total_income)


# There are two ways to mutate existing items in a dictionary: bracket notation and the update() method:

incomes["apple"] = 3000.00

incomes.update({"orange": 90000.00})

print(incomes)


# Also use update() to add an item that doesn't exist


incomes.update({"grapes": 3444.99})

print(incomes)


# copy

cpy = john.copy()

print(cpy)


c = john.clear()

print(john)


# get() is another way to access a key's value


car = {
  "mpg": 18,
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "doors": 2
}


x = car.get("brand")

print(x)


y = car.get("price")

print(y)


# pop(), popitem(), del keyword

car.pop("mpg")
print(car)

car.popitem()
print(car)

car.pop("year")
print(car)

car.popitem()
print(car)

# del can work like pop() for one key/value pair or it can delete the whole dictionary

del car["brand"]
print(car)

del car
print(car)
