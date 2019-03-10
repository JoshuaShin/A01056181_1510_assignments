import io
from unittest.mock import patch
from unittest import TestCase
import character


class TestCharacterMove(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_invalid_input(self, mock_stdout):
        character.move("bad input")
        self.assertTrue("INVALID COMMAND" in mock_stdout.getvalue())

    def test_move_north_valid(self):
        character.set_coordinates(10, 10)
        character.move("north")
        self.assertEqual((10, 9), character.coordinates)

    def test_move_west_valid(self):
        character.set_coordinates(10, 10)
        character.move("west")
        self.assertEqual((9, 10), character.coordinates)

    def test_move_south_valid(self):
        character.set_coordinates(10, 10)
        character.move("south")
        self.assertEqual((10, 11), character.coordinates)

    def test_move_east_valid(self):
        character.set_coordinates(10, 10)
        character.move("east")
        self.assertEqual((11, 10), character.coordinates)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_out_of_bound(self, mock_stdout):
        character.set_coordinates(1, 4)
        character.move("west")
        self.assertTrue("OUT OF BOUND" in mock_stdout.getvalue())
