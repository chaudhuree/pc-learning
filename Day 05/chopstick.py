message = 'welcome to the game'
print(message)
print('*'*len(message))
num_left = 13
player_one = input("Player one, please enter your name: ")
player_two = input("Player two, please enter your name: ")
curent_player = player_one

# while True:
#   print("| "*num_left)
#   print(f'{num_left} chopstick left')
#   input_1=int(input(f'{player_one}, how many chopstic you want to pick: '))

#   num_left -=input_1
#   if num_left <= 0:
#       print(f'{player_one} wins')
#       break
#   print("| "*num_left)
#   print(f'{num_left} chopstick left')
#   input_2=int(input(f'{player_two}, how many chopstic you want to pick: '))
#   num_left -=input_1
#   if num_left <= 0:
#       print(f'{player_two} wins')
#       break

# print('GAME OVER')

while True:
    print("🥢 "*num_left)
    print(f'{num_left} chopstick left')
    choice = int(
        input(f'{curent_player}, how many chopstic you want to pick: '))
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(
            input('enter between 1 to 3: '))
    num_left -= choice
    if num_left <= 0:
        print(f'{curent_player} wins')
        break
    if(curent_player == player_one):
        curent_player = player_two
    else:
        curent_player = player_one

message = 'game over'
print(message)
print('#'*len(message))
