class WindowDig:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height
    def show(self):
        return f'{self.__title}, {self.__width}, {self.__height}'
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if type(width) == int:
            self.__width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if type(height) == int:
            self.__height = height
wnd = WindowDig('roblox', 200, 199)
print(wnd.show())
wnd.height = 10
wnd.width = 10
print(wnd.width)
print(wnd.height)
print(wnd.show())