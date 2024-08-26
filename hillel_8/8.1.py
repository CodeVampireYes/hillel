def add_one(some_list: list) -> list:
    result = []
    convert_to_string = int(''.join(map(str, some_list)))
    convert_to_string += 1
    convert_to_string = str(convert_to_string)
    for el in convert_to_string:
        result.append(int(el))
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
