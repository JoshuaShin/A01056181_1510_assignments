"""
lab_04.py

Collection of Dungeons & Dragons functions.
"""

# Joshua Shin
# A01056181
# Feb 5th 2019

import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Simulate rolling a die of the specified size the specified number of times.

    PARAM positive integer
    PARAM positive integer
    PRE-CONDITION integer must be positive
    PRE-CONDITION integer must be positive
    RETURN the sum of the die of the specified size rolled the specified number of times
    """

    if number_of_rolls < 1 or number_of_sides < 1:
        return 0
    else:
        return random.randrange(1, number_of_sides + 1, 1) + roll_die(number_of_rolls - 1, number_of_sides)


def choose_inventory(inventory, selection):
    """
    Choose selection amount from the list inventory randomly and return sorted selection.

    PARAM none empty list larger than selection
    PARAM positive integer
    PRE-CONDITION list must not be empty and larger than selection
    PRE-CONDITION integer must be positive
    RETURN sorted random selections from inventory amounting to the parameter selection
    """

    if len(inventory) == 0 and selection == 0:
        return []
    elif selection < 0:
        print("WARNING: Selection cannot be negative!")
        return None
    elif selection > len(inventory):
        print("WARNING: Selection cannot be larger than inventory size!")
        return None
    elif selection == len(inventory):
        return inventory[:]
    else:
        return sorted(random.sample(inventory, selection))


def create_name(length):
    """
    Choose random characters from a-z to create a name of given length.

    PARAM positive integer
    PRE-CONDITION integer must be positive
    RETURN random name of given length
    """

    if type(length) != int or length < 1:
        return None
    else:
        return "".join(random.sample(list("abcdefghijklmnopqrstuvwxyz"), length)).title()


def choose_class():
    class_list = ["barbarian", "bard", "cleric", "druid", "fight", "monk", "paladin",
                  "ranger", "rogue", "sorcerer", "warlock", "wizard", "blood hunter"]
    chosen_class = input(str(class_list) + "Pick a class from from the list: ").strip().lower()
    if chosen_class in class_list:
        return chosen_class
    else:
        choose_class()


def create_character(name_length):
    """
    Create a Dungeons and Dragons character.

    PARAM positive integer
    PRE-CONDITION integer must be positive
    RETURN random name of given length
    """

    if type(name_length) != int or name_length < 1:
        print("WARNING: name length must be positive integer!")
        return None
    else:
        # Name
        character = {"Name": create_name(name_length)}

        # Class
        character["Class"] = choose_class()

        # Attributes
        attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        for i in range(len(attributes)):
            character[attributes[i]] = roll_die(3, 6)

        # XP
        character["XP"] = 0

        # Inventory
        character["Inventory"] = []





        return character


def print_character(character):
    """
    Print character information.

    PARAM list contains character information
    PRE-CONDITION list contains character information in the format name followed by 6 attributes in list size 2
    POST-CONDITION print character information
    """

    print("--------------------")
    print("Name:", character[0])
    for i in range(1, len(character)):
        if len(character[i]) == 2:
            print(character[i][0] + ":", character[i][1])
        else:
            print("Item", str(i - 6) + ":", character[i])


def print_inventory(inventory):
    """
    Print items in inventory.

    PARAM list of string
    PRE-CONDITION list contains strings
    POST-CONDITION items in inventory
    """

    print("Supply Shop:")
    for i in range(len(inventory)):
        print(inventory[i])
    print("--------------------")


def generate_consonant():
    """

    """
    return random.choice("bcdfghjklmnpqrstvwxyz")


def generate_vowel():
    """

    """
    return random.choice("aeiouy")


def generate_syllable():
    """

    """
    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """

    """
    name = ""
    for i in range(syllables):
        name += generate_syllable()
    return name.title()


def main():
    """
    Drive the program.
    """

    doctest.testmod()

    print(generate_name(5))


if __name__ == "__main__":
    main()
