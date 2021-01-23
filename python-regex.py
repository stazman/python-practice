# Regex

# Python has a predefined package called re, which can be used with the .search() method to work with Regular Expressions. .search() returns any matching characters and results in a boolean value of True if there is a match and False if not.

# The search() function searches the string for a match, and returns a Match object if there is a match. If there is more than one match, only the first occurrence of the match will be returned. If no matches are found, the value None is returned.


import re

textwithoutnumbers = "There are no digits in this sentence so trying to match for numbers will result in False."

textwithnumbers = "Here are some numbers: 1, 4, 33"

x = re.search("\d", textwithoutnumbers)
y = re.search("\d", textwithnumbers)
xreturningstring = re.search("^There", textwithoutnumbers)
nooccurrences = re.search("heliotropic", textwithoutnumbers)

print(bool(x))
print(bool(y))

print(xreturningstring)
print(nooccurrences)

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# More functions that allows us to search a string for a match:

# findall	  Returns a list containing all matches
# search	  Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	      Replaces one or many matches with a string


# findall()

allmatches = re.findall("re", textwithnumbers)

print(allmatches)

# The list contains the matches in the order they are found. If no matches are found, an empty list is returned.

nomatches = re.findall("syzygy", textwithnumbers)
print(nomatches)


# .split

print(re.split("\s", txt))


# You can control the number of occurrences by specifying the maxsplit parameter

print(re.split("\s", txt, 2))


# sub()

# Think of sub as short for substitute

# The sub() function replaces the matches with the text of your choice

subbedstring = re.sub("Spain", "Portugal", txt)
print(subbedstring)

# You can control the number of replacements by specifying the count parameter:

subbedwithones = re.sub("i", "1", txt, 1)
print(subbedwithones)


# Match Object

# A Match Object is an object containing information about the search and the result. If there is no match, the value None will be returned, instead of the Match Object.

print(xreturningstring) # --> <re.Match object; span=(0, 5), match='There'>

# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# span()

print(xreturningstring.span())

print(xreturningstring.string)

# but string() won't return the string if there are no matches in the regex expression:

# phrase = "This is a phrase"
# nomatch = re.search("salubrious", phrase)
# print(nomatch.string)


# group() prints the distinct part of the string where there was a match.

print(xreturningstring.group())


##### General Regex Reference #####

# Metacharacters

# Metacharacters are characters with a special meaning:

# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"world$"
# *	Zero or more occurrences	"aix*"
# +	One or more occurrences	"aix+"
# {}	Exactly the specified number of occurrences	"al{2}"
# |	Either or	"falls|stays"
# ()	Capture and group


# Special Sequences

# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"


# Sets

# A set is a set of characters inside a pair of square brackets [] with a special meaning:

# [arn]	Returns a match where one of the specified characters (a, r, or n) are present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string