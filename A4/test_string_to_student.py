import io
from unittest.mock import patch
from unittest import TestCase
import crud


class TestStringToStudent(TestCase):
    def test_string_to_student(self):
        student = crud.string_to_student("test test t12345678 True")
        self.assertEqual("T12345678", student.get_student_number())

    def test_string_to_student_grades(self):
        student = crud.string_to_student("test test t12345678 True 10 10 10")
        self.assertEqual([10.0, 10.0, 10.0], student.get_final_grades())
