from unittest import TestCase
import crud


class TestQuitProgram(TestCase):
    def test_quit_game_print(self):
        with self.assertRaises(SystemExit):
            crud.quit_program()
