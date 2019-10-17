
height = input('height (m)')
height = float(height)
weight = input('weight (kg)')
weight = float(weight)

bmi = weight / (height ** 2)

if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else: print('超重')
