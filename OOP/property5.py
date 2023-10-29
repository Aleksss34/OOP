class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__ridht = None
    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, obj):
        self.__left = obj
    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
    

    @classmethod
    def add_obj(cls, obj, node=None, left=True)