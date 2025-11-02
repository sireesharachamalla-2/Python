
# Parent class
class Shape:
    def draw(self):
        print("Drawing a shape")

# Child class - Circle
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

# Child class - Square
class Square(Shape):
    def draw(self):
        print("Drawing a square")

c = Circle()
s = Square()
c.draw()   
