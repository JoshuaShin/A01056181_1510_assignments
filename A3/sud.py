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
          ____ _____      _______
         / __//_  _/ ,/| /____   )
        ( (    / / ,/  |   __ ) /
         \ \  / /,/ _  |  / // /
      ____) )/ //,-' `.| / / \ \\
     /_____//_///     ||/_/   \ \_ ______ ______     ______  __   __
                               \_//_  __//___   )   / ____/ / /  / /
                                   / /    __ ) /   / /_    / / /'/'
                                  / /    / // /   / ___|  / //'/'
                                 / /    / / \ \  / /____ / / \ \\
                                /_/    /_/   \ \/______//_/   \_\\
                                              \/    

    ♪♫♬ PLEASE PLAY ON YOUTUBE STAR TREK: NEXT GENERATION THEME ♪♫♬



    Space... the final frontier...!\n
    
    These are the voyages of the starship Enterprise.\n
    
    Its continuing mission:\n
    
    To explore strange new worlds,\n 
    
    To seek out new life and new civilizations,\n
    
    To boldly go where no one has gone before...!\n
    


    YOU COMMAND:
    
                                                  _______----_______
                                       ___---~~~~~.. ... .... ... ..~~~~~---___
                                 _ ==============================================
     __________________________ - .. ..   _--~~~~~-------____-------~~~~~
    (______________________][__)____     -
       /       /______---~~~.. .. ..~~-_~
      <_______________________________-
          ~~~~~~~-----__           __-
                        ~~~~~~~~~~~


                    _____.-----._____
       ___----~~~~~~. ... ..... ... .~~~~~~----___
    =================================================
       ~~~-----......._____________.......-----~~~
        (____)          \   |   /          (____)
          ||           _/   |   \_           ||
           \\\_______--~  //~~~\\\  ~--_______//
            `~~~~---__   \\\___//   __---~~~~'
                      ~~-_______-~~

               U S S   E N T E R P R I S E
    
    
    VALID COMMANDS: n, w, s, e, quit, restart.
    """)


def game_over():
    """
    End the game.

    POST-CONDITION game over message is printed
    """
    print("...THIS IS THE BRIDGE... ALL HANDS ABANDON SHIP... I REPEAT... ALL HANDS.. ABANDO... ... ...")
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
        map.print_map(character.get_coordinates())
        # Heal
        if character.get_hp() < character.MAX_HP():
            character.modify_hp(1)
            print("STRUCTURAL INTEGRITY +1 POINT", "\nYOUR STRUCTURAL INTEGRITY:", character.get_hp())
        # Combat
        if random.random() < 0.1:
            if not combat.combat():
                game_over()
                break


def main():
    doctest.testmod()
    play_game()


if __name__ == "__main__":
    main()
