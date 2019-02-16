import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import choose_inventory

sample_inventory = ["A", "B", "C", "D", "E", "F", "G", "H"]


class TestChooseInventory(TestCase):
    def test_choose_inventory_length(self):
        self.assertTrue(len(choose_inventory(sample_inventory, 4)), 4)

    def test_choose_inventory_sorted(self):
        inventory = choose_inventory(sample_inventory, 6)
        self.assertEqual(inventory, sorted(inventory))

    def test_choose_inventory_negative_selection(self):
        self.assertEqual(choose_inventory(sample_inventory, -1), None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_negative_selection_warning(self, mock_stdout):
        choose_inventory(sample_inventory, -1)
        self.assertTrue("WARNING" in mock_stdout.getvalue())

    def test_choose_inventory_over_selection(self):
        self.assertEqual(choose_inventory(sample_inventory, 9), None)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_over_selection_warning(self, mock_stdout):
        choose_inventory(sample_inventory, 9)
        self.assertTrue("WARNING" in mock_stdout.getvalue())

    def test_choose_inventory_equal_selection(self):
        self.assertEqual(choose_inventory(sample_inventory, 8), sample_inventory)

    def test_choose_inventory_string_input(self):
        with self.assertRaises(TypeError):
            choose_inventory(sample_inventory, "")
