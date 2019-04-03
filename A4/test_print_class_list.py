import io
from unittest.mock import patch
from unittest import TestCase
import crud


class TestPrintClassList(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list_empty_database(self, mock_stdout):
        crud.file_write([])
        crud.print_class_list()
        self.assertTrue("Database is empty", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "10 20"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list_no_grades(self, mock_stdout, mock_input):
        crud.file_write([])
        crud.add_student()
        crud.print_class_list()
        self.assertTrue("Test                Test                T12345678           True                10.0 / 20.0"
                        , mock_stdout.getvalue())
        crud.file_write([])
