class Employees:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age
    
employ_1 = Employees('Aleks', 20)

employ_1.age = 10
print(employ_1.age)