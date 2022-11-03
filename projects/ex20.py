#this exercise makes the program print each line at a time
from sys import argv

script, input_file = argv

#here i define 3 functions

#this one prints all the content in a open file
def print_all(f):
    print(f.read())
#think of a pointer, when i open the file later in the code, the pointer is in the first character
#when i print the read method, the pointer goes through the file and prints it

#this function rewinds the point to the position 0
def rewind(f):
    f.seek(0)

#this now prints each line
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first let's print the whole file:\n")
print_all(current_file)

print("now let's rewind, kind of like a tape")
rewind(current_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
