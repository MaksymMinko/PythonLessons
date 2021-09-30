month = int(input('Enter the month: '))
day = int(input('Enter the day: '))
year = int(input('Enter last two numbers from the year: '))
magic = month * day
if magic == year:
    print('It is a magical date')
else:
    print("It isn't a magical date")
