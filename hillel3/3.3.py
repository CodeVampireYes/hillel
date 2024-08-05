my_list = []

length_list = len(my_list)

if length_list % 2 == 0:
    divide_list = int(length_list / 2)
else:
    divide_list = int(length_list / 2) + 1

new_list = []
new_list.append(my_list[0:divide_list])
new_list.append((my_list[divide_list:]))
print(new_list)