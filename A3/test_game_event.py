import io
from unittest.mock import patch
from unittest import TestCase
from sud import game_event
import character


class TestGameEvent(TestCase):
    @patch('random.random', side_effect=[1])
    def test_game_event_no_heal(self, mock_random):
        character.set_hp(10)
        game_event()
        self.assertEqual(10, character.get_hp())

    @patch('random.random', side_effect=[1])
    def test_game_event_heal(self, mock_random):
        character.set_hp(9)
        game_event()
        self.assertEqual(10, character.get_hp())

    @patch('combat.combat', side_effect=[False])
    @patch('random.random', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_event_combat_death(self, mock_stdout, mock_random, mock_combat):
        try:
            game_event()
        except SystemExit:
            pass
        self.assertTrue("GAME OVER" in mock_stdout.getvalue())
