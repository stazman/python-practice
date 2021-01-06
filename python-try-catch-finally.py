# Exception handling in Python; its very similar to JS

try:
  number = int(input("Enter a number: "))
  print(number)
except:
  print("Invalid response")
finally:
  print("You'll need to re-run the program if you gave an invalid response.")


# It is a best practice to anticipate specific exceptions:

try:
  number = int(input("Enter a number: "))
  print(number)
  wrong_num = 10/0
except ValueError as err:
  print("Invalid input")
  print(err)
except ZeroDivisionError as err2:
  print("A number cannot be divided by zero")
  print(err2)