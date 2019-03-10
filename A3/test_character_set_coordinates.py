from unittest import TestCase
import character


class TestCharacterSetCoordinates(TestCase):
    def test_set_coordinates(self):
        character.set_coordinates(20, 20)
        self.assertEqual((20, 20), character.coordinates)
