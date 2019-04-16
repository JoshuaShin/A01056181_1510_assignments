"""
q08.py

Tests for a function called line_intersect, which accepts two lines as input and returns their intersection.
"""


# Joshua Shin
# A01056181
# April 15th 2019

"""
from unittest import TestCase


def line_intersect(line_a, line_b):
    pass


class TestTimeCalculator(TestCase):
    def test_line_intersect_return_type(self):
        self.assertEqual(list, type(line_intersect([[1, 1], [-1, -1]], [[-1, 1], [1, -1]])))

    def test_line_intersect_not_a_line_argument(self):
        with self.assertRaises(ValueError):
            line_intersect([[1, 1], [1, 1]], [[0, 0], [0, 0]])

    def test_line_intersect_negative_argument(self):
        self.assertEqual([-1, -1], line_intersect([[0, 0], [-2, -2]], [[0, -2], [-2, 0]]))

    def test_line_intersect_one_point(self):
        self.assertEqual([0, 0], line_intersect([[1, 1], [2, 2]], [[0, 2], [2, 0]]))

    def test_line_intersect_no_point(self):
        self.assertEqual(None, line_intersect([[0, 0], [2, 2]], [[2, 0], [4, 2]]))

    def test_line_intersect_line_overlap(self):
        self.assertEqual([[0, 0], [2, 2]], line_intersect([[0, 0], [2, 2]], [[1, 1], [3, 3]]))
"""
