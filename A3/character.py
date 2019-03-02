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


def move_player(direction):
    """
    Move player in the given map North, East, South, or West.

    PARAM 2D array of strings representing the map of the dungeon and its current state
    PARAM string containing cardinal direction
    PRE-CONDITION 2D array of strings representing the map of the dungeon and its current state
    PRE-CONDITION string containing single cardinal direction - 'north', 'west', 'south', 'east'
    POST CONDITION move player ('p') in the given map North, East, South, or West
    """

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
    else:  # direction == 'east':
        destination_x = current_x + 1
        destination_y = current_y

    if map.is_impassable(destination_x, destination_y):
        return False
    else:
        global character_coordinate
        character_coordinate = (destination_x, destination_y)
        return True


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
