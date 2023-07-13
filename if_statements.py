
# If statements

# If a certain condition is met, any code inside the if statement's block will 
# be executed

age = 55


if age < 18:
    print("You're still just a child")
elif age < 40:
    print("you're an adult")
elif age < 65:
    print("You're over the hump")
else:
    print("You're in your golden years") 

#And / Or

pizza = 'Cheese'
pie = 'Pecan'

if pizza == 'Pepperoni' and pie == 'Apple':
    print("We've got ourselves a party!")
else:
    print("Why did I even show up?")


raining = False
night = False

if raining or night:
    print("I'm definitely inside")
else:
    print("There is a good chance I'm still inside")

# Truesy and Falsey

num = True

if num:
    print('I do have value')
else:
    print('No value')
