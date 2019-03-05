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
import combat


def print_introduction():
    """
    Print introduction.

    POST-CONDITION introduction is printed
    """

    print("""
    Welcome to the game.
    This is very exciting, I know.
    Valid commands: n, w, s, e, quit, restart
    """)


def game_over():
    """
    End the game.

    POST-CONDITION game over message is printed
    """

    print("GAME OVER")
    character.reset()


def restart_game():
    """
    Restart the game.

    POST-CONDITION character is reset and restart message is printed
    """

    print("RESTART GAME")
    character.reset()
    play_game()


def quit_game():
    """
    Quit and save the game.

    POST-CONDITION game saved message is printed
    """

    print("GAME SAVED")


def play_game():
    """
    Process the game play loop.

    POST-CONDITION make appropriate changes to character and monster according to events
    """
    print_introduction()
    map.print_map(character.get_coordinates())
    while True:
        player_input = input("Input: ")
        # Quit
        if player_input.strip().lower() == 'quit':
            quit_game()
            break
        # Restart
        if player_input.strip().lower() == 'restart':
            restart_game()
            break
        # Move
        if not character.move(player_input.strip().lower()):
            print("Invalid.")
            continue
        map.print_map(character.get_coordinates())
        # Heal
        if character.get_hp() < character.MAX_HP():
            character.set_hp(1)
            print("HEALED 1 HP", "\nYOUR HP:", character.get_hp())
        # Combat
        if random.random() < 1:
            if not combat.combat():
                game_over()
                break


def main():
    doctest.testmod()
    play_game()


if __name__ == "__main__":
    main()
