from unittest import TestCase
import character


class TestCharacterReset(TestCase):
    def test_reset_test_hp(self):
        character.reset()
        self.assertEqual(10, character.hp)

    def test_reset_test_coordinates(self):
        character.reset()
        self.assertEqual((29, 16), character.coordinates)
