# list
wishlist = ['shahriar', 'kabir', 'sOhan', 'chaudhuree']
print(wishlist)

# insert method
print('insert')
wishlist.insert(0, 'sahab')
wishlist.insert(2, 'easha')
print(wishlist)

# list slice
# list[start:stop:step]
print('slice')
print(wishlist[1:3])

# list input in slice methods
print('slice and insert')
number = [1, 2, 3, 4, 5]
number[1:3] = ['a', 'b', 'c']
print(number)
number.clear()
print(number)

# list remove methods
# romove the first occurrence of the value
print('remove')
number = [1, 2, 3, 4, 5,2,7,8,2]
number.remove(2)
print(number)

# pop methods
# pop or delete last elements
# pop from index number pop(idx)
print('pop')
print(number.pop())
print(number)

# list iteration
print('iteration')
alphabets=['a','b','c','d','e','f','g']

for item in alphabets:
  print(item)

  # email list 
email = ['chaudhuree@gmail.com', 'sohan@gmail.com','kazi@gmail.com']
for peopel in email:
  print('***sending email to***' )
  print(peopel)