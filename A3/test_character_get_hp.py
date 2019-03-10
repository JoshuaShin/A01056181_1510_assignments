from unittest import TestCase
import character


class TestCharacterGetHp(TestCase):
    def test_get_hp(self):
        self.assertEqual(character.hp, character.get_hp())
