import io
from unittest.mock import patch
from unittest import TestCase
from sud import start_game
import save
import character


class TestStartGame(TestCase):
    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_game_play_game(self, mock_stdout, mock_input):
        try:
            start_game()
        except SystemExit:
            pass
        self.assertTrue("VALID COMMANDS: n, w, s, e, quit, restart." in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_game_check_load(self, mock_stdout, mock_input):
        character.set_hp(5)
        save.save_game()
        try:
            start_game()
        except SystemExit:
            pass
        self.assertEqual(5, character.get_hp())
