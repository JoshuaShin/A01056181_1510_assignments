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

    # Languages have built in methods for everything I can image. I had to google the python specifics though.
    return sorted(random.sample(range(1, 49), 6))


def main():
    """
    Drive the program.
    """

    print(number_generator())


if __name__ == "__main__":
    main()
