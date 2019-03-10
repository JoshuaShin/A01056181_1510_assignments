from unittest import TestCase
import monster


class TestMonsterModifyHp(TestCase):
    def test_modify_hp_negative(self):
        monster.hp = 5
        monster.modify_hp(-1)
        self.assertEqual(4, monster.hp)

    def test_modify_hp_positive(self):
        monster.hp = 4
        monster.modify_hp(1)
        self.assertEqual(5, monster.hp)

    def test_modify_hp_zero(self):
        monster.hp = 5
        monster.modify_hp(0)
        self.assertEqual(5, monster.hp)

    def test_modify_hp_under_min(self):
        monster.hp = 5
        monster.modify_hp(-10)
        self.assertEqual(0, monster.hp)

    def test_modify_hp_over_max(self):
        monster.hp = 0
        monster.modify_hp(10)
        self.assertEqual(5, monster.hp)

