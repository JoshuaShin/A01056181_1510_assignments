import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import print_inventory


sample_inventory = ["a", "b", "c", "d"]


class TestPrintInventory(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_inventory(self, mock_stdout):
        print_inventory(sample_inventory)
        self.assertTrue("SUPPLY SHOP:\na\nb\nc\nd\n" in mock_stdout.getvalue())
