# Geometry Library

A simple Python library to calculate various shapes areas


## Features
- Calculates the area of a **Circle** based on its radius.
- Calculates the area of a **Triangle** based on its three sides.
- Includes a function to check if a triangle is **right-angled**.
- Easy to add support for new geometric shapes.
- Unit tests included for Circle and Triangle shapes.
- **example_usage.py** included to demonstrate the proper way to use the lib

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/VarazdatMK/python-geometry.git
cd python-geometry
python3 -m venv env
source env/bin/activate   # On Windows, use: env\Scripts\activate
pip install -r requirements.txt
```

## Usage
Here's an example of how to use the library:

```python
from geometry import Circle, Triangle

# Create a circle with radius 5
circle = Circle(5)
print(f"Circle area: {circle.area()}")

# Create a triangle with sides 3, 4, and 5
triangle = Triangle(3, 4, 5)
print(f"Triangle area: {triangle.area()}")
print(f"Is the triangle right-angled? {triangle.is_right_angled()}")
```

## Testing
Unit tests are available for the current implementation. To run tests, use the following command:
```bash
pytest
```

## Adding New Shapes
To add a new shape to the library:
1. Create a new Python file for the shape in the geometry/ directory.
2. Implement the Shape class, inheriting from the **Shape** base class.
3. Implement the **area** method and any additional functionality as needed.
4. Add an import for the new shape to the geometry/__init__.py file to make it available at the package level.
5. Write unit tests for your new shape in the tests/ directory.

## License
This project is licensed under the MIT License - see the **LICENSE** file for details.
