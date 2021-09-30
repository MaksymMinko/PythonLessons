m = float(input('Enter the mass: '))
w = m * 9.8
if w <= 100:
    print('Your weight is too small')
elif w >= 500:
    print('Your weight is too large')
