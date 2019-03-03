"""
sud.py

Single User Dungeon game.
Type commands to interact with the environment.
Commands: north, east, south, weest, fight, flee.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import random
import doctest
import map
import character


def roll_die(number_of_rolls, number_of_sides):
    """
    Simulate rolling a die of the specified size the specified number of times.

    PARAM positive integer
    PARAM positive integer
    PRE-CONDITION integer must be positive
    PRE-CONDITION integer must be positive
    RETURN the sum of the die of the specified size rolled the specified number of times

    >>> random.seed(0)
    >>> roll_die(0, 0)
    0
    >>> roll_die(1, 1)
    1
    >>> roll_die(6, 1)
    6
    >>> roll_die(1, 6)
    4
    >>> random.seed()
    """

    if number_of_rolls < 1 or number_of_sides < 1:
        return 0
    else:
        return random.randrange(1, number_of_sides + 1, 1) + roll_die(number_of_rolls - 1, number_of_sides)


def print_map():
    """
    Print the map.

    POST CONDITION map and player location is printed
    """

    game_map = map.get_map()
    char_x, char_y = character.get_character_coordinate()
    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            if char_x == x and char_y == y:
                print('O', end=' ')
            else:
                print(game_map[y][x], end=' ')
        print('')


def play_game():
    while True:
        if not character.move_character(input("Move: ")):
            print("Cannot go there.")
        print_map()
        character.set_character_health(1)


def main():
    doctest.testmod()
    play_game()


if __name__ == "__main__":
    main()
