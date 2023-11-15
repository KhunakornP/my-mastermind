import random
import copy
class Combination:
    def __init__(self, color, length):
        self.__color = color
        self.__length = length
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
    def rand_code(self):
        comb_list = []
        for i in range(self.__length):
            rand_color = random.randint(0, self.__color)
            comb_list.append(rand_color)
        return comb_list


class Board:
    def __init__(self):
        self.combination = Combination(4,6)
        self.__code = [1,2,3,4]

    @property
    def code(self):
        return self.__code

    def gen_puzzle(self):
        self.__code = self.combination.rand_code

    def set_board(self):
        length = input("Enter code length: ")
        color = input("Enter the max amount of colors the code can contain: ")
        while not length.isdigit() and not color.isdigit():
            print("Invalid length or color try again")
            length = input("Enter code length: ")
            color = input("Enter the max amount of colors"
                          " the code can contain: ")
        self.combination.length = length
        self.combination.color = color

    def guess(self, user_input):
        hint = []
        code = copy.copy(self.code)
        for i in range(len(user_input)):
            if int(user_input[i]) == code[i]:
                hint.append("o")
                code[i] = 0
                continue
            elif int(user_input[i]) in code:
                hint.append("*")
                index = code.index(int(user_input[i]))
                code.pop(index)
                code.insert(index, 0)
        hint.sort()
        return "".join(hint)

    def play(self):
        print(f"Playing Mastermind with {self.combination.color} colors and "
              f"{self.combination.length} positions.")
        self.gen_puzzle()
        round = 1
        guess = input("Enter your code: ")
        answer = self.guess(guess)
        print(answer)
        while answer != self.guess(''.join(str(x) for x in self.code)):
            guess = input("Enter your guess: ")
            answer = self.guess(guess)
            print(answer)
            round += 1
        print(f"You win the code was {''.join(str(x) for x in self.code)}"
              f", you took {round} round(s)")

# main part
# print("Welcome to mastermind")
# print("To play enter 1.\nTo edit settings enter 2.\nTo exit press 0.")
# action = input("Enter action: ")
board = Board()
board.play()