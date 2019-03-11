import io
from unittest.mock import patch
from unittest import TestCase
from sud import game_over
import character


class TestGameOver(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over_print(self, mock_stdout):
        try:
            game_over()
        except SystemExit:
            pass
        self.assertTrue("GAME OVER" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over_reset(self, mock_stdout):
        character.set_hp(0)
        try:
            game_over()
        except SystemExit:
            pass
        self.assertEqual(10, character.get_hp())
