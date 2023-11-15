import random
class Combination:
    def __init__(self, color, length):
        self.__color = color
        self.__length = length
        self.__code = []
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def code(self):
        comb_list = []
        for i in range(self.__length):
            rand_color = random.randint(0, self.__color)
            comb_list.append(rand_color)
        self.__code = comb_list
        return self.__code


class Board:
    def __init__(self):
        self.combination = Combination(4,6)

    def set_board(self):
        length = input("Enter code length: ")
        color = input("Enter the max amount of colors the code can contain: ")
        self.combination.length = length
        self.combination.color = color

    def guess(self, user_input):
        for i in self.combination.code:
            pass

