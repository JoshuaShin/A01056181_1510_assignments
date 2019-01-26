"""
lotto.py.

Return length 6 unique sorted list of integers.
"""

# Joshua Shin
# A01056181
# Jan 25 2019

import random


def number_generator():
    """
    Build length 6 unique sorted list of integers.

    RETURN length 6 unique sorted integer list
    """

    """ ORIGINAL ANSWER
    lottery_list = []

    while len(lottery_list) < 6:
        random_number = random.randint(1, 49)
        if random_number in lottery_list:
            continue
        else:
            lottery_list.append(random_number)

    lottery_list.sort()
    return lottery_list
    """

    # GOOGLE-FU ANSWER (I know enough programming to know that there's a million built in functions!)
    lottery_list = random.sample(range(1, 49), 6)
    lottery_list.sort()  # Hey Chris, how come if i do "return lottery_list.sort()" it returns "None"?

    return lottery_list


def main():
    """
    Drive the program.
    """

    print(number_generator())


if __name__ == "__main__":
    main()
