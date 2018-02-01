#!/usr/bin/env python3
import platform
import os
import sys
from random import randint

CLEAR_COMMAND = 'clear' if platform.system() == 'Linux' else 'cls'

SNAKE_CHAR = 'X'
FOOD_CHAR = 'O'
EMPTY_CHAR = ' '

FOOD_LIMIT = 3

POSSIBLE_MOVES = ['N', 'S', 'W', 'E']


class SnakeGame(object):
    def __init__(self):
        self.snake_position = [(5, 5), (5, 6), (5, 7), (5, 8)]
        self.food_position = []
        self.grid_size = 30

    def ask_for_move(self):
        while True:
            move = input('Where to move? {} :'.format(POSSIBLE_MOVES))
            move = move.upper()

            if move not in POSSIBLE_MOVES:
                print('Unrecognized answer! Try it again.')
                continue
            else:
                return move

    def do_move(self, move):
        head = self.snake_position[-1]
        x, y = head
        if move == 'N':
            x -= 1
        elif move == 'S':
            x += 1
        elif move == 'W':
            y -= 1
        elif move == 'E':
            y += 1

        if (x < 0 or y < 0) or (x > self.grid_size - 1 or
                                y > self.grid_size - 1):
            print("It's not possible to break the limits!")
            self.game_over()
        elif (x, y) in self.snake_position:
            print("It's not possible to eat yourself!")
            self.game_over()

        if (x, y) not in self.food_position:
            self.snake_position = list(self.snake_position[1:])
        else:
            self.food_position.remove((x, y))
        self.snake_position.append((x, y))

    def handle_food(self):
        while len(self.food_position) < FOOD_LIMIT:
            self.food_position.append(
                (randint(0, self.grid_size), randint(0, self.grid_size)))

    def print_game(self):
        os.system(CLEAR_COMMAND)
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if (x, y) in self.snake_position:
                    print(SNAKE_CHAR, end='')
                elif (x, y) in self.food_position:
                    print(FOOD_CHAR, end='')
                else:
                    print(EMPTY_CHAR, end='')
            print()

    def game_over(self):
        sys.exit(1)

    def main(self):
        while True:
            self.handle_food()
            self.print_game()
            move = self.ask_for_move()
            self.do_move(move)


def main():
    game = SnakeGame()
    game.main()


if __name__ == '__main__':
    main()
