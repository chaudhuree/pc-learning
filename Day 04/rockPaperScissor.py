import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

# computer choice
num = random.randint(1, 3)
if num == 1:
    computerChoice = 'rock'
elif num == 2:
    computerChoice = 'paper'
else:
    computerChoice = 'scissors'

# user choice
userChoice = input('Enter your choice: rock/paper/scissors: ').lower()
print(f'user choice: {userChoice}')
if userChoice == 'rock':
    print(rock)
elif userChoice == 'paper':
    print(paper)
elif userChoice == 'scissors':
    print(scissors)

print(f'computer choice: {computerChoice}')

if computerChoice == 'rock':
    print(rock)
elif computerChoice == 'paper':
    print(paper)
elif computerChoice == 'scissors':
    print(scissors)
# figur out who wins print the result of the game
if userChoice == computerChoice:
    print('Draw')
elif userChoice == 'rock' and computerChoice == 'scissors':
    print('You win')
elif userChoice == 'rock' and computerChoice == 'paper':
    print('Computer wins')
elif userChoice == 'paper' and computerChoice == 'rock':
    print('You win')
elif userChoice == 'paper' and computerChoice == 'scissors':
    print('Computer wins')
elif userChoice == 'scissors' and computerChoice == 'paper':
    print('You win')
elif userChoice == 'scissors' and computerChoice == 'rock':
    print('Computer wins')
else:
    print('Computer wins')
