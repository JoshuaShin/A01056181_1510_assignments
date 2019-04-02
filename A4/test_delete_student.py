import io
from unittest.mock import patch
from unittest import TestCase
import crud


class TestDeleteStudent(TestCase):
    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "", "t12345678"])
    def test_delete_student(self, mock_input):
        crud.file_write([])
        crud.add_student()
        crud.delete_student()
        self.assertEqual(0, len(crud.file_read()))

    @patch('builtins.input', side_effect=["invalid_student_number"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_student_invalid(self, mock_stdout, mock_input):
        crud.delete_student()
        self.assertTrue("does not exist" in mock_stdout.getvalue())
