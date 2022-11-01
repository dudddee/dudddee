from sys import argv, int_info
from os.path import exists

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()
#indata = open(from_file).read() --> way of doing it in one line

print(f"the input file is {len(indata)} bytes long")

print(f"does the output file exist? {exists(to_file)}")
print("ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("alright, all done")

out_file.close()
in_file.close()
#have no idea of how to close the file in the case of reading it in a single line
#answer --> it closes automatically
