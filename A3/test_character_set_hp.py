from unittest import TestCase
import character


class TestCharacterSetHp(TestCase):
    def test_set_hp(self):
        character.set_hp(3)
        self.assertEqual(3, character.hp)

