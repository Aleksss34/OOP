class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    @classmethod
    def __is_verify(self, value):
        return type(value) == (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD:
      
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if self.__is_verify(x):
            self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if self.__is_verify(y):
            self.__y = y   
    def norm2(vector):
        return vector.__x*vector.__x + vector.__y*vector.__y