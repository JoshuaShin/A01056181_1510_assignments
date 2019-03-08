"""
map.py

Map and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest


game_map = []


def get_map():
    """
    Return the initial 2D array of strings representing the map of the dungeon.

    RETURN 2D array of strings representing the map of the dungeon
    """

    if game_map:
        return game_map
    else:
        with open("map.txt") as file_object:
            for line in file_object.readlines():
                game_map.append(list(line))
        return game_map


def print_map(character_coordinate):
    """
    Print the map and mark the player location.

    PARAM tuple containing x and y coordinate of player
    PRE-CONDITION player coordinate is within the map boundaries
    POST-CONDITION map and player location is printed
    """

    char_x, char_y = character_coordinate
    for y in range(len(get_map())):
        for x in range(len(get_map()[y])):
            if char_x == x and char_y == y:
                print('🚀', end=' ')
            else:
                print(get_map()[y][x], end=' ')
    print()


def is_impassable(x, y):
    """
    Return True if the tile can be traversed by player.

    PARAM zero or positive integer representing x coordinate of tile
    PARAM zero or positive integer representing y coordinate of tile
    RETURN True if the tile can be traversed by player

    >>> is_impassable(0, 5)
    True
    >>> is_impassable(1, 5)
    False
    """

    impassable = "-|"

    if get_map()[y][x] in impassable:
        return True
    else:
        return False


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
