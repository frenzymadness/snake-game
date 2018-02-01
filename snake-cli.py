#!/usr/bin/env python3

snake_position = [(5, 5), (5, 6), (5, 7), (5, 8)]
food_position = [(2, 2), (10, 10)]
grid_size = 30

snake_char = 'X'
food_char = 'O'
empty_char = ' '


def print_game():
    for x in range(grid_size):
        for y in range(grid_size):
            if (x, y) in snake_position:
                print(snake_char, end='')
            elif (x, y) in food_position:
                print(food_char, end='')
            else:
                print(empty_char, end='')
        print()


def main():
    print_game()


if __name__ == '__main__':
    main()
