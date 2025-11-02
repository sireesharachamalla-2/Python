
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Subclass: Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
square = Square(4)
print(square.area()) 
