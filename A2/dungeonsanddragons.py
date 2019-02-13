"""
dungeonsanddragons.py

Collection of Dungeons & Dragons functions.
"""

# Joshua Shin
# A01056181
# Feb 5th 2019

import random
import doctest


def CHARACTER_CLASS():
    """
    Return a dictionary of D&D characters and their corresponding health die.

    RETURN a dictionary of D&D characters and their corresponding health die
    """

    return {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10, "monk": 8, "paladin": 10,
            "ranger": 10, "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6, "blood hunter": 10}


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


def generate_consonant():
    """
    Return a consonant including y.

    RETURN a consonant including y
    """

    return random.choice("bcdfghjklmnpqrstvwxyz")


def generate_vowel():
    """
    Return a vowel including y.

    RETURN a vowel including y
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


def print_class_list():
    """
    Print the list of D&D classes.

    POST-CONDITION print the list of D&D classes
    """

    print("CLASS LIST:")
    for key in CHARACTER_CLASS().keys():
        print(key)


def choose_class():
    """
    Prompt user for class input and return class as string if class is valid.

    RETURN chosen class in string
    """

    print_class_list()
    chosen_class = input("Choose a class: ").strip().lower()

    if chosen_class in CHARACTER_CLASS().keys():
        return chosen_class
    else:
        return choose_class()


def assign_health(chosen_class):
    """
    Calculate random health for given class.

    PARAM class in string
    PRE-CONDITION must be valid class
    RETURN random health for given class
    """

    return roll_die(1, CHARACTER_CLASS()[chosen_class])


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


def combat_initiative(opponent_one, opponent_two):
    """
    Process a single round of combat between two characters.

    PARAM character dictionary object
    PARAM character dictionary object
    PRE-CONDITION both parameters are well-formed dictionaries each containing a correct character
    RETURN name of character who gets initiative
    """

    opponent_one_initiative = roll_die(1, 20)
    opponent_two_initiative = roll_die(1, 20)

    print("Checking initiative...")
    print(opponent_one["Name"], "rolls", opponent_one_initiative)
    print(opponent_two["Name"], "rolls", opponent_two_initiative)

    if opponent_one_initiative == opponent_two_initiative:
        print("Tied. Re-roll...")
        return combat_initiative(opponent_one, opponent_two)

    elif opponent_one_initiative > opponent_two_initiative:
        print(opponent_one["Name"], "gets initiative.")
        return opponent_one, opponent_two

    else:
        print(opponent_two["Name"], "gets initiative.")
        return opponent_two, opponent_one


def combat_attack(attacker, defender):
    """
    Process the attacker's attack to defender's defense.

    PARAM character dictionary object
    PARAM character dictionary object
    PRE-CONDITION both parameters are well-formed dictionaries each containing a correct character
    POST-CONDITION if attack is successful, modify defender's health according to attacker damage
    """

    first_attacker_accuracy = roll_die(1, 20)
    print(attacker["Name"], "rolls accuracy", first_attacker_accuracy)
    print(defender["Name"] + "'s dexterity is", defender["Dexterity"])

    if first_attacker_accuracy > defender["Dexterity"]:
        damage = roll_die(1, CHARACTER_CLASS()[attacker["Class"]])
        defender["HP"] -= damage
        print(attacker["Name"], "hits", defender["Name"], "for", damage, "damage!")

    else:
        print(attacker["Name"], "misses!")


def check_death(character):
    """
    Check if character is alive (HP > 0) and announce death if dead.

    PARAM character dictionary object
    PRE-CONDITION parameter is well-formed dictionaries each containing a correct character
    POST-CONDITION announce death if character is dead
    """

    if character["HP"] <= 0:
        print(character["Name"], "is dead!")


def combat_round(opponent_one, opponent_two):
    """
    Process a single round of combat between two characters.

    PARAM character dictionary object
    PARAM character dictionary object
    PRE-CONDITION both parameters are well-formed dictionaries each containing a correct character
    POST-CONDITION a single round of combat between two characters are processed
    """

    print("START COMBAT ROUND:")

    # Check initiative
    opponent_one, opponent_two = combat_initiative(opponent_one, opponent_two)

    print(opponent_one["Name"], "HP", opponent_one["HP"])
    print(opponent_two["Name"], "HP", opponent_two["HP"])

    # Combat
    combat_attack(opponent_one, opponent_two)
    combat_attack(opponent_two, opponent_one)

    print(opponent_one["Name"], "HP", opponent_one["HP"])
    print(opponent_two["Name"], "HP", opponent_two["HP"])

    # Check death
    check_death(opponent_one)
    check_death(opponent_two)


def print_character(character):
    """
    Print character information.

    PARAM list contains character information
    PRE-CONDITION list contains character information in the format name followed by 6 attributes in list size 2
    POST-CONDITION print character information
    """

    print("--------------------")
    print("CHARACTER INFO:")
    for key, value in character.items():
        if key == "Inventory":
            for item in character["Inventory"]:
                print("Item", item)
        else:
            print(key, value)
    print("--------------------")


def print_inventory(inventory):
    """
    Print items in inventory.

    PARAM list of string
    PRE-CONDITION list contains strings
    POST-CONDITION items in inventory
    """

    print("--------------------")
    print("SUPPLY SHOP:")
    for i in range(len(inventory)):
        print(inventory[i])
    print("--------------------")


def main():
    """
    Demonstrate D&D.
    """

    doctest.testmod()

    # Print supply shop
    sample_inventory = ["Map", "Sword", "Bow", "Potion", "Scroll", "Shield", "Bread", "Water"]
    print_inventory(sample_inventory)

    # Build character 1
    print("CREATE CHARACTER 1:")
    input_name_length = int(input("Enter number of syllables in name: "))
    input_item_amount = int(input("Enter item amount (less than 8): "))
    character_1 = create_character(input_name_length)
    inventory = choose_inventory(sample_inventory, input_item_amount)
    character_1["Inventory"] = inventory
    print_character(character_1)

    # Build character 2
    print("CREATE CHARACTER 2:")
    input_name_length = int(input("Enter number of syllables in name: "))
    input_item_amount = int(input("Enter item amount (less than 8): "))
    character_2 = create_character(input_name_length)
    inventory = choose_inventory(sample_inventory, input_item_amount)
    character_2["Inventory"] = inventory
    print_character(character_2)

    # Demonstrate combat_round()
    combat_round(character_1, character_2)

    # Demonstrate generate_name()
    print("--------------------")
    print("NAME GEN DEMO:")
    for i in range(1, 10):
        print(generate_name(i))

    # Demonstrate roll_die()
    print("--------------------")
    print("DICE ROLL DEMO:")
    print("Sum of 1 roll 1 sided die:", roll_die(1, 1))
    print("Sum of 6 rolls 1 sided die:", roll_die(6, 1))
    print("Sum of 1 roll 6 sided die:", roll_die(1, 6))
    print("Sum of 1 roll 6 sided die:", roll_die(1, 6))
    print("Sum of 6 rolls 6 sided die:", roll_die(6, 6))
    print("Sum of 6 rolls 6 sided die:", roll_die(6, 6))


if __name__ == "__main__":
    main()
