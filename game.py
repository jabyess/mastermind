from ansitest import ansi
import random


class Game:

    def __init__(self):
        # generate 4 colors
        # red green yellow blue magenta cyan
        self.red = f"   {ansi.background.red}   {ansi.end}"
        self.green = f"   {ansi.background.green}   {ansi.end}"
        self.yellow = f"   {ansi.background.yellow}   {ansi.end}"
        self.blue = f"   {ansi.background.blue}   {ansi.end}"
        self.purple = f"   {ansi.background.magenta}   {ansi.end}"
        self.cyan = f"   {ansi.background.cyan}   {ansi.end}"
        self.black = f" {ansi.background.black} {ansi.end}"
        self.white = f" {ansi.background.white} {ansi.end}"
        # display game board
        self.guess_count = 0

        self.prev_guesses = []
        self.prev_pegs = []

        self.color_map = {
            "r": self.red,
            "g": self.green,
            "y": self.yellow,
            "b": self.blue,
            "p": self.purple,
            "c": self.cyan,
            "black": self.black,
            "white": self.white
        }

        # take user input
        self.generate_colors()

        for i in range(10):
            print(i)
            if i == 9:
                print("game over. here is the answer:")
                print(self.chosen_colors)
            elif i < 9:
                self.take_input()
                self.display_board()
                if self.prev_pegs[-1] == ['black']*4:
                    print("you win!")
                    break

    def take_input(self):
        self.guess = input("enter your guess (r g y b p c): ")
        if len(self.guess) != 4:
            print("enter only 4 characters")
            # self.take_input()
        else:
            pegs = []
            self.prev_guesses.append(self.guess)
            for index, c in enumerate(self.guess):
                if self.chosen_colors[index] == c:
                    pegs.append('black')
                elif c in self.chosen_colors:
                    pegs.append('white')
            self.prev_pegs.append(pegs)

    def display_board(self):
        board = ''

        for guesses, pegs in zip(self.prev_guesses, self.prev_pegs):
            for guess in guesses:
                g = self.color_map[guess]
                board += g
            for peg in pegs:
                p = self.color_map[peg]
                board += p

            board += '\n\n'

        print(board)
        # for each color in colors
        # black = color & position
        # white = color only

    def generate_colors(self):
        self.available_colors = ['r', 'g', 'b', 'y', 'p', 'c']
        # self.chosen_colors = []

        random.shuffle(self.available_colors)

        self.chosen_colors = self.available_colors[:4]


g = Game()
