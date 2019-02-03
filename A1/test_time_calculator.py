"""
test_time_calculator.py

Test time_calculator function.
"""

# Joshua Shin
# A01056181
# Jan 31 2019

from unittest import TestCase
from time_calculator import time_calculator


class TestTimeCalculator(TestCase):
    """
    Test time_calculator function.
    """

    def test_time_calculator_zero_integer(self):
        """
        Test lowest input.
        """
        self.assertEqual([0, 0, 0, 0], time_calculator(0))

    def test_time_calculator_medium_integer(self):
        """
        Test medium size input.
        """
        self.assertEqual([0, 0, 16, 40], time_calculator(1000))

    def test_time_calculator_large_integer(self):
        """
        Test large input.
        """
        self.assertEqual([11, 13, 46, 40], time_calculator(1000000))
