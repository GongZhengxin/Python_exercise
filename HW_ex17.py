from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {0} to {1}".format(from_file, to_file))

# we could do these two in one line, how?
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()
print("input file is {0} bytes long".format(len(indata)))
# print("does the output file exist? {0}".format(exists(to_file)))
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)
open(to_file, "w").write(indata)
print("Alright, all done")

# out_file.close()
# in_file.close()
