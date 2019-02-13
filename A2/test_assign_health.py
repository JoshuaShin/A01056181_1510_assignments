from unittest import TestCase
from dungeonsanddragons import assign_health, CHARACTER_CLASS
import random


class TestAssignHealth(TestCase):
    def test_assign_health_integer(self):
        self.assertEqual(type(assign_health("bard")), int)

    def test_assign_health_range(self):
        for i in range(0, 1000):
            random_class = random.choice(list(CHARACTER_CLASS().keys()))
            self.assertTrue(1 <= assign_health(random_class) <= CHARACTER_CLASS()[random_class])
