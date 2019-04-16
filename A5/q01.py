"""
q01.py

Calculate the sum of all prime within given upper bound.
"""


# Joshua Shin
# A01056181
# April 15th 2019


import doctest
import math


def sum_of_primes(upperbound: int) -> int:
    """
    Calculate the sum of all prime within given upper bound.

    PRE-CONDITION upperbound must be larger than 0
    RETURN sum of all prime within given upper bound

    >>> sum_of_primes(1)
    0
    >>> sum_of_primes(10)
    17
    >>> sum_of_primes(100)
    1060
    """
    if upperbound < 1:
        raise ValueError("Must be larger than 0")
    else:
        prime = list(range(upperbound + 1))
        for i in range(2, math.ceil(math.sqrt(upperbound + 1))):
            if all(i % x for x in range(2, i)):  # If prime
                for j in range(i * 2, upperbound + 1, i):
                    prime[j] = 0
            else:
                for j in range(i, upperbound + 1, i):
                    prime[j] = 0
    return sum(prime) - 1


def main():
    doctest.testmod()
    print(sum_of_primes(10))


if __name__ == '__main__':
    main()






