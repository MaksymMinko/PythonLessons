a1 = input('Enter the first side of the first rectangle: ')
b1 = input('Enter the second side of the first rectangle: ')
a2 = input('Enter the first side of the second rectangle: ')
b2 = input('Enter the second side of the second rectangle: ')
s1 = float(a1) * float(b1)
s2 = float(a2) * float(b2)
print('Area of the first rectangle = ', s1)
print('Area of the second rectangle = ', s2)
if s1 > s2:
    print('So, the first rectangle is larger than the second')
elif s2 > s1:
    print('So, the second rectangle is larger than the first')
else:
    print('So, rectangles are equal')
