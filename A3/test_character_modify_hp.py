from unittest import TestCase
import character


class TestCharacterModifyHp(TestCase):
    def test_modify_hp_negative(self):
        character.hp = 6
        character.modify_hp(-1)
        self.assertEqual(5, character.hp)

    def test_modify_hp_positive(self):
        character.hp = 4
        character.modify_hp(1)
        self.assertEqual(5, character.hp)

    def test_modify_hp_zero(self):
        character.hp = 5
        character.modify_hp(0)
        self.assertEqual(5, character.hp)

    def test_modify_hp_under_min(self):
        character.hp = 5
        character.modify_hp(-10)
        self.assertEqual(0, character.hp)

    def test_modify_hp_over_max(self):
        character.hp = 5
        character.modify_hp(10)
        self.assertEqual(10, character.hp)

