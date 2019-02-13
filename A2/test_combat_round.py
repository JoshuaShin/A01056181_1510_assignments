import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import combat_round


opponent_1 = {'Name': 'A', 'Class': 'barbarian', 'HP': 10, 'Strength': 10, 'Dexterity': 10,
              'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': []}
opponent_2 = {'Name': 'A', 'Class': 'barbarian', 'HP': 10, 'Strength': 10, 'Dexterity': 10,
              'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': []}


class TestCombatRound(TestCase):
    @patch('dungeonsanddragons.roll_die', side_effect=[1, 2, 11, 10, 0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_opponent_1_dies(self, mock_stdout, input):
        combat_round(opponent_1, opponent_2)
        self.assertEqual(opponent_1["HP"], 0)

    @patch('dungeonsanddragons.roll_die', side_effect=[1, 2, 0, 11, 10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_opponent_2_dies(self, mock_stdout, input):
        combat_round(opponent_1, opponent_2)
        self.assertEqual(opponent_2["HP"], 0)
