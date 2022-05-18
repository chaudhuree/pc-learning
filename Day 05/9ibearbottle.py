# 99 bear bottle coding with for loop
for i in range(99, 0, -1):
    print("*"*i)
    print(f'{i}, bottles of beer on the wall')
    print(f'{i}, bottles of beer')

    if i == 1:
        print('take one down, pass it around')
        print('no more bottles of beer on the wall')
    else:
        print('take one down, pass it around')

print('no more bottles of beer on the wall, no more bottles of beer')
print('go to the store and buy some more')
