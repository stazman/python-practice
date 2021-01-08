# open a file:

# (default mode is read and default format is text)

# open_and_read_whole_file = open("sample-text-file-1.txt")

# the same result with explicit parameters for read and text: 
open_and_read_whole_file = open("sample-text-file-1.txt", "rt")

# the same result with explicit parameters for read and binary: 
# open_and_read_whole_binary_file = open("sample-binary-file.bin", "rb")


# read a file (print to console)

print(open_and_read_whole_file.read())

open_and_read_diff_location = open("./sample_files/sample_text_file_2.txt")

print(open_and_read_diff_location.read())


# close a file

open_and_read_diff_location.close()


# read only part of a file -- first characters

open_and_read_diff_location = open("./sample_files/sample_text_file_2.txt", "r")

print(open_and_read_diff_location.read(11))

open_and_read_diff_location.close()



# read first line/s

open_and_read_diff_location = open("./sample_files/sample_text_file_2.txt")

print(open_and_read_diff_location.readline())

open_and_read_diff_location.close()


open_and_read_diff_location = open("./sample_files/sample_text_file_2.txt")

print(open_and_read_diff_location.readline())
print(open_and_read_diff_location.readline())

open_and_read_diff_location.close()


open_and_read_diff_location = open("./sample_files/sample_text_file_2.txt")

print(open_and_read_diff_location.readline())
print(open_and_read_diff_location.readline())
print(open_and_read_diff_location.readline())
print(open_and_read_diff_location.readline())
print(open_and_read_diff_location.readline())
print(open_and_read_diff_location.readline())

open_and_read_diff_location.close()