"""
character.py

Character and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest
import map
import save


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

    return save.load_character()["hp"]


def set_hp(change_amount):
    """
    Change character's current hp by change amount specified.

    PARAM positive or negative integer
    PRE-CONDITION change amount is a positive or negative integer
    POST-CONDITION change character hp by the change amount
    RETURN True if hp is not 0
    RETURN False if hp is 0
    """

    hp = get_hp()
    hp += change_amount
    if hp > MAX_HP():
        hp = MAX_HP()
    elif hp <= 0:
        hp = 0
        save.save_character({"hp": hp, "coordinate_x": get_coordinates()[0], "coordinate_y": get_coordinates()[1]})
        return False
    save.save_character({"hp": hp, "coordinate_x": get_coordinates()[0], "coordinate_y": get_coordinates()[1]})
    return True


def get_coordinates():
    """
    Return character coordinates.

    RETURN character coordinates x and y in integer
    """

    character = save.load_character()
    return character["coordinate_x"], character["coordinate_y"]


def move(direction):
    """
    Move character in the given map North, East, South, or West.

    PARAM string containing cardinal direction
    PRE-CONDITION string containing single cardinal direction - 'north', 'west', 'south', 'east'
    POST-CONDITION move character coordinate North, East, South, or West
    RETURN True if character is moved
    """

    # TODO: this function is too long (20+ lines)
    current_x, current_y = get_coordinates()

    if direction == 'north' or direction == 'n':
        destination_x = current_x
        destination_y = current_y - 1
    elif direction == 'west' or direction == 'w':
        destination_x = current_x - 1
        destination_y = current_y
    elif direction == 'south' or direction == 's':
        destination_x = current_x
        destination_y = current_y + 1
    elif direction == 'east' or direction == 'e':
        destination_x = current_x + 1
        destination_y = current_y
    else:
        return False

    if map.is_impassable(destination_x, destination_y):
        return False
    else:
        save.save_character({"hp": get_hp(), "coordinate_x": destination_x, "coordinate_y": destination_y})
        return True


def reset():
    """
    Reset character.

    POST-CONDITION Set character hp to max hp
    POST-CONDITION Set character coordinate to default
    """

    save.reset_character()


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
