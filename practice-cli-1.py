# List


# def pet_survey():

#   l = []

#   pet_survey_name = input("What is your name?")

#   l.append(pet_survey_name)

#   pet_survey_dog = input("Do you have a dog?")

#   l.append(pet_survey_dog)

#   pet_survey_cat = input("Do you have a cat?")

#   l.append(pet_survey_cat)

#   for i in l:
#     if i == "":
#       print("No response indicated")
#     else:
#       print(i)

#   print(l.count("Yes"))
#   print(l.count("No"))
#   print(len(l))
#   sorted_l = l.sort()
#   print(sorted_l)
#   print(l)
#   sortedl_rev = l.sort(reverse=True)
#   print(sortedl_rev)
#   print(l)
#   l.sort(key=contains_e)
#   print(l)

# def contains_e(i):  # This didn't work to sort the list by whether or not the item contains an e, but it did change the order

#   if i.find("e"):
#     return i

# def contains_e(i):  # same here
#   return i.find("land") == True

# pet_survey()
# def pwd_sort(i):
#     return abs(i) == 3



# def sorted_nums():

#   l = []

#   number_question_1 = input("Enter a number: ")

#   l.append(int(number_question_1))

#   number_question_2 = input("Enter another number: ")

#   l.append(int(number_question_2))

#   number_question_3 = input("Enter one more number: ")

#   l.append(int(number_question_3))

#   l.sort(key=pwd_sort) # This works; notice that resulting negative numbers aren't changed to show their absolute value, but instead only checked them for their order in the list to be set

#   print(l)

# sorted_nums()


# Tuple

# Making a collection that is ordered but unchangeable ... like a set in JS or enum in Java
# Task: Need to make a list of kinds of pets not allowed in apartments


# t1 = tuple({"dog", "cat", "bird"})
# message = ""

# def petform():
#   petkind = input("What kind of pet do you have? ")
#   print("Your pet is a " + petkind)
#   for p in t1:
#     if petkind.lower() == p:
#       message = "This kind of pet is not allowed."
#       break
#     else:
#       message = "This kind of pet is allowed."

#   print(message)

# petform()

# combining two tuples ... casting necessary

# t3 = { "Name", "Birthday", "Phone", "Email" }
# t4 = { "Address", "Social Media Link" }

# # def tuplecomb(t, t2):
# #   makelist = list(t)
# #   makelist2 = list(t2)
# #   makelist.extend(makelist2)
# #   backtotuple = tuple(makelist)
# #   print(backtotuple)

# # tuplecomb(t3, t4)


# def tuplecomb(t, t2):
# # Note: Python will consider a list to be a set even if you cast it unless you assign the casting to a variable and use it to do the extending.
#   list(t)
#   list(t2)
#   t.extend(t2)
#   backtotuple = tuple(t)
#   print(backtotuple)

# tuplecomb(t3, t4)


# Set

# Use case: order not important but not be changeable nor allow duplicates
# Make an email mailing list from a dictionary of accountholders


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

emailset = set()

# def populateset(s):
#   for obj in populateset:
#     for key in obj:
#       if key == "email":
#         emailset.add(key.value())
# print(emailset)

# populateset(employeeinfo)


# Error: TypeError: 'function' object is not iterable

# But remember: using items() on a dictionary results in tuples, which are iterable

def populateset(s):

  for obj in s:
    emailset.add(obj.setdefault("email"))

    # setdefault() returns the value of a given key, and when used with a loop or iteration, it can return the values of all objects in an array based on a given key

  print(emailset)

populateset(employeeinfo)


# Task: Handle the error that comes when a duplicate item is added to a set
