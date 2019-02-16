import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import combat_attack


attacker = {'Name': 'A', 'Class': 'barbarian', 'HP': 10, 'Strength': 10, 'Dexterity': 10,
            'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': []}
defender = {'Name': 'B', 'Class': 'barbarian', 'HP': 10, 'Strength': 10, 'Dexterity': 10,
            'Constitution': 10, 'Intelligence': 10, 'Wisdom': 10, 'Charisma': 10, 'XP': 0, 'Inventory': []}


class TestCombatAttack(TestCase):
    @patch('dungeonsanddragons.roll_die', side_effect=[11, 0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_attack_success(self, mock_stdout, mock_input):
        combat_attack(attacker, defender)
        self.assertTrue("hits" in mock_stdout.getvalue())

    @patch('dungeonsanddragons.roll_die', side_effect=[10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_attack_fail(self, mock_stdout, mock_input):
        combat_attack(attacker, defender)
        self.assertTrue("misses" in mock_stdout.getvalue())

    @patch('dungeonsanddragons.roll_die', side_effect=[11, 1])
    def test_combat_attack_damage(self, mock_input):
        combat_attack(attacker, defender)
        self.assertEqual(defender["HP"], 9)
