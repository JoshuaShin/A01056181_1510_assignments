"""
sud.py

Single User Dungeon game.
Type commands to interact with the environment.
Commands: north, east, south, weest, fight, flee.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import random
import doctest
import map
import character
import monster


def roll_die(number_of_rolls, number_of_sides):
    """
    Simulate rolling a die of the specified size the specified number of times.

    PARAM positive integer
    PARAM positive integer
    PRE-CONDITION integer must be positive
    PRE-CONDITION integer must be positive
    RETURN the sum of the die of the specified size rolled the specified number of times

    >>> random.seed(0)
    >>> roll_die(0, 0)
    0
    >>> roll_die(1, 1)
    1
    >>> roll_die(6, 1)
    6
    >>> roll_die(1, 6)
    4
    >>> random.seed()
    """

    if number_of_rolls < 1 or number_of_sides < 1:
        return 0
    else:
        return random.randrange(1, number_of_sides + 1, 1) + roll_die(number_of_rolls - 1, number_of_sides)


def combat():
    """
    Process the combat loop between character and monster.

    POST-CONDITION character and monster takes damage until one dies
    RETURN True if monster is slain
    RETURN False if character is slain
    """

    monster.reset()
    print("--- COMBAT STARTS ---")

    while True:
        print("YOUR HP:", character.get_hp())
        print("MONSTER HP:", monster.get_hp())

        user_input = input("--- PRESS ANY KEY TO CONTINUE ---")

        character_roll = roll_die(1, 6)
        print("CHARACTER ROLL:", character_roll, "ATTACK")
        if not monster.set_hp(-character_roll):
            print("MONSTER HP: 0", "\nMONSTER SLAIN", "\n--- COMBAT ENDS ---")
            return True

        monster_roll = roll_die(1, 6)
        print("MONSTER ROLL:", monster_roll, "ATTACK")
        if not character.set_hp(-monster_roll):
            print("YOUR HP: 0", "\nYOU DIED")
            return False


def game_over():
    """
    End the game.

    POST-CONDITION game over message is printed
    """

    print("GAME OVER")


def quit_game():
    """
    Quit and save the game.

    POST-CONDITION game is saved to JSON file
    POST-CONDITION game saved message is printed
    """

    # TODO: save game TO JSON file
    print("GAME SAVED")


def play_game():
    """
    Process the game play loop.

    POST-CONDITION make appropriate changes to character and monster according to events
    """

    map.print_map(character.get_coordinates())
    while True:
        player_input = input("Input: ")
        # Quit
        if player_input.strip().lower() == 'quit':
            quit_game()
            break
        # Move
        if not character.move(player_input):
            print("Invalid.")
            continue
        map.print_map(character.get_coordinates())
        # Heal
        if character.get_hp() < character.MAX_HP():
            character.set_hp(1)
            print("HEALED 1 HP", "\nYOUR HP:", character.get_hp())
        # Combat
        if random.random() < 1:
            if not combat():
                game_over()
                break


def main():
    doctest.testmod()
    play_game()


if __name__ == "__main__":
    main()
