import random

roll_1 = random.randint(1, 6)
roll_2 = random.randint(1, 6)
roll_count = 1

while roll_1 != 1 or roll_2 != 1:
    print('Rolled:', roll_1, 'and', roll_2, '\n')
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    roll_count += 1

print('Rolled:', roll_1, 'and', roll_2, '\n')
print('yeaa.. snake eyes!')
print(f'it took {roll_count} rolls to get snake eyes')
