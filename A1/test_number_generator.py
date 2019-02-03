"""
test_number_generator.py

Test number_generator function.
"""

# Joshua Shin
# A01056181
# Jan 31 2019

from unittest import TestCase
from lotto import number_generator


class TestNumberGenerator(TestCase):
    """
    Test number_generator function.
    """

    def test_number_generator_length(self):
        """
        Test length is 6.
        """
        self.assertEqual(6, len(number_generator()))

    def test_number_generator_integer(self):
        """
        Test list items are integers.
        """
        random_numbers = number_generator()
        self.assertTrue(random_numbers[0] == int(random_numbers[0]) and
                        random_numbers[1] == int(random_numbers[1]) and
                        random_numbers[2] == int(random_numbers[2]) and
                        random_numbers[3] == int(random_numbers[3]) and
                        random_numbers[4] == int(random_numbers[4]) and
                        random_numbers[5] == int(random_numbers[5]))

    def test_number_generator_unique(self):
        """
        Test list items are unique.
        """
        self.assertEqual(6, len(set(number_generator())))

    def test_number_generator_sorted(self):
        """
        Test list is sorted.
        """
        random_numbers = number_generator()
        self.assertEqual(sorted(random_numbers), random_numbers)

    def test_number_generator_range(self):
        """
        Test list items are within range 1 to 49.
        """
        lotto_range = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                       10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                       20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                       30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                       40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
        random_numbers = number_generator()
        self.assertTrue(random_numbers[0] in lotto_range and
                        random_numbers[1] in lotto_range and
                        random_numbers[2] in lotto_range and
                        random_numbers[3] in lotto_range and
                        random_numbers[4] in lotto_range and
                        random_numbers[5] in lotto_range)
