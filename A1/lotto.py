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

    lotto_range = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                   20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                   30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                   40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

    return sorted(random.sample(lotto_range, 6))


def main():
    """
    Drive the program.
    """

    print(number_generator())


if __name__ == "__main__":
    main()
