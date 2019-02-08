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
    class_list = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin",
                  "ranger", "rogue", "sorcerer", "warlock", "wizard", "blood hunter"]
    chosen_class = input(str(class_list) + "\nPick a class: ").strip().lower()
    if chosen_class in class_list:
        return chosen_class
    else:
        return choose_class()


def assign_health(chosen_class):
    class_hp_roll = {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10, "monk": 8, "paladin": 10,
                     "ranger": 10, "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6, "blood hunter": 10}
    return roll_die(1, class_hp_roll[chosen_class])


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
        player_class = choose_class()

        # Name & Class & HP
        character = {"Name": generate_name(name_length), "Class": player_class, "HP": assign_health(player_class)}

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
    for key, value in character.items():
        print(key, value)
    #
    # print("Name:", character[0])
    # for i in range(1, len(character)):
    #     if len(character[i]) == 2:
    #         print(character[i][0] + ":", character[i][1])
    #     else:
    #         print("Item", str(i - 6) + ":", character[i])


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
    Return a consonant.

    RETURN a consonant
    """

    return random.choice("bcdfghjklmnpqrstvwxyz")


def generate_vowel():
    """
    Return a vowel.

    RETURN a vowel
    """

    return random.choice("aeiouy")


def generate_syllable():
    """
    Return a syllable made of a consonant and vowel.

    RETURN a syllable made of a consonant and vowel
    """

    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """
    Return a random name of length syllables * 2 by generating syllables made of a consonant and vowel.

    PARAM positive integer
    PRE-CONDITION integer must be positive
    RETURN a random name of length syllables * 2
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

    print_character(create_character(int(input("Number of syllables in name: "))))


if __name__ == "__main__":
    main()
