import keyword

#input_user = input()
input_user = "assert_exception"
check_digit = not input_user.isidentifier()
check_up_letters = bool()
check_space = bool()
check_registered_word = bool()
check_double_underscore = bool(input_user.count('_') == len(input_user) and len(input_user) != 1)

for index, el in enumerate(input_user):
    if el.isupper():
        check_up_letters = True
    if el.isspace():
        check_space = True

for el in keyword.kwlist:
    if el == input_user:
        check_registered_word = True

if check_digit or check_up_letters or check_space or check_registered_word or check_double_underscore == True:
    print(False)
else:
    print(True)




