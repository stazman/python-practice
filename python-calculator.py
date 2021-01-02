
first_num = input("Enter the first number")

print(int(first_num))

second_num = input("Enter the second number")

print(int(second_num))

operator = input("Choose an operator")

print("+ \n \n - \n \n * \n \n %")

if operator == "+":
  print(first_num + second_num)
elif operator == "-":
  print(first_num - second_num)
elif operator == "*":
  print(first_num * second_num)
else:
  print(first_num % second_num)