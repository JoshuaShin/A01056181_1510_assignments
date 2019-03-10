from unittest import TestCase
import monster


class TestMonsterReset(TestCase):
    def test_reset(self):
        monster.reset()
        self.assertEqual(5, monster.hp)
