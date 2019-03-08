"""
character.py

Character and associated functions for SUD.
"""


# Joshua Shin
# A01056181
# Mar 1st 2019


import doctest


hp = 5


def reset():
    """
    Reset monster.

    POST-CONDITION Set monster hp to max hp
    """

    modify_hp(MAX_HP())


def MAX_HP():
    """
    Max hp constant.

    RETURN character coordinates x and y in integer

    >>> MAX_HP()
    5
    """

    return 5


def get_hp():
    """
    Return character's current hp.

    RETURN character's current hp

    >>> get_hp()
    5
    """

    return hp


def modify_hp(change_amount):
    """
    Change character's current hp by change amount specified.

    PARAM positive or negative integer
    PRE-CONDITION change amount is a positive or negative integer
    POST-CONDITION change character hp by the change amount
    RETURN True if hp is not 0
    RETURN False if hp is 0

    >>> modify_hp(10)
    True
    >>> modify_hp(-10)
    False
    """

    global hp
    hp += change_amount
    if hp > MAX_HP():
        hp = MAX_HP()
    elif hp <= 0:
        hp = 0
        return False
    return True


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
