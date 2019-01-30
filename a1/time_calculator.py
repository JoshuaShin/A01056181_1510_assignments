"""
time_calculator.py

Return days, hours, minutes, seconds from given seconds.
"""

# Joshua Shin
# A01056181
# Jan 24 2019


def time_calculator(seconds):
    """
    Return days, hours, minutes, seconds from given seconds.

    PARAM seconds positive integer
    PRE-CONDITION seconds must be a positive integer
    POST-CONDITION find days, hours, minutes, seconds of the input seconds
    RETURN return days, hours, minutes, seconds of the input seconds
    """

    days = seconds // 86400
    seconds %= 86400

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    return [days, hours, minutes, seconds]


def main():
    """
    Drive the program.
    """

    print(time_calculator(int(input("Input seconds: "))))


if __name__ == "__main__":
    main()
