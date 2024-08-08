test_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for element in test_list:
    if element == 0:
        test_list.remove(element)
        test_list.append(element)
print(test_list)