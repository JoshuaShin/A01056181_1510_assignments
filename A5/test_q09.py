from unittest import TestCase
import q09


class TestBaseConversion(TestCase):
    def test_base_conversion_return_type(self):
        self.assertEqual(int, type(q09.base_conversion(2, 10101, 8)))

    def test_base_conversion_positive(self):
        self.assertEqual(25, q09.base_conversion(2, 10101, 8))

    def test_base_conversion_zero(self):
        self.assertEqual(0, q09.base_conversion(2, 0, 10))

    def test_base_conversion_negative(self):
        self.assertEqual(-25, q09.base_conversion(2, -10101, 8))
