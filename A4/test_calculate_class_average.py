import io
from unittest.mock import patch
from unittest import TestCase
import crud


class TestCalculateClassAverage(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_class_average_empty_database(self, mock_stdout):
        crud.file_write([])
        crud.calculate_class_average()
        self.assertTrue("Database is empty", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", ""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_class_average_no_grades(self, mock_stdout, mock_input):
        crud.file_write([])
        crud.add_student()
        crud.calculate_class_average()
        self.assertTrue("No available grades", mock_stdout.getvalue())
        crud.file_write([])

    @patch('builtins.input', side_effect=["test", "test", "t12345678", "True", "",
                                          "test", "test", "t12345678", "True", "10, 10",
                                          "test", "test", "t12345678", "True", "20"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_class_average(self, mock_stdout, mock_input):
        crud.file_write([])
        crud.add_student()
        crud.add_student()
        crud.add_student()
        crud.calculate_class_average()
        self.assertTrue("15", mock_stdout.getvalue())




