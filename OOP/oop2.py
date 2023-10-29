from random import *
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
line = [[randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)] for i in range(217)]

points = [f'point_{j}' for j in range(1, 217)]

a = [Line, Rect, Ellipse]
for _ in range(216):
    
    
    points[_] = a[randint(0, 2)](line[_][0], line[_][1], line[_][2], line[_][3])

for i in points:
    if type(i)==Line:
        i.sp = (0, 0)
        i.ep = (0, 0)
for j in points:
    print(j.__dict__)