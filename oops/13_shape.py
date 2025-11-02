
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")
# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return math.pi * self.radius * 2

# Subclass: Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    def perimeter(self):
        return self.side * 4
    
# Subclass: Triangle
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.a = side1
        self.b = side2
        self.c = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.a + self.b + self.c
    
t=Triangle(base=6,height=4,side1=5,side2=6,side3=7)
print(t.area())
