"""
phone_fun.py.

Translate a phone number with letters to all numbers.
"""

# Joshua Shin
# A01056181
# Jan 25 2019


def letter_to_number(character):
    """
    Take phone number character and return corresponding number in string.

    PARAM character is an alphabet character
    PRE-CONDITION character must be a an alphabet character
    POST-CONDITION find the number in string equivalent of the input alphabet character
    RETURN corresponding number of alphabet character in string
    """

    if character == "a" or character == "b" or character == "c":
        return "2"
    elif character == "d" or character == "e" or character == "f":
        return "3"
    elif character == "g" or character == "h" or character == "i":
        return "4"
    elif character == "j" or character == "k" or character == "l":
        return "5"
    elif character == "m" or character == "n" or character == "o":
        return "6"
    elif character == "p" or character == "q" or character == "r" or character == "s":
        return "7"
    elif character == "t" or character == "u" or character == "v":
        return "8"
    elif character == "w" or character == "x" or character == "y" or character == "z":
        return "9"
    else:
        return character


def number_translator():
    """
    Translate a phone number with letters to all numbers.

    RETURN translated phone number with letters to all numbers
    """

    """
    for i in range(len(phone_number)):
        if phone_number[i] == "-":
            continue
        elif phone_number[i].isalpha():
            phone_number = phone_number[0:i] + letter_to_number(phone_number[i]) + phone_number[i+1:len(phone_number)]
    return phone_number
    """

    phone_number = input("Enter a phone number in the format XXX-XXX-XXXX: ")

    translated_number = ""

    translated_number += letter_to_number(phone_number[0])
    translated_number += letter_to_number(phone_number[1])
    translated_number += letter_to_number(phone_number[2])
    translated_number += letter_to_number(phone_number[3])
    translated_number += letter_to_number(phone_number[4])
    translated_number += letter_to_number(phone_number[5])
    translated_number += letter_to_number(phone_number[6])
    translated_number += letter_to_number(phone_number[7])
    translated_number += letter_to_number(phone_number[8])
    translated_number += letter_to_number(phone_number[9])
    translated_number += letter_to_number(phone_number[10])
    translated_number += letter_to_number(phone_number[11])

    return translated_number


def main():
    """
    Drive the program.
    """

    print("Translated number:", number_translator())


if __name__ == "__main__":
    main()
