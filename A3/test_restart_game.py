import io
from unittest.mock import patch
from unittest import TestCase
from sud import restart_game
import character


class TestRestartGame(TestCase):
    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_restart_game_print(self, mock_stdout, mock_input):
        try:
            restart_game()
        except SystemExit:
            pass
        self.assertTrue("RESTART GAME" in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['quit'])
    def test_restart_game_reset(self, mock_input):
        character.set_hp(0)
        try:
            restart_game()
        except SystemExit:
            pass
        self.assertEqual(10, character.get_hp())

    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_restart_game_play_again(self, mock_stdout, mock_input):
        try:
            restart_game()
        except SystemExit:
            pass
        self.assertTrue("VALID COMMANDS: n, w, s, e, quit, restart." in mock_stdout.getvalue())
