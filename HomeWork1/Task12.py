num = int(input('How many packages do you want to buy? '))
if num >= 100:
    sum = num * 99 * (1 - 0.4)
elif num >= 50:
    sum = num * 99 * (1 - 0.3)
elif num >= 20:
    sum = num * 99 * (1 - 0.2)
elif num >= 10:
    sum = num * 99 * (1 - 0.1)
elif num > 0:
    sum = num * 99
else:
    print('You put incorrect value!')
print('You have to pay - ', sum)
