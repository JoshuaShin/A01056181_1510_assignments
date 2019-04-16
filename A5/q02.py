"""
q02.py

Calculate greatest common divisor between two numbers.
"""


# Joshua Shin
# A01056181
# April 9th 2019


import doctest


def gcd(a: int, b: int) -> int:
    """
    Calculate greatest common divisor.

    PRE-CONDITION a must not be 0
    PRE-CONDITION b must not be 0
    RETURN greatest common divisor between a and b

    >>> gcd(4, 12)
    4
    >>> gcd(4, -12)
    4
    >>> gcd(0, 12)
    12
    """
    if a == 0 and b == 0:
        raise ValueError("Invalid Inputs")
    elif a % b == 0:
        return abs(b)
    else:
        return gcd(b, (a % b))


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
