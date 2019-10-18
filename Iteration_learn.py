# from collections import Iterable
#
# isinstance((1, 2.8, [1, 2]), Iterable)
#

def findMinAndMax(L):
    if len(L) != 0:
        min = L[0]
        max = L[0]
        for a in range(len(L)):
            if min >= L[a]:
                min = L[a]
            pass
            if max <= L[a]:
                max = L[a]
            pass
        return (min, max)
    else:
        return (None, None)



if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

