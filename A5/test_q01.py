from unittest import TestCase
import q01


class TestSumOfPrimes(TestCase):
    def test_sum_of_primes_zero(self):
        with self.assertRaises(ValueError):
            q01.sum_of_primes(0)

    def test_sum_of_primes_negative(self):
        with self.assertRaises(ValueError):
            q01.sum_of_primes(-1)

    def test_sum_of_primes_one(self):
        self.assertEqual(0, q01.sum_of_primes(1))

    def test_sum_of_primes_small(self):
        self.assertEqual(17, q01.sum_of_primes(10))

    def test_sum_of_primes_large(self):
        self.assertEqual(1060, q01.sum_of_primes(100))
