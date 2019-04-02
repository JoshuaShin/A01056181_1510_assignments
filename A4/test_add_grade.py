import io
from unittest.mock import patch
from unittest import TestCase
import crud


class TestAddGrade(TestCase):
    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "t12345678", "42"])
    def test_add_grade_successfully(self, mock_input):
        crud.file_write([])
        crud.add_student()
        crud.add_grade()
        self.assertEqual(42.0, crud.file_read()[0].get_final_grades()[0])
        crud.file_write([])

    @patch('builtins.input', side_effect=["t12345678"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_grade_invalid_student_number(self, mock_stdout, mock_input):
        crud.file_write([])
        crud.add_grade()
        self.assertTrue("does not exist" in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "t12345678", "999"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_grade_invalid_grade(self, mock_stdout, mock_input):
        crud.file_write([])
        crud.add_student()
        crud.add_grade()
        self.assertTrue("Invalid grade" in mock_stdout.getvalue())
