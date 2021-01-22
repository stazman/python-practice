# Modules

# Consider a module to be the same as a code library, a file containing a set of functions you want to include in your application. A module is a file containing definitions of functions, classes, variables, constants or any other Python objects. Contents of this file can be made available to any other program.


# Accessing custom modules created in practicemodule1.py and practicemodule2.py

import practicemodule1

practicemodule1.samplefunction()

practicemodule1.samplefunctionwithparams("Dave", "Nice to see you!")


import practicemodule2 as pm2

print(pm2.personobject["name"])


# Built-in modules

# Built-in modules are written in C and integrated with the Python interpreter. Each built-in module contains resources for certain system-specific functionalities such as OS management, disk IO, etc. The standard library also contains many Python scripts (with the .py extension) containing useful utilities.

# To display a list of all available modules, use the following command in the Python console: >>> help("modules")

# Predefined modules in libraries from Python distributions that require the import keyword: https://docs.python.org/3/py-modindex.html

# example of predefined module named platform:

import platform

x = platform.system()
print(x)

# The dir() function: is a built-in function to list all the function names (or variable names) in a module.

y = dir(platform)
print(y)


# Importing specific part of a module:

# Use from keyword:

from practicemodule3 import plantgrow

print(plantgrow())

# print(botanicalobject["name"])


from practicemodule3 import botanicalobject

print(botanicalobject["name"])

# print(plantgrow())

# Each of the commented out lines will result in an error unless mentioned specifically in a partial import

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: botanical["name"], not practicemodule3.person1["age"]
