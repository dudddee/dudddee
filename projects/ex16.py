from sys import argv

script, filename = argv

print(f"we're going to erase {filename}")
print("if you don't want that, hit ctrl-c (^C)")
print("if you do want that hit return")
#this is just dummy text for a simple test of permission
input("?")

#this opens it in w mode, which already truncates it
print("opening the file...")
target = open(filename, 'w')

print("truncating the file. goodbye!")
#target.truncate() --> não necessário por conta to 'w'

print("now i'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to write these to the file")

#writes what the user gave inside the file
target.write(line1 + "\n" + line2 + "\n" + line3)

#closes it
print("and finally, we close it")
target.close()
