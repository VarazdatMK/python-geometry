import pytest
from geometry import Triangle

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert abs(triangle.area() - 6.0) < 1e-6

def test_triangle_right_angled():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_angled()

def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)  # Not a valid triangle