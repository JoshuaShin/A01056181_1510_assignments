"""
test_compound_interest.py

Test compound_interest function.
"""

# Joshua Shin
# A01056181
# Jan 31 2019

from unittest import TestCase
from compound_interest import compound_interest


class TestCompoundInterest(TestCase):
    """
    Test compound_interest function.
    """

    def test_compound_interest_zero(self):
        """
        Test zero inputs.
        """
        self.assertEqual(0.0, compound_interest(0, 0, 1, 0))

    def test_compound_interest_low(self):
        """
        Test low inputs.
        """
        self.assertEqual(2.0, compound_interest(1.0, 1.0, 1, 1.0))

    def test_compound_interest_high(self):
        """
        Test high inputs.
        """
        self.assertEqual(1947808.0514961318, compound_interest(100.0, 0.1, 4, 100.0))
