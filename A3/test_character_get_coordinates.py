from unittest import TestCase
import character


class TestCharacterGetCoordinates(TestCase):
    def test_get_coordinates(self):
        self.assertEqual(character.coordinates, character.get_coordinates())
