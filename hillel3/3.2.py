my_list = [12, 10 ,11]
if len(my_list) > 0:
    last_number = my_list[-1]
    my_list.remove(last_number)
    my_list.insert(0, last_number)
    print(my_list)
else:
    print(my_list)
