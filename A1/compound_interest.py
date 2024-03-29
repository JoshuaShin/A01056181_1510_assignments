"""
compound_interest.py.

Return amount of money in the account according to specified input.
"""

# Joshua Shin
# A01056181
# Jan 25 2019

import doctest


def compound_interest(principle, annual_interest_rate, compounded_times_per_year, years):
    """
    Return amount of money in the account according to specified input.

    PARAM principle positive float
    PARAM annual_interest_rate positive float
    PARAM compounded_times_per_year positive integer
    PARAM years positive float
    PRE-CONDITION principle must be a positive float
    PRE-CONDITION annual_interest_rate must be a positive float
    PRE-CONDITION compounded_times_per_year must be a positive integer
    PRE-CONDITION years must be a positive float
    POST-CONDITION find amount of money in the account according to specified input
    RETURN return amount of money in the account according to specified input

    >>> compound_interest(0, 0, 1, 0)
    0.0
    >>> compound_interest(1.0, 1.0, 1, 1.0)
    2.0
    >>> compound_interest(100.0, 0.1, 4, 100.0)
    1947808.0514961318
    """

    return principle * (1 + (annual_interest_rate / compounded_times_per_year)) ** (compounded_times_per_year * years)


def main():
    """
    Drive the program.
    """

    doctest.testmod()
    print(compound_interest(float(input("Principal: ")),
                            float(input("Annual interest rate: ")),
                            int(input("Compounded times per year: ")),
                            float(input("Years: ")), ))


if __name__ == "__main__":
    main()
