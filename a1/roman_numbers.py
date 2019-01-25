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

    while positive_int > 0:
        if positive_int // 1000 > 0:
            positive_int -= 1000
            answer += "M"

        elif positive_int // 900 > 0:
            positive_int -= 900
            answer += "CM"

        elif positive_int // 500 > 0:
            positive_int -= 500
            answer += "D"

        elif positive_int // 400 > 0:
            positive_int -= 400
            answer += "CD"

        elif positive_int // 100 > 0:
            positive_int -= 100
            answer += "C"

        elif positive_int // 90 > 0:
            positive_int -= 90
            answer += "XC"

        elif positive_int // 50 > 0:
            positive_int -= 50
            answer += "L"

        elif positive_int // 40 > 0:
            positive_int -= 40
            answer += "XL"

        elif positive_int // 10 > 0:
            positive_int -= 10
            answer += "X"

        elif positive_int // 9 > 0:
            positive_int -= 9
            answer += "IX"

        elif positive_int // 5 > 0:
            positive_int -= 5
            answer += "V"

        elif positive_int // 4 > 0:
            positive_int -= 4
            answer += "IV"

        elif positive_int // 1 > 0:
            positive_int -= 1
            answer += "I"

    return answer


def main():
    """
    Drive the program.
    """
    print(convert_to_roman_numeral(int(input("Input positive integer: "))))


if __name__ == "__main__":
    main()
