class conjunto:
    __conjunto=[]
    def __init__(self,conjunto):
        self.__conjunto=conjunto
    def __add__(self,otro):
        self.__conjunto += otro
        return self