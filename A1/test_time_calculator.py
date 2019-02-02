from unittest import TestCase
from time_calculator import time_calculator


class TestTimeCalculator(TestCase):
    def test_time_calculator_zero_integer(self):
        self.assertEqual([0, 0, 0, 0], time_calculator(0))

    def test_time_calculator_medium_integer(self):
        self.assertEqual([0, 0, 16, 40], time_calculator(1000))

    def test_time_calculator_large_integer(self):
        self.assertEqual([11, 13, 46, 40], time_calculator(1000000))
