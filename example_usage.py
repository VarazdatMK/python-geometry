from geometry import Circle, Triangle

def main():
    shapes = [
        Circle(5),
        Triangle(3, 4, 5)
    ]

    for shape in shapes:
        print(f"Shape type is: {type(shape).__name__}, Area: {shape.area()}")

    triangle = Triangle(3, 4, 5)
    print(f"Is triangle right-angled? {triangle.is_right_angled()}")

if __name__ == "__main__":
    main()
