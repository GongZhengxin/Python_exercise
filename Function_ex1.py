#
# n1 = 255
# n2 = 1000
#
# print(hex(n1), hex(n2))

import math

print(math.sqrt(100))


def quadratic(a, b, c):
    if b ** 2 - 4 * a * c >= 0:
        slt1 = -b + math.sqrt(b ** 2 - 4 * a * c)
        slt1 = slt1/(2*a)
        slt2 = -b - math.sqrt(b ** 2 - 4 * a * c)
        slt2 = slt2 / (2 * a)
        return slt1, slt2
    else:
        print('no solution for the equation')
    return


# print(quadratic(2, 6, 3))
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')