import io
from unittest.mock import patch
from unittest import TestCase
from map import print_map


class TestPrintMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map(self, mock_stdout):
        print_map((29, 16))
        self.assertTrue("                             |                             🚀"
                        "                   .             K L I N G O N               "
                        "*             |" in mock_stdout.getvalue())
