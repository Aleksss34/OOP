class Car:
    def __init__(self):
        self.__model = ''
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        if type(model) == str and 1<len(model)<101:
            self.__model = model
        
car1 = Car()
car1.model = 'Toyota'
print(car1.model)       

    