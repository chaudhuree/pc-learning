# creating dictionary
my_dict={'name':'sOhan','age':'27','salary':'50000'}
# accessing dictionary
print(my_dict['name'])
# updating data
my_dict['name']='chaudhuree'
# adding data
my_dict['address']='Panchbibi'
print(my_dict)

# check if a key is available in dictionary or notScoped
# in operator
print('name' in my_dict)
print('hobby' in my_dict)

# another methot. it will also return the value if available or return none
# get method
print(my_dict.get('name'))
print(my_dict.get('hobby'))