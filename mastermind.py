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
            rand_color = random.randint(1, self.__color)
            comb_list.append(rand_color)
        return comb_list


class Board:
    def __init__(self):
        self.combination = Combination(6,4)
        self.__code = [1,2,3,4]

    @property
    def code(self):
        return self.__code

    def gen_puzzle(self):
        self.__code = self.combination.rand_code

    def set_board(self):
        length = input("Enter code length (1-10): ")
        color = input("Enter the max amount of colors "
                      "the code can contain (1-8): ")
        while not length.isdigit() and not color.isdigit():
            print("Invalid length or color try again")
            length = input("Enter code length: ")
            color = input("Enter the max amount of colors"
                          " the code can contain: ")
        if not 1 <= int(color) <= 8 or not 1 <= int(length) <= 10:
            print("Length or color exceeds maximum limit.")
            self.set_board()
        self.combination.length = int(length)
        self.combination.color = int(color)

    def guess(self, user_input):
        hint = []
        code = copy.copy(self.code)
        if len(user_input) < len(code):
            return "Invalid guess"
        for i in range(len(user_input)):
            if int(user_input[i]) == code[i]:
                hint.append("o")
                code[i] = -1
                continue
            elif int(user_input[i]) in code:
                index = code.index(int(user_input[i]))
                if user_input[index] == user_input[i]:
                    hint.append("o")
                    code[index] = -1
                    continue
                hint.append("*")
                code.pop(index)
                code.insert(index, -1)
        hint.sort()
        return "".join(hint)

    def play(self):
        print(f"Playing Mastermind with {self.combination.color} colors and "
              f"{self.combination.length} positions.")
        self.gen_puzzle()
        round = 1
        guess = input("Enter your guess: ")
        answer = self.guess(guess)
        print(answer)
        if answer == "Invalid guess":
            round -= 1
        while answer != self.guess(''.join(str(x) for x in self.code)):
            guess = input("Enter your guess: ")
            answer = self.guess(guess)
            print(answer)
            if answer != "Invalid guess":
                round += 1
        print(f"You win the code was {''.join(str(x) for x in self.code)}"
              f", you took {round} round(s)")

    def menu(self, action):
        if action == "1":
            self.play()
        if action == "2":
            self.set_board()

# main part
print("Welcome to mastermind")
print("To play enter 1.\nTo edit settings enter 2.\nTo exit press 0.")
board = Board()
action = input("Enter action: ")
print()
while action != "0":
    board.menu(action)
    action = input("Enter action: ")
    print()