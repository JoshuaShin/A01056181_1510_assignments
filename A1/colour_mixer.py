"""
colour_mixer.py

Print secondary colour from two primary colour inputs.
"""

# Joshua Shin
# A01056181
# Jan 24 2019

import doctest


def is_primary_colour(colour_chosen):
    """
    Take a string as input and return True if one of three primary colours.

    PARAM string
    PRE-CONDITION colour_chosen is a string
    POST-CONDITION find out if colour_chosen is primary colour or not
    RETURN True if primary colour and False if else

    >>> is_primary_colour("red")
    True
    >>> is_primary_colour("yellow")
    True
    >>> is_primary_colour("blue")
    True
    >>> is_primary_colour("white")
    False
    """

    primary_colour = ["red", "yellow", "blue"]

    if colour_chosen in primary_colour:
        return True

    else:
        return False


def get_secondary_colour(color_1, color_2):
    """
    Take two strings of two unique primary colours as input and return the corresponding secondary colour.

    PARAM unique primary colour one
    PARAM unique primary colour two
    PRE-CONDITION string must be unique primary colour
    PRE-CONDITION string must be unique primary colour
    POST-CONDITION find the corresponding secondary colour
    RETURN the corresponding secondary colour

    >>> get_secondary_colour("red", "blue")
    'purple'
    >>> get_secondary_colour("yellow", "red")
    'orange'
    >>> get_secondary_colour("blue", "yellow")
    'green'
    """

    colours_chosen = [color_1, color_2]

    if "red" in colours_chosen and "blue" in colours_chosen:
        return "purple"

    elif "red" in colours_chosen and "yellow" in colours_chosen:
        return "orange"

    else:
        return "green"


def colour_mixer():
    """
    Print secondary colour from two primary colour inputs.
    """

    colour_chosen_1 = input("First primary colour: ").strip().lower()
    if not is_primary_colour(colour_chosen_1):
        print("Please input a primary colour!")
        colour_mixer()
        return

    colour_chosen_2 = input("Second primary colour: ").strip().lower()
    if not is_primary_colour(colour_chosen_2):
        print("Please input a primary colour!")
        colour_mixer()
        return

    if colour_chosen_1 == colour_chosen_2:
        print("First and second colours must be different!")
        colour_mixer()
        return

    print("Secondary colour:", get_secondary_colour(colour_chosen_1, colour_chosen_2))


def main():
    """
    Drive the program.
    """

    doctest.testmod()
    colour_mixer()


if __name__ == "__main__":
    main()
