from random import randint
class Cell:
    def __init__(self, around_mines=0, mine=False):
        
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
        
        self.init()
        self.show()
        proverka = True
        while proverka:
            # a, b = map(int, input('Введите место которое хотите проверить в формате строка пробел место в строке').split())
            self.opens(1, 1)
            return self.pole
    def init(self):
        for i in range(self._m):
            self.pole[randint(0, self._n-1)][randint(0, self._n-1)].mine = True
    def show(self):
        for i in range(self._n):
            for j in range(self._n):
                if self.pole[i][j].fl_open == False:
                    self.pole[i][j] = '#'
            
        
    def opens(self, a , b):
        if self.pole[a][b].mine == True:
            print('Вы проиграли')
        else:
            check=0
            if self.pole[a-1][b].mine == True:
                 check+=1
            if self.pole[a+1][b].mine == True:
                 check+=1
            if self.pole[a-1][b].mine == True:
                 check+=1
            if self.pole[a-1][b+1].mine == True:
                 check+=1
            if self.pole[a-1][b-1].mine == True:
                 check+=1
            if self.pole[a+1][b-1].mine == True:
                 check+=1
            if self.pole[a+1][b+1].mine == True:
                 check+=1
            if self.pole[a][b+1].mine == True:
                 check+=1
            if self.pole[a][b-1].mine == True:
                 check+=1
            self.pole[a][b] = check
            self.pole[a][b].fl_open = True

                
        
a = GamePole(3, 3)

