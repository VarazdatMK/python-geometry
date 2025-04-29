from math import sqrt
from geometry import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        sides = sorted([a, b, c])
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid triangle sides.")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-6