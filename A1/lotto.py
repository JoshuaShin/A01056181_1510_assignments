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

    return sorted(random.sample(range(1, 49), 6))


def main():
    """
    Drive the program.
    """

    print(number_generator())


if __name__ == "__main__":
    main()
