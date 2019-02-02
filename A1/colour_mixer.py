"""
colour_mixer.py

Print secondary color from two primary color inputs.
"""

# Joshua Shin
# A01056181
# Jan 24 2019

import doctest


def color_combinations(colors_chosen):
    """
    Take a string list of two unique primary colors as input and return the corresponding secondary color.

    PARAM list of strings length two holding two unique primary colors
    PRE-CONDITION list of strings must hold two unique primary colors
    POST-CONDITION find the corresponding secondary color
    RETURN the corresponding secondary color

    >>> color_combinations(["red", "blue"])
    'purple'
    >>> color_combinations(["yellow", "red"])
    'orange'
    >>> color_combinations(["blue", "yellow"])
    'green'
    """

    if "red" in colors_chosen and "blue" in colors_chosen:
        return "purple"

    elif "red" in colors_chosen and "yellow" in colors_chosen:
        return "orange"

    else:  # "yellow" in colors_chosen and "blue" in colors_chosen
        return "green"


def color_mixer():
    """
    Print secondary color from two primary color inputs.
    """

    colors_chosen = ["color_1", "color_2"]
    primary_color = ["red", "yellow", "blue"]

    colors_chosen[0] = input("First primary color: ").strip().lower()
    if colors_chosen[0] not in primary_color:
        print("Please input a primary color!")
        color_mixer()
        return

    colors_chosen[1] = input("Second primary color: ").strip().lower()
    if colors_chosen[1] not in primary_color:
        print("Please input a primary color!")
        color_mixer()
        return

    if colors_chosen[0] == colors_chosen[1]:
        print("First and second colors must be different!")
        color_mixer()

    print("Secondary color:", color_combinations(colors_chosen))


def main():
    """
    Drive the program.
    """

    doctest.testmod()
    color_mixer()


if __name__ == "__main__":
    main()
