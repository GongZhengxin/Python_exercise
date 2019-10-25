from sys import argv

script, filename = argv

txt = open(filename) #makes a file object

print("Here's your file {0}:".format(filename))
print(txt.read())

txt.close()
# print("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
#
# print(txt_again.read())
