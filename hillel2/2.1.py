number = input('Введите четырёхзначное число:')
number = int(number)

print(number // 1000)
print((number // 100) % 10)
print((number // 10) % 10)
print(number % 10)