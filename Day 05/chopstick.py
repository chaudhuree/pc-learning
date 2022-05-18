print('welcome to the game')
print('*'*19)
num_left = 13
player_one = input("Player one, please enter your name: ")
player_two = input("Player two, please enter your name: ")
# curent_player=player_one

while True:
  print("| "*num_left)
  print(f'{num_left} chopstick left')
  input_1=int(input(f'{player_one}, how many chopstic you want to pick: '))
  
  num_left -=input_1
  if num_left <= 0:
      print(f'{player_one} wins')
      break
  print("| "*num_left)
  print(f'{num_left} chopstick left')
  input_2=int(input(f'{player_two}, how many chopstic you want to pick: '))
  num_left -=input_1
  if num_left <= 0:
      print(f'{player_two} wins')
      break

print('GAME OVER')


