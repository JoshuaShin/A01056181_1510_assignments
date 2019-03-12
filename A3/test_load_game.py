from unittest import TestCase
import json
import save
import character


class TestLoadGame(TestCase):
    def test_load_game(self):
        character_dictionary = {'hp': 5, 'column': 20, 'row': 20}
        with open('character.json', 'w') as file_object:
            json.dump(character_dictionary, file_object, sort_keys=True, indent=4)

        save.load_game()

        current_character = {"hp": character.get_hp(),
                             "column": character.get_coordinates()[0],
                             "row": character.get_coordinates()[1]}
        self.assertEqual({"hp": 5, "column": 20, "row": 20}, current_character)
