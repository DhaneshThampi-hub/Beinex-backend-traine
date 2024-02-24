'''1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise
NotImplementedError() exception with a suitable message.
2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)
Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from 
abc).
3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
Define constructor for each of them to assign the necessary parameters required for calculating the area.
Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.
Create an object for each of the subclasses and call the area method on the objects.'''




from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        This method should be overridden in the subclasses.
        """
        raise NotImplementedError("Area calculation is not implemented for this shape.")

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2

class Pentagon(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return (5 / 4) * self.side ** 2 / (pi / 5)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

while 1:
    print('1.Triangle')
    print('2.Square')
    print('3.Pentagon')
    print('4.Circle')
    print('5.Exit')
    ch=input("enter u r choice: ")
    if ch=='5':
        print('Exit')
        break
    else:
        if ch=='1':
            a=float(input("enter base of triangle: "))
            b=float(input('enter height of triangle: '))
            triangle = Triangle(base=a, height=b)
            print(f"Area of Triangle: {triangle.area()}")
        elif ch=='2':
            c=float(input('enter side of square: '))
            square = Square(side=c)
            print(f"Area of Square: {square.area()}")
        elif ch=='3':
            d=float(input('enter side of pentagon: '))
            pentagon = Pentagon(side=d)
            print(f"Area of Pentagon: {pentagon.area()}")
        elif ch=='4':
            r=float(input('enter radius of circle: '))
            circle = Circle(radius=r)
            print(f"Area of Circle: {circle.area()}")




