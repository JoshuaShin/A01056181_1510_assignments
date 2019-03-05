"""
save.py

Handles game data saving.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest
import json


def load_character():
    with open('character.json') as data_file:
        return json.load(data_file)


def save_character(character):
    with open('character.json', 'w') as outfile:
        json.dump(character, outfile, sort_keys=True, indent=4)


def reset_character():
    with open('character.json', 'w') as outfile:
        json.dump({
            "coordinate_x": 2,
            "coordinate_y": 2,
            "hp": 10
        }, outfile, sort_keys=True, indent=4)


def load_monster():
    with open('monster.json') as data_file:
        return json.load(data_file)


def save_monster(monster):
    with open('monster.json', 'w') as outfile:
        json.dump(monster, outfile, sort_keys=True, indent=4)


def reset_monster():
    with open('monster.json', 'w') as outfile:
        json.dump({
            "hp": 5
        }, outfile, sort_keys=True, indent=4)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
