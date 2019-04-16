"""
q02.py

Calculate greatest common divisor between two numbers.
"""


import doctest


# Joshua Shin
# A01056181
# April 9th 2019


def gcd(a: int, b: int) -> int:
    """
    Calculate greatest common divisor.

    PRECONDITION a must not be 0
    PRECONDITION B must not be 0
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
