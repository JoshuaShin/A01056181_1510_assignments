from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import choose_class


class TestChooseClass(TestCase):
    @patch('builtins.input', side_effect=["bard"])
    def test_choose_class_bard(self, input):
        self.assertEqual(choose_class(), "bard")

    @patch('builtins.input', side_effect=[" bard "])
    def test_choose_class_name_whitespace(self, input):
        self.assertEqual(choose_class(), "bard")

    @patch('builtins.input', side_effect=["BaRd"])
    def test_choose_class_name_capitalized(self, input):
        self.assertEqual(choose_class(), "bard")
