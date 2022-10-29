#imports argv from sys module
from sys import argv

#assigns two variables to argv, script (the name of the current file) and filename (the name of the file we want to read)
script, filename = argv

#performs the pydoc function, open, on the file we determined and stores the open file in a variable called txt
txt = open(filename)

#prints out the name of the file we gave earlier
print(f"here's yout file {filename}:")
#prints out the contents of txt by performing a read function without parameters
print(txt.read())

#does the same but with input instead of argv
print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#it is important to close files after being done with them
txt.close()
txt_again.close()
#NOTE: call close to the opened variables
