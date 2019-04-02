from unittest.mock import patch
from unittest import TestCase
import crud


class TestIsStudentNumberDuplicate(TestCase):
    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "t12345678"])
    def test_is_student_number_duplicate_true(self, mock_input):
        crud.add_student()
        self.assertEqual(True, crud.is_student_number_duplicate("t12345678"))
        crud.delete_student()

    @patch('builtins.input', side_effect=["t12345678"])
    def test_is_student_number_duplicate_false(self, mock_input):
        crud.delete_student()
        self.assertEqual(False, crud.is_student_number_duplicate("t11111111"))
