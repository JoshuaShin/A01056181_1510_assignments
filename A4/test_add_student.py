import io
from unittest.mock import patch
from unittest import TestCase
import crud


class TestAddStudent(TestCase):
    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", ""])
    def test_add_student_successfully(self, mock_input):
        crud.add_student()
        self.assertEqual("T12345678", crud.file_read()[0].get_student_number())
        crud.file_write([])

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "test", "test", "t12345678"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_duplicate_student_number(self, mock_stdout, mock_input):
        crud.add_student()
        crud.add_student()
        self.assertTrue("ERROR" in mock_stdout.getvalue())
        crud.file_write([])

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "not number"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_invalid_grade(self, mock_stdout, mock_input):
        crud.add_student()
        self.assertTrue("ERROR" in mock_stdout.getvalue())

