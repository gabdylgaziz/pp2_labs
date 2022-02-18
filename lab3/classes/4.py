class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
        self.x = x
        self.y = y
        return self.x, self.y
    def dist(self):
        return self.x - self.y

x, y = map(int, input().split())
P1 = Point(x, y)

print(*P1.show())

a, b = map(int, input().split())

print(*P1.move(a, b))
print(P1.dist())
    
        
        

        
        