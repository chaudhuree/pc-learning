# list
alist=[21,31,45]
print(alist)

# accessing list elements
print(alist[0])
print(alist[1])

# updating list element
alist[0]=22
print(alist)

# appending elements to list
wishlist=['apple','banana','mango']
print(wishlist)
wishlist.append('orange')

# append takes itterable object
fruits=['cherry','watermelon','grapes']

wishlist.extend(fruits)
print(wishlist)