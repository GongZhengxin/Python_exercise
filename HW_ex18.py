# this would have the same effect as argv
def print_two(*args):
    args1, args2 = args
    print("args 1:{0},args 2:{1}".format(args1, args2))


def print_two_again(args1, args2):
    print("args 1:{0},args 2:{1}".format(args1, args2))


print_two("haha","uyhu")
print_two_again("uhg","jih")