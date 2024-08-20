import string

user_input = input()


if len(user_input) == 3:
    if user_input[0] or user_input[2] == user_input.isalpha():
        if user_input[1] == '-':
            first_letters = user_input[0]
            last_letters = user_input[2]
        else:
            print('Не правильный формат')
    else:
        print('Не правильный формат')
else:
    print('Не правильный формат')


result = []
first_index = 0
last_index = 0

for index, element in enumerate(string.ascii_letters):
    if first_letters == element:
        first_index = index
    elif last_letters == element:
        last_index = index

for index, letters in enumerate(string.ascii_letters):
    if index >= first_index and index <=last_index:
        result.append(letters)

result = ''.join(result)


print(result)




