"""
save.py

Handles game data saving.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest
import json


def read_data():
    """
    Read data from character.json.

    RETURN dictionary of character data
    """

    with open('character.json') as file_object:
        return json.load(file_object)


def write_data(dictionary):
    """
    Save data to character.json.

    POST-CONDITION character data is saved to character.json
    """

    with open('character.json', 'w') as file_object:
        json.dump(dictionary, file_object, sort_keys=True, indent=4)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
