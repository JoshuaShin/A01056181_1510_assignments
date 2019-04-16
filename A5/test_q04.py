from unittest import TestCase
import q04


class TestSelectionSort(TestCase):
    def setUp(self):
        self.int_list = [1, 5, 9, 3, -4]
        self.str_list = ['O', 'A', 'J', 'Z', 'Y']
        self.empty_list = list()

    def test_selection_sort_return_type(self):
        self.assertEqual(list, type(q04.selection_sort([3, 5, 1, 9, -4])))

    def test_selection_sort_return_length(self):
        self.assertEqual(5, len(q04.selection_sort([3, 5, 1, 9, -4])))

    def test_selection_sort_number(self):
        self.assertEqual(sorted([3, 5, 1, 9, -4]), q04.selection_sort([3, 5, 1, 9, -4]))

    def test_selection_sort_string(self):
        self.assertEqual(sorted(['c', 'h', 'r', 'i', 's']), q04.selection_sort(['c', 'h', 'r', 'i', 's']))

    def test_selection_sort_empty_list(self):
        with self.assertRaises(ValueError):
            q04.selection_sort([])
