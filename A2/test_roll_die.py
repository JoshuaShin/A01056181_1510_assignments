from unittest import TestCase
from dungeonsanddragons import roll_die
import random

class TestRollDie(TestCase):
    def test_roll_die_no_sides(self):
        self.assertEqual(roll_die(10, 0), 0)

    def test_roll_die_no_rolls(self):
        self.assertEqual(roll_die(0, 10), 0)

    def test_roll_die_integer(self):
        self.assertEqual(type(roll_die(0, 10)), int)

    def test_roll_die_range(self):
        for i in range(0, 1000):
            random_sides = random.randint(1, 20)
            random_rolls = random.randint(1, 4)
            self.assertTrue(random_rolls <= roll_die(random_rolls, random_sides) <= random_rolls * random_sides)

