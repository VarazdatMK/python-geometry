import pytest
from geometry import Circle

def test_circle_area():
    circle = Circle(2)
    assert abs(circle.area() - 12.5663706) < 1e-6

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)