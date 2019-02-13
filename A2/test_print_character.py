import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import print_character


character = {'Name': 'A', 'Class': 'barbarian', 'HP': 10, 'Strength': 10, 'Dexterity': 10,
             'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': ["a", "b"]}


class TestPrintCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        print_character(character)
        self.assertTrue("CHARACTER INFO:\nName A\nClass barbarian\nHP 10\nStrength 10\nDexterity 10\nConstitution 10\n"
                        "Intelligence 10\nWisdom 10\nCharisma 10\nXP 0\nItem a\nItem b" in mock_stdout.getvalue())
