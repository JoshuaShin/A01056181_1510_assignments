from unittest import TestCase
from dungeonsanddragons import assign_health, character_class
import random


class TestAssignHealth(TestCase):
    def test_assign_health_integer(self):
        self.assertEqual(type(assign_health("bard")), int)

    def test_assign_health_range(self):
        for i in range(0, 1000):
            random_class = random.choice(list(character_class().keys()))
            self.assertTrue(1 <= assign_health(random_class) <= character_class()[random_class])
