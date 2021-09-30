color1 = input('Please choose the first color from: red, yellow and blue: ').lower()
color2 = input('Please choose the second color from: red, yellow and blue: ').lower()
if color1 == color2:
    print('Your color is - ', color1)
elif (color1 == 'red' or color2 == 'red') and (color1 == 'blue' or color2 == 'blue'):
    print('Your color is - purple')
elif (color1 == 'red' or color2 == 'red') and (color1 == 'yellow' or color2 == 'yellow'):
    print('Your color is - orange')
elif (color1 == 'yellow' or color2 == 'yellow') and (color1 == 'blue' or color2 == 'blue'):
    print('Your color is - green')
else:
    print("You didn't choose correct colors")
