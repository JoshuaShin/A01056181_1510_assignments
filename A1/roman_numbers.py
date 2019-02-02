"""
roman_numbers.py

Take a number between 1- 10,000 as input and return the roman numeral equivalent.
"""

# Joshua Shin
# A01056181
# Jan 24 2019

import doctest


"""
roman_number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_letter = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


def convert_to_roman_numeral_recursively(positive_int):
    if not positive_int:
        return ""

    else:
        answer = roman_letter[0] * (positive_int // roman_number[0])
        positive_int %= roman_number[0]
        roman_number.pop(0)
        roman_letter.pop(0)
        return answer + convert_to_roman_numeral_recursively(positive_int)
"""


def convert_to_roman_numeral(positive_int):
    """
    Take a number between 1- 10,000 as input and return the roman numeral equivalent.

    PARAM positive_int is a positive integer
    PRE-CONDITION positive int must be a positive integer
    POST-CONDITION find the roman numeral equivalent of the input positive integer
    RETURN roman numeral equivalent of the input positive integer

    >>> convert_to_roman_numeral(1)
    'I'
    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    >>> convert_to_roman_numeral(4999)
    'MMMMCMXCIX'
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

    doctest.testmod()
    print(convert_to_roman_numeral(int(input("Input positive integer: "))))


if __name__ == "__main__":
    main()
