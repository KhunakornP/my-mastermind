import random
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
        comb_list = []
        for i in range(self.__length):
            rand_color = random.randint(0, self.__length)
            comb_list.append(rand_color)
        return comb_list

