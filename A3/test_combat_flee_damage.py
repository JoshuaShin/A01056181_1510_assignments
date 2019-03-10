import io
from unittest.mock import patch
from unittest import TestCase
from combat import combat_flee_damage
import character


class TestCombatFleeDamage(TestCase):
    @patch('random.random', side_effect=[1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_flee_damage_no_damage(self, mock_stdout, mock_random):
        combat_flee_damage()
        self.assertTrue("WARPED OUT SAFELY" in mock_stdout.getvalue())

    @patch('combat.roll_die', side_effect=[1])
    @patch('random.random', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_flee_damage_take_damage_message(self, mock_stdout, mock_random, mock_roll):
        combat_flee_damage()
        self.assertTrue("WARP OUT PENALTY" in mock_stdout.getvalue())

    @patch('combat.roll_die', side_effect=[1])
    @patch('random.random', side_effect=[0])
    def test_combat_flee_damage_take_damage_hp(self, mock_random, mock_roll):
        character.modify_hp(10)
        combat_flee_damage()
        self.assertEqual(9, character.get_hp())
