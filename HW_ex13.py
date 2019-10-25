from sys import argv

# read the WYSS section for hoe to run this

script, first, second, third = argv

print("the script is called:", script)
print("your first variable is:", first)
print("the second variable is:", second)
print("the third variable is:", third)

first = input("please give first variable:")
second = input("please give second variable:")
third = input("please give third variable:")
