"""
save.py

Handles game data saving.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest
import json
import character


def load_game():
    """
    Load character data from character.json.

    POST-CONDITION character data is loaded and character is updated
    """

    try:
        with open('character.json') as file_object:
            char = json.load(file_object)
            character.set_hp(char['hp'])
            character.set_coordinates(char['column'], char['row'])

    except FileNotFoundError:
        char = {"hp": 10, "column": 29, "row": 16}
        character.set_hp(char['hp'])
        character.set_coordinates(char['column'], char['row'])


def save_game():
    """
    Save character data to character.json.

    POST-CONDITION character data is saved to character.json
    """

    character_dictionary = {'hp': character.get_hp(),
                            'column': character.get_coordinates()[0],
                            'row': character.get_coordinates()[1]}

    with open('character.json', 'w') as file_object:
        json.dump(character_dictionary, file_object, sort_keys=True, indent=4)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
