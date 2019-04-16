from unittest import TestCase
import q02


class TestGcd(TestCase):
    def test_gcd_argument_zero(self):
        self.assertEqual(12, q02.gcd(0, 12))

    def test_gcd_zeroes(self):
        with self.assertRaises(ValueError):
            q02.gcd(0, 0)

    def test_gcd_positives(self):
        self.assertEqual(4, q02.gcd(4, 12))

    def test_gcd_first_positive_negative(self):
        self.assertEqual(4, q02.gcd(4, -12))

    def test_gcd_first_negative_positive(self):
        self.assertEqual(4, q02.gcd(-4, 12))

    def test_gcd_negatives(self):
        self.assertEqual(4, q02.gcd(-4, -12))

