class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, a):
        self.lenght = a
    def area(self):
        return self.lenght ** 2
    
class Rectangle(Square):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    
a = Shape()
b = Square(4)
c = Rectangle(3,5)
print(f"S = {a.area()}")
print(f"S = {b.area()}")
print(f"S = {c.area()}")