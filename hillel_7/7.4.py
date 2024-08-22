def common_elements() -> set:
    set1 = set()
    set2 = set()
    for num in range(100):
        if num % 3 == 0:
            set1.add(num)
        if num % 5 == 0:
            set2.add(num)
    return set1.intersection(set2)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')
