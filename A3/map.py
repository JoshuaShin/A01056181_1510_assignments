"""
map.py

Map and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import random
import doctest


def get_map():
    """
    Return the initial 2D array of strings representing the map of the dungeon.

    RETURN 2D array of strings representing the map of the dungeon
    """

    return [['w', 'w', 'w', 'w', 'w'],
            ['w', 'o', 'o', 'o', 'w'],
            ['w', 'o', 'o', 'o', 'w'],
            ['w', 'o', 'o', 'o', 'w'],
            ['w', 'w', 'w', 'w', 'w']]


def can_traverse(x, y):
    """
    Return True if the tile can be traversed by player.

    PARAM zero or positive integer representing x coordinate of tile
    PARAM zero or positive integer representing y coordinate of tile
    RETURN True if the tile can be traversed by player

    >>> can_traverse(0, 0)
    False
    >>> can_traverse(1, 1)
    True
    """

    impassable = "w"

    if get_map()[x][y][0] in impassable:
        return False
    else:
        return True


def remove_player(map):
    """
    Remove player ('p') from the given map.

    PARAM 2D array of strings representing the map of the dungeon and its current state
    POST CONDITION remove player ('p') from the given map
    """

    for y in range(len(map)):
        for x in range(len(map[y])):
            if 'p' in map[y][x]:
                map[y][x] = map[y][x].replace("P", "")
                return


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
