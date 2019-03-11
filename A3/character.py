"""
character.py

Character and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest
import map


hp = 10
coordinates = (29, 16)


def MAX_HP():
    """
    Max hp constant.

    RETURN character coordinates x and y in integer

    >>> MAX_HP()
    10
    """

    return 10


def reset():
    """
    Reset character.

    POST-CONDITION Set character hp to max hp
    POST-CONDITION Set character coordinate to default
    """

    global hp
    global coordinates
    hp = 10
    coordinates = (29, 16)


def get_hp():
    """
    Return character's current hp.

    RETURN character's current hp

    >>> get_hp()
    10
    """

    return hp


def set_hp(new_hp):
    """
    Set character's current hp.

    PARAM positive integer
    PRE-CONDITION integer is within valid character health
    POST-CONDITION character's current hp
    """

    global hp
    hp = new_hp


def modify_hp(change_amount):
    """
    Change character's current hp by change amount specified.

    PARAM positive or negative integer
    PRE-CONDITION change amount is a positive or negative integer
    POST-CONDITION change character hp by the change amount
    RETURN True if hp is not 0
    RETURN False if hp is 0

    >>> modify_hp(10)
    True
    >>> modify_hp(-10)
    False
    """

    global hp
    hp += change_amount
    if hp > MAX_HP():
        hp = MAX_HP()
    elif hp <= 0:
        hp = 0
        return False
    return True


def get_coordinates():
    """
    Return character coordinates.

    RETURN character coordinates x and y in integer

    >>> get_coordinates()
    (29, 16)
    """

    return coordinates


def set_coordinates(column, row):
    """
    Set character coordinates to column and row.

    PARAM is positive integer
    PARAM is positive integer
    PRE-CONDITION integer is within the map width
    PRE-CONDITION integer is within the map height
    POST-CONDITION set character coordinates
    """

    global coordinates
    coordinates = (column, row)


def move(direction):
    """
    Move character in the given map North, East, South, or West.

    PARAM string containing cardinal direction
    PRE-CONDITION string containing single cardinal direction - 'north', 'west', 'south', 'east'
    POST-CONDITION move character coordinate North, East, South, or West
    """

    global coordinates
    current_column, current_row = coordinates
    destination_column, destination_row = coordinates
    if direction == 'north' or direction == 'n':
        destination_column = current_column
        destination_row = current_row - 1
    elif direction == 'west' or direction == 'w':
        destination_column = current_column - 1
        destination_row = current_row
    elif direction == 'south' or direction == 's':
        destination_column = current_column
        destination_row = current_row + 1
    elif direction == 'east' or direction == 'e':
        destination_column = current_column + 1
        destination_row = current_row
    else:
        print("INVALID COMMAND")
    if map.is_impassable(destination_column, destination_row):
        print("OUT OF BOUND")
    else:
        coordinates = (destination_column, destination_row)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
