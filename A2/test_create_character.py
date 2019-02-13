import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import create_character


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
    def test_create_character_dictionary_length(self, input):
        self.assertEqual(len(create_character(1)), 11)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_name(self, input):
        self.assertEqual(len(create_character(1)["Name"]), 2)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_class(self, input):
        self.assertEqual(create_character(1)["Class"], "bard")

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_hp(self, input):
        self.assertTrue(create_character(1)["HP"] > 0)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_attributes(self, input):
        attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        for u in range(0, 1000):
            character = create_character(1)
            for i in range(len(attributes)):
                self.assertTrue(3 <= character[attributes[i]] <= 18)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_xp(self, input):
        self.assertEqual(create_character(1)["XP"], 0)

    @patch('dungeonsanddragons.choose_class', return_value="bard")
    def test_create_character_inventory(self, input):
        self.assertEqual(create_character(1)["Inventory"], [])
