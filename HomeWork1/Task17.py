print('Please reboot the PC and try connect again')
a = input('It was helped (Yes/No)? ').lower()
if a == 'yes':
    print('Congratulation!')
elif a == 'no':
    print('Please reboot the router and try connect again')
    a = input('It was helped (Yes/No)? ').lower()
    if a == 'yes':
        print('Congratulation!')
    elif a == 'no':
        print('Make sure the cables between the router and the modem are firmly connected')
        a = input('It was helped (Yes/No)? ').lower()
        if a == 'yes':
            print('Congratulation!')
        elif a == 'no':
            print('Move your router to a new location')
            a = input('It was helped (Yes/No)? ').lower()
            if a == 'yes':
                print('Congratulation!')
            elif a == 'no':
                print('Take a new router!')
else:
    print('Incorrect value!')
