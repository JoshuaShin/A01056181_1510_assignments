"""
roman_number.py

Take a number between 1- 10,000 as input and return the roman numeral equivalent.
"""

# Joshua Shin
# A01056181
# Jan 24 2019


def convert_to_roman_numeral(positive_int):
    """
    Take a number between 1- 10,000 as input and return the roman numeral equivalent.

    PARAM positive_int is a positive integer
    PRE-CONDITION positive int must be a positive integer
    POST-CONDITION find the roman numeral equivalent of the input positive integer
    RETURN roman numeral equivalent of the input positive integer
    """

    answer = ""

    answer += "M" * (positive_int // 1000)
    positive_int %= 1000

    answer += "CM" * (positive_int // 900)
    positive_int %= 900

    answer += "D" * (positive_int // 500)
    positive_int %= 500

    answer += "CD" * (positive_int // 400)
    positive_int %= 400

    answer += "C" * (positive_int // 100)
    positive_int %= 100

    answer += "XC" * (positive_int // 90)
    positive_int %= 90

    answer += "L" * (positive_int // 50)
    positive_int %= 50

    answer += "XL" * (positive_int // 40)
    positive_int %= 40

    answer += "X" * (positive_int // 10)
    positive_int %= 10

    answer += "IX" * (positive_int // 9)
    positive_int %= 9

    answer += "V" * (positive_int // 5)
    positive_int %= 5

    answer += "IV" * (positive_int // 4)
    positive_int %= 4

    answer += "I" * (positive_int // 1)
    positive_int %= 1

    return answer


def main():
    """
    Drive the program.
    """

    print(convert_to_roman_numeral(int(input("Input positive integer: "))))


if __name__ == "__main__":
    main()
