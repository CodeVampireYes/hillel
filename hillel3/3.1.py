first_number = float(input())
second_number = float(input())
sign = input()

if sign in ('*', '/', '-', '+'):
    if sign == '*':
        print(first_number * second_number)
    elif sign == '/':
        if second_number != 0:
            print(first_number / second_number)
        else:
            print('Делить на ноль нельзя')
    elif sign == '-':
        print(first_number - second_number)
    elif sign == '+':
        print(first_number + second_number)
else:
    print("Используйте только знаки: (*, /, -, +)")
















