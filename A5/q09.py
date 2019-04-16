"""
q09.py

A base conversion module.
"""


# Joshua Shin
# A01056181
# April 15th 2019


import doctest
import math


def base_conversion(original_base: int, original_number: int, destination_base: int) -> int:
    """
    Convert original number in original base to destination base.

    PRECONDITION original base must be between 2 and 10
    PRECONDITION destination base must be between 2 and 10
    RETURN Correctly converted number with destination base

    >>> base_conversion(2, 10101, 8)
    25
    """
    if original_number == 0:
        return 0
    elif original_number < 0:
        return -1 * to_destination_base(to_decimal(abs(original_number), original_base), destination_base)
    else:
        return to_destination_base(to_decimal(abs(original_number), original_base), destination_base)


def to_decimal(number: int, original_base: int) -> int:
    """
    Convert the number with original base to decimal.

    PRE-CONDITION original base must be an integer between 2 and 10
    RETURN the number with given base converted to decimal

    >>> to_decimal(10101, 2)
    21
    """
    if 2 <= original_base <= 10:
        sep_numbers, dec_number = [int(index) for index in str(abs(number))], 0
        num_length = len(sep_numbers)
        for i in range(0, num_length):
            dec_number += sep_numbers[i] * (original_base ** (num_length - 1 - i))
        return dec_number
    else:
        raise ValueError("Base must be an integer between 2 and 10.")


def to_destination_base(number: int, destination_base: int) -> int:
    """
    Convert decimal number to destination base.

    PRE-CONDITION destination_base must be an integer between 2 and 10
    RETURN the number in decimal converted to destination base

    >>> to_destination_base(21, 8)
    25
    """
    if 2 <= destination_base <= 10:
        destination_number = ""
        for i in range(math.trunc(math.log(number, destination_base)) + 1):
            destination_number += str(number % destination_base)
            number = math.trunc(number / destination_base)
        return int(destination_number[::-1])
    else:
        raise ValueError("Base must be an integer between 2 and 10.")


def main():
    doctest.testmod()
    print(base_conversion(10, -21, 2))


if __name__ == '__main__':
    main()
