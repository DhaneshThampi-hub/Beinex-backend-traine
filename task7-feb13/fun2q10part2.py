

from fun2q10part1 import rectangle_area
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = rectangle_area(length, width)
print(f"The area of the rectangle with length {length} and width {width} is: {area}")