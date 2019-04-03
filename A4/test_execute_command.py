from unittest import TestCase
import crud


class TestExecuteCommand(TestCase):
    def test_execute_command_valid(self):
        with self.assertRaises(SystemExit):
            crud.execute_command(6)

    def test_execute_command_invalid_1(self):
        with self.assertRaises(ValueError):
            crud.execute_command(0)

    def test_execute_command_invalid_2(self):
        with self.assertRaises(ValueError):
            crud.execute_command(7)
