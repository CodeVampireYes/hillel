def is_even(number: int) -> bool:
    str_num = str(number)
    if str_num[-1] == '0' or str_num[-1] == '2' or str_num[-1] == '4' or str_num[-1] == '6' or str_num[-1] == '8':
        return True
    else:
        return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')