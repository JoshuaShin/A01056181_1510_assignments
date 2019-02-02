from unittest import TestCase
from compound_interest import compound_interest


class TestCompoundInterest(TestCase):
    def test_compound_interest_zero(self):
        self.assertEqual(0.0, compound_interest(0, 0, 1, 0))

    def test_compound_interest_low(self):
        self.assertEqual(2.0, compound_interest(1.0, 1.0, 1, 1.0))

    def test_compound_interest_high(self):
        self.assertEqual(1947808.0514961318, compound_interest(100.0, 0.1, 4, 100.0))
