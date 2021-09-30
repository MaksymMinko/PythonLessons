year = int(input('Enter the year: '))
a = year % 100
b = year % 400
c = year % 4
if (a == 0 and b == 0) or (a != 0 and c == 0):
    print('We have 29 days in February')
else:
    print('We have 28 days in February')
