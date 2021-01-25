# File handling and Regex practice: Searching for a word in a file

import re

article = "We should all be so lucky as to come from fun parents. My parents were fun, and we always had a good time."

def quickwordsearch(word, filepath):
  openfile = open(filepath, "r")
  readfile = openfile.read()
  findword = re.search(word.lower(), readfile)
  print(findword)

quickwordsearch("lorem", "/Users/christopher_distasio/AAA-Practice/PYTHON_PRACTICE/python-practice/sample_files/sample_text_file_2.txt")
