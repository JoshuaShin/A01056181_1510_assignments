import io
from unittest.mock import patch
from unittest import TestCase
from combat import combat_flee


class TestCombatFlee(TestCase):
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_flee_print(self, mock_stdout, mock_input):
        combat_flee()
        self.assertTrue("ENEMY ENCOUNTER" in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['y'])
    def test_combat_flee_yes(self, mock_input):
        self.assertEqual(False, combat_flee())

    @patch('builtins.input', side_effect=['n'])
    def test_combat_flee_no(self, mock_input):
        self.assertEqual(True, combat_flee())

    @patch('builtins.input', side_effect=['invalid input', 'y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_flee_invalid_input(self, mock_stdout, mock_input):
        combat_flee()
        self.assertTrue("INVALID COMMAND" in mock_stdout.getvalue())
