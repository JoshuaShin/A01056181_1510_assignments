import io
from unittest.mock import patch
from unittest import TestCase
from sud import quit_game
from save import load_game
import character


class TestQuitGame(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_game_print(self, mock_stdout):
        try:
            quit_game()
        except SystemExit:
            pass
        self.assertTrue("GAME SAVED" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_game_save_game(self, mock_stdout):
        character.set_hp(5)
        try:
            quit_game()
        except SystemExit:
            pass
        character.set_hp(10)
        load_game()
        self.assertEqual(5, character.get_hp())
