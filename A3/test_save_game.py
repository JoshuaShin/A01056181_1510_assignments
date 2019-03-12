from unittest import TestCase
import json
import save
import character


class TestSaveGame(TestCase):
    def test_save_game(self):
        character.set_hp(6)
        character.set_coordinates(21, 21)
        save.save_game()

        with open('character.json') as file_object:
            current_character = json.load(file_object)

        self.assertEqual({"hp": 6, "column": 21, "row": 21}, current_character)
