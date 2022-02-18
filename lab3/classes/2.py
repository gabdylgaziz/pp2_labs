class Shape:
    def __init__(self, area):
        self.area = 0
class Square(Shape):
    def __init__(self, length, area):
        self.length = length
        super().__init__(area)
    def Area(self):
        return self.area, self.length * self.length
        
S1 = Square(int(input()), 0)

print(*S1.Area())

        
        