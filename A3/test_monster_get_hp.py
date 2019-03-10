from unittest import TestCase
import monster


class TestMonsterGetHp(TestCase):
    def test_get_hp(self):
        self.assertEqual(monster.hp, monster.get_hp())

