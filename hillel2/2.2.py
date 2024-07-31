number = input('Введите пятизначное число:')
number = int(number)

number5 = number // 10000
number4 = number // 1000 % 10
number3 = number // 100 % 10
number2 = number // 10 % 10
number1 = number % 10

result = (number1 * 10000) + (number2 * 1000) + (number3 * 100) + (number4 * 10) + (number5 )
print(result)