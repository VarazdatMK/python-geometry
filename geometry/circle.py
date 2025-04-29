from math import pi
from geometry import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2