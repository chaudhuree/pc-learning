order = {'cost': 34, 'quantity': 2}

order.update({'name': 'tacho', 'date': "23/04/2022"})
print(order)
print("\n")

# combne dictionary
print('combine dictionary')
dict_1 = {'name': 'tacho', 'date': "23/04/2022"}
dict_2 = {'cost': 34, 'quantity': 2}
main_dict = {**dict_1, **dict_2}
print(main_dict)
print("\n")

# union
print('union')
union_dict = dict_2 | dict_1
print(union_dict)
print("\n")
