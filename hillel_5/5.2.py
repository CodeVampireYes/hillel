while True:
    first_number = float(input('Первое число:'))
    second_number = float(input('Второе число:'))
    sign = input('Знак:')

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

    continuation = input('Нажмите "y" для продолжения:')
    if continuation == 'y':
        continue
    else:
        break
