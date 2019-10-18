#
# L = list(range(100))
#
# a= L[::4]
#
# print(a)
#

# def trim(s):
#     i = 0
#     j = -1
#     while i <= len(s) - 1:
#         if s[i] == ' ':
#             i = i + 1
#         else:
#             break
#
#     while j >= -len(s):
#         if s[j] == ' ':
#             j = j - 1
#         else:
#             break
#
#     first = i
#     last = len(s) + j + 1
#     return s[first:last]


def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    if s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s


if trim('hello  ') != 'hello':
    print(trim('hello  '), 'hello', '测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
