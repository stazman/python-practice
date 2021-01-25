# Note: If you run this file, you'll need to create the directory ./sample_empty_dir from the project root directory to try out the removing empty directory steps later in this file; empty directories aren't checked into version control

# IMPT:
    # A file must be opened before it can be read, written to, or deleted from the command line
    # Best practice is that a file should be closed if not needed to be used anymore

# open a file:

# (default mode is read and default format is text)

# open_and_read_whole_file = open("sample-text-file-1.txt")

# the same result with explicit *string parameters* for read and text:
open_and_read_whole_file = open("sample-text-file-1.txt", "rt")

# the same result with explicit parameters for read and binary:
# open_and_read_whole_binary_file = open("sample-binary-file.bin", "rb")


# read a file (print to console)

print(open_and_read_whole_file.read())

# close a file
open_and_read_whole_file.close()


open_and_read_diff_dir_location = open("./sample_files/sample_text_file_2.txt")

print(open_and_read_diff_dir_location.read())

open_and_read_diff_dir_location.close()


# read only part of a file -- first characters

open_and_read_diff_dir_location = open("./sample_files/sample_text_file_2.txt", "r")

print(open_and_read_diff_dir_location.read(11))

open_and_read_diff_dir_location.close()



# read first line/s ... use .readline() for each line from the top of the file

open_and_read_diff_dir_location = open("./sample_files/sample_text_file_2.txt")

print(open_and_read_diff_dir_location.readline()) # one line

open_and_read_diff_dir_location.close()


open_and_read_diff_dir_location = open("./sample_files/sample_text_file_2.txt")

print(open_and_read_diff_dir_location.readline()) # two lines
print(open_and_read_diff_dir_location.readline())

open_and_read_diff_dir_location.close()


open_and_read_diff_dir_location = open("./sample_files/sample_text_file_2.txt")

print(open_and_read_diff_dir_location.readline()) # six lines
print(open_and_read_diff_dir_location.readline())
print(open_and_read_diff_dir_location.readline())
print(open_and_read_diff_dir_location.readline())
print(open_and_read_diff_dir_location.readline())
print(open_and_read_diff_dir_location.readline())

open_and_read_diff_dir_location.close()


# looping through lines to print them:

open_and_read_looping = open("./sample_files/sample_text_file_3.txt")

for line in open_and_read_looping:
  if "consecrate" not in line:

# The line that includes "consecrate" is skipped but all of other lines are returned correctly

    continue
  else:
    print(line)

open_and_read_looping.close()


# overwrite an existing file or create a new one if the file doesn't exist

open_and_overwrite = open("./sample_files/sample_text_file_3.txt", "w")
open_and_overwrite.write("The Gettysburg Address has been overwritten.")
open_and_overwrite.close()

open_and_read_overwritten = open("./sample_files/sample_text_file_3.txt", "r")
# note: the "r" must be included here
print(open_and_read_overwritten.read())

open_and_read_overwritten.close()

open_and_write_new_file_w = open("./sample_files/sample_text_file_4.txt", "w")
open_and_write_new_file_w.write("This is a file created and then written to using \"w\".")
open_and_write_new_file_w.close()

open_and_read_new_file_w = open("./sample_files/sample_text_file_4.txt", "r")
print(open_and_read_new_file_w.read())
open_and_read_new_file_w.close()


# same as "w": overwrites and creates a new file if one with the same name doesn't already exist

open_and_write_new_file_a = open("./sample_files/sample_text_file_5.txt", "a")
open_and_write_new_file_a.write("This is a file created and then written to using \"a\".")
open_and_write_new_file_a.close()

open_and_read_new_file_a = open("./sample_files/sample_text_file_5.txt", "r")
print(open_and_read_new_file_a.read())

open_and_read_new_file_a.close()


# create a file; error if file with the same name already exists -- WITHOUT creating a new file with the name indicated (this is the difference between x and w/a)

create_new_file_not_already_exists = open("./sample_files/sample_text_file_6.txt", "x")
create_new_file_not_already_exists.write("This is a file created and written to using \"x\"")
create_new_file_not_already_exists.close()

read_new_file_not_already_exists = open("./sample_files/sample_text_file_6.txt", "r")
print(read_new_file_not_already_exists.read())
read_new_file_not_already_exists.close()


# To create and write to file but shows error if file already exists instead of overwriting the existing file the way "a" and "w" do, use "x":

  # create_new_file_but_exists = open("./sample_files/sample_text_file_5.txt", "x")
  # create_new_file_but_exists.write("This is a file whose creation and writing to with \"x\" is being attempted, but it will fail because it already exists. The existing file with the same name will not be overwritten.")
  # create_new_file_but_exists.close()

# (so it won't continue to be readable in the same series of invocations when running this file)

  # create_new_file_but_exists = open("./sample_files/sample_text_file_5.txt", "r")
  # create_new_file_but_exists.read()
  # create_new_file_but_exists.close()


# To delete a file (you'll need to comment out the previous two sections to see this work because the previous sections result in an execution-stopping error)

# Check if it exists then delete it, to avoid an error:

import os

if os.path.exists("./sample_files/sample_text_file_5.txt"):
  os.remove("./sample_files/sample_text_file_5.txt")
else:
  print("The file does not exist")

# makes an error because file doesn't exist:
  # futile_attempt_to_open_deleted_file = open("./sample_files/sample_text_file_5.txt")


# attempting to remove a file that doesn't exist (you'll need to comment out the previous three sections to see this work correctly)

import os

if os.path.exists("./sample_files/sample_text_file_7.txt"):
  os.remove("./sample_files/sample_text_file_7.txt")
else:
  print("The file does not exist")


# To delete a directory

# Note: A directory deleted this way must be empty. Otherwise this doesn't work and you'll get an error.)

# (You'll need to comment out the previous four sections to see this work correctly):

import os

os.rmdir("./sample_empty_dir")

print("sample_empty_dir has been removed")


# makes an error because directory doesn't exist:

  # futile_attempt_to_open_deleted_file = open("./sample_empty_dir")

# Note: don't forget to re-create the sample_empty_dir directory if you try out this section repeatedly
