import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import create_character, character_class


class TestCreateCharacter(TestCase):
    def test_create_character_bad_argument_no_syllables(self):
        self.assertEqual(create_character(0), None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_bad_argument_no_syllables_warning(self, mock_stdout):
        create_character(0)
        self.assertTrue("WARNING" in mock_stdout.getvalue())

    def test_create_character_bad_argument_string(self):
        self.assertEqual(create_character("bad_name"), None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_bad_argument_string_warning(self, mock_stdout):
        create_character("bad_name")
        self.assertTrue("WARNING" in mock_stdout.getvalue())

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_dictionary_length(self, mock_input):
        self.assertEqual(len(create_character(1)), 11)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_name(self, mock_input):
        self.assertEqual(len(create_character(1)["Name"]), 2)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_class(self, mock_input):
        self.assertEqual(create_character(1)["Class"], "bard")

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_hp(self, mock_input):
        for i in range(0, 1000):
            character = create_character(1)
            self.assertTrue(1 <= character["HP"] <= character_class()[character["Class"]])

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_attributes(self, mock_input):
        attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        for u in range(0, 1000):
            character = create_character(1)
            for i in range(len(attributes)):
                self.assertTrue(3 <= character[attributes[i]] <= 18)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_xp(self, mock_input):
        self.assertEqual(create_character(1)["XP"], 0)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_inventory(self, mock_input):
        self.assertEqual(create_character(1)["Inventory"], [])
