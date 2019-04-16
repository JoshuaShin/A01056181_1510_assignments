"""
q04.py

Given a sum of money, determines the fewest of each bill and coin needed to represent it.
"""


# Joshua Shin
# A01056181
# April 15th 2019


import doctest


def cash_money(amount: float) -> dict:
    """
    Given a sum of money, determines the fewest of each bill and coin needed to represent it.

    PARAM positive float
    PRE-CONDITION amount must be limited to two decimal places
    RETURN dictionary representing fewest of each bill and coin needed to represent amount

    >>> cash_money(12.34)
    {100: 0, 50: 0, 20: 0, 10: 1, 5: 0, 2: 1, 1: 0, 0.25: 1, 0.1: 0, 0.05: 1, 0.01: 4}
    """
    bills = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    if type(amount) == float and amount > 0:
        for bill in bills.keys():
            if amount >= bill:
                count = int(amount / bill)
                amount -= (bill * count)
                amount = round(amount, 2)
                bills[bill] = count
        return bills
    else:
        raise ValueError("Amount must be a positive float.")


def main():
    doctest.testmod()
    print(cash_money(12.34))


if __name__ == "__main__":
    main()
