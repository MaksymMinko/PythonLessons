penny = int(input('Enter the amount of pennies '))
nickel = int(input('Enter the amount of nickels '))
dime = int(input('Enter the amount of dimes '))
quarter = int(input('Enter the amount of quarters '))
sum = penny + nickel * 5 + dime * 10 + quarter * 25
if sum == 100:
    print('You WON!!!')
elif sum < 100:
    print('Amount is lesser than required!')
else:
    print('Amount is greater than required!')
