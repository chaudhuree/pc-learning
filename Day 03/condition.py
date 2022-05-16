# in
var = 'a' in 'abba'
print(var)
var1 = 'A' in 'abba'
print(var1)
# 'int' is not iterable
# var2= 1 in 312
# print(var2)
var3 = 1 in [2, 1, 3, 4, 5, 6, 7, 8, 9]
print(var3)

# conditions input
# var = int(input('enter your age'))
var = 17
if (var > 18):
    print('you are in')
elif (var >= 16):
    print('come back after two years')
else:
    print('you are a kid')

# average length of american people name is 12
# check the input now

first_name = input(' Enter your first name')
last_name = input(' Enter your last name')
full_name = first_name+' '+last_name
name_length = len(full_name)

if(name_length == 12):
    print(f'{first_name} {last_name} is good as average length of american people name')
elif(name_length < 12):
    print(f'{first_name} {last_name} is shorter then average length of american people name')
elif(name_length > 12):
    print(f'{first_name} {last_name} is larger then average length of american people name')

