# while loop
from itertools import count


answer=input('say hi: ')
while answer != 'hi':
    answer=input('rude,say hi: ')
print('hi to you too..')

# pyramid using while loop
count=8
while count > 0:
    print(' '*(count-1),'*'*(count))
    count-=1
    
count=1
while count < 8:
    print(' '*(count-1),'*'*(count))
    count+=1
