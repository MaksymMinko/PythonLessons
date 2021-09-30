num = int(input('How many books did you buy? '))
if num >= 8:
    print('You earned 60 points')
elif num >= 6:
    print('You earned 30 points')
elif num >= 4:
    print('You earned 15 points')
elif num >= 2:
    print('You earned 5 points')
else:
    print('You earned 0 points')
