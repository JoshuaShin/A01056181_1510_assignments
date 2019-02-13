import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import combat_initiative


opponent_1 = {'Name': 'A', 'Class': 'barbarian', 'HP': 10, 'Strength': 10, 'Dexterity': 10,
              'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': []}
opponent_2 = {'Name': 'A', 'Class': 'barbarian', 'HP': 10, 'Strength': 10, 'Dexterity': 10,
              'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': []}


class TestCombatInitiative(TestCase):
    @patch('dungeonsanddragons.roll_die', side_effect=[2, 1])
    def test_combat_initiative_opponent_1_wins(self, input):
        self.assertEqual(combat_initiative(opponent_1, opponent_2), (opponent_1, opponent_2))

    @patch('dungeonsanddragons.roll_die', side_effect=[1, 2])
    def test_combat_initiative_opponent_2_wins(self, input):
        self.assertEqual(combat_initiative(opponent_1, opponent_2), (opponent_2, opponent_1))

    @patch('dungeonsanddragons.roll_die', side_effect=[1, 1, 1, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_initiative_tie(self, mock_stdout, input):
        combat_initiative(opponent_1, opponent_2)
        self.assertTrue("Tied. Re-roll...\n" in mock_stdout.getvalue())
