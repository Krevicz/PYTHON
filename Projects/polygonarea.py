class triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        print(1/2 * self.base * self.height)
        
class square:
    def __init__(self, side):
        self.side = side
        
    def area(self):
        print(self.side * self.side)
        
class rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        
    def area(self):
        print(self.side1 * self.side2)
        
x = triangle(12, 6)
y = square(5)
z = rectangle(10, 5)

x.area()
y.area()
z.area()