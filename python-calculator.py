first_num = input("Enter the first number:  ")

second_num = input("Enter the second number:  ")

print("\n")

print("+ \n \n - \n \n * \n \n / \n")

operator = input("Enter an operator from the list above:  ")

if operator == "+":
  print(int(first_num) + int(second_num))
elif operator == "-":
  print(int(first_num) - int(second_num))
elif operator == "*":
  print(int(first_num) * int(second_num))
else:
  print(int(first_num) / int(second_num))