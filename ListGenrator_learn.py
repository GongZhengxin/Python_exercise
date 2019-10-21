# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L1 if isinstance(x,str) ]
# print(L2)
#
#

# g = (x % 2 for x in range(10))
#
#
# def fac(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fac(n - 1)
#
#
# def triangles():
#     # res = [1]
#     n = 0
#     while True:
#         res = [int(fac(n) / (fac(a) * fac(n - a))) for a in list(range(n + 1))]
#         yield res
#         n += 1
#
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')
#
#
#     def triangles():
#         L = [1]
#         while 1:
#             yield L
#             L = [0] + L + [0]
#             L = [L[i] + L[i + 1] for i in range(len(L) - 1)]

names = 'gzx '
print('wo de mingzi {0}'.format(names))
print('wo de mingzi' + names)
print('%s' % names)
