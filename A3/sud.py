"""
sud.py

Single User Dungeon game.
Type commands to interact with the environment.
Commands: north, east, south, weest, restart, quit.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import random
import doctest
import map
import character
import combat
import save


def print_introduction():
    """
    Print introduction.

    POST-CONDITION introduction is printed
    """

    print("""
    You are stuck in an incredibly dull dungeon with no exits. ☹
    You are filled to the brim with excitement at the prospect of exploring all 9 identical tiles.  ♪~ ᕕ(ᐛ)ᕗ
    Valid commands: n, w, s, e, quit, restart.
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
    save_game()
    play_game()


def quit_game():
    """
    Quit and save the game.

    POST-CONDITION game is saved
    POST-CONDITION game saved message is printed
    POST-CONDITION program terminates
    """

    save_game()
    print("GAME SAVED")
    quit()


def save_game():
    """
    Save character data to character.json.

    POST-CONDITION character data is saved
    """

    save.write_data({'hp': character.get_hp(),
                     'x': character.get_coordinates()[0],
                     'y': character.get_coordinates()[1]})


def load_game():
    """
    Load character data from character.json.

    POST-CONDITION character data is loaded and character is updated
    """

    char = save.read_data()
    character.set_hp(char['hp'])
    character.set_coordinates(char['x'], char['y'])
    print("YOUR HP:", character.get_hp())
    print("YOUR COORDINATES:", character.get_coordinates())


def play_game():
    """
    Process the game play loop.

    POST-CONDITION make appropriate changes to character and monster according to events
    """

    print_introduction()
    load_game()
    map.print_map(character.get_coordinates())
    while True:
        player_input = input(">>> ")
        # Quit
        if player_input.strip().lower() == 'quit':
            quit_game()
        # Restart
        if player_input.strip().lower() == 'restart':
            restart_game()
            break
        # Move
        if not character.move(player_input.strip().lower()):
            print("INVALID INPUT")
            continue
        print("You find absolutely nothing of interest in this tile.")
        map.print_map(character.get_coordinates())
        # Heal
        if character.get_hp() < character.MAX_HP():
            character.modify_hp(1)
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
