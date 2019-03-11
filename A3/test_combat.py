import io
from unittest.mock import patch
from unittest import TestCase
from combat import combat
import character


class TestCombat(TestCase):
    @patch('combat.combat_flee', side_effect=[True])
    def test_combat_flee_dead(self, mock_combat_flee):
        character.set_hp(0)
        self.assertEqual(False, combat())

    @patch('combat.combat_flee', side_effect=[True])
    def test_combat_flee_alive(self, mock_combat_flee):
        character.set_hp(10)
        self.assertEqual(True, combat())

    @patch('builtins.input', side_effect=['', ''])
    @patch('combat.roll_die', side_effect=[5])
    @patch('combat.combat_flee', side_effect=[False])
    def test_combat_win(self, mock_combat_flee, mock_roll, mock_input):
        character.set_hp(10)
        self.assertEqual(True, combat())

    @patch('builtins.input', side_effect=['', ''])
    @patch('combat.roll_die', side_effect=[5])
    @patch('combat.combat_flee', side_effect=[False])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_win_print(self, mock_stdout, mock_combat_flee, mock_roll, mock_input):
        character.set_hp(10)
        combat()
        self.assertTrue("ENEMY DESTROYED" in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['', ''])
    @patch('combat.roll_die', side_effect=[0, 5, 0, 5])
    @patch('combat.combat_flee', side_effect=[False])
    def test_combat_lose(self, mock_combat_flee, mock_roll, mock_input):
        character.set_hp(10)
        self.assertEqual(False, combat())

    @patch('builtins.input', side_effect=['', ''])
    @patch('combat.roll_die', side_effect=[0, 5, 0, 5])
    @patch('combat.combat_flee', side_effect=[False])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_lose_print(self, mock_stdout, mock_combat_flee, mock_roll, mock_input):
        character.set_hp(10)
        combat()
        self.assertTrue("DEFEATED" in mock_stdout.getvalue())
