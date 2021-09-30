weight = int(input('Enter the weight on grams: '))
if weight > 1000:
    p = weight * 475 / 100
elif weight > 600:
    p = weight * 400 / 100
elif weight > 200:
    p = weight * 300 / 100
elif weight > 0:
    p = weight * 150 / 100
else:
    print('You entered incorrect weight!')
print('You have to pay for the delivery - ', p)
