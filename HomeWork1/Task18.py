a = input('Will there be a vegetarian at dinner (Yes/No)? ').lower()
b = input('Will there be a vegan at dinner (Yes/No)? ').lower()
c = input('Will there be a gluten-free diet lover at dinner (Yes/No)? ').lower()
print('Here are your options for restaurants:')
rest1 = "Joe's Gourmet Burgers"
rest2 = 'Central Pizzeria'
rest3 = 'Cafe around the corner'
rest4 = 'Dishes from Italian mom'
rest5 = "Chef's Kitchen"
if a == 'no' and b == 'no' and c == 'no':
    print(rest1, '\n',
          rest2, '\n',
          rest3, '\n',
          rest4, '\n',
          rest5)
elif a == 'yes' and b == 'no' and c == 'no':
    print(rest2, '\n',
          rest3, '\n',
          rest4, '\n',
          rest5)
elif b == 'no' and c == 'yes':
    print(rest2, '\n',
          rest3, '\n',
          rest5)
elif b == 'yes':
    print(rest3, '\n',
          rest5)
