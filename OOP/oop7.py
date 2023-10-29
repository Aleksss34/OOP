class Clock:
    def __init__(self):
        self.__time = 0
        def set_time(self, tm):
            if __check_time:
                __time = tm
        def get_time(self):
            return self.__time

        
        
        @classmethod
        def __check_time(cls, tm):
            if type(tm)!=int or tm<0 or tm>100000:
                return False
            else:
                return True 