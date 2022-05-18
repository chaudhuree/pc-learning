# print every character of the string 'chaudhuree' using for loop

name = 'chaudhuree'
for i in name:
  print(i)

# print every character of the string 'chaudhuree' using while loop
index = 0
while index < len(name):
  print(name[index])
  index += 1

# print every even number between 100 to 140 inclusive 140 using for loop
for i in range(100,142,2):
  print(i)

# do same with while loop 

var=100
while var<=140:
  print(var)
  var+=2


# ask use to input 'goose' if not then ask again and again

quote=input('enter goose: ')

while quote !='goose':
  print('enter goose')

print('thank you for perticipation')