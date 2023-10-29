class Clock:
    def __init__(self):
        self.__time = 0
        def set_time(self, tm):
            if __check_time:
                __time = tm
       

        
        
        @property
        def time(self):
            return self.__time
        @time.setter
        def time(cls, tm):
            if type(tm)!=int or tm<0 or tm>100000:
                return False
            else:
                return True 
a = Clock()
a.time = 10
print(a.time)