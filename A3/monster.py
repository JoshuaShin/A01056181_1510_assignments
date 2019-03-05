"""
character.py

Character and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest
import save


def MAX_HP():
    """
    Max hp constant.

    RETURN character coordinates x and y in integer
    """

    return 5


def get_hp():
    """
    Return character's current hp.

    RETURN character's current hp
    """

    return save.load_monster()["hp"]


def set_hp(change_amount):
    """
    Change character's current hp by change amount specified.

    PARAM positive or negative integer
    PRE-CONDITION change amount is a positive or negative integer
    POST-CONDITION change character hp by the change amount
    RETURN True if hp is not 0
    RETURN False if hp is 0
    """

    hp = get_hp()
    hp += change_amount
    if hp > MAX_HP():
        hp = MAX_HP()
    elif hp <= 0:
        hp = 0
        save.save_monster({"hp": hp})
        return False
    save.save_monster({"hp": hp})
    return True


def reset():
    """
    Reset monster.

    POST-CONDITION Set monster hp to max hp
    """

    save.reset_monster()


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
