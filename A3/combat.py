"""
combat.py

Combat functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import random
import doctest
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

    if combat_flee():
        if character.get_hp() > 0:
            return True
        else:
            return False

    monster.reset()
    print("--- COMBAT STARTS ---")

    while True:
        print("YOUR STRUCTURAL INTEGRITY:", character.get_hp(), "\nENEMY STRUCTURAL INTEGRITY:", monster.get_hp())
        input("--- PRESS ANY KEY TO CONTINUE ---")

        character_roll = roll_die(1, 6)
        print("USS ENTERPRISE FIRES:", character_roll, "PHOTON TORPEDO(ES)")
        if not monster.modify_hp(-character_roll):
            print("ENEMY STRUCTURAL INTEGRITY: 0", "\nENEMY DESTROYED", "\n--- COMBAT ENDS ---")
            return True

        monster_roll = roll_die(1, 6)
        print("BIRD OF PREY FIRES:", monster_roll, "PHOTON TORPEDO(ES)")
        if not character.modify_hp(-monster_roll):
            print("ENEMY STRUCTURAL INTEGRITY:", monster.get_hp(), "\nYOUR STRUCTURAL INTEGRITY: 0", "\nDEFEATED")
            return False


def combat_flee():
    """
    Check if user will flee the combat.

    POST-CONDITION 10% chance character takes damage from fleeing
    RETURN True if user flees
    RETURN False if user fights
    """

    print("--- ENEMY ENCOUNTER ---")
    print("""
                            _------_        _------_
                           / /~~~~~~~\----/~~~~~~~\ \\
                        __|_|    /~ _-~~~~-_ ~\    |_|__
                  __--~~____|   |  /________\  |   |____~~--__
            __--~~__--~~     ~---__\   ()   /__---~     ~~--__~~--__
         /~~__--~~                  ~--__--~                  ~~--__~~\\
       / /~~                                                        ~~\ \\
     / /                                                                \ \\
    (0)                                                                  (0)
                    K L I N G O N   B I R D   O F   P R E Y
    
    """)
    while True:
        user_input = input("FIGHT? (y/n)").strip().lower()
        if user_input == "y":
            return False
        elif user_input == "n":
            combat_flee_damage()
            return True
        else:
            print("INVALID INPUT")


def combat_flee_damage():
    """
    Check if character takes damage from fleeing.

    POST-CONDITION 10% chance character takes damage from fleeing
    """

    if random.random() < 0.1:
        monster_roll = roll_die(1, 4)
        print("--- WARP OUT PENALTY ---", "\nBIRD OF PREY FIRES:", monster_roll, "PHOTON TORPEDO(ES)")
        if not character.modify_hp(-monster_roll):
            print("YOUR STRUCTURAL INTEGRITY: 0", "\nYOU ARE DESTROYED")
        else:
            print("YOUR STRUCTURAL INTEGRITY:", character.get_hp())
    else:
        print("WARPED OUT SAFELY")


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
