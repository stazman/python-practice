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


t1 = tuple({"dog", "cat", "bird"})
message = ""

def petform():
  petkind = input("What kind of pet do you have? ")
  print("Your pet is a " + petkind)
  for p in t1:
    if petkind.lower() == p:
      message = "This kind of pet is not allowed."
      break
    else:
      message = "This kind of pet is allowed."
  print(message)

petform()