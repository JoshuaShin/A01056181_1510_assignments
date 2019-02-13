import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import check_death

alive_character = {'Name': 'A', 'Class': 'barbarian', 'HP': 1, 'Strength': 10, 'Dexterity': 10,
                   'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': []}
dead_character = {'Name': 'A', 'Class': 'barbarian', 'HP': 0, 'Strength': 10, 'Dexterity': 10,
                  'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': []}


class TestCheckDeath(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_death_alive_character(self, mock_stdout):
        check_death(alive_character)
        self.assertEqual("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_death_dead_character(self, mock_stdout):
        check_death(dead_character)
        self.assertTrue("dead" in mock_stdout.getvalue())
