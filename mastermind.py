import random
import copy


class Combination:
    """
    Represents a combination of colors.
    """
    def __init__(self, color, length):
        """
        Properties of the combination
        The length and color must be int.
        """
        self.__color = color
        self.__length = length

    @property
    def color(self):
        """color getter"""
        return self.__color

    @color.setter
    def color(self, color):
        """color setter"""
        self.__color = color

    @property
    def length(self):
        """length getter"""
        return self.__length

    @length.setter
    def length(self, length):
        """length setter"""
        self.__length = length

    @property
    def rand_code(self):
        """
        Randomizes a combination based on the
        parameters provided.
        """
        comb_list = []
        for _ in range(self.__length):
            rand_color = random.randint(1, self.__color)
            comb_list.append(rand_color)
        return comb_list


class Board:
    """
    Represents the board state.
    """
    def __init__(self):
        """
        The state of the board.
        """
        self.combination = Combination(6, 4)
        self.__code = [1, 2, 3, 4]

    @property
    def code(self):
        """code getter"""
        return self.__code

    def gen_puzzle(self):
        """Generates the puzzle."""
        self.__code = self.combination.rand_code

    def set_board(self):
        """
        Sets the game rules based on user input.
        If user inputs an invalid rule ask for new input.
        """
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
        """
        Submits the guess of the user.
        If a color matches but is in an incorrect position return "*"
        If a color matches both position and color return "o"
        """
        hint = []
        code = copy.copy(self.code)
        if len(user_input) < len(code):
            return "Invalid guess"
        if not user_input.isdigit():
            return "Invalid guess"
        for i in range(len(user_input)):
            if int(user_input[i]) == code[i]:
                hint.append("o")
                code[i] = -1
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
        """
        Runs the game.
        """
        print(f"Playing Mastermind with {self.combination.color} colors and "
              f"{self.combination.length} positions.")
        rounds = 1
        guess = input("Enter your guess: ")
        answer = self.guess(guess)
        print(answer)
        if answer == "Invalid guess":
            rounds -= 1
        while answer != self.guess(''.join(str(x) for x in self.code)):
            guess = input("Enter your guess: ")
            answer = self.guess(guess)
            print(answer)
            if answer != "Invalid guess":
                rounds += 1
        print(f"You win the code was {''.join(str(x) for x in self.code)}"
              f", you took {rounds} round(s)")
        again = input("Retry? (y/n): ")
        if again == "y":
            self.play()
        print()

    def menu(self, choice):
        """
        Menu to choose which function to run
        """
        if choice == "1":
            self.gen_puzzle()
            self.play()
        if choice == "2":
            self.set_board()


# main part
print("Welcome to mastermind")
print("To play enter 1.\nTo edit settings enter 2.\nTo exit press 0.")
board = Board()
action = input("Enter action: ")
print()
while action != "0":
    board.menu(action)
    print("To play enter 1.\nTo edit settings enter 2.\nTo exit press 0.")
    action = input("Enter action: ")
    print()
