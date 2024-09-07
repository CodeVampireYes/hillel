def some_gen(begin: int, n: int, func) -> list[int]:
    """
    begin: перший елемент послідовності
    n: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    current = begin
    for _ in range(n):
        yield current
        current = func(current)


def pow(x: int) -> int:
    return x ** 2


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
