age = int(input('Enter the age: '))
if age < 1:
    print('You are a baby')
elif not age < 1 and age < 13:
    print('You are a child')
elif not 13 > age and age < 20:
    print('You are a teenager')
else:
    print('You are an adult')
