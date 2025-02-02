class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'X: {self.x}    Y: {self.y}')

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y
        return self.x, self.y
    
    def dist(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
        return ((self.x - self.x2)**2 + (self.y - self.y2)**2)**0.5
    
point = Point(2,4)
point.show()
point.move(3,2)
point.show()
print(f"distance: {point.dist(5,7)}")
print(f"distance: {point.dist(1,1)}")
