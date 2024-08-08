import random

test_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
my_list = []
result = []


for el in test_list:
    my_list.append(el)

index = len(my_list) - 2

result.append(my_list[0])
result.append(my_list[2])
result.append(my_list[index])

print(my_list)
print(result)

