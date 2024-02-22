'''3)Write a Python class, Square, and define two methods that return the square area and perimeter.'''

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
side_length = float(input("Enter the side length of the square: "))
square = Square(side_length)
print(f"Area of the square: {square.area()}")
print(f"Perimeter of the square: {square.perimeter()}")
