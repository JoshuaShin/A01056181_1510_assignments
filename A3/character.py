"""
character.py

Character and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest
import map


coordinates = (1, 1)
hp = 10


def MAX_HP():
    """
    Max hp constant.

    RETURN character coordinates x and y in integer
    """

    return 10


def get_hp():
    """
    Return character's current hp.

    RETURN character's current hp
    """

    return hp


def set_hp(change_amount):
    """
    Change character's current hp by change amount specified.

    PARAM positive or negative integer
    PRE-CONDITION change amount is a positive or negative integer
    POST CONDITION change character hp by the change amount
    """

    global hp
    hp += change_amount
    if hp > MAX_HP():
        hp = MAX_HP()
    elif hp < 0:
        hp = 0


def get_coordinates():
    """
    Return character coordinates.

    RETURN character coordinates x and y in integer
    """

    return coordinates


def move(direction):
    """
    Move character in the given map North, East, South, or West.

    PARAM string containing cardinal direction
    PRE-CONDITION string containing single cardinal direction - 'north', 'west', 'south', 'east'
    POST CONDITION move character coordinate North, East, South, or West
    RETURN True if character is moved
    """

    global coordinates
    current_x, current_y = coordinates

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
        coordinates = (destination_x, destination_y)
        return True


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
