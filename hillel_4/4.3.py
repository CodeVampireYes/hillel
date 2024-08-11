import random

test_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]

result = [test_list[0], test_list[2], test_list[-2]]
print(test_list)
print(result)

