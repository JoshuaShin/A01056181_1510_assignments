from unittest import TestCase
from lotto import number_generator


class TestNumberGenerator(TestCase):


    def test_number_generator_length(self):
        self.assertEqual(6, len(number_generator()))

    def test_number_generator_unique(self):
        self.assertEqual(6, len(set(number_generator())))

    def test_number_generator_range(self):
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

    def test_number_generator_sorted(self):
        random_numbers = number_generator()
        self.assertTrue(random_numbers[0] < random_numbers[1] and
                        random_numbers[1] < random_numbers[2] and
                        random_numbers[2] < random_numbers[3] and
                        random_numbers[3] < random_numbers[4] and
                        random_numbers[4] < random_numbers[5])
