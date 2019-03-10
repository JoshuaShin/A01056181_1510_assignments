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
    POST-CONDITION program terminates
    """
    print("...THIS IS THE BRIDGE... ALL HANDS ABANDON SHIP... I REPEAT... ALL HANDS.. ABANDO... ... ...")
    print("GAME OVER")
    character.reset()
    quit()


def quit_game():
    """
    Quit and save the game.

    POST-CONDITION game is saved
    POST-CONDITION game saved message is printed
    POST-CONDITION program terminates
    """

    save.save_game()
    print("GAME SAVED")
    quit()


def restart_game():
    """
    Restart the game.

    POST-CONDITION restart message is printed
    POST-CONDITION game is restarted
    """

    print("RESTART GAME")
    character.reset()
    play_game()


def start_game():
    """
    Start the game.

    POST-CONDITION load game
    POST-CONDITION begin game play loop
    """

    save.load_game()
    play_game()


def game_event():
    """
    Process the game play loop.

    POST-CONDITION make appropriate changes to character and monster according to events
    """

    # Heal
    if character.get_hp() < character.MAX_HP():
        character.modify_hp(1)
        print("STRUCTURAL INTEGRITY +1 POINT", "\nYOUR STRUCTURAL INTEGRITY:", character.get_hp())
    # Combat
    if random.random() < 0.1:
        if not combat.combat():
            game_over()


def play_game():
    """
    Process the game play loop.

    POST-CONDITION make appropriate changes to character and monster according to events
    """

    print_introduction()
    map.print_map(character.get_coordinates())
    while True:
        player_input = input("YOUR COMMAND, CAPTAIN: ")
        # Quit
        if player_input.strip().lower() == 'quit':
            quit_game()
        # Restart
        if player_input.strip().lower() == 'restart':
            restart_game()
            break
        # Move
        character.move(player_input.strip().lower())
        # Heal & Combat
        game_event()
        map.print_map(character.get_coordinates())


def main():
    doctest.testmod()
    play_game()


if __name__ == "__main__":
    main()
