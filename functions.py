
# functions purpose is to recycle functionality/logic




def add_nums(first_num, second_num):
    output = first_num + second_num
    return output



new_sum = add_nums(25, 82)


print(new_sum)



def print_favorites(alist_of_food):
    for food in alist_of_food:
        if type(food) == str:
            print('I love to eat ' + food)
        else:
            print('Theses are my favorite ice cream flavors:')
            for ice_cream in food:
                print(ice_cream)


new_foods = ['Broccoli', 'Squash', 'Apples', 'Potatoes']

carnivor = ['Steak', 'Chicken', 'Pork']

print_favorites(carnivor)


def greeting(name):
    return 'Hello there ' + name + '!'


jake_greeting = greeting('Jake')

print(jake_greeting)