import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import combat_initiative

character_1 = {'Name': 'A', 'Class': 'barbarian', 'HP': 12, 'Strength': 9, 'Dexterity': 7,
               'Constitution': 13, 'Intelligence': 4, 'Wisdom': 15, 'Charisma': 11, 'XP': 0, 'Inventory': []}
character_2 = {'Name': 'B', 'Class': 'barbarian', 'HP': 12, 'Strength': 9, 'Dexterity': 7,
               'Constitution': 13, 'Intelligence': 4, 'Wisdom': 15, 'Charisma': 11, 'XP': 0, 'Inventory': []}


class TestCombatInitiative(TestCase):
    @patch('dungeonsanddragons.roll_die', side_effect=[2, 1])
    def test_combat_initiative_opponent_1_wins(self, input):
        self.assertEqual(combat_initiative(character_1, character_2), (character_1, character_2))

    @patch('dungeonsanddragons.roll_die', side_effect=[1, 2])
    def test_combat_initiative_opponent_2_wins(self, input):
        self.assertEqual(combat_initiative(character_1, character_2), (character_2, character_1))

    @patch('dungeonsanddragons.roll_die', side_effect=[1, 1, 1, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_initiative_tie(self, mock_stdout, input):
        combat_initiative(character_1, character_2)
        self.assertTrue("Tied. Re-roll...\n" in mock_stdout.getvalue())
