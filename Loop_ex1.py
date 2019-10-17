numlist = []
sum1 = 0
# for i in range(201):
#     if i % 2:
#         numlist.append(i)
#     pass
#
# for x in numlist:
#     sum1 = sum1 + x
#     print(sum1)

# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print('hello, %s' % x)

n = 100

while n >= 0:
    if n % 2:
        n -= 1
        continue
    sum1 = sum1 + n
    n -= 1
    print(sum1)
print('end')

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)

