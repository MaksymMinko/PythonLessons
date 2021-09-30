num = int(input('Please put the number - '))
if num == 0:
    print('The pocket is green')
else:
    b = num % 2
    if 1 <= num and 10 >= num and b == 0:
        print('The pocket is black')
    elif 11 <= num and 18 >= num and 0 != b:
        print('The pocket is black')
    elif 11 <= num and 18 >= num and 0 == b:
        print('The pocket is red')
    elif 19 <= num and 28 >= num and 0 != b:
        print('The pocket is red')
    elif 19 <= num and 28 >= num and 0 == b:
        print('The pocket is black')
    elif 29 <= num and 36 >= num and 0 != b:
        print('The pocket is black')
    elif 29 <= num and 36 >= num and 0 == b:
        print('The pocket is red')
    else:
        print('Your number is not correct')
