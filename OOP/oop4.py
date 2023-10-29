class Cart:
    def __init__(self, *goods):
        self.goods = list(goods)
    def add(self, gd):
        self.goods.append(gd)
    def remove(self, itm):
        del self.goods[itm]
    def get_list(self):
        return [f'{self.goods[i].name}:{self.goods[i].price}' for i in range(len(self.goods))]
            
        
class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

table1 = Table('glass', 15000)
tv = TV('плазма', 50000)
table2 = Table('дерево', 10000)
notebook = Notebook('аймак', 150000)
cup = Cup('кап', 13000)


cart = Cart(table1, tv, table2, notebook, cup)




print(cart.get_list ())
