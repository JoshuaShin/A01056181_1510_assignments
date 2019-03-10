from unittest import TestCase
from map import is_impassable


class TestIsImpassable(TestCase):
    def test_is_impassable_true_a(self):
        self.assertTrue(is_impassable(0, 2))

    def test_is_impassable_true_b(self):
        self.assertTrue(is_impassable(1, 2))

    def test_is_impassable_true(self):
        self.assertFalse(is_impassable(3, 3))
