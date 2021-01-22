# Dates

import datetime

def datetimenow():
  x = datetime.datetime.now()
  print(x)

datetimenow()

# prints out hours, minutes, seconds then microseconds (not milliseconds)

def datetimeyear():
  x = datetime.datetime.now()
  print(datetime.datetime.now().year)
  print(x.year)
  print(x.strftime("%A"))

datetimeyear()

# strftime formatting directives reference: https://strftime.org/


# Creating Date Objects

# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

def createdate():
  x = datetime.datetime(1965, 8, 24)
  print(x)
  y = datetime.datetime(1965, 8, 24, 4, 33, 34, 456323, None)
  print(y)

  # strptime is the opposite of strftime; starting from string representation with correct formatting directives ... it all has to be correct or you'll get an exception:

  print(datetime.datetime.strptime("December 25, 2010", "%B %d, %Y"))

  print(y.tzinfo)

createdate()


# Math

# Like JS, Python has built-in math methods (though in JS, the methods are called on the built-in Math object directly):


minnum = min(12, 14, 2)
print(minnum)

maxnum = max(12, 14, 2)
print(maxnum)

absnum = abs(-6.345)
print(absnum)

exponum = pow(2, 4)
print(exponum)

roundup = round(7.9)
print("\"Normal\" rounding up: " + str(roundup))


# In Python, a separate module called math is required for some functions (that JS doesn't require a separate module for)

import math

roundnumupinanycase = math.ceil(7.1)
print(roundnumupinanycase)

roundnumdowninanycase = math.floor(7.9)
print(roundnumdowninanycase)

squarerootof64 = math.sqrt(64)
print(squarerootof64)

simplypi = math.pi

# Note that pi has no invocation operator (parentheses) because it is a constant

print(simplypi)


# Math module reference: https://www.w3schools.com/python/module_math.asp


# JSON

# Python has a built-in package called json, which can be used to work with JSON data.

# Parsing JSON (Converting from JSON to Python)(similar to the built-in object JSON's .parse() method in JS)

# If you have a JSON string, you can parse it by using the json.loads() method. The result will be a Python dictionary.

import json

samplejsonstring = '{ "name": "Joe", "position": "president" }'

# Note: the interpreter expects property names to be in double quotes, not single quotes, specifically, and using single quotes will result in a JSONDecodeError

print(samplejsonstring)

x = json.loads(samplejsonstring)
print(x)

print(x["name"])

# Converting from Python to JSON: If you have a Python object, you can convert it into a JSON string by using the json.dumps() method. (similar to the built-in object JSON's .stringify() method in JS)


