#!/usr/bin/env python3
import platform
import os
import sys
from random import randint

clear_command = 'clear' if platform.system() == 'Linux' else 'cls'

snake_char = 'X'
food_char = 'O'
empty_char = ' '

food_limit = 3

possible_moves = ['N', 'S', 'W', 'E']


def ask_for_move():
    while True:
        move = input('Where to move? {} :'.format(possible_moves))
        move = move.upper()

        if move not in possible_moves:
            print('Unrecognized answer! Try it again.')
            continue
        else:
            return move


def do_move(move, snake_position, food_position, grid_size):
    head = snake_position[-1]
    x, y = head
    if move == 'N':
        x -= 1
    elif move == 'S':
        x += 1
    elif move == 'W':
        y -= 1
    elif move == 'E':
        y += 1

    if (x < 0 or y < 0) or (x > grid_size - 1 or y > grid_size - 1):
        print("It's not possible to break the limits!")
        game_over()
    elif (x, y) in snake_position:
        print("It's not possible to eat yourself!")
        game_over()

    if (x, y) not in food_position:
        snake_position = list(snake_position[1:])
    else:
        food_position.remove((x, y))
    snake_position.append((x, y))

    return snake_position


def handle_food(grid_size, food_position):
    while len(food_position) < food_limit:
        food_position.append((randint(0, grid_size), randint(0, grid_size)))

    return food_position


def print_game(grid_size, snake_position, food_position):
    os.system(clear_command)
    for x in range(grid_size):
        for y in range(grid_size):
            if (x, y) in snake_position:
                print(snake_char, end='')
            elif (x, y) in food_position:
                print(food_char, end='')
            else:
                print(empty_char, end='')
        print()


def game_over():
    sys.exit(1)


def main():
    snake_position = [(5, 5), (5, 6), (5, 7), (5, 8)]
    food_position = []
    grid_size = 30

    while True:
        food_position = handle_food(grid_size, food_position)
        print_game(grid_size, snake_position, food_position)
        move = ask_for_move()
        snake_position = do_move(move, snake_position, food_position,
                                 grid_size)


if __name__ == '__main__':
    main()
