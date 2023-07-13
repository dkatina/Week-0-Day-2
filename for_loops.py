#Iterable Data Type, String, Lists

favorite_foods = ['Apple Pie', 'Pepperoni Pizza', 'Hibachi', 'Shawarma', ['vanilla', 'moose tracks', 'mint cc']] 


for food in favorite_foods:

    if type(food) == str:
        print('I love to eat ' + food)
    else:
        print('Theses are my favorite ice cream flavors:')
        for ice_cream in food:
            print(ice_cream)



first = 'Dylan'
last = 'Katina'

fullname = first + ' ' + last
print(fullname)