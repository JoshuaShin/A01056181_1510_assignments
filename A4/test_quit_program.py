import io
from unittest.mock import patch
from unittest import TestCase
import crud


class TestQuitProgram(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_game_print(self, mock_stdout):
        try:
            crud.quit_program()
        except SystemExit:
            pass
        self.assertTrue("Program Terminated" in mock_stdout.getvalue())
