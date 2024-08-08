test_list = []
my_list = []
result = 0

for index, el in enumerate(test_list):
    if sum(test_list) != 0:
        x = el
        if index % 2 == 0:
            my_list.append(el)
        result = sum(my_list) * x

print(result)


