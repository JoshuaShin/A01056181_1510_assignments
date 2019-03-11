import io
from unittest.mock import patch
from unittest import TestCase
from sud import print_introduction


class TestPrintIntroduction(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_introduction(self, mock_stdout):
        print_introduction()
        self.assertTrue("VALID COMMANDS: n, w, s, e, quit, restart." in mock_stdout.getvalue())
