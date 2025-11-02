
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return math.pi * self.radius * 2 
o=Circle(3)
print(f"Area: {o.area():.2f}")
print(f"Perimeter: {o.perimeter():.2f}")
