def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n -= 1
    return s


def calc(*numbers):
    sum2 = 0
    for n in numbers:
        sum2 = sum2 + n * n
    return sum2


nums = [1, 2, 3]
print(calc(*nums))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)




