import math


class Rectangle:

    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> int | float:
        return self.width * self.height

    def __eq__(self, other: 'Rectangle') -> bool:
        return self.get_square() == other.get_square()

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        new_area = self.get_square() + other.get_square()
        new_width = math.sqrt(new_area)
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n: int | float) -> 'Rectangle':
        new_area = self.get_square() * n
        new_width = math.sqrt(new_area)
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
