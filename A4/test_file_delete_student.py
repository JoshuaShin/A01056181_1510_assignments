import io
from unittest.mock import patch
from unittest import TestCase
import crud


class TestFileDeleteStudent(TestCase):
    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "t12345678"])
    def test_file_delete_student_deleted(self, mock_input):
        crud.add_student()
        crud.file_delete_student("t12345678")
        self.assertEqual(False, crud.is_student_number_duplicate("t12345678"))

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "t12345678"])
    def test_file_delete_student_deleted_true(self, mock_input):
        crud.add_student()
        self.assertEqual(True, crud.file_delete_student("t12345678"))

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "t12345678"])
    def test_file_delete_student_deleted_false(self, mock_input):
        crud.file_delete_student("t12345678")
        self.assertEqual(False, crud.file_delete_student("t12345678"))
