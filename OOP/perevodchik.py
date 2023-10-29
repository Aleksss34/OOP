class p1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class p2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    __slots__ = ('x', 'y')
a = p1(1, 2)
print(a.x, a.y)
a.z = 0
a2 = p2(2, 3)
print(a.__sizeof__() + a.__dict__.__sizeof__())         
print(a2.__sizeof__())