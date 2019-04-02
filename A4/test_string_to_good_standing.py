from unittest import TestCase
import crud


class TestStringToGoodStanding(TestCase):
    def test_string_to_good_standing_true(self):
        status = crud.string_to_good_standing("true")
        self.assertEqual(True, status)

    def test_string_to_good_standing_false(self):
        status = crud.string_to_good_standing("false")
        self.assertEqual(False, status)

    def test_string_to_good_standing_invalid(self):
        with self.assertRaises(ValueError):
            crud.string_to_good_standing("invalid input")
