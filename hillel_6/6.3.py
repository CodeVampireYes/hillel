# Введення числа користувачем
input_number = int(input("Введите целое число: "))

while input_number > 9:
    result = 1
    while input_number > 0:
        digit = input_number % 10
        result *= digit
        input_number //= 10
    input_number = result

print(input_number)
