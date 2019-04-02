from unittest.mock import patch
from unittest import TestCase
import crud


class TestCreateStudent(TestCase):
    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", ""])
    def test_create_student_successfully(self, mock_input):
        student = crud.create_student()
        self.assertEqual("Test Test T12345678 True", str(student).strip())

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "test", "test", "t12345678"])
    def test_create_student_duplicate_student_number(self, mock_input):
        crud.add_student()
        with self.assertRaises(ValueError):
            crud.create_student()
        crud.file_write([])

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "not number"])
    def test_create_student_invalid_grade(self, mock_input):
        with self.assertRaises(ValueError):
            crud.create_student()
