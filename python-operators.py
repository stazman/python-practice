# Operators

# 1. Arithmetic Operators

# Python has the floor division operator, but JS doesn't

print(10//4)


# 2. Assignment Operators

# Shorthand for x = x % 3

x = 5

x %= 3

print(x)


y = 12

y //= 5

print(y)

yy = 3456

while yy > 2:
  yy //= 2
  print(yy)


yy = 3457

while yy > 2:
  yy //= 2
  print(yy)



# 3. Logical Operators

# not works like ! does in JS

print(not(2 == 2))


# 4. Identity operators

x = 'happy'
y = 'happy'

print(x is y)
print(x is not y)


s = "string"
l = ["Bob", "Sally"]

print(l)

l2 = ["Bob", "Sally"]
s2 = "string"

print(s is s2)

# such as equals() in Java, is/is not refers to the memory addresses of collections objects and not values,
# but == refers to the assigned value no matter if memory addresses are the same or not

print(l is l2)
print(l == l2)


# 5. Membership Operators

a = "antidisestablishmentarianism"

print('anti'in a)
print('anti' not in a)


# 6. Bitwise Operators