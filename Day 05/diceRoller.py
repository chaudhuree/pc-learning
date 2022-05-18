import random

num_dice = int(input("How many dice would you like to roll? "))
num_sides = int(input("How many sides are on each die? "))

while True:
    result = '|'
    for i in range(num_dice):

        value = random.randint(1, num_sides)
        result += f'{value}|'
        # print(value)
    print(result)

    quit = input("Roll again?? press q to quit..")
    if quit == 'q':
        break
