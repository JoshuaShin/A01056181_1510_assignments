import io
from unittest.mock import patch
from unittest import TestCase
from sud import play_game
import character


class TestPlayGame(TestCase):
    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_print_introduction(self, mock_stdout, mock_input):
        try:
            play_game()
        except SystemExit:
            pass
        self.assertTrue("VALID COMMANDS: n, w, s, e, quit, restart." in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_print_map(self, mock_stdout, mock_input):
        try:
            play_game()
        except SystemExit:
            pass
        self.assertTrue("| - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                        "- - - - - - - - - - - - - - - |" in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_quit_game(self, mock_stdout, mock_input):
        try:
            play_game()
        except SystemExit:
            pass
        self.assertTrue("GAME SAVED" in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['restart', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_restart_game(self, mock_stdout, mock_input):
        try:
            play_game()
        except SystemExit:
            pass
        self.assertTrue("RESTART GAME" in mock_stdout.getvalue())

    @patch('sud.game_event', side_effect=[None])
    @patch('builtins.input', side_effect=['north', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_move(self, mock_stdout, mock_input, mock_game_event):
        character.set_coordinates(20, 20)
        try:
            play_game()
        except SystemExit:
            pass
        self.assertEqual((20, 19), character.get_coordinates())

    @patch('random.random', side_effect=[1])
    @patch('builtins.input', side_effect=['north', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_game_event(self, mock_stdout, mock_input, mock_random):
        character.set_hp(9)
        character.set_coordinates(20, 20)
        try:
            play_game()
        except SystemExit:
            pass
        self.assertEqual(10, character.get_hp())
