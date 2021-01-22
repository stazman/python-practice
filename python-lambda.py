# Lambdas

# Lambdas are similar to arrow functions in JS

sampleLam = lambda a : a + 3
print(sampleLam(5))

# JS:
# const arrEx = x => { return x + 3};

# arrEx(5);

# Use lambda functions when an anonymous function is required for a short period of time and/or you want to provide encapsulation

def quickreturn(y):
  return lambda x : x * y

quickreturndoubler = quickreturn(2)

print(quickreturndoubler(5))

quickreturntripler = quickreturn(3)

print(quickreturntripler(5))


# Syntax for a lambda can be very simple:

def longway(x):
  return x + 3

print(longway(2))


print((lambda x : x + 3)(2))