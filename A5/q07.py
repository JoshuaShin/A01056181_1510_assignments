"""
q07.py

A password validation function that uses regular expressions to validate a potential password.
"""


# Joshua Shin
# A01056181
# April 15th 2019


import doctest
import re


def password_validator(password: str) -> bool:
    """
    Validate password strength.

    RETURN True if strong password
    RETURN False if weak password

    >>> password_validator("helloThere3")
    True
    >>> password_validator("hello")
    False
    """
    if re.compile(r'.{8,}').search(password) \
            and re.compile(r'[a-z]+').search(password) \
            and re.compile(r'[A-Z]+').search(password) \
            and re.compile(r'\d+').search(password):
        return True
    else:
        return False


def main():
    doctest.testmod()

    print(password_validator("hello"))
    print(password_validator(""))
    print(password_validator("helloTherehowareyou"))
    print(password_validator("helloThere3"))


if __name__ == "__main__":
    main()
