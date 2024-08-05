first_number = float(input())
second_number = float(input())
if second_number == 0:
    print('На ноль делить нельзя')
else:
    sign = input()
    if sign == '*':
        print(first_number * second_number)
    elif sign == '/':
        print(first_number / second_number)
    elif sign == '-':
        print(first_number - second_number)
    elif sign == '+':
        print(first_number + second_number)
    else:
        print("Используйте только знаки: (*, /, -, +)")
















