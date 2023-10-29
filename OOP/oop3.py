class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if type(self.a)!=int or type(self.b)!=int or type(self.c)!=int or self.a<=0 or self.b<=0 or self.c<=0:
            return 1
        if self.a+self.b <= self.c or self.a+self.c <= self.b or self.c+self.b <= self.a:
            return 2
        else:
            return 3
a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
