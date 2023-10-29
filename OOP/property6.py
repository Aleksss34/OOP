class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0),)+args)
    def get_path(self):
        return self.coords[1:]
    def get_length(self):
        for i in range(1, len(self.coords)):
            g = (self.coords[i-1], self.coords[i]
class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
line1 = LineTo(1, 1)    
line2 = LineTo(2, 2)
p = PathLines(line1, line2)
print(p.get_path())