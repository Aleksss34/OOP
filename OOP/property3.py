class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) and isinstance(next, None)
        self.__next = next
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data
class Stack:
    def __init__(self):
        self.top = None
        self.last = None
    def push(self, obj):
        if self.last:
            self.last.next = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        