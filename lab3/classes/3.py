class Shape:
    def __init__(self, area):
        self.area = 0
        
class Square(Shape):
    def __init__(self, length, area):
        self.length = length
        super().__init__(area)
    def Area(self):
        return self.area, self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width, area):
        self.length = length
        self.width = width
        super().__init__(area)
    def Area(self):
        return self.area, self.length * self.width

a, b = map(int, input().split())
S1 = Rectangle(a, b, 0)

print(*S1.Area())

        
        