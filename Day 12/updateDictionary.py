order={'cost':34,'quantity':2}

order.update({'name':'tacho','date':"23/04/2022"})
print(order)

# combne dictionary
dict_1={'name':'tacho','date':"23/04/2022"}
dict_2={'cost':34,'quantity':2}
main_dict={**dict_1,**dict_2}
print(main_dict)