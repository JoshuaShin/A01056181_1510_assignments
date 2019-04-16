from unittest import TestCase
from A5 import q05


class TestCashMoney(TestCase):
    def test_cash_money_invalid_integer(self):
        with self.assertRaises(ValueError):
            q05.cash_money(100)

    def test_cash_money_invalid_zero(self):
        with self.assertRaises(ValueError):
            q05.cash_money(0)

    def test_cash_money_invalid_negative(self):
        with self.assertRaises(ValueError):
            q05.cash_money(-1.32)

    def test_cash_money_valid(self):
        self.assertEqual({100: 0, 50: 0, 20: 0, 10: 1, 5: 0, 2: 1, 1: 0, 0.25: 1, 0.1: 0, 0.05: 1, 0.01: 4}
                         , q05.cash_money(12.34))
