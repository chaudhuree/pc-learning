# dictionary
my_dict={
  'name':'chaudhuree',
  'age':27,
  'salary':50000,
  'address':'panchbibi',
  'hobby':'cricket',
  'favFood':'beef',
  'interestedIn':'web development'
}

# accessing dictionary
print(my_dict)
# pop method of dictionary
# return any item and delete it
name=my_dict.pop('name')
print(name)

# popitem return the last key vale pair
popItem=my_dict.popitem()
print(popItem)

# del method
del my_dict['age']
print(my_dict)

# clear method
my_dict.clear()
print(my_dict)