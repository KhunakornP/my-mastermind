class Combination:
    def __init__(self, color, length):
        self.__color = color
        self.__length = length

    @property
    def color(self):
        return self.__color

    @property
    def length(self):
        return self.__length

    @property
    def combination(self):
        return self.__color*self.__length
