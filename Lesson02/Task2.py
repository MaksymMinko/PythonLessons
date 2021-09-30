num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))
num4 = int(input('Enter the forth number: '))
f = 0
if num1 <= num2 and num3 <= num2 and num4 <= num2:
    c = num2
elif num1 <= num3 and num2 <= num3 and num4 <= num3:
    c = num3
elif num1 <= num4 and num2 <= num4 and num3 <= num4:
    c = num4
elif num2 <= num1 and num3 <= num1 and num4 <= num1:
    c = num1
if num1 == c:
    f = f + 1
if num2 == c:
    f = f + 1
if num3 == c:
    f = f + 1
if num4 == c:
    f = f + 1
print(c)
print(f)
