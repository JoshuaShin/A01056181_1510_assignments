"""
test_convert_to_roman_numeral.py

Test covert_to_roman_numeral function.
"""

# Joshua Shin
# A01056181
# Jan 31 2019

from unittest import TestCase
from roman_numbers import convert_to_roman_numeral


class TestConvertToRomanNumeral(TestCase):
    """
    Test covert_to_roman_numeral function.
    """

    def test_convert_to_roman_numeral_max_integer(self):
        """
        Test maximum input.
        """
        self.assertEqual(convert_to_roman_numeral(10000), "MMMMMMMMMM")

    def test_convert_to_roman_numeral_larger_integer(self):
        """
        Test large input.
        """
        self.assertEqual(convert_to_roman_numeral(3999), "MMMCMXCIX")

    def test_convert_to_roman_numeral_lower_integer(self):
        """
        Test lower input.
        """
        self.assertEqual(convert_to_roman_numeral(444), "CDXLIV")

    def test_convert_to_roman_numeral_min_integer(self):
        """
        Test minimum input.
        """
        self.assertEqual(convert_to_roman_numeral(1), "I")
