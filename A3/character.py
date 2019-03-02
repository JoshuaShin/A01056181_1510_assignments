"""
character.py

Character and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import random
import doctest
import map


character_coordinate = (1, 1)


def get_character_coordinate():
    """
    Get character coordinates.

    RETURN character coordinates x and y in integer
    """

    return character_coordinate


def move_character(direction):
    """
    Move character in the given map North, East, South, or West.

    PARAM string containing cardinal direction
    PRE-CONDITION string containing single cardinal direction - 'north', 'west', 'south', 'east'
    POST CONDITION move character coordinate North, East, South, or West
    RETURN True if character is moved
    """

    global character_coordinate
    current_x, current_y = character_coordinate

    if direction == 'north':
        destination_x = current_x
        destination_y = current_y - 1
    elif direction == 'west':
        destination_x = current_x - 1
        destination_y = current_y
    elif direction == 'south':
        destination_x = current_x
        destination_y = current_y + 1
    elif direction == 'east':
        destination_x = current_x + 1
        destination_y = current_y
    else:
        return False

    if map.is_impassable(destination_x, destination_y):
        return False
    else:
        character_coordinate = (destination_x, destination_y)
        return True


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
