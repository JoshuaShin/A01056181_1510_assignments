"""
map.py

Map and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import random
import doctest
import character


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


def print_map():
    """
    Print the map.

    POST CONDITION map and player location is printed
    """

    print([['w', 'w', 'w', 'w', 'w'],
           ['w', 'o', 'o', 'o', 'w'],
           ['w', 'o', 'o', 'o', 'w'],
           ['w', 'o', 'o', 'o', 'w'],
           ['w', 'w', 'w', 'w', 'w']])


def is_impassable(x, y):
    """
    Return True if the tile can be traversed by player.

    PARAM zero or positive integer representing x coordinate of tile
    PARAM zero or positive integer representing y coordinate of tile
    RETURN True if the tile can be traversed by player

    >>> is_impassable(0, 0)
    False
    >>> is_impassable(1, 1)
    True
    """

    impassable = "w"

    if get_map()[x][y][0] in impassable:
        return False
    else:
        return True


# def remove_player(current_map):
#     """
#     Remove player ('p') from the given map.
#
#     PARAM 2D array of strings representing the map of the dungeon and its current state
#     POST CONDITION remove player ('p') from the given map
#     """
#
#     x, y = get_player_coordinate(current_map)
#     current_map[y][x] = current_map[y][x].replace('p', '')
#
#
# def get_player_coordinate(current_map):
#     """
#     Return the x, y coordinate of player ('p') in the given map.
#
#     PARAM 2D array of strings representing the map of the dungeon and its current state
#     RETURN the x, y coordinate of player ('p') in the given map
#
#     >>> get_player_coordinate([['o', 'o'], ['o', 'op']])
#     (1, 1)
#     """
#
#     for y in range(len(current_map)):
#         for x in range(len(current_map[y])):
#             if 'p' in current_map[y][x]:
#                 return x, y


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
